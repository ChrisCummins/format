"""A script which exports the subset of this repository required for target(s).

This project is getting large. This has two major downsides:
  * Fresh checkouts of the git repository take longer and consume more space.
  * The large number of packages is confusing to newcomers.

I feel like there's a 90-10 rule that applies to this repo: 90% of people who
checkout this repo only need 10% of the code contained within it.
This script provides a way to export that 10%.
"""
import contextlib
import datetime
import glob
import os
import pathlib
import re
import shutil
import stat
import subprocess
import tempfile
import typing

import git
import github as github_lib

from config import getconfig
from datasets.github import api
from labm8 import app
from labm8 import bazelutil
from labm8 import fs

FLAGS = app.FLAGS

app.DEFINE_list('target', [], 'The bazel target(s) to export.')
app.DEFINE_string(
    'targets_list', None, 'Path to a file containing a list of bazel targets. '
    'Supersedes --target flag.')
app.DEFINE_string('destination', '/tmp/phd/tools/source_tree/export',
                  'The destination directory to export to.')
app.DEFINE_string('github_repo', None, 'Name of a GitHub repo to export to.')
app.DEFINE_boolean('github_repo_create_private', True,
                   'Whether to create new GitHub repos as private.')

BAZEL_WRAPPER = bazelutil.DataPath(
    'phd/tools/source_tree/data/bazel_wrapper.py')

# A list of relative paths to include in every export. Glob patterns are
# expanded.
ALWAYS_INCLUDED_FILES = [
    '.bazelrc',  # Not strictly required, but provides consistency.
    'configure',  # Needed to generate config proto.
    'WORKSPACE',
    'README.md',
    'tools/bzl/*',  # Implicit dependency of WORKSPACE file.
    'third_party/*.BUILD',  # Implicit dependencies of WORKSPACE file.
    'third_party/py/tensorflow/BUILD.in',  # Needed by ./configure
    'tools/workspace_status.sh',  # Needed by .bazelrc
    # tools/requirements.txt is always needed, but is handled separately.
]

# A list of relative paths to files which are excluded from export. Glob
# patterns are NOT supported.
EXCLUDED_FILES = [
    'config.pbtxt',  # Generated by ./configure
    'third_party/py/tensorflow/BUILD',  # Generated by ./configure
]


def BazelQuery(args: typing.List[str], timeout_seconds: int = 360, **kwargs):
  """Run bazel query with the specified args."""
  return subprocess.Popen([
      'timeout', '-s9',
      str(timeout_seconds), 'bazel', 'query',
      '--incompatible_remove_native_http_archive=false'
  ] + args, **kwargs)


def MaybeTargetToPath(fully_qualified_target: str, source_root: pathlib.Path
                     ) -> typing.Optional[pathlib.Path]:
  """Determine if a bazel target refers to a file, and if so return the path."""

  def PathIfFile(path: str) -> typing.Optional[pathlib.Path]:
    """Return if given relative path is a file."""
    path = source_root / path
    return path if path.is_file() else None

  if fully_qualified_target.startswith('//:'):
    return PathIfFile(fully_qualified_target[3:])
  elif fully_qualified_target.startswith('//'):
    return PathIfFile(fully_qualified_target[2:].replace(':', '/'))
  else:
    raise TypeError('Target is not fully qualified (does not begin with `//`): '
                    f'{fully_qualified_target}')


def GetDependentFilesOrDie(
    target: str, source_root: pathlib.Path) -> typing.List[pathlib.Path]:
  """Get the file dependencies of the target or die."""
  with fs.chdir(source_root):
    bazel = BazelQuery([f'deps({target})'], stdout=subprocess.PIPE)
    grep = subprocess.Popen(['grep', '^/'],
                            stdout=subprocess.PIPE,
                            stdin=bazel.stdout,
                            universal_newlines=True)

  stdout, _ = grep.communicate()
  assert not bazel.returncode
  assert not grep.returncode

  targets = stdout.rstrip().split('\n')
  paths = [MaybeTargetToPath(target, source_root) for target in targets]
  return [p for p in paths if p]


def GetBuildFilesOrDie(target: str,
                       repo_root: pathlib.Path) -> typing.List[pathlib.Path]:
  """Get the BUILD files required for the given target."""
  with fs.chdir(repo_root):
    bazel = BazelQuery([f'buildfiles(deps({target}))'], stdout=subprocess.PIPE)
    cut = subprocess.Popen(['cut', '-f1', '-d:'],
                           stdout=subprocess.PIPE,
                           stdin=bazel.stdout)
    grep = subprocess.Popen(['grep', '^/'],
                            stdout=subprocess.PIPE,
                            stdin=cut.stdout,
                            universal_newlines=True)

  stdout, _ = grep.communicate()
  assert not bazel.returncode
  assert not cut.returncode
  assert not grep.returncode

  for line in stdout.rstrip().split('\n'):
    if line == '//external':
      continue
    path = repo_root / line[2:] / 'BUILD'
    if not path.is_file():
      raise OSError(f'BUILD file not found: {path}')
    yield path


def GetAlwaysExportedFilesOrDie(
    repo_root: pathlib.Path) -> typing.Iterable[pathlib.Path]:
  """Get hardcoded additional files to export."""
  paths = []
  for p in ALWAYS_INCLUDED_FILES:
    files = glob.glob(f'{repo_root}/{p}')
    assert files
    paths += [pathlib.Path(repo_root, p) for p in files]
  return paths


def GetAuxiliaryExportFiles(paths: typing.List[pathlib.Path]):
  """Get a list of auxiliary files to export."""

  def GlobToPaths(glob_pattern: str) -> typing.List[pathlib.Path]:
    return [pathlib.Path(p) for p in glob.glob(glob_pattern)]

  auxiliary_exports = []
  for path in paths:
    auxiliary_exports += GlobToPaths(f'{path.parent}/DEPS.txt')
    auxiliary_exports += GlobToPaths(f'{path.parent}/README*')
    auxiliary_exports += GlobToPaths(f'{path.parent}/LICENSE*')

  return paths + auxiliary_exports


def FilterExcludedPaths(
    paths: typing.List[pathlib.Path],
    repo_root: pathlib.Path) -> typing.Iterable[pathlib.Path]:
  for path in paths:
    relpath = os.path.relpath(path, repo_root)
    if relpath not in EXCLUDED_FILES:
      yield path


def GetAllSourceTreeFilesOrDie(
    target: str, repo_root: pathlib.Path) -> typing.List[pathlib.Path]:
  """Get the full list of source files to export for a target."""
  paths = list(GetDependentFilesOrDie(target, repo_root))
  paths += list(GetBuildFilesOrDie(target, repo_root))
  paths += list(GetAlwaysExportedFilesOrDie(repo_root))
  paths += list(GetAuxiliaryExportFiles(paths))
  return list(sorted(set(FilterExcludedPaths(paths, repo_root))))


def GetPythonRequirementsForTargetOrDie(
    target: str, source_root: pathlib.Path) -> typing.List[str]:
  """Get the subset of requirements.txt which is needed for a target."""
  with fs.chdir(source_root):
    bazel = BazelQuery([f'deps({target})'], stdout=subprocess.PIPE)
    grep = subprocess.Popen(['grep', '^@pypi__'],
                            stdout=subprocess.PIPE,
                            stdin=bazel.stdout,
                            universal_newlines=True)

  stdout, _ = grep.communicate()
  assert not bazel.returncode

  with open(source_root / 'tools/requirements.txt') as f:
    requirements = set(f.readlines())

  output = stdout.rstrip()
  if not output:
    return []

  needed = []
  for line in output.split('\n'):
    # This is a pretty hacky approach that tries to match the package component
    # of the generated @pypi__<package>_<vesion> package to the name as it
    # appears in tools/requirements.txt.
    m = re.match(r'^@pypi__([^_]+)_', line)
    assert m.group(1)
    for r in requirements:
      if r.lower().startswith(m.group(1).lower()):
        needed.append(r)

  return list(sorted(set(needed)))


def ExportTargetOrDie(target: str, destination: pathlib.Path):
  """Export the source tree of the given target to the destination directory."""
  repo_root = pathlib.Path(getconfig.GetGlobalConfig().paths.repo_root)
  destination.mkdir(parents=True, exist_ok=True)

  # Copy each source tree file to its relative location in the destination tree.
  for path in GetAllSourceTreeFilesOrDie(target, repo_root):
    relpath = os.path.relpath(path, repo_root)
    dst = destination / relpath
    dst.parent.mkdir(parents=True, exist_ok=True)
    print(relpath)
    shutil.copy(path, dst)

  # Export the subset of python requirements requirements that are needed.
  print('tools/requirements.txt')
  # If there is already a requirements.txt (i.e. from a previous export) then
  # read that and append to it.
  if (destination / 'tools/requirements.txt').is_file():
    with open(destination / 'tools/requirements.txt') as f:
      requirements = f.readlines()
  else:
    requirements = []

  requirements += GetPythonRequirementsForTargetOrDie(target, repo_root)
  requirements = sorted(set(requirements))
  with open(destination / 'tools/requirements.txt', 'w') as f:
    for r in requirements:
      f.write(f'{r}')


def CreateBazelWrapperForExports(destination: pathlib.Path,
                                 exported_targets: typing.List[str]) -> None:
  """Create a 'bazel_wrapper.py' script in the root of the destination tree.

  The bazel_wrapper.py script checks that any targets passed to bazel were part
  of the original export set.
  """
  print('bazel_wrapper.py')
  aux_targets = []
  for target in exported_targets:
    if ':' not in target:
      package_name = target.split('/')[-1]
      aux_targets.append(f'{target}:{package_name}')
  exported_targets += aux_targets

  targets_str = ',\n  '.join([f"'{x}'" for x in sorted(exported_targets)])
  with open(BAZEL_WRAPPER) as f:
    wrapper = f.read()
  wrapper = wrapper.replace('# @EXPORTED_TARGETS@ #', targets_str)
  with open(destination / 'bazel_wrapper.py', 'w') as f:
    f.write(wrapper)
  st = os.stat(destination / 'bazel_wrapper.py')
  os.chmod(destination / 'bazel_wrapper.py', st.st_mode | stat.S_IEXEC)


def UpdateReadme(destination: pathlib.Path,
                 exported_targets: typing.List[str]) -> None:
  """Prepend a header to the README.md with details."""
  phd_repo = git.Repo(path=getconfig.GetGlobalConfig().paths.repo_root)
  parent_hash = phd_repo.head.object.hexsha
  with open(destination / 'README.md') as f:
    readme = f.read()

  targets_str = '\n  '.join(
      [f'./bazel_wrapper.py build {x}' for x in exported_targets])
  readme = f"""# Subtree export from [phd](https://github.com/ChrisCummins/phd)

This repository was automatically generated by
[//tools/source_tree:export_source_tree](https://github.com/ChrisCummins/phd/blob/master/tools/source_tree/export_source_tree.py)
at {datetime.datetime.now()} from
[{parent_hash}](https://github.com/ChrisCummins/phd/commit/{parent_hash}).
It contains only the dependencies required for the following bazel targets:

```
  {targets_str}
```

To report issues, contribute patches, or use other targets,
please use the [parent repository](https://github.com/ChrisCummins/phd).

Begin original README:

""" + readme

  with open(destination / 'README.md', 'w') as f:
    f.write(readme)


@contextlib.contextmanager
def DestinationDirectoryFromFlags() -> pathlib.Path:
  """Get the export destination."""
  if FLAGS.github_repo:
    with tempfile.TemporaryDirectory(prefix='phd_tools_source_tree_') as d:
      yield pathlib.Path(d)
  else:
    yield pathlib.Path(FLAGS.destination)


def GetOrCreateRepoOrDie(github: github_lib.Github) -> github_lib.Repository:
  """Get the github repository to export to. Create it if it doesn't exist."""
  repo_name = FLAGS.github_repo
  try:
    return github.get_user().get_repo(repo_name)
  except github_lib.UnknownObjectException as e:
    assert e.status == 404
    app.Log(1, "Creating repo %s", repo_name)
    github.get_user().create_repo(
        repo_name,
        description='PhD repo subtree export',
        homepage='https://github.com/ChrisCummins/phd',
        has_wiki=False,
        has_issues=False,
        private=FLAGS.github_repo_create_private)
    return GetOrCreateRepoOrDie(github)


def ExportToDirectoryOrDie(destination: pathlib.Path,
                           exported_targets: typing.List[str]) -> None:
  """Export the requested targets to the destination directory."""
  for target in FLAGS.target:
    ExportTargetOrDie(target, destination)

  CreateBazelWrapperForExports(destination, exported_targets)
  UpdateReadme(destination, exported_targets)


def CloneRepoToDestinationOrDie(repo: github_lib.Repository,
                                destination: pathlib.Path):
  """Clone repo from github."""
  app.Log(1, 'Cloning from %s', repo.ssh_url)
  subprocess.check_call(['git', 'clone', repo.ssh_url, str(destination)])
  # Delete everything except the .git directory. This is to enable files to be
  # removed between commits, as otherwise incremental commits would only ever
  # be additive.
  for path in list(destination.iterdir()):
    if path.exists() and path != (destination / '.git'):
      fs.rm(path)
  assert (destination / '.git').is_dir()


def CommitAndPushOrDie(local: pathlib.Path, remote: github_lib.Repository):
  """Create a commit, a tag, and push both to the remote repo."""
  phd_repo = git.Repo(path=getconfig.GetGlobalConfig().paths.repo_root)
  parent_hash = phd_repo.head.object.hexsha

  tag_name = datetime.datetime.now().strftime("%y%m%dT%H%M%S")
  app.Log(1, "Creating tag %s", tag_name)
  with fs.chdir(local):
    subprocess.check_call(['git', 'add', '.'])
    subprocess.check_call(
        ['git', 'commit', '-m', f'Subtree export from {parent_hash}'])
    subprocess.check_call([
        'git', 'tag', '-a', tag_name, '-m', f'Subtree export from {parent_hash}'
    ])
    subprocess.check_call(['git', 'push', 'origin', 'master'])
    subprocess.check_call(['git', 'push', 'origin', tag_name])
  app.Log(1, 'Exported to %s', remote.html_url)


def main(argv: typing.List[str]):
  """Main entry point."""
  if len(argv) > 1:
    raise app.UsageError("Unknown arguments: '{}'.".format(' '.join(argv[1:])))

  # Get the list of targets to export.
  if not FLAGS.target and not FLAGS.targets_list:
    raise app.UsageError('--target must be a bazel target(s)')
  elif FLAGS.targets_list:
    with open(FLAGS.targets_list) as f:
      targets = f.read().rstrip().split('\n')
  else:
    targets = FLAGS.target

  if not FLAGS.destination:
    raise app.UsageError('--destination must be a directory to create')

  targets = list(sorted(targets))

  with DestinationDirectoryFromFlags() as destination:

    if FLAGS.github_repo:
      github = api.GetGithubConectionFromFlagsOrDie()
      repo = GetOrCreateRepoOrDie(github)
      CloneRepoToDestinationOrDie(repo, destination)
      ExportToDirectoryOrDie(destination, targets)
      CommitAndPushOrDie(destination, repo)
    else:
      ExportToDirectoryOrDie(destination, targets)
      app.Log(1, 'Exported subtree to %s', destination)


if __name__ == '__main__':
  app.RunWithArgs(main)
