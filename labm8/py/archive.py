"""Module for handling archive files."""
import pathlib
import shutil
import tarfile
import tempfile
import typing
import zipfile

<<<<<<< HEAD:labm8/py/archive.py
<<<<<<< HEAD:labm8/py/archive.py
<<<<<<< HEAD:labm8/py/archive.py
=======
from absl import flags
=======
from labm8 import app
>>>>>>> 89b790ba9... Merge absl logging, app, and flags modules.:labm8/archive.py

FLAGS = app.FLAGS

>>>>>>> 105797fd4... Auto format files.:labm8/archive.py
=======
>>>>>>> d97a0b31a... Populate BuildInfo protobuf during build stamping.:labm8/archive.py

class UnsupportedArchiveFormat(ValueError):
  """Raised in case an archive has an unsupported file format."""

  pass


class Archive(object):
  """An archive file.

  Provides uniform access unpacked archives when used as a context manager by
  extracting the archive contents to a temporary directory.

  Example:
    >>> with Archive("/tmp/data.zip") as uncompressed_root:
    ...   print(uncompressed_root.iterdir())
    ['a', 'README.txt']

  If the archive is a bazel data dependency, you can use the subclass
  labm8.py.bazelutil.DataArchive to resolve the absolute path.
  """

  def __init__(
<<<<<<< HEAD
<<<<<<< HEAD:labm8/py/archive.py
    self,
    path: typing.Union[str, pathlib.Path],
    assume_filename: typing.Optional[typing.Union[str, pathlib.Path]] = None,
  ):
=======
      self,
      path: typing.Union[str, pathlib.Path],
<<<<<<< HEAD:labm8/py/archive.py
      assume_filename: typing.Optional[typing.Union[str, pathlib.Path]] = None):
>>>>>>> 105797fd4... Auto format files.:labm8/archive.py
=======
      assume_filename: typing.Optional[typing.Union[str, pathlib.Path]] = None,
=======
    self,
    path: typing.Union[str, pathlib.Path],
    assume_filename: typing.Optional[typing.Union[str, pathlib.Path]] = None,
>>>>>>> 4242aed2a... Automated code format.
  ):
>>>>>>> 49340dc00... Auto-format labm8 python files.:labm8/archive.py
    """Create an archive.

    Will determine the type of the archive from the suffix, e.g. if path is
    'foo.zip', will treat the file as a zip file. The assume_filename path
    can be used to change the determined type.

    Args:
      path: The path to the data, including the name of the workspace.
      assume_filename: For the purpose of determining the encoding of the
        archive from the file extension, use this name rather than the true
        path.

    Raises:
      FileNotFoundError: If path is not a file.
    """
    self._compressed_path = pathlib.Path(path)
    if not self._compressed_path.is_file():
      raise FileNotFoundError(f"No such file: '{path}'")

    # The path used to determine the type of the archive.
    path_to_determine_type = pathlib.Path(assume_filename or path)
    suffixes = path_to_determine_type.suffixes

    if not suffixes:
      raise UnsupportedArchiveFormat(
<<<<<<< HEAD
<<<<<<< HEAD:labm8/py/archive.py
        f"Archive '{path_to_determine_type.name}' has no extension",
      )
=======
          f"Archive '{path_to_determine_type.name}' has no extension",)
>>>>>>> 49340dc00... Auto-format labm8 python files.:labm8/archive.py

    if suffixes[-1] == ".zip":
      self._open_function = zipfile.ZipFile
<<<<<<< HEAD:labm8/py/archive.py
    elif suffixes[-2:] == [".tar", ".bz2"]:
=======
    elif suffixes[-2:] == ['.tar', '.bz2']:
<<<<<<< HEAD:labm8/py/archive.py
>>>>>>> ee0eceb12... Add support for .tar.bz2 data archives.:labm8/archive.py
      self._open_function = lambda f: tarfile.open(f, "r:bz2")
      # TODO(cec): Add support for .tar, and .tar.gz.
    else:
      raise UnsupportedArchiveFormat(
        f"Unsupported file extension '{suffixes[-1]}' for archive "
        f"'{path_to_determine_type.name}'",
      )
=======
      self._open_function = lambda f: tarfile.open(f, 'r:bz2')
      # TODO(cec): Add support for .tar, and .tar.gz.
    else:
      raise UnsupportedArchiveFormat(
          f"Unsupported file extension '{suffixes[-1]}' for archive "
          f"'{path_to_determine_type.name}'",)
>>>>>>> 49340dc00... Auto-format labm8 python files.:labm8/archive.py
=======
        f"Archive '{path_to_determine_type.name}' has no extension",
      )

    if suffixes[-1] == ".zip":
      self._open_function = zipfile.ZipFile
    elif suffixes[-2:] == [".tar", ".bz2"]:
      self._open_function = lambda f: tarfile.open(f, "r:bz2")
      # TODO(cec): Add support for .tar, and .tar.gz.
    else:
      raise UnsupportedArchiveFormat(
        f"Unsupported file extension '{suffixes[-1]}' for archive "
        f"'{path_to_determine_type.name}'",
      )
>>>>>>> 4242aed2a... Automated code format.

    # Set in __enter__().
    self._uncompressed_path: typing.Optional[pathlib.Path] = None

  @property
  def path(self) -> pathlib.Path:
    """Return the path of the archive."""
    return self._compressed_path

  def ExtractAll(self, path: pathlib.Path) -> pathlib.Path:
    """Extract the archive contents to a directory.

    Args:
      path: The directory to extract to.

    Returns:
      The path of the extracted archive.
    """
    with self._open_function(str(self._compressed_path)) as f:
      f.extractall(path=str(path))
    return path

  def __enter__(self) -> pathlib.Path:
    """Unpack the archive and return the uncompressed path.

    Returns:
      The path of the directory containing the uncompressed archive.
    """
    assert not self._uncompressed_path
<<<<<<< HEAD
<<<<<<< HEAD:labm8/py/archive.py
    self._uncompressed_path = pathlib.Path(tempfile.mkdtemp(prefix="phd_"))
=======
    self._uncompressed_path = pathlib.Path(tempfile.mkdtemp(prefix='phd_'))
>>>>>>> 0c7d6c0f1... Add ExtractAll() method to Archive.:labm8/archive.py
=======
    self._uncompressed_path = pathlib.Path(tempfile.mkdtemp(prefix="phd_"))
>>>>>>> 4242aed2a... Automated code format.
    return self.ExtractAll(self._uncompressed_path)

  def __exit__(self, *args):
    """Exit the scope of the archive.

    This deletes the temporary directory that the archive has been unpacked to.
    """
    assert self._uncompressed_path
    shutil.rmtree(self._uncompressed_path)
    self._uncompressed_path = None
