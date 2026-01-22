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
| migraphx_bert__bert-large-uncased | PASS | 12.657238636165857 | |
| migraphx_cadene__dpn92i1 | PASS | 3.0344519416277094 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.11938171372527 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.457613232191543 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.2426217579350025 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.580082243515385 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.078780406438709 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.521767981074472 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.27092271049817 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.93089920424279 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 282.76188112795353 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.726826053112745 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.1270352602005 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 285.83726907769835 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.7617887377187 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.57885922367374 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.4318401119093482 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9028593094970396 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.256008207798004 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.90618347033622 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.77690002780695 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.764701869752672 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.512498546303028 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.866970422593027 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.397928250550526 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.836313473455832 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.4420037459996 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.676429634292916 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.47933519925132 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.51624430432206 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.710075893185355 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.323967021136056 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.30168243629091 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.384174390005418 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.620788776260966 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.060324653983116 | |
