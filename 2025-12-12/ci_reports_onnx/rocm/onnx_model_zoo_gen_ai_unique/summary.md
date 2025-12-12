## Passing Summary

**TOTAL TESTS = 18**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 0 | 0.0% | 0.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 18**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 18 | 100.0% |
| IREE Compilation | 0 | 0.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/onnx_model_zoo_gen_ai_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/onnx_model_zoo_gen_ai_unique.md', get_metadata=True)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| biogpt_Opset16_transformers | setup | None | |
| biogpt_Opset17_transformers | setup | None | |
| gpt2_Opset16_transformers | setup | None | |
| gpt2_Opset18_transformers | setup | None | |
| gpt2doubleheads_Opset16_transformers | setup | None | |
| gpt2doubleheads_Opset17_transformers | setup | None | |
| gpt2lmhead_Opset16_transformers | setup | None | |
| gpt2lmhead_Opset17_transformers | setup | None | |
| gptj_Opset16_transformers | setup | None | |
| gptj_Opset18_transformers | setup | None | |
| gptneox_Opset16_transformers | setup | None | |
| gptneox_Opset18_transformers | setup | None | |
| openaigpt_Opset16_transformers | setup | None | |
| openaigpt_Opset18_transformers | setup | None | |
| openaigptdoubleheads_Opset16_transformers | setup | None | |
| openaigptdoubleheads_Opset17_transformers | setup | None | |
| openaigptlmhead_Opset16_transformers | setup | None | |
| openaigptlmhead_Opset17_transformers | setup | None | |
