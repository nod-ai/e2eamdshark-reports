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
| migraphx_bert__bert-large-uncased | PASS | 12.631424092909407 | |
| migraphx_cadene__dpn92i1 | PASS | 9.681864796827236 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.11659936535926 | |
| migraphx_cadene__resnext101_64x4di1 | Numerics | 3.3174367742186277 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.236346660047462 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.85241937495413 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.117204715068455 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.264214169943614 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.87220153543683 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.48905476218177 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 282.77430435021716 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.172290472106795 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.04404467095931 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 285.71039220939076 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.741253626843296 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.255571337480122 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.607745652397472 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.432475539242349 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9036507861607748 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.272655341596828 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.84241811978438 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.56173657339354 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.770873858282963 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.493079783217537 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.81628543228814 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.471934259381321 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.724403111320553 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.350263883366063 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.6716923632405 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.43051368946379 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.08231095969677 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.732133867614195 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.390581737266103 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.286168282230694 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.388804773793737 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.5897180290491 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.003924457356334 | |
