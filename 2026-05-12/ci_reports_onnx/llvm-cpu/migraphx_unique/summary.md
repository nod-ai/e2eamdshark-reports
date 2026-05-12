## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 36 | 87.8% | 87.8% |
| Gold Inference | 36 | 87.8% | 100.0% |
| IREE Inference Invocation | 24 | 58.5% | 66.7% |
| Inference Comparison (PASS) | 19 | 46.3% | 79.2% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 5 | 12.2% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 12 | 29.3% |
| Inference Comparison | 5 | 12.2% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | ERROR | |
| migraphx_cadene__dpn92i1 | compilation | None | |
| migraphx_cadene__inceptionv4i16 | compilation | None | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 740.8480950004256 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 10478.801204667736 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | ERROR | |
| migraphx_mlperf__resnet50_v1 | PASS | 213.18740177735484 | |
| migraphx_models__whisper-tiny-decoder | PASS | 262.75634411103965 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 1297.4921136671278 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1543.6178646656724 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1484.281298999728 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 13127.653459333791 | |
| migraphx_ORT__distilgpt2_1 | PASS | 701.0168509999252 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 1114.4509753339662 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 6493.456559332723 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 569.5657533342455 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 95.39548772227135 | |
| migraphx_pytorch-examples__wlang_lstm | PASS | 16.180000899210906 | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | compilation | None | |
| migraphx_torchvision__inceptioni1 | PASS | 340.77274216663983 | |
| migraphx_torchvision__resnet50i1 | PASS | 150.80019713362464 | |
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
