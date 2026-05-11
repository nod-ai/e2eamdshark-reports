## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 36 | 87.8% | 87.8% |
| Gold Inference | 36 | 87.8% | 100.0% |
| IREE Inference Invocation | 19 | 46.3% | 52.8% |
| Inference Comparison (PASS) | 14 | 34.1% | 73.7% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 5 | 12.2% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 17 | 41.5% |
| Inference Comparison | 5 | 12.2% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | ERROR | |
| migraphx_cadene__dpn92i1 | compilation | None | |
| migraphx_cadene__inceptionv4i16 | compilation | None | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 776.5217573323753 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 11232.968449005662 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | ERROR | |
| migraphx_mlperf__resnet50_v1 | PASS | 253.99978616527127 | |
| migraphx_models__whisper-tiny-decoder | PASS | 441.2798226670323 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 2899.145428663663 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1787.8006236666504 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1712.6862036626942 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 20330.215221998515 | |
| migraphx_ORT__distilgpt2_1 | PASS | 830.5962903298981 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 988.6070306626303 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 5319.357400658191 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 495.6472445046529 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 261.8643099970844 | |
| migraphx_pytorch-examples__wlang_lstm | PASS | 22.12931807055914 | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | compilation | None | |
| migraphx_torchvision__inceptioni1 | PASS | 412.41919966948143 | |
| migraphx_torchvision__resnet50i1 | PASS | 188.50413508577427 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_2_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_2_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_2_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_32_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_32_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_32_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_4_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_4_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_4_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_8_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_8_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_8_384 | compiled_inference | None | |
