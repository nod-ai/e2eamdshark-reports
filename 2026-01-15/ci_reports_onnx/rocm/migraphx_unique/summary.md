## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 36 | 87.8% | 94.7% |
| Inference Comparison (PASS) | 27 | 65.9% | 75.0% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 9 | 22.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.633801814878268 | |
| migraphx_cadene__dpn92i1 | Numerics | 3.1013431791271078 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.08253800727072 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.454294499643755 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.223012457086457 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.328044537730786 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.067848343904133 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.12345789575282 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.49320943736366 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.62665208464576 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.0087020993233 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.5936456831793 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.00946335991223 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 285.772860981524 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.45640730664685 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.51423926713566 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.4286122829691177 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8990235690000479 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.208289953214784 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.80964638623926 | |
| migx_bench_bert-large-uncased_16_384 | Numerics | 51.51478244135013 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.78086025433408 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.50920577773026 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.809995979522213 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.39913977595449 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.795524389454812 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.352595598316514 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.671097050562043 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.3308065768444 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.03617882728577 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.69763238502271 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.367089790551839 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.301882975867816 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.385967357020798 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.550429693185816 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.019886006911594 | |
