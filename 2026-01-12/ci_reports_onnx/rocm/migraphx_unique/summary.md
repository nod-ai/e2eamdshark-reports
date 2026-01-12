## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 97.4% |
| Inference Comparison (PASS) | 29 | 70.7% | 78.4% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.4% |
| Inference Comparison | 8 | 19.5% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.626302583763994 | |
| migraphx_cadene__dpn92i1 | PASS | 9.8452453409702 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.15072533062526 | |
| migraphx_cadene__resnext101_64x4di1 | Numerics | 3.3188518901807242 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.240723991363319 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.694891075293224 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.114784591655798 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.864436463625342 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.9215657711029 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.95849872699803 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 284.0810436755419 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.47701869242721 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.01478481292725 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.3314483935634 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.65165018511039 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.736872892958898 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.608026042580605 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.4408515830542523 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9063555409429942 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.24158425629139 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.27049255844146 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.0900262471957 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.769252311852243 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.467600261082959 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.844305000070369 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.4253601146241 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.82359298431512 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.41711630849611 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.017020198206104 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.07240937334117 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 96.08925196031727 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.741785022345455 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.400970266789807 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.30683574931962 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.39177491987238 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.592452593001664 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.23968651642402 | |
