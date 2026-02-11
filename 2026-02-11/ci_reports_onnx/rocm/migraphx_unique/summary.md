## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 94.9% |
| Inference Comparison (PASS) | 31 | 75.6% | 83.8% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 6 | 14.6% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.692233005707912 | |
| migraphx_cadene__dpn92i1 | PASS | 2.909079722204808 | |
| migraphx_cadene__inceptionv4i16 | PASS | 19.654499841164107 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.3534595257950572 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.244326753535426 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.589021939922258 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.900984506763463 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.875531734875683 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.94786275054018 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 99.56259967847949 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 99.61657297043571 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 292.78526129201055 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.32866816429628 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.67206287756562 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 288.2355082159241 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.69016759994405 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.4279097855712 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.329039438967667 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8534959848732389 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.404955783091925 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.877015690363585 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 53.134136546689724 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.791993242998918 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.536134631816473 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 24.389007634678737 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 29.4751964309918 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.767989448074138 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.449655349987248 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.595386968530484 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.83986128189347 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 97.13619140287238 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.720252466246935 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.37830177395522 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.435505720111085 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.386707853500532 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.752050776911133 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.653496445260114 | |
