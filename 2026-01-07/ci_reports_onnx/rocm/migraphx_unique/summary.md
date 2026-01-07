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
| migraphx_bert__bert-large-uncased | PASS | 12.696837123031868 | |
| migraphx_cadene__dpn92i1 | PASS | 10.447083372056632 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 22.074945278291125 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.158284981168631 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.2983602850771545 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.761393674868433 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.141162290777741 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.645050240823853 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 114.5641447769271 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.68991659191391 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 288.69528315650916 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.00417188503261 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.53185563410321 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.97769716382027 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.12766470522102 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 16.626591219877202 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.857508735858605 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.690339263753603 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.7438292525303614 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.329265681771087 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 34.16874684718629 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 53.508953346560396 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.885200599524175 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.536860010143192 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.899369286429701 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.457315388712145 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.835666638883678 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.50521402229141 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.868781322909015 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 63.572008508455106 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 98.16869531225944 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.763457154064916 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.452364045467709 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.376632951072178 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.434968229053782 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.712774739984205 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.895820512643287 | |
