## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 36 | 87.8% | 94.7% |
| Inference Comparison (PASS) | 28 | 68.3% | 77.8% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 8 | 19.5% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.728695083183771 | |
| migraphx_cadene__dpn92i1 | Numerics | 3.1569082826276174 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.198620611890437 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.5217002279566767 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.302571907383469 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.294853157940363 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.139757767848089 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.788040101574154 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.74117382284668 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.3688867512558 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 287.2826211775342 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.60887724399152 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.12864126389225 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.30867786705494 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.708545595269506 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.63815365654106 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.437932082489738 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8973175378208402 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.25329907469097 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 34.035879157720096 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 53.58076585122407 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.860731318277324 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.482043982128657 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.878801845804306 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.449471734552864 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.77876091048573 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.455198753802549 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.78891612139959 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 63.38148077272556 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 98.42130858894613 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.75612422631997 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.370972290635109 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.327963291064783 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.375904917108768 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.670334895269253 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.873263349549635 | |
