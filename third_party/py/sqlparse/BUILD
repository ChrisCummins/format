# A wrapper around pip package to pull in undeclared dependencies.

load("@requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # Apache

py_library(
    name = "sqlparse",
    srcs = ["//third_party/py:empty.py"],
    deps = [
<<<<<<< HEAD:third_party/py/sqlparse/BUILD
        requirement("sqlparse"),
=======
        requirement("dm-sonnet"),
        requirement("tensorflow"),
>>>>>>> f336d7120... Add implicit tensorflow dependencies.:third_party/py/sonnet/BUILD
    ],
)
