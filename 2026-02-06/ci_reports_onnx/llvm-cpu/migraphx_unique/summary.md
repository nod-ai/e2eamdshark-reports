## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 22 | 53.7% | 56.4% |
| Inference Comparison (PASS) | 17 | 41.5% | 77.3% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 17 | 41.5% |
| Inference Comparison | 5 | 12.2% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | ERROR | |
| migraphx_cadene__dpn92i1 | PASS | 1043.0582909987909 | |
| migraphx_cadene__inceptionv4i16 | PASS | 16394.059952332704 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 1045.494916999208 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 11638.367109000683 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | ERROR | |
| migraphx_mlperf__resnet50_v1 | PASS | 451.58191733571584 | |
| migraphx_models__whisper-tiny-decoder | PASS | 604.0575363319173 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 2337.25899433072 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1652.0765756655844 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1614.76416766709 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 24664.81966566668 | |
| migraphx_ORT__distilgpt2_1 | PASS | 856.480483666625 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2539.1314680006567 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 7368.232740666524 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 561.7193126660519 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 185.48958988847312 | |
| migraphx_pytorch-examples__wlang_lstm | PASS | 44.731112974542874 | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 6722.048037999532 | |
| migraphx_torchvision__inceptioni1 | PASS | 436.7603591654188 | |
| migraphx_torchvision__resnet50i1 | PASS | 251.36002455514645 | |
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
