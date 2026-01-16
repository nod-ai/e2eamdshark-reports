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
| migraphx_bert__bert-large-uncased | PASS | 12.686031131130273 | |
| migraphx_cadene__dpn92i1 | Numerics | 3.1084755688334282 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.134523936680385 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.4752891403863404 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.246331436578761 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.77418753362837 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.104421913839767 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.887409432066807 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.0416401558452 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.69891579803965 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 282.3085328564048 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.62939351714319 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 71.81740912298362 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 285.75045956919587 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.822512935709064 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.62294772391518 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.437714964711393 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9042860105822699 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.280551892660913 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.11454436726986 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.03029584999268 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.79429328896933 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.533249067408697 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.892663156912647 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.416499788828546 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.788064653674759 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.452135707769129 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.857430878462207 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.89069439741698 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.96976504794186 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.737973508509723 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.392867811074872 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.324522391984278 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.394669077631567 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.574821250549718 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.126995967494114 | |
