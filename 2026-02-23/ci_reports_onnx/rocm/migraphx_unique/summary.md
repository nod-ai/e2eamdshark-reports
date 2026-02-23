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
| migraphx_bert__bert-large-uncased | PASS | 12.696713931632763 | |
| migraphx_cadene__dpn92i1 | PASS | 2.941295328653521 | |
| migraphx_cadene__inceptionv4i16 | PASS | 19.665911345294226 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.3637356882629628 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.270475452657007 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.65166328989324 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.002252732185609 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.267904397330167 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.48644385321272 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.15732954655374 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 99.39470150995822 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 293.66257041692734 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.23075052143798 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.88106411198775 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 288.44837161401904 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.370308112767006 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.43724732659757 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.3469052310955765 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8771942191653783 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.44733474944152 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.508769872169644 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.414625978622674 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.865761173141879 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.471471480759128 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.914275808006892 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.560147204480709 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.85927054105383 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.509486099187697 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.214461966897495 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.633145374782146 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 96.81742256950763 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.786949414646985 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.438034915903797 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.484244779628867 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.443988778761453 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.778715610504154 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.35260027233097 | |
