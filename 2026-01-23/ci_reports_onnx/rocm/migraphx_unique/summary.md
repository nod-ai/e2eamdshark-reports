## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 36 | 87.8% | 94.7% |
| Inference Comparison (PASS) | 29 | 70.7% | 80.6% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 2 | 4.9% |
| Inference Comparison | 7 | 17.1% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.687812079534387 | |
| migraphx_cadene__dpn92i1 | PASS | 3.0700023268421313 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.11640847084068 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.5152426133764547 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.294618310182774 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.287264357594882 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.083123394783506 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.653070186759212 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.44539632813797 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.09570241045382 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 285.65449205537635 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.622626639488665 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.38126906255881 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 285.9120797365904 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.96659436739153 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.587382160127163 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.4350100658809386 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9274120047715628 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.242900915798685 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.694443291614924 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.401332259560235 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.835917125398156 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.554997589350457 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.92516395771577 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.503974494479948 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.815641013510296 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.455175711488238 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.732212074778293 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.48657388985157 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.40685461390586 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.76239470550508 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.361537954941086 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.367171213615173 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.392351744329035 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.538826235661322 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.123925603926182 | |
