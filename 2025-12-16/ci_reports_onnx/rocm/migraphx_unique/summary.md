## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 97.4% |
| Inference Comparison (PASS) | 28 | 68.3% | 75.7% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.4% |
| Inference Comparison | 9 | 22.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.69600959212491 | |
| migraphx_cadene__dpn92i1 | Numerics | 10.214668856078875 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.971375526239473 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.147747627203014 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.273255773784778 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.624912454791012 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.909843484877692 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.526919434754507 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.6571219863577 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 102.01703772569694 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 286.3972634853174 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.46065506597773 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 75.7620089204499 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 294.6360368126382 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 40.63521982992397 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 15.239528664905164 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.819579348413864 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.713819542445525 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.766295167247295 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.31026588575471 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.326807054912756 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.47351531990063 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.849367086075794 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.505107345835613 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.894162786842294 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.549469374962861 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.79705650822231 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.416768402494741 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.13249504650858 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.2994062264986 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 96.32682798075534 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.752690138013072 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.379160095411699 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.33453078611809 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.38283801496941 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.619310730812597 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.414669481209582 | |
