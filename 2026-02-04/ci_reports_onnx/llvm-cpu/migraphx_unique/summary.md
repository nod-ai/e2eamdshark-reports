## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 39 | 95.1% | 100.0% |
| Inference Comparison (PASS) | 32 | 78.0% | 82.1% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 7 | 17.1% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 175.463626416672 | |
| migraphx_cadene__dpn92i1 | PASS | 200.30381433332423 | |
| migraphx_cadene__inceptionv4i16 | PASS | 4166.381392000024 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 153.9349343333318 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 154.38324891666372 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 237.39276199998787 | |
| migraphx_mlperf__resnet50_v1 | PASS | 84.718430374996 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.75261405128373 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 38.99042455555833 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 59.48199766666466 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 58.85078676666447 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 194.58857511110259 | |
| migraphx_ORT__distilgpt2_1 | PASS | 19.7531205882342 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 99.82118022222467 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 304.0158841666596 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 18.48508876923381 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 34.435080116675934 | |
| migraphx_pytorch-examples__wlang_lstm | PASS | 18.3664855526291 | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 417.34343766665916 | |
| migraphx_torchvision__inceptioni1 | PASS | 166.96044325002882 | |
| migraphx_torchvision__resnet50i1 | PASS | 156.59918091667652 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 729.7448663332489 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 1340.9129413334238 | |
| migx_bench_bert-large-uncased_16_384 | Numerics | 2001.9240336666069 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 77.48970518518607 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 130.33108666663793 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 177.32694791667805 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 136.12881006664185 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 219.4795961111645 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 302.0817880000095 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 1332.5664416666616 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 2573.723868333218 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 3820.679225999887 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 216.31788555552905 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 405.54184600004345 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 635.6102376666968 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 403.95958966663176 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 723.1293413332575 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 1068.8083106666302 | |
