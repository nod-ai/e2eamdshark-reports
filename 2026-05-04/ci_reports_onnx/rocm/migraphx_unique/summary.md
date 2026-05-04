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
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.633919395046263 | |
| migraphx_cadene__dpn92i1 | PASS | 3.4429175452804013 | |
| migraphx_cadene__inceptionv4i16 | PASS | 18.3593053146053 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.663124394732424 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.204085701306787 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.451718871197144 | |
| migraphx_mlperf__resnet50_v1 | Numerics | 14.580018310678293 | |
| migraphx_models__whisper-tiny-decoder | PASS | 24.724754761250335 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.95736709143966 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 97.71289038915363 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 98.50434079167566 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 325.9408501520132 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.13324968302104 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 76.0731089696357 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 279.96044739848 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.63359947205969 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 15.007290833114466 | |
| migraphx_pytorch-examples__wlang_lstm | PASS | 5.469440133310854 | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 12.908795741415455 | |
| migraphx_torchvision__inceptioni1 | PASS | 4.053679264154148 | |
| migraphx_torchvision__resnet50i1 | PASS | 2.170689462158364 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.1712983793446 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.873689470487456 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.618814683304386 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.796851200698358 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.512432281038768 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.88452240088108 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.412488185501063 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.774092828939585 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.418801846343795 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.639269680123437 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.364467545045585 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.88535957681457 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.695394726611221 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.353723771280931 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.23236582255257 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.342057871866691 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.53850440892811 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.036190047109912 | |
