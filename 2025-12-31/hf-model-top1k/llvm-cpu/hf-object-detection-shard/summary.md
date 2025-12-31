## Passing Summary

**TOTAL TESTS = 21**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 0 | 0.0% | 0.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 21**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 21 | 100.0% |
| IREE Compilation | 0 | 0.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-object-detection-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-object-detection-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_detr-doc-table-detection | setup | None | |
| hf_detr-resnet-101 | setup | None | |
| hf_detr-resnet-101-dc5 | setup | None | |
| hf_detr-resnet-50 | setup | None | |
| hf_detr-resnet-50-dc5 | setup | None | |
| hf_detr-resnet-50-finetuned-10k-cppe5 | setup | None | |
| hf_detr-resnet-50-sku110k | setup | None | |
| hf_diagram_detr_r50_finetuned | setup | None | |
| hf_ditr-e15 | setup | None | |
| hf_pix2text-table-rec | setup | None | |
| hf_table-transformer-detection | setup | None | |
| hf_table-transformer-detection-custom-ale | setup | None | |
| hf_table-transformer-structure-recognition | setup | None | |
| hf_table-transformer-structure-recognition-v1.1-all | setup | None | |
| hf_table-transformer-structure-recognition-v1.1-pub | setup | None | |
| hf_yolos-base | setup | None | |
| hf_yolos-fashionpedia | setup | None | |
| hf_yolos-small | setup | None | |
| hf_yolos-small-finetuned-license-plate-detection | setup | None | |
| hf_yolos-small-rego-plates-detection | setup | None | |
| hf_yolos-tiny | setup | None | |
