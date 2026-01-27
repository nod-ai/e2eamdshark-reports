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
| migraphx_bert__bert-large-uncased | PASS | 12.634028528224336 | |
| migraphx_cadene__dpn92i1 | PASS | 2.9890183332851126 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 19.956077032145995 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.457256784927456 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.2371351926289895 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.702922811524733 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.2962708953714 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.220011096493693 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.39066647572649 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.62653110140843 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 282.167033602794 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.37432216604551 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.10806601991256 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 285.94090013454354 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.81275984976026 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.546245905881126 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.3947983636101857 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8958121554942817 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.18288398782412 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.98791471336569 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.87573379431015 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.780431980474127 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.47739424884674 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.838358477209553 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.40089442036305 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.771852675712468 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.416623999979217 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.733434873096865 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.56401138639811 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.6040106358982 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.694196007920032 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.367113003925398 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.29059080495721 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.35160293516253 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.573905687413966 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.11045032346414 | |
