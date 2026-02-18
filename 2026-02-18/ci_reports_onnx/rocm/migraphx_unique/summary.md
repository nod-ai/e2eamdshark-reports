## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 94.9% |
| Inference Comparison (PASS) | 31 | 75.6% | 83.8% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 6 | 14.6% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.684664039900808 | |
| migraphx_cadene__dpn92i1 | PASS | 2.909599083319904 | |
| migraphx_cadene__inceptionv4i16 | PASS | 19.62343453326159 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.355739653477199 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.233519708782537 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.382328329676827 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.983275997723247 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.215369627057083 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.57263107432259 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 99.68233933406215 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 99.9972732471568 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 290.26055553307134 | |
| migraphx_ORT__distilgpt2_1 | PASS | 56.97703790954417 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.36484281222025 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 287.1877821162343 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.51476949812085 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.321682985251147 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.332270959776545 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8502115099518386 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.375101735778884 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.9117803346543 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.62347423342558 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.786149980293379 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.485086285908304 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.885251346929572 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.51492103827851 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.839473569483467 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.433191861121022 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.69279311303839 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.6282204899824 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.16330914837972 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.717233316013305 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.408970074284644 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.397235000250387 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.380708108751142 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.695056565398094 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.121723646918934 | |
