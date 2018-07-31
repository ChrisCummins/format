# CLSmith - A random generator of OpenCL C programs.
# See: https://github.com/ChrisLidbury/CLSmith

package(default_visibility = ["//visibility:public"])

cc_binary(
    name = "CLSmith",
    srcs = [
        "src/AbsExtension.cpp",
        "src/AbsExtension.h",
        "src/AbsProgramGenerator.cpp",
        "src/AbsProgramGenerator.h",
        "src/AbsRndNumGenerator.cpp",
        "src/AbsRndNumGenerator.h",
        "src/ArrayVariable.cpp",
        "src/ArrayVariable.h",
        "src/Block.cpp",
        "src/Block.h",
        "src/Bookkeeper.cpp",
        "src/Bookkeeper.h",
        "src/CFGEdge.cpp",
        "src/CFGEdge.h",
        "src/CGContext.cpp",
        "src/CGContext.h",
        "src/CGOptions.cpp",
        "src/CGOptions.h",
        "src/CLSmith/CLExpression.cpp",
        "src/CLSmith/CLExpression.h",
        "src/CLSmith/CLOptions.cpp",
        "src/CLSmith/CLOptions.h",
        "src/CLSmith/CLOutputMgr.cpp",
        "src/CLSmith/CLOutputMgr.h",
        "src/CLSmith/CLProgramGenerator.cpp",
        "src/CLSmith/CLProgramGenerator.h",
        "src/CLSmith/CLRandomProgramGenerator.cpp",
        "src/CLSmith/CLStatement.cpp",
        "src/CLSmith/CLStatement.h",
        "src/CLSmith/CLVariable.cpp",
        "src/CLSmith/CLVariable.h",
        "src/CLSmith/Divergence.cpp",
        "src/CLSmith/Divergence.h",
        "src/CLSmith/ExpressionAtomic.cpp",
        "src/CLSmith/ExpressionAtomic.h",
        "src/CLSmith/ExpressionID.cpp",
        "src/CLSmith/ExpressionID.h",
        "src/CLSmith/ExpressionVector.cpp",
        "src/CLSmith/ExpressionVector.h",
        "src/CLSmith/FunctionInvocationBuiltIn.cpp",
        "src/CLSmith/FunctionInvocationBuiltIn.h",
        "src/CLSmith/Globals.cpp",
        "src/CLSmith/Globals.h",
        "src/CLSmith/MemoryBuffer.cpp",
        "src/CLSmith/MemoryBuffer.h",
        "src/CLSmith/StatementAtomicReduction.cpp",
        "src/CLSmith/StatementAtomicReduction.h",
        "src/CLSmith/StatementAtomicResult.cpp",
        "src/CLSmith/StatementAtomicResult.h",
        "src/CLSmith/StatementBarrier.cpp",
        "src/CLSmith/StatementBarrier.h",
        "src/CLSmith/StatementComm.cpp",
        "src/CLSmith/StatementComm.h",
        "src/CLSmith/StatementEMI.cpp",
        "src/CLSmith/StatementEMI.h",
        "src/CLSmith/StatementMessage.cpp",
        "src/CLSmith/StatementMessage.h",
        "src/CLSmith/Vector.cpp",
        "src/CLSmith/Vector.h",
        "src/CLSmith/Walker.cpp",
        "src/CLSmith/Walker.h",
        "src/CVQualifiers.cpp",
        "src/CVQualifiers.h",
        "src/Common.h",
        "src/CommonMacros.h",
        "src/CompatibleChecker.cpp",
        "src/CompatibleChecker.h",
        "src/Constant.cpp",
        "src/Constant.h",
        "src/CoverageTestExtension.cpp",
        "src/CoverageTestExtension.h",
        "src/CrestExtension.cpp",
        "src/CrestExtension.h",
        "src/DFSOutputMgr.cpp",
        "src/DFSOutputMgr.h",
        "src/DFSProgramGenerator.cpp",
        "src/DFSProgramGenerator.h",
        "src/DFSRndNumGenerator.cpp",
        "src/DFSRndNumGenerator.h",
        "src/DefaultOutputMgr.cpp",
        "src/DefaultOutputMgr.h",
        "src/DefaultProgramGenerator.cpp",
        "src/DefaultProgramGenerator.h",
        "src/DefaultRndNumGenerator.cpp",
        "src/DefaultRndNumGenerator.h",
        "src/DeltaMonitor.cpp",
        "src/DeltaMonitor.h",
        "src/DepthSpec.cpp",
        "src/DepthSpec.h",
        "src/Effect.cpp",
        "src/Effect.h",
        "src/Enumerator.h",
        "src/Error.cpp",
        "src/Error.h",
        "src/Expression.cpp",
        "src/Expression.h",
        "src/ExpressionAssign.cpp",
        "src/ExpressionAssign.h",
        "src/ExpressionComma.cpp",
        "src/ExpressionComma.h",
        "src/ExpressionFuncall.cpp",
        "src/ExpressionFuncall.h",
        "src/ExpressionVariable.cpp",
        "src/ExpressionVariable.h",
        "src/ExtensionMgr.cpp",
        "src/ExtensionMgr.h",
        "src/ExtensionValue.cpp",
        "src/ExtensionValue.h",
        "src/Fact.cpp",
        "src/Fact.h",
        "src/FactMgr.cpp",
        "src/FactMgr.h",
        "src/FactPointTo.cpp",
        "src/FactPointTo.h",
        "src/FactUnion.cpp",
        "src/FactUnion.h",
        "src/Filter.cpp",
        "src/Filter.h",
        "src/Finalization.cpp",
        "src/Finalization.h",
        "src/Function.cpp",
        "src/Function.h",
        "src/FunctionInvocation.cpp",
        "src/FunctionInvocation.h",
        "src/FunctionInvocationBinary.cpp",
        "src/FunctionInvocationBinary.h",
        "src/FunctionInvocationUnary.cpp",
        "src/FunctionInvocationUnary.h",
        "src/FunctionInvocationUser.cpp",
        "src/FunctionInvocationUser.h",
        "src/KleeExtension.cpp",
        "src/KleeExtension.h",
        "src/Lhs.cpp",
        "src/Lhs.h",
        "src/LinearSequence.cpp",
        "src/LinearSequence.h",
        "src/MspFilters.cpp",
        "src/MspFilters.h",
        "src/OutputMgr.cpp",
        "src/OutputMgr.h",
        "src/PartialExpander.cpp",
        "src/PartialExpander.h",
        "src/Probabilities.cpp",
        "src/Probabilities.h",
        "src/ProbabilityTable.h",
        "src/RandomNumber.cpp",
        "src/RandomNumber.h",
        "src/Reducer.cpp",
        "src/Reducer.h",
        "src/ReducerOutputMgr.cpp",
        "src/ReducerOutputMgr.h",
        "src/SafeOpFlags.cpp",
        "src/SafeOpFlags.h",
        "src/Sequence.cpp",
        "src/Sequence.h",
        "src/SequenceFactory.cpp",
        "src/SequenceFactory.h",
        "src/SequenceLineParser.h",
        "src/SimpleDeltaRndNumGenerator.cpp",
        "src/SimpleDeltaRndNumGenerator.h",
        "src/SimpleDeltaSequence.cpp",
        "src/SimpleDeltaSequence.h",
        "src/SplatExtension.cpp",
        "src/SplatExtension.h",
        "src/Statement.cpp",
        "src/Statement.h",
        "src/StatementArrayOp.cpp",
        "src/StatementArrayOp.h",
        "src/StatementAssign.cpp",
        "src/StatementAssign.h",
        "src/StatementBreak.cpp",
        "src/StatementBreak.h",
        "src/StatementContinue.cpp",
        "src/StatementContinue.h",
        "src/StatementExpr.cpp",
        "src/StatementExpr.h",
        "src/StatementFor.cpp",
        "src/StatementFor.h",
        "src/StatementGoto.cpp",
        "src/StatementGoto.h",
        "src/StatementIf.cpp",
        "src/StatementIf.h",
        "src/StatementReturn.cpp",
        "src/StatementReturn.h",
        "src/StringUtils.cpp",
        "src/StringUtils.h",
        "src/Type.cpp",
        "src/Type.h",
        "src/Variable.cpp",
        "src/Variable.h",
        "src/VariableSelector.cpp",
        "src/VariableSelector.h",
        "src/VectorFilter.cpp",
        "src/VectorFilter.h",
        "src/platform.cpp",
        "src/platform.h",
        "src/random.cpp",
        "src/random.h",
        "src/util.cpp",
        "src/util.h",
    ],
    copts = [
        "-Iexternal/CLSmith/src",
        "-DPACKAGE_STRING=1",
    ],
    linkopts = ["-ldl"] + select({
        "//:darwin": [],
        "//conditions:default": ["-pthread"],
    }),
)

config_setting(
    name = "darwin",
    values = {"cpu": "darwin"},
)

cc_binary(
    name = "cl_launcher",
    srcs = ["src/CLSmith/cl_launcher.c"],
    linkopts = select({
        "//:darwin": ["-framework OpenCL"],
        "//conditions:default": [
            "-pthread",
            "-lOpenCL",
        ],
    }),
    deps = [
        "@opencl_220_headers//:headers",
    ],
)

genrule(
    name = "cl_safe_math_macros",
    srcs = ["runtime/cl_safe_math_macros.m4"],
    outs = ["cl_safe_math_macros.h"],
    cmd = "m4 $< > $@",
)

genrule(
    name = "safe_math_macros",
    srcs = ["runtime/safe_math_macros.m4"],
    outs = ["safe_math_macros.h"],
    cmd = "m4 $< > $@",
)

filegroup(
    name = "runtime_headers",
    srcs = glob(["runtime/*.h"]),
)
