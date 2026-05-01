## Passing Summary

**TOTAL TESTS = 21**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 20 | 95.2% | 95.2% |
| IREE Compilation | 1 | 4.8% | 5.0% |
| Gold Inference | 1 | 4.8% | 100.0% |
| IREE Inference Invocation | 1 | 4.8% | 100.0% |
| Inference Comparison (PASS) | 1 | 4.8% | 100.0% |
## Fail Summary

**TOTAL TESTS = 21**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 4.8% |
| IREE Compilation | 19 | 90.5% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-object-detection-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-object-detection-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_detr-doc-table-detection | compilation | None | |
| hf_detr-resnet-101 | compilation | None | |
| hf_detr-resnet-101-dc5 | compilation | None | |
| hf_detr-resnet-50 | compilation | None | |
| hf_detr-resnet-50-dc5 | compilation | None | |
| hf_detr-resnet-50-finetuned-10k-cppe5 | compilation | None | |
| hf_detr-resnet-50-sku110k | compilation | None | |
| hf_diagram_detr_r50_finetuned | setup | None | |
| hf_ditr-e15 | compilation | None | |
| hf_pix2text-table-rec | compilation | None | |
| hf_table-transformer-detection | compilation | None | |
| hf_table-transformer-detection-custom-ale | compilation | None | |
| hf_table-transformer-structure-recognition | compilation | None | |
| hf_table-transformer-structure-recognition-v1.1-all | compilation | None | |
| hf_table-transformer-structure-recognition-v1.1-pub | compilation | None | |
| hf_yolos-base | compilation | None | |
| hf_yolos-fashionpedia | compilation | None | |
| hf_yolos-small | compilation | None | |
| hf_yolos-small-finetuned-license-plate-detection | compilation | None | |
| hf_yolos-small-rego-plates-detection | compilation | None | |
| hf_yolos-tiny | PASS | None | |
