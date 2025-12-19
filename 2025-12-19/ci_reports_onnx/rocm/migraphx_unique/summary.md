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
| migraphx_bert__bert-large-uncased | PASS | 12.608616174908263 | |
| migraphx_cadene__dpn92i1 | Numerics | 10.098940737833434 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.967213785198208 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.0458494398486 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.21650517504035 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.666785141453147 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.085557354209215 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.082154639341212 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.90783321277962 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.11500464734576 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 285.1791465654969 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.759108409906425 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 75.54731590466366 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 295.23899421716726 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 40.19909534676402 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.594858479944781 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.737295137097437 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.658440301815669 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.694876325456343 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.28467272896142 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.318704289812885 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.266133376038994 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.794950399133894 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.490039203493367 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.84449222412976 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.390154593607834 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.825268100608477 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.428908873324083 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.07230631431395 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.11969431376818 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 96.1746736651375 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.710117238263289 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.405575390829116 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.311346375161694 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.374559079962118 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.57334850085717 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.210418682648903 | |
