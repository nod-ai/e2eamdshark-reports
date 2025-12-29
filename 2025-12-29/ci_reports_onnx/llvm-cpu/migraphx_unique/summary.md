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
| migraphx_bert__bert-large-uncased | PASS | ERROR | |
| migraphx_cadene__dpn92i1 | PASS | 468.52885599999655 | |
| migraphx_cadene__inceptionv4i16 | PASS | 8774.24300866672 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 1117.4154353331382 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7605.805085666664 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 32604.835136666832 | |
| migraphx_mlperf__resnet50_v1 | PASS | 203.61526155551874 | |
| migraphx_models__whisper-tiny-decoder | PASS | 260.93194133333475 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 1028.171291666543 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1356.8422966667033 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1338.076744333345 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 10930.451642333233 | |
| migraphx_ORT__distilgpt2_1 | PASS | 579.3080830000387 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2299.523450666584 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 8793.142538333086 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 492.5134856666015 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 49.40343673810535 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 4851.999702666641 | |
| migraphx_torchvision__inceptioni1 | PASS | 355.22417883354746 | |
| migraphx_torchvision__resnet50i1 | PASS | 196.51942566648964 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | 23584.793696333083 | |
| migx_bench_bert-large-uncased_1_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_384 | PASS | 32384.985682000053 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 23740.97096100013 | |
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
