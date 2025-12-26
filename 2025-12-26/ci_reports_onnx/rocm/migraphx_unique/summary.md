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
| migraphx_bert__bert-large-uncased | PASS | 12.630887118922102 | |
| migraphx_cadene__dpn92i1 | PASS | 9.906840051563693 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.946080203633755 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.111817609896694 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.229662209083535 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.554170538429858 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.083135125915641 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.75799482472149 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.81373703645335 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.17920403856607 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.3477477543056 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.38307716738846 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.41953931127985 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.2817423107723 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.75663607484764 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.379137848206115 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.745005237495796 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.674319457262754 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.7013976941479783 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.2745324178111 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.831066007178926 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.51172686750308 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.79608857880036 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.477456741700216 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.832878484870447 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.415293565330403 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.776615724644877 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.45095831540977 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.590617529935 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.33898423815315 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.0202020328669 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.730892634753024 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.37599344343758 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.329053577620023 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.385220277927765 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.588026372898444 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 28.99393995499445 | |
