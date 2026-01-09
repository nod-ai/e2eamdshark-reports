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
| migraphx_bert__bert-large-uncased | PASS | 12.62263506872668 | |
| migraphx_cadene__dpn92i1 | PASS | 9.862032548432618 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.856908026772242 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.0702893289103015 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.2452383007073315 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.652905322059436 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.11658132340468 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.684751616215994 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.13925414449638 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.64883723925975 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 284.3111710002025 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.82458734595113 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 71.74765231708686 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.453280908366 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.681702895296944 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 15.196790918707846 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.746926898248176 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.628683419963507 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.7057698528550067 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.285227451296077 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.52474926837853 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.46490373825416 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.809739677442444 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.540769996121526 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.878617779775098 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.432173382313477 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.764713563250773 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.451002999622787 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.269068316302516 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.57050681972141 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 97.05810355288641 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.72972411278522 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.36627344513426 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.298196818856965 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.398968189346546 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.60324207459595 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.375282659505803 | |
