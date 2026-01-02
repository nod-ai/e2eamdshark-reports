## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 21 | 51.2% | 53.8% |
| Inference Comparison (PASS) | 16 | 39.0% | 76.2% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 18 | 43.9% |
| Inference Comparison | 5 | 12.2% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | ERROR | |
| migraphx_cadene__dpn92i1 | PASS | 812.9834413333205 | |
| migraphx_cadene__inceptionv4i16 | PASS | 15354.416775332842 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 1019.5760810008019 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 14701.136813666986 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | ERROR | |
| migraphx_mlperf__resnet50_v1 | PASS | 397.0700950006479 | |
| migraphx_models__whisper-tiny-decoder | PASS | 541.9739243322207 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 2414.787156667444 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1874.7268589989592 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1761.2892866679128 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 20304.584019000686 | |
| migraphx_ORT__distilgpt2_1 | PASS | 894.4114109993583 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2615.2036159995378 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 14116.609724999458 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 650.2703513318313 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 99.34522472233057 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 5099.079600999781 | |
| migraphx_torchvision__inceptioni1 | PASS | 371.22339083331707 | |
| migraphx_torchvision__resnet50i1 | PASS | 214.16493744497225 | |
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
