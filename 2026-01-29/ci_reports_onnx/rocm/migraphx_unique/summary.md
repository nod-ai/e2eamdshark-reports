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
| migraphx_bert__bert-large-uncased | PASS | 12.669292205210887 | |
| migraphx_cadene__dpn92i1 | PASS | 3.062519587825826 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 19.99835405676138 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.463052086314262 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.24473995671854 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.758492938819384 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.12811735164428 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.81021741584495 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.64471533811754 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.51019488416966 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 282.5671859706441 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.70040013723903 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.20487383504708 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.1537641535202 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.87066632217052 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.588256811723113 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.4071287399453247 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8964113403438123 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.273723435543832 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.98900536601506 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.77931616512629 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.778223121331798 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.51099147789535 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.895607780435201 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.379082311925133 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.821712311018596 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.409798888020774 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.7442843295408 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.60597006479898 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.41210824889795 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.726348401470617 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.375761835550776 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.319511865576107 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.386570752680706 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.609419756368094 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.104146537267496 | |
