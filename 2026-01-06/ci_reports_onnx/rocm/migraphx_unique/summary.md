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
| migraphx_bert__bert-large-uncased | PASS | 12.59793937649755 | |
| migraphx_cadene__dpn92i1 | PASS | 9.852564272781214 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.916757919825613 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.054486239050654 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.233968465444968 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.086931370668584 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.030595691914252 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.591116743507204 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.23073210567236 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.74021197145892 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.96538831293583 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.45528917759657 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.04993354777496 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.25878381232417 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.59880694222671 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.009619653224945 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.685157883291442 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.579918426593404 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.680621901232946 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.26264422706195 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.86559953694306 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.601771838389915 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.791729720102417 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.50408747277799 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.833257662979038 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.46679932366879 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.713749345504874 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.358230213932439 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.78471800955859 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.65997260673479 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.02670603493847 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.693127628528709 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.382755878020307 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.219552960424195 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.372638597780345 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.547893354851826 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.062065373485286 | |
