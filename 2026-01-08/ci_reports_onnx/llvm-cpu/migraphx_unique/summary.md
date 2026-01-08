## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 26 | 63.4% | 66.7% |
| Inference Comparison (PASS) | 21 | 51.2% | 80.8% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 13 | 31.7% |
| Inference Comparison | 5 | 12.2% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 30014.734643333362 | |
| migraphx_cadene__dpn92i1 | PASS | 401.61968300018697 | |
| migraphx_cadene__inceptionv4i16 | PASS | 9472.4150476668 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 882.0448553333335 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7385.599593000127 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 31959.903062000347 | |
| migraphx_mlperf__resnet50_v1 | PASS | 222.12243133329443 | |
| migraphx_models__whisper-tiny-decoder | PASS | 242.77095844455388 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 768.9912463332197 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1283.488590333339 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1257.908885000082 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 10743.227450333356 | |
| migraphx_ORT__distilgpt2_1 | PASS | 680.6086019999688 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2260.660565000004 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 7583.026297999974 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 484.40234366686735 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 49.708455380921016 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 4901.57533333316 | |
| migraphx_torchvision__inceptioni1 | PASS | 347.91446950013477 | |
| migraphx_torchvision__resnet50i1 | PASS | 233.39666222232657 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | 21210.393749333583 | |
| migx_bench_bert-large-uncased_1_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_384 | PASS | 30157.673287666814 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 20819.872023333723 | |
| migx_bench_bert-large-uncased_2_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_2_384 | PASS | ERROR | |
| migx_bench_bert-large-uncased_32_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_32_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_32_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_4_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_4_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_4_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_8_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_8_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_8_384 | compiled_inference | None | |
