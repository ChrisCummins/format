# A wrapper around pip package to pull in undeclared dependencies.

load("@requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # BSD

py_library(
<<<<<<< HEAD
<<<<<<< HEAD:third_party/py/attrs/BUILD
    name = "attrs",
=======
    name = "jupyter",
>>>>>>> 10d0bba21... Remove the empty python library files.:third_party/py/jupyter/BUILD
    srcs = ["//third_party/py:empty.py"],
    deps = [
<<<<<<< HEAD:third_party/py/attrs/BUILD
        requirement("attrs"),
=======
        requirement("jupyter-client"),
        requirement("jupyter_http_over_ws"),
<<<<<<< HEAD:third_party/py/attrs/BUILD
>>>>>>> 791b827d0... Enable support for Colaboratory notebooks.:third_party/py/jupyter/BUILD
=======
        requirement("notebook"),
        requirement("nbformat"),
        requirement("prometheus_client"),
<<<<<<< HEAD:third_party/py/attrs/BUILD
>>>>>>> c676bc140... Add docker image to build notebook.:third_party/py/jupyter/BUILD
=======
        "//third_party/py/jinja2",
>>>>>>> 575a2237e... Add implicit deps to jupyter package.:third_party/py/jupyter/BUILD
=======
    name = "attrs",
    srcs = ["//third_party/py:empty.py"],
    deps = [
        requirement("attrs"),
>>>>>>> 4903bd176... Pull in black sources directly.
    ],
)
