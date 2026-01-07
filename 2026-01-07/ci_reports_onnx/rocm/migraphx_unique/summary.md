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
| migraphx_bert__bert-large-uncased | PASS | 12.653959937619438 | |
| migraphx_cadene__dpn92i1 | PASS | 9.991773173567795 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.88350830692798 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.1046969091546694 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.253848509126922 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.693151788993013 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.1166551462982 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.74614180182969 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.93186692314015 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.06729041962394 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.44527383645374 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.7341311921676 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.13285596420367 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.0380792990327 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.81063281248013 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.761689667266308 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.755568632458008 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.654635072872865 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.717951882789109 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.298083641511553 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.73829004981301 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.272464581789116 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.81925903732157 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.545592960945905 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.875717099417338 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.536594710711919 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.83886774697087 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.459487594043216 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.50024502114816 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 60.94453421731789 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 94.40523288434458 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.755295668135988 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.397489147729614 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.326757493118446 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.439858774952336 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.597424266823367 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 28.986816967113146 | |
