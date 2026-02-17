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
| migraphx_bert__bert-large-uncased | PASS | 12.74098441230528 | |
| migraphx_cadene__dpn92i1 | PASS | 2.9038377080427 | |
| migraphx_cadene__inceptionv4i16 | PASS | 19.62743416704513 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.3442993507437087 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.26657851736775 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.1118109084311 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.982643702351451 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.895838913174316 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.68991925236251 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 99.4584723597481 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 99.47738166721092 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 290.26025254279375 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.26443795073363 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.53664543976386 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 287.8294851010044 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.00135263662647 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.370631638914347 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.320201941467119 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8682598238744843 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.357372166187155 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.10005417064068 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.006329385898056 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.763642448931932 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.486521054857542 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.893611530738847 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.45154435968115 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.845476220051445 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.456861574823657 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.845356507057488 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.583167562882096 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 94.80112560448191 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.676982908989443 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.422220285652445 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.40046274515928 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.415910378808064 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.697595807267167 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.06414706053005 | |
