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
| migraphx_bert__bert-large-uncased | PASS | 12.709726731885565 | |
| migraphx_cadene__dpn92i1 | PASS | 9.957277264113715 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.188075853955176 | |
| migraphx_cadene__resnext101_64x4di1 | Numerics | 3.3251898308107593 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.300603069057785 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.387643868369715 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.159675534274696 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.60703079568015 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.80261001694532 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.83678199315352 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 286.38015625377494 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.19096235144469 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.66452585657437 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 287.0672714586059 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.158621113057485 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 17.14687281136596 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.656323709525168 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.480380116571934 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9272486526580128 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.390441394684945 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.19966318529276 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.036242678952526 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.851175819749884 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.554273519310213 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.894698621874506 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.53742773440622 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.86351221867583 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.437153561636295 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.926625097791348 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.020825419687846 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 96.08578477941808 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.762018140744077 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.449854438402214 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.414459847790354 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.479123309356012 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.693557629106092 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.15223812063535 | |
