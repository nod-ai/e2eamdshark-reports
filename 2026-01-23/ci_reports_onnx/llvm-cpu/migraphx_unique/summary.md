## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 26 | 63.4% | 66.7% |
| Inference Comparison (PASS) | 21 | 51.2% | 80.8% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 13 | 31.7% |
| Inference Comparison | 5 | 12.2% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | ERROR | |
| migraphx_cadene__dpn92i1 | PASS | 438.8148303332097 | |
| migraphx_cadene__inceptionv4i16 | PASS | 8875.128277333411 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 823.7374919998123 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 10301.765028000165 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | ERROR | |
| migraphx_mlperf__resnet50_v1 | PASS | 204.17675000008884 | |
| migraphx_models__whisper-tiny-decoder | PASS | 293.0406349998975 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 1071.0625970000365 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1524.7376993333244 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1565.859735999993 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 12486.654938666712 | |
| migraphx_ORT__distilgpt2_1 | PASS | 744.9039293333044 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2521.2952923328276 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 10263.379780333555 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 627.6207299999138 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 56.494945846096904 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 4796.690031666761 | |
| migraphx_torchvision__inceptioni1 | PASS | 358.5608481667653 | |
| migraphx_torchvision__resnet50i1 | PASS | 192.98857341671768 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_384 | PASS | ERROR | |
| migx_bench_bert-large-uncased_2_128 | PASS | ERROR | |
| migx_bench_bert-large-uncased_2_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_2_384 | PASS | ERROR | |
| migx_bench_bert-large-uncased_32_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_32_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_32_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_4_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_4_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_4_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_8_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_8_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_8_384 | compiled_inference | None | |
