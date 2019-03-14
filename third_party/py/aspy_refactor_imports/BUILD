# A wrapper around pip package to pull in undeclared dependencies.

load("@requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # BSD

py_library(
    name = "aspy_refactor_imports",
    srcs = ["//third_party/py:empty.py"],
    deps = [
<<<<<<< HEAD:third_party/py/aspy_refactor_imports/BUILD
        requirement("aspy.refactor-imports"),
=======
        requirement("Flask"),
        requirement("Flask-Compress"),
        requirement("flask-cors"),
        requirement("Werkzeug"),
>>>>>>> 0aae7e3cf... Make implicit dep explicit.:third_party/py/flask/BUILD
    ],
)
