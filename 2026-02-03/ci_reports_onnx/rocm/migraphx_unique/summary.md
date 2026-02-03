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
| migraphx_bert__bert-large-uncased | PASS | 12.623615950966872 | |
| migraphx_cadene__dpn92i1 | PASS | 9.851185246392594 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.817960718180984 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.084960574905076 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.234735811238026 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.546588934544058 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.082646993563529 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.25156345448376 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.44966410514381 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.20465074266707 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.0463017647465 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.611443205840054 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.26928900927305 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 285.52608098834753 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.727731340461304 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 15.009585379933318 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.71964283349613 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.630545659965237 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.678376688376853 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.24312235769771 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.76293195547565 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.363966738184295 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.78292143676016 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.469164506044415 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.846822370633936 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.479272593433656 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.765536017038606 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.375377598465704 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.558755503007855 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.15306947718966 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 94.66821274587086 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.712089096506434 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.336506246912235 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.282841296423047 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.36450470517687 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.496820939668254 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 28.958956348813242 | |
