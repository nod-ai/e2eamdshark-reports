## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 97.4% |
| Inference Comparison (PASS) | 29 | 70.7% | 78.4% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.4% |
| Inference Comparison | 8 | 19.5% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.651245719329877 | |
| migraphx_cadene__dpn92i1 | PASS | 10.043215531278664 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 22.03233207304341 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.109176646324172 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.262132303386005 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.54214281230873 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.092664682273321 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.706820795646845 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 114.02006230006616 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.12108547417888 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 285.1475733332336 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.33749550705155 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.03194663549462 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.29038762301207 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.16015681224288 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 16.96963758201252 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.823693541507435 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.723476152242029 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.714366374139852 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.28464933059045 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.91041197178382 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 53.142589254257 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.846409195055399 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.500005352887369 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.853838904111674 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.426345864133465 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.869524013138175 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.409164752380375 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.584518857413165 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 63.246479032166064 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 97.34945722101698 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.743161923506044 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.378277724292 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.30442781923782 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.388759899250909 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.649841374845483 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.688511302487715 | |
