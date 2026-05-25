## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 39 | 95.1% | 100.0% |
| Inference Comparison (PASS) | 32 | 78.0% | 82.1% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 7 | 17.1% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 310.1648308333438 | |
| migraphx_cadene__dpn92i1 | PASS | 221.00145299999792 | |
| migraphx_cadene__inceptionv4i16 | PASS | 4993.548183666651 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 169.85604433336712 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 205.28738933333238 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 376.6294268333657 | |
| migraphx_mlperf__resnet50_v1 | PASS | 84.19549683334064 | |
| migraphx_models__whisper-tiny-decoder | PASS | 27.078232948715947 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 242.4910571110988 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 47.444348923075715 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 48.71417325641147 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 172.58019299999697 | |
| migraphx_ORT__distilgpt2_1 | PASS | 23.51925301149481 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 51.21454069697248 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 165.287798333343 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 18.616792280702636 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 71.03773196667285 | |
| migraphx_pytorch-examples__wlang_lstm | PASS | 7.857244647730319 | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 491.9470996666557 | |
| migraphx_torchvision__inceptioni1 | PASS | 156.36531475003795 | |
| migraphx_torchvision__resnet50i1 | PASS | 86.75607304164146 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 1433.7319616665052 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 2870.7469533333856 | |
| migx_bench_bert-large-uncased_16_384 | Numerics | 4266.9880906667 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 116.14564233333465 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 228.65378233334215 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 306.549326333311 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 222.70777644442 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 389.01051250002183 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 573.6545040000843 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 2696.720814333427 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 5516.385049666799 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 8405.654153333368 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 390.32621133333123 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 732.0457650001421 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 1236.2185570000293 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 723.4183609997066 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 1402.4248646666517 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 2006.7716913331424 | |
