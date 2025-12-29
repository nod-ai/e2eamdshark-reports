## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 97.4% |
| Inference Comparison (PASS) | 29 | 70.7% | 78.4% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.4% |
| Inference Comparison | 8 | 19.5% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.610864348798279 | |
| migraphx_cadene__dpn92i1 | PASS | 9.969178323323527 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.80299971466108 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.094382896317519 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.231974242178282 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.5225365244335 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.050385707117456 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.787679708482305 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.6735019756274 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.961016269312 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.7460339457417 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.389520891269456 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 71.63157227138679 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 285.671454660284 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.80351948275886 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.354829978805759 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.720893925676744 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.625311888766622 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.6741727191072546 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.243242797663523 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.01654112643547 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.636389713400064 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.777136529174946 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.507996642463176 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.811251416463742 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.402970012963602 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.808169032249486 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.422938272002193 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.732592199025955 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.436657702098735 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.1171331218488 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.684917980522819 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.358799378736082 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.28323409280607 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.363431772470575 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.52712382967858 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.061776362747576 | |
