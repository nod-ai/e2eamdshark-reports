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
| migraphx_bert__bert-large-uncased | PASS | 12.6668155419104 | |
| migraphx_cadene__dpn92i1 | PASS | 2.894094090693253 | |
| migraphx_cadene__inceptionv4i16 | PASS | 19.591228519048954 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.3281671160805053 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.220434914647099 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.327046694578947 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.844450452331953 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.526078095958553 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.3281033295724 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 98.76760343710579 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 99.63465535214966 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 289.190085294346 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.34026840784483 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.33135599146286 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 287.66838647425175 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.70486230072048 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.2954843326555 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.327848736967709 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8609997317696927 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.3207245315699 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.23085508531048 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.18023892778617 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 13.33803352382448 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.434546403320773 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.877364772738831 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.487171062578755 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.788462864630148 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.460303218794515 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.960362370944377 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.227027547178835 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.9753445571377 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.701697444373911 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.409977765310378 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.37429493651086 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.386863010574361 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.66272141083199 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.196769594111373 | |
