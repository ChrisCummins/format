# Tools for working with the source tree.

load("//tools/bzl:exports.bzl", "exports_repo")
load("@subpar//:subpar.bzl", "par_binary")

exports_repo(
    name = "export",
    github_repo = "bazel_subtree_github_export",
    move_file_mapping = {
        "tools/source_tree/README.md": "README.md",
        "tools/source_tree/LICENSE": "LICENSE",
        "tools/source_tree/travis.yml": ".travis.yml",
    },
    targets = ["//tools/source_tree:export_source_tree"],
)

par_binary(
    name = "deploy_pip",
    srcs = ["deploy_pip.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":phd_workspace",
        "//:getconfig",
        "//labm8/py:app",
        "//labm8/py:fs",
    ],
)

par_binary(
    name = "export_source_tree",
    srcs = ["export_source_tree.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":phd_workspace",
        ":source_tree",
        "//:getconfig",
        "//datasets/github:api",
        "//labm8/py:app",
        "//labm8/py:bazelutil",
        "//labm8/py:fs",
        "//labm8/py:humanize",
        "//third_party/py/git",
        "//third_party/py/github",
    ],
)

py_library(
    name = "phd_workspace",
    srcs = ["phd_workspace.py"],
    visibility = ["//visibility:public"],
    deps = [
        ":source_tree",
        "//labm8/py:bazelutil",
        "//labm8/py:fs",
        "//labm8/py:humanize",
        "//third_party/py/git",
        "//tools/git:export_subtree",
    ],
)

py_library(
    name = "source_tree",
    srcs = ["source_tree.py"],
    deps = [
        "//labm8/py:app",
        "//labm8/py:humanize",
        "//third_party/py/git",
    ],
)

py_test(
    name = "source_tree_test",
    srcs = ["source_tree_test.py"],
    deps = [
        ":conftest",
        ":source_tree",
        "//labm8/py:fs",
        "//labm8/py:test",
        "//third_party/py/git",
    ],
)
