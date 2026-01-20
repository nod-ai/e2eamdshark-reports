## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 36 | 87.8% | 94.7% |
| Inference Comparison (PASS) | 28 | 68.3% | 77.8% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 8 | 19.5% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.670014186226055 | |
| migraphx_cadene__dpn92i1 | Numerics | 3.109136887446598 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.075957126738057 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.4803160778625277 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.240201125747151 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.77898155649503 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.085515373831859 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.912854602031498 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.66517533092862 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.21766058728099 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 282.87310114440817 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.80611836558415 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 71.88730241420367 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 285.8048566461851 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.80232677760499 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.591564605633415 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.4331874769741018 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9044309485015338 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.22054483670564 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.988588074370035 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.874089018943216 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.803417218228182 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.459691048466732 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.813072022276394 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.502071494790945 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.80476777729663 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.413233415610122 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.757579185068604 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.53323030042828 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.29691176222902 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.695913330059158 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.338889213114165 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.3203169451583 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.388594608500497 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.539911281244425 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.114490032144303 | |
