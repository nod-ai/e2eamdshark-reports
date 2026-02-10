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
| migraphx_bert__bert-large-uncased | PASS | 12.724733234129168 | |
| migraphx_cadene__dpn92i1 | PASS | 2.916667089999793 | |
| migraphx_cadene__inceptionv4i16 | PASS | 19.644000981416966 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.3353839497332554 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.231062607794898 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.729836429986687 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.885987769416035 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.87039176558638 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.71065375250247 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 99.14284833662566 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 99.5796394223968 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 290.24720191955566 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.322582540412746 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.27040502677362 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 287.74788323789835 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.91661140584835 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.393988161347806 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.3340936644919332 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.855205374111206 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.36603156696348 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.24945080315783 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.096717656613926 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.79658506686489 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.538047734692336 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.906697567230387 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.433924024835939 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.808115136894314 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.469077344983816 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.96682477595679 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.06710489861893 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.65839073842479 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.747420776974069 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.394693051268453 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.35741905188736 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.40301431076867 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.681310198543702 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.207976741923222 | |
