## Passing Summary

**TOTAL TESTS = 4**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 4 | 100.0% | 100.0% |
| IREE Compilation | 3 | 75.0% | 75.0% |
| Gold Inference | 3 | 75.0% | 100.0% |
| IREE Inference Invocation | 3 | 75.0% | 100.0% |
| Inference Comparison (PASS) | 3 | 75.0% | 100.0% |
## Fail Summary

**TOTAL TESTS = 4**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 1 | 25.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_others.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_others.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_agentmodel__AgentModel | compilation | None | |
| migraphx_cadene__resnext101_64x4di16 | PASS | 12633.19489666901 | |
| migraphx_torchvision__inceptioni32 | PASS | 8663.778519665357 | |
| migraphx_torchvision__resnet50i64 | PASS | 9991.140423999846 | |
