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
| migraphx_bert__bert-large-uncased | PASS | 12.589923970933471 | |
| migraphx_cadene__dpn92i1 | Numerics | 10.120427559706426 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.92750318014684 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.097047981144725 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.229461881917778 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.70350033647957 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.860752752011125 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.8417745684216 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.77682246226402 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.61729006185418 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 285.93891377871233 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.40452865656051 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 75.7502369513666 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 295.2393083833158 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 40.363927280493805 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.462787276392595 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.716551370297868 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.645022863797663 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.70151111675423 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.284984651066008 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.31680437697777 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.551643493083816 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.754743542729152 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.498860840596969 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.852985727967637 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.458743111762617 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.799632080802409 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.381077140569687 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.32916548961039 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.3983469876376 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 96.71286830589884 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.697218922954614 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.340546051813226 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.303908895168984 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.363168168584911 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.605657003162538 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.43293540738523 | |
