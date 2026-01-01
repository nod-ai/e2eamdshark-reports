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
| migraphx_bert__bert-large-uncased | PASS | 12.70844888958064 | |
| migraphx_cadene__dpn92i1 | PASS | 10.19162635008494 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.92567956323425 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.140607276904409 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.303745127395051 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.117583270702095 | |
| migraphx_mlperf__resnet50_v1 | PASS | 21.56208849728408 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.615828735592917 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 148.68902675807476 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.5039517411164 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 305.0910443998873 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.278353212194304 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 75.26869433759539 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 299.4582215324044 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.53780487386717 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 17.102502603930503 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.789292857687695 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.682549544228803 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.7349514232872862 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.307734910221324 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.84910404019885 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.46417563828902 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.8765628365221 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.552738150892155 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.941797637599118 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.570999668068472 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.862646720851911 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.479379518096948 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.598263349609837 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.3128946473201 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 94.99609692110901 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.778011009548647 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.417096104498215 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.34549675334026 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.435929544016616 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.609232916624524 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.07367570636173 | |
