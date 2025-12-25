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
| migraphx_bert__bert-large-uncased | PASS | 28795.33900133337 | |
| migraphx_cadene__dpn92i1 | PASS | 522.2398333333255 | |
| migraphx_cadene__inceptionv4i16 | PASS | 8428.575101333421 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 802.1274976666367 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7353.978738333278 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 31306.218268333247 | |
| migraphx_mlperf__resnet50_v1 | PASS | 244.35432666670445 | |
| migraphx_models__whisper-tiny-decoder | PASS | 242.84088444442708 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 728.9896373332946 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1269.9801973333251 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1266.5540620000115 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 10907.376434333324 | |
| migraphx_ORT__distilgpt2_1 | PASS | 548.274863666658 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2230.3665796666032 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 7771.637228666653 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 765.2546446665838 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 54.32385076667287 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 4787.452057333363 | |
| migraphx_torchvision__inceptioni1 | PASS | 356.89181466682385 | |
| migraphx_torchvision__resnet50i1 | PASS | 231.21287433337378 | |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | None | |
| migx_bench_bert-large-uncased_16_384 | compiled_inference | None | |
| migx_bench_bert-large-uncased_1_128 | PASS | 22271.916013333033 | |
| migx_bench_bert-large-uncased_1_256 | PASS | ERROR | |
| migx_bench_bert-large-uncased_1_384 | PASS | 30665.494417000144 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 21435.33911333361 | |
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
