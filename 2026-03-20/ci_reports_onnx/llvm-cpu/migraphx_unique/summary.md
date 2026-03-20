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
| migraphx_cadene__dpn92i1 | PASS | 437.5316173333393 | |
| migraphx_cadene__inceptionv4i16 | PASS | 9331.199441333372 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 815.4422536665985 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 9731.401419666705 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | ERROR | |
| migraphx_mlperf__resnet50_v1 | PASS | 164.27698241667105 | |
| migraphx_models__whisper-tiny-decoder | PASS | 302.5712581666463 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 1436.8227753332878 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1580.8283929999998 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1554.7036753333523 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 12244.139598333351 | |
| migraphx_ORT__distilgpt2_1 | PASS | 728.7058516666699 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 1249.8873409999949 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 6994.2266323333415 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 623.134451666677 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 55.59349212820473 | |
| migraphx_pytorch-examples__wlang_lstm | PASS | 32.03383346033025 | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 3574.4530083332697 | |
| migraphx_torchvision__inceptioni1 | PASS | 368.24784533329574 | |
| migraphx_torchvision__resnet50i1 | PASS | 196.38417658336493 | |
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
