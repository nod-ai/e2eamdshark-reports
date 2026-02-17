## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 94.9% |
| Inference Comparison (PASS) | 31 | 75.6% | 83.8% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 6 | 14.6% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.722613109332142 | |
| migraphx_cadene__dpn92i1 | PASS | 2.8997893325397084 | |
| migraphx_cadene__inceptionv4i16 | PASS | 19.600363586235925 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.3667725381734956 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.307633245523852 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.26452613728387 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.014772362848547 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.917102065351273 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.66887318177355 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 99.89485410707336 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 99.34387400391556 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 293.2685470829407 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.47271474036905 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.66844012588263 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 288.08759773770964 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.984719939805835 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.43208826519549 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.381075237481891 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8740973967054844 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.425153914473807 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.24831696966337 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.20841850416783 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.819782356421152 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.541884955550943 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.963155491484535 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.439008269991193 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.886771221052514 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.460849658060233 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.93851190647392 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.1760713896065 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 96.02856786832922 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.795740862687426 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.435416771745196 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.38760934317229 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.431143749733359 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.748941373883508 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.27718857406742 | |
