## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 21 | 51.2% | 53.8% |
| Inference Comparison (PASS) | 16 | 39.0% | 76.2% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 18 | 43.9% |
| Inference Comparison | 5 | 12.2% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | ERROR | |
| migraphx_cadene__dpn92i1 | PASS | 861.5502310000617 | |
| migraphx_cadene__inceptionv4i16 | PASS | 9549.741798333343 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 1016.7834940002649 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 13755.61675133319 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | ERROR | |
| migraphx_mlperf__resnet50_v1 | PASS | 413.38132433323455 | |
| migraphx_models__whisper-tiny-decoder | PASS | 489.6271910001815 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 2454.5918286665556 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1824.6712473332234 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1751.181420000118 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 20195.67480633342 | |
| migraphx_ORT__distilgpt2_1 | PASS | 837.1257529999335 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2609.3986443335475 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 14059.855788999812 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 642.4110613332534 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 99.22585333320707 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 5088.25646833308 | |
| migraphx_torchvision__inceptioni1 | PASS | 369.1836634999011 | |
| migraphx_torchvision__resnet50i1 | PASS | 216.9015857776786 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | ERROR | |
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
