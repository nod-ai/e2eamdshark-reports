## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 97.4% |
| Inference Comparison (PASS) | 29 | 70.7% | 78.4% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.4% |
| Inference Comparison | 8 | 19.5% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.63779758927271 | |
| migraphx_cadene__dpn92i1 | PASS | 9.914880381249974 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.896620853416 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.127385403525236 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.241965849208565 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.715509110095873 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.06411594814284 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.727132401417617 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.73018180185721 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.22516912053383 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.46191106053686 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.47654041948004 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.23374873865396 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 285.92102613765746 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.63150770862207 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.526671322528273 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.729526242384544 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.599364259966502 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.7130926788260594 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.230604648323997 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.925370578018445 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.66673533116969 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.742768866113488 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.512802986228571 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.844736264510587 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.490058083563952 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.799782138035601 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.41879077738493 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.694793664483402 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.404529676744424 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.09372500525342 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.711589677597987 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.373920542713838 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.27139939101679 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.354417947925576 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.530756699907432 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.040376798042818 | |
