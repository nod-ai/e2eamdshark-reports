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
| migraphx_cadene__dpn92i1 | PASS | 437.08822016670484 | |
| migraphx_cadene__inceptionv4i16 | PASS | 8760.508766333334 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 807.1925583333647 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 10474.37530066668 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | ERROR | |
| migraphx_mlperf__resnet50_v1 | PASS | 163.13915349995037 | |
| migraphx_models__whisper-tiny-decoder | PASS | 294.47515666667334 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 1432.145384666531 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 1597.9897956666584 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 1589.3946226666742 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 12896.741071666629 | |
| migraphx_ORT__distilgpt2_1 | PASS | 738.1373253333171 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 2507.9459413333702 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 10140.874816666648 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 615.5751223333065 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 55.41657207691176 | |
| migraphx_pytorch-examples__wlang_lstm | PASS | 35.57527198413048 | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 3541.0457596667584 | |
| migraphx_torchvision__inceptioni1 | PASS | 357.26077350000196 | |
| migraphx_torchvision__resnet50i1 | PASS | 200.38249766667425 | |
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
