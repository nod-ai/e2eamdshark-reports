## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 97.4% |
| Inference Comparison (PASS) | 28 | 68.3% | 75.7% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.4% |
| Inference Comparison | 9 | 22.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.620771375839553 | |
| migraphx_cadene__dpn92i1 | Numerics | 10.112570607719789 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.886122830134507 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.123860241376865 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.221989388036769 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.56469193963265 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.86858326598262 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.75501351168862 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.77805920690298 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.28563549369574 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.09514420107007 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.3175460514095 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 75.68137054504066 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 294.73718053971726 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 40.05735692586385 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.358001729460801 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.686930624768134 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.655832069089212 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.717141765902968 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.27739274005095 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.89280410501218 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.73567092667023 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.74410429990126 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.432084235894893 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.819687040014701 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.464747581231807 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.729093996864377 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.378017410129104 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.66132633376753 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.48704457463639 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.3621029676426 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.685355448135823 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.380593670113962 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.330154318727697 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.377874486959302 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.60407760790458 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.05407304772072 | |
