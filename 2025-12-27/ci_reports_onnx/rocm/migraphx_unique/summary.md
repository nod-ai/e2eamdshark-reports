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
| migraphx_bert__bert-large-uncased | PASS | 12.646925447153903 | |
| migraphx_cadene__dpn92i1 | PASS | 10.134714309658323 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 22.03172131946 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.14703452617627 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.275696898269694 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 21.178013268820564 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.084605569532814 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.61855449831044 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 114.08987211891345 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.86616162813844 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 287.41041974474984 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.24009251470367 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.16369571785131 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.2885839616259 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.136094644803684 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 17.156525574151484 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.818443477153778 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.72073445525812 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.734666672502214 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.294615936776 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.94656675675558 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 53.186501089770054 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.830960726628533 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.539484953906916 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.890595678286049 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.521141164359591 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.853574628631272 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.429843477702057 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.66871630242376 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 63.321280744716965 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 97.42462559647502 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.752349336038934 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.378546223956711 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.29507844930603 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.376720571953827 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.64629173015847 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.719592628276178 | |
