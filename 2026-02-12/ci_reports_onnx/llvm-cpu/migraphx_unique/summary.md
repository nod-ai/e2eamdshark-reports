## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 39 | 95.1% | 100.0% |
| Inference Comparison (PASS) | 32 | 78.0% | 82.1% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 7 | 17.1% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 178.2493046666739 | |
| migraphx_cadene__dpn92i1 | PASS | 200.36749299998112 | |
| migraphx_cadene__inceptionv4i16 | PASS | 4482.899433333349 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 147.52511573336352 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 161.60652133333048 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 259.1584375555587 | |
| migraphx_mlperf__resnet50_v1 | PASS | 119.81815055555165 | |
| migraphx_models__whisper-tiny-decoder | PASS | 28.226532833337924 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 202.7579484444383 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 68.10642914814689 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 64.26394423333193 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 189.20756855555965 | |
| migraphx_ORT__distilgpt2_1 | PASS | 20.437043019608513 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 106.02739422222068 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 315.71099700000593 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 19.585256107843946 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 35.19773248332854 | |
| migraphx_pytorch-examples__wlang_lstm | PASS | 19.71703525000142 | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 1763.7182189999596 | |
| migraphx_torchvision__inceptioni1 | PASS | 168.46296775001215 | |
| migraphx_torchvision__resnet50i1 | PASS | 134.28777783335968 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 713.4668793334337 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 1396.6904086667757 | |
| migx_bench_bert-large-uncased_16_384 | Numerics | 2065.351081333271 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 77.96948970371886 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 130.62823460001405 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 181.23451641667998 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 137.50708379995254 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 226.66256099996136 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 314.4919578333353 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 1347.567161666575 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 2669.2849280000246 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 4062.060532333438 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 216.97157966660697 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 392.82814833332696 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 642.816397333263 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 397.601839999993 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 735.7718846668225 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 1104.3447676665892 | |
