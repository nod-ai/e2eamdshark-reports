## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 38 | 92.7% | 97.4% |
| Inference Comparison (PASS) | 31 | 75.6% | 81.6% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.4% |
| Inference Comparison | 7 | 17.1% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 171.36748175001534 | |
| migraphx_cadene__dpn92i1 | PASS | 200.35240555555194 | |
| migraphx_cadene__inceptionv4i16 | PASS | 4389.840939666707 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 135.51742453303933 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 153.24475858331726 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 231.49989577763736 | |
| migraphx_mlperf__resnet50_v1 | PASS | 121.7012432666403 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.89316380250894 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 53.05551018177952 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 57.686058233381715 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 55.777887599985355 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 196.05898855530134 | |
| migraphx_ORT__distilgpt2_1 | PASS | 20.113195657107834 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 96.84814288897945 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 293.12911983303513 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 18.035375598240215 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 35.62902638589692 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 1525.289407000552 | |
| migraphx_torchvision__inceptioni1 | PASS | 150.4832290665945 | |
| migraphx_torchvision__resnet50i1 | PASS | 125.79935086663075 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 758.7597536670122 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 1449.2037529998925 | |
| migx_bench_bert-large-uncased_16_384 | Numerics | 2143.7383923318216 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 73.25294207428803 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 127.69661053328794 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 174.6318464165597 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 130.90140160032507 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 225.7723340001879 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 316.7172436666684 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 1437.3920829984854 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 2783.4730653333586 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 4262.3769156659055 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 218.4554665553959 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 406.42038716699363 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 652.2733136662282 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 399.78128916694305 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 778.225486333516 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 1125.1402496667044 | |
