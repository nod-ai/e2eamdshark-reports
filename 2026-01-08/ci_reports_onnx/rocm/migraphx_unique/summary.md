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
| migraphx_bert__bert-large-uncased | PASS | 12.631098673279796 | |
| migraphx_cadene__dpn92i1 | PASS | 10.060742182504152 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.942028872823965 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.077489402631055 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.246209724559816 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.60449051801805 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.082875523122324 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.730897247055427 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.74551631261905 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.63832588919571 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.2921538501978 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.640550761587086 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 71.95277971525987 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.2522962192694 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.68708207651421 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.176111694218383 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.747511823351186 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.682072156833278 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.697056612377654 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.28429822197982 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.93115420946999 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.582992172394036 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.802453413191769 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.533873674415403 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.824274859193599 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.416950781785303 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.790489795081541 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.439027477689338 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.672390460064914 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.47990714419972 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.19349428869428 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.72135328388575 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.400327198055324 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.290258739675796 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.414479613912349 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.536532808168264 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.043655816672572 | |
