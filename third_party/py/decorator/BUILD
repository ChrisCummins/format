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
<<<<<<< HEAD:third_party/py/decorator/BUILD
>>>>>>> 791b827d0... Enable support for Colaboratory notebooks.:third_party/py/jupyter/BUILD
=======
        requirement("notebook"),
        requirement("nbformat"),
        # requirement("nbconvert"),
        requirement("prometheus_client"),
<<<<<<< HEAD:third_party/py/decorator/BUILD
>>>>>>> c676bc140... Add docker image to build notebook.:third_party/py/jupyter/BUILD
=======
        "//third_party/py/jinja2",
>>>>>>> 575a2237e... Add implicit deps to jupyter package.:third_party/py/jupyter/BUILD
    ],
)
