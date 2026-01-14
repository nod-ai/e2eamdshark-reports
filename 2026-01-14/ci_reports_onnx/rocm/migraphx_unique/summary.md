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
| migraphx_bert__bert-large-uncased | PASS | 12.618903503088013 | |
| migraphx_cadene__dpn92i1 | Numerics | 3.1013163987953747 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.082559454299155 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.4786759716391704 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.233377270835781 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.731788301751724 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.070289214874833 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.064473856746414 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.55867872387171 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.94677124704634 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.04634119073546 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.70470429625775 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 71.83527722954749 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 285.3325813387831 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.78340642485353 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.5660893941919 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.435232600477201 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9033268040073088 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.229923938001907 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.84820701394762 | |
| migx_bench_bert-large-uncased_16_384 | Numerics | 51.53751812684229 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.795627522385784 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.504856745224622 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.838724300716862 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.406847695683874 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.7630617243774 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.386030180113657 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.632022424177688 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.30751916630701 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.02616258604185 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.727273503939308 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.344880598134734 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.302651095248404 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.350439288786477 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.532780692127407 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 28.997787377900547 | |
