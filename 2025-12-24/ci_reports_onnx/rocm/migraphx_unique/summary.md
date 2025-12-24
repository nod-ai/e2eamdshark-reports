## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 37 | 90.2% | 92.5% |
| Gold Inference | 37 | 90.2% | 100.0% |
| IREE Inference Invocation | 36 | 87.8% | 97.3% |
| Inference Comparison (PASS) | 28 | 68.3% | 77.8% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 3 | 7.3% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.4% |
| Inference Comparison | 8 | 19.5% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.653631124306807 | |
| migraphx_cadene__dpn92i1 | compilation | None | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.938050165772438 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.067915514496893 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.250662685029489 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.646266527060003 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.092415616233296 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.989450997224562 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.95666742242044 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.55690235218829 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 284.0062992957731 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.46744379090766 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.28736542165278 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.5182355356713 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.87070396363183 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.675380694421214 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.745829203253628 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.637707466831139 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.7045228069999645 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.28301501025756 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.1693547851746 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.16102631619344 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.804642555656406 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.46831849926994 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.898155585805206 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.488613914077478 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.827299772338433 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.434924925721825 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.924369053520035 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.85623805857065 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 96.0257113245981 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.738650416334467 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.36005547946813 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.30262141031962 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.346831693586443 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.583697147302185 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.20282704548703 | |
