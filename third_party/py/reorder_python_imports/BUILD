# A wrapper around pip package to pull in undeclared dependencies.

load("@requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # BSD

py_library(
    name = "reorder_python_imports",
    srcs = ["//third_party/py:empty.py"],
    deps = [
<<<<<<< HEAD:third_party/py/reorder_python_imports/BUILD
        requirement("reorder-python-imports"),
        "//third_party/py/aspy_refactor_imports",
        "//third_party/py/cached_property",
=======
        requirement("dash"),
        requirement("plotly"),
        "//third_party/py/flask",
        "//third_party/py/requests",
>>>>>>> 9ef956645... Add explicit requests dependency.:third_party/py/dash/BUILD
    ],
)
