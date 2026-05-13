## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 41 | 100.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | compilation | None | |
| migraphx_cadene__dpn92i1 | compilation | None | |
| migraphx_cadene__inceptionv4i16 | compilation | None | |
| migraphx_cadene__resnext101_64x4di1 | compilation | None | |
| migraphx_huggingface-transformers__bert_mrpc8 | compilation | None | |
| migraphx_mlperf__bert_large_mlperf | compilation | None | |
| migraphx_mlperf__resnet50_v1 | compilation | None | |
| migraphx_models__whisper-tiny-decoder | compilation | None | |
| migraphx_models__whisper-tiny-encoder | compilation | None | |
| migraphx_ORT__bert_base_cased_1 | compilation | None | |
| migraphx_ORT__bert_base_uncased_1 | compilation | None | |
| migraphx_ORT__bert_large_uncased_1 | compilation | None | |
| migraphx_ORT__distilgpt2_1 | compilation | None | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | compilation | None | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | compilation | None | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | compilation | None | |
| migraphx_pytorch-examples__wlang_gru | compilation | None | |
| migraphx_pytorch-examples__wlang_lstm | compilation | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | compilation | None | |
| migraphx_torchvision__inceptioni1 | compilation | None | |
| migraphx_torchvision__resnet50i1 | compilation | None | |
| migx_bench_bert-large-uncased_16_128 | compilation | None | |
| migx_bench_bert-large-uncased_16_256 | compilation | None | |
| migx_bench_bert-large-uncased_16_384 | compilation | None | |
| migx_bench_bert-large-uncased_1_128 | compilation | None | |
| migx_bench_bert-large-uncased_1_256 | compilation | None | |
| migx_bench_bert-large-uncased_1_384 | compilation | None | |
| migx_bench_bert-large-uncased_2_128 | compilation | None | |
| migx_bench_bert-large-uncased_2_256 | compilation | None | |
| migx_bench_bert-large-uncased_2_384 | compilation | None | |
| migx_bench_bert-large-uncased_32_128 | compilation | None | |
| migx_bench_bert-large-uncased_32_256 | compilation | None | |
| migx_bench_bert-large-uncased_32_384 | compilation | None | |
| migx_bench_bert-large-uncased_4_128 | compilation | None | |
| migx_bench_bert-large-uncased_4_256 | compilation | None | |
| migx_bench_bert-large-uncased_4_384 | compilation | None | |
| migx_bench_bert-large-uncased_8_128 | compilation | None | |
| migx_bench_bert-large-uncased_8_256 | compilation | None | |
| migx_bench_bert-large-uncased_8_384 | compilation | None | |
