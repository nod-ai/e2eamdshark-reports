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
| migraphx_bert__bert-large-uncased | PASS | 12.635463222284756 | |
| migraphx_cadene__dpn92i1 | Numerics | 9.909505308383986 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.903335204115137 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.0858652481566295 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.233326844999062 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.50303168484458 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.085143799745085 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.74923122876588 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.85725955127013 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.95965177956082 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 284.2890185614427 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.41625196403927 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 75.54435485077124 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 294.7194941031436 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 40.31825518491221 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.43336347842382 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.74546250235289 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.637612959176763 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.687184044208966 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.29513099363872 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.21210272787582 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.03971037497888 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.793206430350741 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.471857857668681 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.865831759391407 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.408266132642998 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.766260834354341 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.383060281120594 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.975118697366927 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.23514348720058 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.97096317225976 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.719938040456988 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.393154500039662 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.300660218459132 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.3908471705354 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.58522086407916 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.19440418999228 | |
