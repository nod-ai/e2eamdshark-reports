## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 94.9% |
| Inference Comparison (PASS) | 31 | 75.6% | 83.8% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 6 | 14.6% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.6995436282772 | |
| migraphx_cadene__dpn92i1 | PASS | 2.9164571629339426 | |
| migraphx_cadene__inceptionv4i16 | PASS | 19.619420877899284 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.3646092822652753 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.295108387483559 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.93600244944294 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.000299867638882 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.738760127232243 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.93302939480377 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.09040439590102 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 100.06688881133283 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 292.2382227455576 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.31557889117135 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.47420746336381 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 287.61561370144284 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.24641524510527 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.415977063744016 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.3735698723317817 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8794913141226228 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.398866727619488 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.408645998745676 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.403731176104294 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.820744847257933 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.48716741212688 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.897380877769102 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.450623583780335 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.856137030052414 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.471171088009868 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.15336891342744 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.63954639717033 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 96.56449943958292 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.794175055442432 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.350462204390235 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.438026413138882 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.387122428260083 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.67228758652859 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.379201639029713 | |
