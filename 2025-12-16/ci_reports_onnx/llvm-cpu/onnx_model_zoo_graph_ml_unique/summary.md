## Passing Summary

**TOTAL TESTS = 8**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 8 | 100.0% | 100.0% |
| IREE Compilation | 8 | 100.0% | 100.0% |
| Gold Inference | 8 | 100.0% | 100.0% |
| IREE Inference Invocation | 8 | 100.0% | 100.0% |
| Inference Comparison (PASS) | 8 | 100.0% | 100.0% |
## Fail Summary

**TOTAL TESTS = 8**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 0 | 0.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/onnx_model_zoo_graph_ml_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/onnx_model_zoo_graph_ml_unique.md', get_metadata=True)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| feastconv_Opset17_graph_convolutions | PASS | None | |
| generalconv_Opset17_graph_convolutions | PASS | None | |
| leconv_Opset17_graph_convolutions | PASS | None | |
| pnaconv_Opset16_graph_convolutions | PASS | None | |
| pnaconv_Opset17_graph_convolutions | PASS | None | |
| resgatedgraphconv_Opset17_graph_convolutions | PASS | None | |
| sageconv_Opset16_graph_convolutions | PASS | None | |
| tagconv_Opset17_graph_convolutions | PASS | None | |
