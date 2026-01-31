## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 36 | 87.8% | 94.7% |
| Inference Comparison (PASS) | 29 | 70.7% | 80.6% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 7 | 17.1% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.761252373456953 | |
| migraphx_cadene__dpn92i1 | PASS | 2.9519038443039687 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 19.82740857416675 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.379093813391168 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.289863207547115 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.386586509024102 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.174276195466518 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.534984187211517 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.63149263585608 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 99.0011319961576 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 292.2398314500848 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.77684063650668 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.54661860068639 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 287.41673116261757 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.10943063803845 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.49655995517969 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.371970160888173 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.888363999625047 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.403127167739118 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.155945129692554 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.945218028357395 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.891970195212942 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.583123242837331 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 13.01500298381771 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.495282815680618 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.869255876902377 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.57859948924225 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.900701324709434 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.981524848802515 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.75971437706833 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.856054859179437 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.512928584331853 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.43227873304311 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.49909405912169 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.70042378652622 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.24348522598545 | |
