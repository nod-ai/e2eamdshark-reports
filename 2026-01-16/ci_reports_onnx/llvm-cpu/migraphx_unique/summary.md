## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 41 | 100.0% | 100.0% |
| IREE Compilation | 39 | 95.1% | 95.1% |
| Gold Inference | 39 | 95.1% | 100.0% |
| IREE Inference Invocation | 38 | 92.7% | 97.4% |
| Inference Comparison (PASS) | 30 | 73.2% | 78.9% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.4% |
| Inference Comparison | 8 | 19.5% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 176.46513191675695 | |
| migraphx_cadene__dpn92i1 | Numerics | 198.87127388887566 | |
| migraphx_cadene__inceptionv4i16 | PASS | 4368.65561400009 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 135.10990433339126 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 152.47195241674186 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 219.78208011094262 | |
| migraphx_mlperf__resnet50_v1 | PASS | 122.96220588885059 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.953284988071612 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 53.95703803027242 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 54.80856143331039 | |
| migraphx_ORT__bert_base_uncased_1 | PASS | 56.23335136354425 | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 191.26639099997394 | |
| migraphx_ORT__distilgpt2_1 | PASS | 19.71759627619273 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 95.17981616681936 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 289.5383761665471 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 17.706470416677195 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 35.39654811662937 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 1540.9409099999418 | |
| migraphx_torchvision__inceptioni1 | PASS | 150.73452333332776 | |
| migraphx_torchvision__resnet50i1 | PASS | 126.30769580015716 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 725.49240366637 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 1420.9633789999618 | |
| migx_bench_bert-large-uncased_16_384 | Numerics | 2088.7630816672145 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 75.69834111119336 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 128.76511093333343 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 173.04457658345504 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 125.2036482001131 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 221.99039944441915 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 305.89290100003075 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 1324.3669016668111 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 2666.800566000044 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 4189.185381000243 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 216.31525566661162 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 425.5509351666357 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 645.0794240002626 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 379.6857740001845 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 742.8333319994636 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 1067.3833593336894 | |
