## Passing Summary

**TOTAL TESTS = 5**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 5 | 100.0% | 100.0% |
| IREE Compilation | 5 | 100.0% | 100.0% |
| Gold Inference | 4 | 80.0% | 80.0% |
| IREE Inference Invocation | 4 | 80.0% | 100.0% |
| Inference Comparison (PASS) | 4 | 80.0% | 100.0% |
## Fail Summary

**TOTAL TESTS = 5**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 0 | 0.0% |
| Gold Inference | 1 | 20.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/onnx_model_zoo_validated_text_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/onnx_model_zoo_validated_text_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| gpt2-lm-head-10 | PASS | None | |
| roberta-base-11 | PASS | None | |
| roberta-sequence-classification-9 | PASS | None | |
| t5-decoder-with-lm-head-12 | native_inference | None | |
| t5-encoder-12 | PASS | None | |
