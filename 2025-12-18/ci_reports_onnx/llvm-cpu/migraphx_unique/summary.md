## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 18 | 43.9% | 46.2% |
| Inference Comparison (PASS) | 14 | 34.1% | 77.8% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 21 | 51.2% |
| Inference Comparison | 4 | 9.8% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | compiled_inference | None | |
| migraphx_cadene__dpn92i1 | PASS | 595.6335670001256 | |
| migraphx_cadene__inceptionv4i16 | PASS | 12909.324792332882 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 1293.959807999272 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 15344.240701333243 | |
| migraphx_mlperf__bert_large_mlperf | compiled_inference | None | |
| migraphx_mlperf__resnet50_v1 | PASS | 548.3999243333528 | |
| migraphx_models__whisper-tiny-decoder | PASS | 372.6379325000077 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 1653.987984666249 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1947.771040666339 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1931.3084749998477 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | ERROR | |
| migraphx_ORT__distilgpt2_1 | PASS | 1033.8233083336186 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2777.6295586666797 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 12855.119092333553 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 641.73871000033 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 133.32027874988245 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 6604.195830666565 | |
| migraphx_torchvision__inceptioni1 | PASS | 492.4882418334467 | |
| migraphx_torchvision__resnet50i1 | PASS | 276.5113093333235 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_2_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_2_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_2_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_32_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_32_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_32_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_4_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_4_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_4_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_8_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_8_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_8_384 | compiled_inference | None | |
