## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 97.4% |
| Inference Comparison (PASS) | 28 | 68.3% | 75.7% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.4% |
| Inference Comparison | 9 | 22.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.63533075637367 | |
| migraphx_cadene__dpn92i1 | Numerics | 10.141629180760079 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.886574824141764 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.103575895574159 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.2182160349789255 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.671305582354154 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.833467764819554 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.870403999615068 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.81044767302875 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.83775052844015 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 284.64608133557095 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.58964858654912 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 75.33361492850989 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 295.0061446657249 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 40.263408801847085 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.576646173736663 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.74063947474739 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.675539259656539 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.7168760742997935 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.25063767546921 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.0289646360417 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.88494040899409 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.747970771587765 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.465598036214942 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.843345775565302 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.461353684990343 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.757408048844697 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.367104952261611 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.74791873960092 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.526376029977456 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.428228001332 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.67427369761704 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.331553992181762 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.19984251403782 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.319738197547451 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.559634126245736 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.107847513740932 | |
