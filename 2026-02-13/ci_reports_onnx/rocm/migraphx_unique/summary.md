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
| migraphx_bert__bert-large-uncased | PASS | 12.735981324856931 | |
| migraphx_cadene__dpn92i1 | PASS | 2.952395422667306 | |
| migraphx_cadene__inceptionv4i16 | PASS | 19.692444432250877 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.390746906114457 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.321902867598632 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.61229179657641 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.013614537339683 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.6423215744672 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.37524559348822 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 99.93227278547626 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 99.73278765877086 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 294.65541150420904 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.703501493152636 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.81595746179421 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 288.3155901605884 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.43556905896575 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.412813659757376 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.3170831404508103 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8737070643239548 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.369351439762347 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.38108983423029 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.42320565650096 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.862205667684307 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.507911693925656 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.921958644356991 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.518501862706172 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.877617979591543 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.512347212682167 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.892960693574306 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.17271450794104 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 96.15820610807054 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.797364761883562 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.437022118442721 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.460735659535025 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.411893046023897 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.790132200893236 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.3570457595504 | |
