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
| migraphx_bert__bert-large-uncased | PASS | 12.68433647399599 | |
| migraphx_cadene__dpn92i1 | PASS | 2.908171050219615 | |
| migraphx_cadene__inceptionv4i16 | PASS | 19.60809963444869 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.3521689710601064 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.2562601417303085 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.61563547097501 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.898081950790491 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.46485759501839 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.42550652888086 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 99.4181279980001 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 99.35488214805012 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 290.79164657741785 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.132095201975766 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.59270385652779 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 287.30331112941104 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.88130122450766 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.360921638707318 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.301374943806285 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.859877876109547 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.34695265705095 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.0606915115837 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.83572527498771 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.734608581496609 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.468660594008506 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.87467843266549 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.402434457550969 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.825101659153447 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.461176508727172 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.803103784720097 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.93605799115065 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.68551981023377 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.724137769052476 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.380174872725187 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.41126084605268 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.38491819363062 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.71964620229076 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.180382973411014 | |
