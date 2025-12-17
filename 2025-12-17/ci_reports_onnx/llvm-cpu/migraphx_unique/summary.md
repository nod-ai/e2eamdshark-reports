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
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 30472.94823399716 | |
| migraphx_cadene__dpn92i1 | PASS | 444.63421616577153 | |
| migraphx_cadene__inceptionv4i16 | PASS | 13399.970276999133 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 888.2731486616345 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 8187.984707998112 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 31460.017983670696 | |
| migraphx_mlperf__resnet50_v1 | PASS | 246.47698877702672 | |
| migraphx_models__whisper-tiny-decoder | PASS | 275.19144100248616 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 857.2762206652745 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1422.9141773321317 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1415.3898763349086 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 10516.655439663737 | |
| migraphx_ORT__distilgpt2_1 | PASS | 630.262734334489 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2370.6324706654414 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 8579.044750666071 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 548.6774523330192 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 51.78240030662169 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 6184.588388665968 | |
| migraphx_torchvision__inceptioni1 | PASS | 381.1940833317446 | |
| migraphx_torchvision__resnet50i1 | PASS | 217.71619711378457 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | 21189.392924330605 | |
| migx_bench_bert-large-uncased_1_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_384 | PASS | 30661.878748328792 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 20892.686662664346 | |
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
