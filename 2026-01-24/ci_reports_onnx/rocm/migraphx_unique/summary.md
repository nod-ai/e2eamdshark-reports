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
| migraphx_bert__bert-large-uncased | PASS | 12.725703333589165 | |
| migraphx_cadene__dpn92i1 | PASS | 3.069987934044789 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.02943614941268 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.487443927500589 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.3166023907843725 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 21.047540876430038 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.399342598528534 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.2664120276401 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.73615958210495 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.43184617516539 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 286.11313054958975 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.11907397583127 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 71.95398950328429 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.0813139316936 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.68483726142181 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.624801870745916 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.448845290584989 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9125535616387512 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.277523754962854 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.16316384053419 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.07161961171107 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.859016256185912 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.515127741997794 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.931968280930574 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.480807357600755 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.83727479590611 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.491944729040066 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.92567967837958 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.897850877633594 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.91294825077057 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.78524049416636 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.401167346050544 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.36460491773837 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.421524011156185 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.613618213318144 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.231744145767554 | |
