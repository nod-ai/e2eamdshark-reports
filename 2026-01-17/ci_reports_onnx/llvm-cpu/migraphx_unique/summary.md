## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 26 | 63.4% | 66.7% |
| Inference Comparison (PASS) | 20 | 48.8% | 76.9% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 13 | 31.7% |
| Inference Comparison | 6 | 14.6% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | ERROR | |
| migraphx_cadene__dpn92i1 | Numerics | 430.80914883285004 | |
| migraphx_cadene__inceptionv4i16 | PASS | 8843.78840833233 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 814.8584806664682 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 9858.104430333697 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | ERROR | |
| migraphx_mlperf__resnet50_v1 | PASS | 201.7498585557607 | |
| migraphx_models__whisper-tiny-decoder | PASS | 289.39934299917996 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 1030.8742753331899 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1588.9739166662669 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1403.5413600001145 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 12470.551893333322 | |
| migraphx_ORT__distilgpt2_1 | PASS | 726.4706346674453 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2524.3073803333873 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 10424.45088733378 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 655.170946334086 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 58.71575958331555 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 4750.0306953334075 | |
| migraphx_torchvision__inceptioni1 | PASS | 344.1210806668096 | |
| migraphx_torchvision__resnet50i1 | PASS | 194.86294308292904 | |
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
