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
| migraphx_bert__bert-large-uncased | PASS | 28046.26467397126 | |
| migraphx_cadene__dpn92i1 | PASS | 393.00380111671984 | |
| migraphx_cadene__inceptionv4i16 | PASS | 8368.703946277188 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 803.0094488834342 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 6992.148051969707 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 31392.11221501076 | |
| migraphx_mlperf__resnet50_v1 | PASS | 201.55389766053608 | |
| migraphx_models__whisper-tiny-decoder | PASS | 253.84796002051894 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 789.6000959832842 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1245.9499756805599 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1200.6124767164388 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 10788.760540386042 | |
| migraphx_ORT__distilgpt2_1 | PASS | 554.2141780412445 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2229.9273956644656 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 7411.87883397409 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 469.0731683319124 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 48.56869225235034 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 4739.917489001527 | |
| migraphx_torchvision__inceptioni1 | PASS | 351.8563646745558 | |
| migraphx_torchvision__resnet50i1 | PASS | 195.27533300182162 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | 20646.90145966597 | |
| migx_bench_bert-large-uncased_1_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_384 | PASS | 30012.207300945494 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 20798.57554628203 | |
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
