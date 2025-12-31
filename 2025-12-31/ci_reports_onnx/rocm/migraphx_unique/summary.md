## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 97.4% |
| Inference Comparison (PASS) | 29 | 70.7% | 78.4% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.4% |
| Inference Comparison | 8 | 19.5% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.65828982418911 | |
| migraphx_cadene__dpn92i1 | PASS | 9.969501983496784 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.920042677569047 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.086649076230283 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.236694789065937 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.677092636092784 | |
| migraphx_mlperf__resnet50_v1 | PASS | 21.486916134811256 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.872546777037186 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 147.6125533847759 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.63437627211567 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 302.80038733811426 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.959917978021416 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 75.22422596984714 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 299.08571477668977 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.197772978460065 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.317463316834294 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.736681973716863 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.632834987570973 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.7018123421180706 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.252743314596866 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.89349294001503 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.59597932241666 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.804784511009023 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.481254468660888 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.851903937531238 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.412234582284109 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.792581204099184 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.413985623312847 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.5907247484464 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.27072920825219 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 94.7865010128312 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.729196442347584 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.351521320894461 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.280111113208388 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.352803809099456 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.527979868062424 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.037721691161597 | |
