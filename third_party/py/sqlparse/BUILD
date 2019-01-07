# A wrapper around pip package to pull in undeclared dependencies.

load("@requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # Apache

py_library(
    name = "sqlparse",
    srcs = ["//third_party/py:empty.py"],
    deps = [
<<<<<<< HEAD:third_party/py/sqlparse/BUILD
<<<<<<< HEAD:third_party/py/sqlparse/BUILD
        requirement("sqlparse"),
=======
        requirement("dm-sonnet"),
        requirement("tensorflow"),
>>>>>>> f336d7120... Add implicit tensorflow dependencies.:third_party/py/sonnet/BUILD
=======
        requirement("graph_nets"),
        "//third_party/py/sonnet",
        "//third_party/py/tensorflow",
>>>>>>> 3fc848997... Use //third_party deps.:third_party/py/graph_nets/BUILD
    ],
)
