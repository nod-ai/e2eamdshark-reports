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
| migraphx_bert__bert-large-uncased | PASS | 28532.566236666677 | |
| migraphx_cadene__dpn92i1 | PASS | 410.5578914999721 | |
| migraphx_cadene__inceptionv4i16 | PASS | 8439.148535666542 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 837.479870999914 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7600.552554666516 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 31260.804940999835 | |
| migraphx_mlperf__resnet50_v1 | PASS | 243.11552466669025 | |
| migraphx_models__whisper-tiny-decoder | PASS | 245.4965567777789 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 838.2573446665447 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1522.032460333321 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1330.815591666692 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 10838.676967666666 | |
| migraphx_ORT__distilgpt2_1 | PASS | 588.121906666629 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2213.2745943332943 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 7861.719954333391 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 491.0939353333106 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 50.01516988096725 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 5188.777121666741 | |
| migraphx_torchvision__inceptioni1 | PASS | 380.52150433334947 | |
| migraphx_torchvision__resnet50i1 | PASS | 208.3503691110814 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | 21131.64888133315 | |
| migx_bench_bert-large-uncased_1_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_384 | PASS | 30014.976331999907 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 20709.937395666504 | |
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
