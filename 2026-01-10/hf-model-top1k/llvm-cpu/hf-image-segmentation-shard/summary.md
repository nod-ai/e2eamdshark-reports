## Passing Summary

**TOTAL TESTS = 24**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 24 | 100.0% | 100.0% |
| IREE Compilation | 2 | 8.3% | 8.3% |
| Gold Inference | 2 | 8.3% | 100.0% |
| IREE Inference Invocation | 2 | 8.3% | 100.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 24**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 22 | 91.7% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 2 | 8.3% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-image-segmentation-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-image-segmentation-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_deeplabv3-mobilevit-small | compilation | None | |
| hf_deeplabv3-mobilevit-xx-small | compilation | None | |
| hf_detr-layout-detection | Numerics | None | |
| hf_detr-resnet-50-panoptic | Numerics | None | |
| hf_dpt-large-ade | compilation | None | |
| hf_face-parsing | compilation | None | |
| hf_segformer-b0-finetuned-ade-512-512 | compilation | None | |
| hf_segformer-b0-finetuned-cityscapes-1024-1024 | compilation | None | |
| hf_segformer-b0-finetuned-cityscapes-512-1024 | compilation | None | |
| hf_segformer-b1-finetuned-ade-512-512 | compilation | None | |
| hf_segformer-b1-finetuned-cityscapes-1024-1024 | compilation | None | |
| hf_segformer-b2-fashion | compilation | None | |
| hf_segformer-b2-finetuned-ade-512-512 | compilation | None | |
| hf_segformer-b2-finetuned-cityscapes-1024-1024 | compilation | None | |
| hf_segformer-b3-fashion | compilation | None | |
| hf_segformer-b3-finetuned-ade-512-512 | compilation | None | |
| hf_segformer-b3-finetuned-cityscapes-1024-1024 | compilation | None | |
| hf_segformer-b4-finetuned-ade-512-512 | compilation | None | |
| hf_segformer-b4-finetuned-cityscapes-1024-1024 | compilation | None | |
| hf_segformer-b5-finetuned-ade-640-640 | compilation | None | |
| hf_segformer-b5-finetuned-cityscapes-1024-1024 | compilation | None | |
| hf_segformer_b2_clothes | compilation | None | |
| hf_segformer_b3_clothes | compilation | None | |
| hf_segformer_for_optic_disc_cup_segmentation | compilation | None | |
