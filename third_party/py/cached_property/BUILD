# A wrapper around pip package to pull in undeclared dependencies.

load("@requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # BSD

py_library(
<<<<<<< HEAD:third_party/py/cached_property/BUILD
    name = "cached_property",
=======
    name = "flask",
>>>>>>> 10d0bba21... Remove the empty python library files.:third_party/py/flask/BUILD
    srcs = ["//third_party/py:empty.py"],
    deps = [
<<<<<<< HEAD:third_party/py/cached_property/BUILD
<<<<<<< HEAD:third_party/py/cached_property/BUILD
        requirement("cached-property"),
=======
=======
        "//third_party/py/requests",
>>>>>>> 9ef956645... Add explicit requests dependency.:third_party/py/flask/BUILD
        requirement("Flask"),
        requirement("Flask-Compress"),
        requirement("flask-cors"),
        requirement("Flask-SQLalchemy"),
        requirement("Werkzeug"),
<<<<<<< HEAD:third_party/py/cached_property/BUILD
>>>>>>> 0aae7e3cf... Make implicit dep explicit.:third_party/py/flask/BUILD
=======
        requirement("jinja2"),
        "//third_party/py/click",
        requirement("itsdangerous"),
        requirement("chardet"),
        requirement("certifi"),
        requirement("retrying"),
>>>>>>> fa2dbdcdb... Move implicit deps into correct package.:third_party/py/flask/BUILD
    ],
)
