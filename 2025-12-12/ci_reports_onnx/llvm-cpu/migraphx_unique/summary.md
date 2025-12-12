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
| migraphx_bert__bert-large-uncased | PASS | 30432.960423000015 | |
| migraphx_cadene__dpn92i1 | PASS | 442.13547700000316 | |
| migraphx_cadene__inceptionv4i16 | PASS | 10309.37401066679 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 884.7426423333218 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7474.450138333395 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 30148.881318666783 | |
| migraphx_mlperf__resnet50_v1 | PASS | 213.87789855556446 | |
| migraphx_models__whisper-tiny-decoder | PASS | 226.03618833330881 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 713.4399726666439 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1116.903565999981 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1133.9850840000356 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 11027.444812666698 | |
| migraphx_ORT__distilgpt2_1 | PASS | 630.614022999983 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2803.9024086667723 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 8080.537021999968 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 749.0738840000782 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 42.600738058813384 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 5622.5964789999425 | |
| migraphx_torchvision__inceptioni1 | PASS | 337.58237783331424 | |
| migraphx_torchvision__resnet50i1 | PASS | 224.4040056666563 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | 20401.70951566673 | |
| migx_bench_bert-large-uncased_1_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_384 | PASS | 30241.040180000102 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 20584.820198333397 | |
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
