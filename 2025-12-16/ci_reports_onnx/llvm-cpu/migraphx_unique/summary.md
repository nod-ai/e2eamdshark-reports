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
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 28251.689860333234 | |
| migraphx_cadene__dpn92i1 | PASS | 401.83480733340576 | |
| migraphx_cadene__inceptionv4i16 | PASS | 11891.451931666552 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 830.0772639999346 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7256.862360999927 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | ERROR | |
| migraphx_mlperf__resnet50_v1 | PASS | 205.98120322220993 | |
| migraphx_models__whisper-tiny-decoder | PASS | 317.6959445000496 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 803.8981769999131 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1307.7803179999705 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1453.2326986666437 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 14062.522310333332 | |
| migraphx_ORT__distilgpt2_1 | PASS | 556.9689670000267 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2230.5019483333126 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 13086.721083000042 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 498.0605356666577 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 53.511891102586496 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 5679.4950243333915 | |
| migraphx_torchvision__inceptioni1 | PASS | 350.79163399996105 | |
| migraphx_torchvision__resnet50i1 | PASS | 227.7444897777564 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | 29174.588979666627 | |
| migx_bench_bert-large-uncased_1_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_384 | PASS | 30902.031939666816 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 21657.43698899981 | |
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
