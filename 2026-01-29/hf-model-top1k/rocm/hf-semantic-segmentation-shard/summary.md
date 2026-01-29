## Passing Summary

**TOTAL TESTS = 7**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 7 | 100.0% | 100.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 7**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 7 | 100.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-semantic-segmentation-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-semantic-segmentation-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_segformer-b0-finetuned-segments-sidewalk-2 | compilation | None | |
| hf_segformer-b4-finetuned-segments-sidewalk | compilation | None | |
| hf_tcd-segformer-mit-b0 | compilation | None | |
| hf_tcd-segformer-mit-b1 | compilation | None | |
| hf_tcd-segformer-mit-b2 | compilation | None | |
| hf_tcd-segformer-mit-b3 | compilation | None | |
| hf_tcd-segformer-mit-b4 | compilation | None | |
