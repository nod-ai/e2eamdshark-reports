## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 27 | 65.9% | 69.2% |
| Inference Comparison (PASS) | 22 | 53.7% | 81.5% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 12 | 29.3% |
| Inference Comparison | 5 | 12.2% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | ERROR | |
| migraphx_cadene__dpn92i1 | PASS | 438.7367831667082 | |
| migraphx_cadene__inceptionv4i16 | PASS | 9021.581220333548 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 815.5666903330712 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 10152.964973666712 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | ERROR | |
| migraphx_mlperf__resnet50_v1 | PASS | 196.45719233327932 | |
| migraphx_models__whisper-tiny-decoder | PASS | 296.66887900035965 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 1423.1732310002674 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1526.5667199995125 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1520.2142739996514 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 12450.636115999865 | |
| migraphx_ORT__distilgpt2_1 | PASS | 752.8725986667268 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2523.9820169993736 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 10243.306117666785 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 671.5233103332139 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 57.04447441669597 | |
| migraphx_pytorch-examples__wlang_lstm | PASS | 32.24390634914882 | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 4948.393974666335 | |
| migraphx_torchvision__inceptioni1 | PASS | 355.3275476666992 | |
| migraphx_torchvision__resnet50i1 | PASS | 198.3431555002729 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_384 | PASS | ERROR | |
| migx_bench_bert-large-uncased_2_128 | PASS | ERROR | |
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
