# A wrapper around pip package to pull in undeclared dependencies.

load("@requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # BSD

py_library(
    name = "cached_property",
    srcs = ["//third_party/py:empty.py"],
    deps = [
<<<<<<< HEAD:third_party/py/cached_property/BUILD
        requirement("cached-property"),
=======
        requirement("Flask"),
        requirement("flask-cors"),
        requirement("Werkzeug"),
>>>>>>> 0aae7e3cf... Make implicit dep explicit.:third_party/py/flask/BUILD
    ],
)
