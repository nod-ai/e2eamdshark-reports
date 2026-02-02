## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 36 | 87.8% | 94.7% |
| Inference Comparison (PASS) | 29 | 70.7% | 80.6% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 7 | 17.1% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.775911593979053 | |
| migraphx_cadene__dpn92i1 | PASS | 2.962737439026227 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 19.808394213517506 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.3892260335310542 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.273343711758602 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.495355870850656 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.152321602015393 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.385093441256032 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.76177793782618 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 99.29949519712301 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 292.0947147843738 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.91130897382067 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.40697525565822 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 287.24834617848194 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.05291660447363 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.442192106197275 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.386965242810131 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8826273391139485 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.42481631004051 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.334082849915056 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.28647274466662 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.833842438619351 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.578057795984757 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.93144295176054 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.54755383845241 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.861771123874702 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.530745703571787 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.02098013946052 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.28737741934529 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 96.20343126533994 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.837592551879808 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.477043677794022 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.45623258705817 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.452974919954107 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.736979895873983 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.30865828723957 | |
