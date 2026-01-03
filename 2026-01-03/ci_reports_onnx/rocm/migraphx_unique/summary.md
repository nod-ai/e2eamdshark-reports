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
| migraphx_bert__bert-large-uncased | PASS | 12.608963508336316 | |
| migraphx_cadene__dpn92i1 | PASS | 9.946952464644896 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.884352938892942 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.087503560643264 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.22786549901225 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.67469240642256 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.056866333417013 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.629166674650744 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.90153271208207 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.93465615950879 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.8207414994637 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.25491786789562 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.33563121408223 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 285.98544218887884 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.65399791134728 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.625398493889305 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.74334124265573 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.680878669023514 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.6893379564086595 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.283708206954454 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.42454448815376 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.37468895621788 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.789508505413929 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.470918252975459 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.80382800508629 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.394433873787262 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.813446817524502 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.406896380036054 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.168730472524956 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.41734529083425 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.97393178514069 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.709985176722206 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.360986257187362 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.257131045772912 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.383273921450792 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.571551742214783 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.321349510509105 | |
