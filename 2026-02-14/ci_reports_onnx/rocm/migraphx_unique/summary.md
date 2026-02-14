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
| migraphx_bert__bert-large-uncased | PASS | 12.699965043275641 | |
| migraphx_cadene__dpn92i1 | PASS | 2.9122655139527542 | |
| migraphx_cadene__inceptionv4i16 | PASS | 19.64338920596573 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.3537947658196074 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.23320295989411 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.616736150864096 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.996278040269585 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.805992936646494 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.66544114591346 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 99.55252032904396 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 99.79718874785162 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 290.06911674514413 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.3441559034917 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.19336835170786 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 287.9763954939941 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.842586455521754 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.388106836006045 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.3364264545814386 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8642329922976328 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.3560629001289 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.13507553603913 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.92662333735288 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.785015489699113 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.483719708619725 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.913711823201103 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.453102368107508 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.84438677019242 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.451807567558319 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.897196997747272 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.92178981886668 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.51647970718996 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.76850341960336 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.41473649421922 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.38068090583764 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.403314114275837 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.683254206589623 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.21736059296462 | |
