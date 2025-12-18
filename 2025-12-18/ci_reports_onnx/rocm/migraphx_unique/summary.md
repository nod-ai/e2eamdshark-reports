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
| migraphx_bert__bert-large-uncased | PASS | 12.62433834130033 | |
| migraphx_cadene__dpn92i1 | Numerics | 10.152066880393596 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.796987944981083 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.0933470591038885 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.2106199300627125 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.641572531933587 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.851108173582146 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.879209734683414 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.63451890812979 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.8137220027191 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.29345940922695 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.50883753514952 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 75.60584828671482 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 294.00805539141095 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 40.323771974619696 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.573618756710653 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.71021094949295 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.655142824595206 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.70073428039145 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.237643732911064 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.68458028182838 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.34340807891045 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.751521327015427 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.413443583581182 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.822719962533675 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.29415244657045 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.720794936246945 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.35010083856023 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.435465934037254 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.14248880608515 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 94.92971242538518 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.66352900049903 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.347170137477164 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.247198942871318 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.305692349820314 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.550455761087292 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 28.86941567218552 | |
