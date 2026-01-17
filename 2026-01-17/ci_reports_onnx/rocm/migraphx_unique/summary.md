## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 36 | 87.8% | 94.7% |
| Inference Comparison (PASS) | 28 | 68.3% | 77.8% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 8 | 19.5% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.701751692502787 | |
| migraphx_cadene__dpn92i1 | Numerics | 3.144746861524052 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.208538780432374 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.508183914178171 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.2924105092063805 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.53404147071498 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.153072821651245 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.579269840393536 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 114.24375511705875 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.16378419722118 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 286.40254136795795 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.19392499203483 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.27206622871259 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.2244421460976 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.963301176274264 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.65135327198853 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.4744231732277737 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9193672527815548 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.288846282554527 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 34.03645096760656 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 53.510265699468356 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.844450907813291 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.506138286664195 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.904604386086715 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.449844122221249 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.8421772468948 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.486617728834972 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.80161952392922 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 63.35423006252808 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 98.29755723919895 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.762126510003299 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.385168174547807 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.332249679735728 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.373958063292868 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.586199930631647 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.849249132287998 | |
