## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 37 | 90.2% | 90.2% |
| Gold Inference | 37 | 90.2% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 100.0% |
| Inference Comparison (PASS) | 30 | 73.2% | 81.1% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 4 | 9.8% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 7 | 17.1% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.626316451046259 | |
| migraphx_cadene__dpn92i1 | compilation | None | |
| migraphx_cadene__inceptionv4i16 | PASS | 18.335968423471375 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.6740456007052735 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.2113206462864206 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.55994045689564 | |
| migraphx_mlperf__resnet50_v1 | Numerics | 14.82382553781495 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.21552679328514 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 133.09881603345275 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 97.262732285474 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 98.6423612394858 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 327.0794437266886 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.2030257123212 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 76.11528770239264 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 279.76909031470615 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.87896407050666 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 18.06205963620391 | |
| migraphx_pytorch-examples__wlang_lstm | PASS | 6.5715430983863525 | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | compilation | None | |
| migraphx_torchvision__inceptioni1 | PASS | 4.0750283876058555 | |
| migraphx_torchvision__resnet50i1 | PASS | 2.1654605765522326 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.081214393888203 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.05234967745722 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.751038835694395 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.847045215674571 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.528203898996466 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.892184474356013 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.484809167550077 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.821326153635072 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.43305296101132 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.79798973018698 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.39745165339924 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.9103648284716 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.736601464337468 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.371988851399648 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.246593414672784 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.395379505696747 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.57704970459728 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.025470747405453 | |
