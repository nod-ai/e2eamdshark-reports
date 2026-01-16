## Passing Summary

**TOTAL TESTS = 9**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 0 | 0.0% | 0.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 9**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 9 | 100.0% |
| IREE Compilation | 0 | 0.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/onnx_model_zoo_gen_ai_others.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/onnx_model_zoo_gen_ai_others.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| biogpt_Opset18_transformers | setup | None | |
| gpt2_Opset17_transformers | setup | None | |
| gpt2doubleheads_Opset18_transformers | setup | None | |
| gpt2lmhead_Opset18_transformers | setup | None | |
| gptj_Opset17_transformers | setup | None | |
| gptneox_Opset17_transformers | setup | None | |
| openaigpt_Opset17_transformers | setup | None | |
| openaigptdoubleheads_Opset18_transformers | setup | None | |
| openaigptlmhead_Opset18_transformers | setup | None | |
