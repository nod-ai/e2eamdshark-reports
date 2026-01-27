## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 27 | 65.9% | 69.2% |
| Inference Comparison (PASS) | 22 | 53.7% | 81.5% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 12 | 29.3% |
| Inference Comparison | 5 | 12.2% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | ERROR | |
| migraphx_cadene__dpn92i1 | PASS | 463.1181281666841 | |
| migraphx_cadene__inceptionv4i16 | PASS | 8978.720375666664 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 845.5735696666883 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 10005.712112999996 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | ERROR | |
| migraphx_mlperf__resnet50_v1 | PASS | 217.60150677778256 | |
| migraphx_models__whisper-tiny-decoder | PASS | 325.5797841666966 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 1165.8648343332818 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1553.1070793333395 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1574.951773333339 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 12562.625073333342 | |
| migraphx_ORT__distilgpt2_1 | PASS | 789.6654320000115 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2431.7581200000022 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 8379.052645666736 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 589.8357739999558 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 75.98701851849101 | |
| migraphx_pytorch-examples__wlang_lstm | PASS | 54.58168258336273 | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 5065.984454333223 | |
| migraphx_torchvision__inceptioni1 | PASS | 375.36023483331365 | |
| migraphx_torchvision__resnet50i1 | PASS | 207.3429719999543 | |
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
