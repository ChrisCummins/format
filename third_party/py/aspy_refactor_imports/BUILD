# A wrapper around pip package to pull in undeclared dependencies.

load("@requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # BSD

py_library(
    name = "aspy_refactor_imports",
    srcs = ["//third_party/py:empty.py"],
    deps = [
<<<<<<< HEAD:third_party/py/aspy_refactor_imports/BUILD
<<<<<<< HEAD:third_party/py/aspy_refactor_imports/BUILD
        requirement("aspy.refactor-imports"),
=======
=======
        "//third_party/py/requests",
>>>>>>> 9ef956645... Add explicit requests dependency.:third_party/py/flask/BUILD
        requirement("Flask"),
        requirement("Flask-Compress"),
        requirement("flask-cors"),
        requirement("Werkzeug"),
<<<<<<< HEAD:third_party/py/aspy_refactor_imports/BUILD
>>>>>>> 0aae7e3cf... Make implicit dep explicit.:third_party/py/flask/BUILD
=======
        requirement("jinja2"),
        requirement("Click"),
        requirement("itsdangerous"),
        requirement("chardet"),
        requirement("certifi"),
        requirement("retrying"),
>>>>>>> fa2dbdcdb... Move implicit deps into correct package.:third_party/py/flask/BUILD
    ],
)
