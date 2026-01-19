## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 36 | 87.8% | 94.7% |
| Inference Comparison (PASS) | 28 | 68.3% | 77.8% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 8 | 19.5% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.733972385864364 | |
| migraphx_cadene__dpn92i1 | Numerics | 3.139702988167604 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.19697618449018 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.480542281132546 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.294485393489144 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.665589857491707 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.102680023435665 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.527026909644956 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 114.16070610802205 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.94621713228878 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 286.87932497511304 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.576160502827 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.29026313871145 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.416324476401 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.85224542615038 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.68376244387279 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.4955655467774474 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9124856351500037 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.327417743170546 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 34.07803346358594 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 53.560085702114385 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.803001845772895 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.57570332104695 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.94001687122624 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.475406274288181 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.837850748363769 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.452464520601795 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.79202227537153 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 63.461038241670884 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 98.07551222010737 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.7561367794194 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.43427201157727 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.39842591073145 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.403794740079618 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.649023007090186 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.86680151661858 | |
