## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 36 | 87.8% | 94.7% |
| Inference Comparison (PASS) | 29 | 70.7% | 80.6% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 7 | 17.1% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.706956289934388 | |
| migraphx_cadene__dpn92i1 | PASS | 3.036709870567913 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.027069552313712 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.452065983661266 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.263251967548914 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.74556048711141 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.376720226545261 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.594620585993482 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.86231947855816 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.98186516690822 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 282.32896731545526 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.604643516242504 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 71.85115292668343 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.04595456272364 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.82939271904804 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.577197325105466 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.3997009933284184 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9051549885341006 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.299837259309633 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.79036721066823 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.53415103753408 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.809637633252278 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.510732847398943 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.901561035786145 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.516242163699296 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.812014985265153 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.443217174840619 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.42036782634077 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 60.927604974219285 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 94.5664954682191 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.74785359926296 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.386282372130017 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.369670992972804 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.384947539795013 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.584488926711035 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.05210469745927 | |
