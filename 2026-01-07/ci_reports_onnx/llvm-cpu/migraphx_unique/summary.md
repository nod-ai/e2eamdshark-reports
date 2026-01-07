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
| migraphx_bert__bert-large-uncased | PASS | 29603.185970667862 | |
| migraphx_cadene__dpn92i1 | PASS | 409.3721339998713 | |
| migraphx_cadene__inceptionv4i16 | PASS | 11177.10824299987 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 950.9347486667442 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 8889.477133000884 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 31660.356899999897 | |
| migraphx_mlperf__resnet50_v1 | PASS | 270.47144466632744 | |
| migraphx_models__whisper-tiny-decoder | PASS | 267.6569683329338 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 763.0812920003033 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1312.7200016660936 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1494.9533263346286 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 10028.262481000638 | |
| migraphx_ORT__distilgpt2_1 | PASS | 720.3093433327012 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2386.3080693336087 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 8569.951979333078 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 571.0695170006753 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 53.32469925638296 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 6722.239316333798 | |
| migraphx_torchvision__inceptioni1 | PASS | 366.610154166968 | |
| migraphx_torchvision__resnet50i1 | PASS | 229.58741899957303 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | 21037.474744000065 | |
| migx_bench_bert-large-uncased_1_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_384 | PASS | ERROR | |
| migx_bench_bert-large-uncased_2_128 | PASS | 23305.1776563334 | |
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
