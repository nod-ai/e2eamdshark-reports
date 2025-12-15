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
| migraphx_bert__bert-large-uncased | PASS | 28906.661319333274 | |
| migraphx_cadene__dpn92i1 | PASS | 409.00775233334724 | |
| migraphx_cadene__inceptionv4i16 | PASS | 8484.976980333233 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 803.6746176668809 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7696.764750333311 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 31485.218360333267 | |
| migraphx_mlperf__resnet50_v1 | PASS | 206.44692733336947 | |
| migraphx_models__whisper-tiny-decoder | PASS | 250.7792240000223 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 765.6514723332748 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1315.4151770000149 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1268.9818913333397 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 11026.012648000005 | |
| migraphx_ORT__distilgpt2_1 | PASS | 593.9834593332686 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2436.738749333282 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 7697.386439999984 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 499.8259606666882 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 50.80342471428268 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 4882.805174333194 | |
| migraphx_torchvision__inceptioni1 | PASS | 350.76029566668393 | |
| migraphx_torchvision__resnet50i1 | PASS | 200.29951375007235 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | 20738.97944833364 | |
| migx_bench_bert-large-uncased_1_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_384 | PASS | 29898.61978233345 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 22412.20077500005 | |
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
