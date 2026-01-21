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
| migraphx_bert__bert-large-uncased | PASS | 12.71876754860083 | |
| migraphx_cadene__dpn92i1 | PASS | 3.0821981382985997 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.177151014407475 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.527619337077779 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.284833457564161 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.9965549764179 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.07982648099246 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.525351943241223 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.8751854499181 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.24503838874044 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 286.5205450604359 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.30387967742151 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.46191824475923 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.70187263439095 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.21407461166382 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.678683235620458 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.4725556183722603 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9208504426064508 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.298954365508898 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.89990226262145 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 53.33475739910052 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.836730859289736 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.563564182658277 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.889737263321877 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.50675940398304 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.809300377513422 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.464319075664712 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.64206145523172 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 63.40546759240555 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 98.03004243544167 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.758800951820428 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.386392052785878 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.33967648943265 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.393526072404823 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.65178912644293 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.868015709022682 | |
