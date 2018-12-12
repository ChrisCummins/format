# A wrapper around pip package to pull in undeclared dependencies.

load("@requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # BSD

py_library(
    name = "decorator",
    srcs = ["//third_party/py:empty.py"],
    deps = [
<<<<<<< HEAD:third_party/py/decorator/BUILD
        requirement("decorator"),
=======
        requirement("jupyter-client"),
        requirement("jupyter_http_over_ws"),
>>>>>>> 791b827d0... Enable support for Colaboratory notebooks.:third_party/py/jupyter/BUILD
    ],
)
