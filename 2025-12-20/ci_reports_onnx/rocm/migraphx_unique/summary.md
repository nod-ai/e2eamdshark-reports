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
| migraphx_bert__bert-large-uncased | PASS | 12.684157372198321 | |
| migraphx_cadene__dpn92i1 | Numerics | 10.181761918148556 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.93163672927767 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.16080132515534 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.297724751032299 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.757752887549852 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.120186714752426 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.642753945615812 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.10897984852393 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 102.29707912852365 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 286.3178647433718 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.567572152242064 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 75.82507893029187 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 294.69214022780454 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 40.94433921444065 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 16.39348420279997 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.804336495315418 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.698854779420415 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.713700537246169 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.32687865635928 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.89366917063793 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.52510204471838 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.87911216632626 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.578822916284913 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.903748097381104 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.476200703531504 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.877877248507554 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.474364062253798 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.61778011726159 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.378004932493866 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.11247277259827 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.783375331623986 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.409588510487355 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.35153214363199 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.426349358138987 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.613801775171478 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.04742571990937 | |
