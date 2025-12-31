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
| migraphx_bert__bert-large-uncased | PASS | 12.666810738543669 | |
| migraphx_cadene__dpn92i1 | PASS | 9.965062884727553 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 22.033072988657903 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.113070389930751 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.2217705688372105 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.58883218294768 | |
| migraphx_mlperf__resnet50_v1 | PASS | 21.53462033267274 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.889224568266926 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 148.8934806237618 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.6706675734548 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 303.903978317976 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.107450526828565 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 75.376499340766 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 299.0050368631879 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 39.22934887102908 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.078992884606123 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.804974976640484 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.62157999394102 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.7149968713101464 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.275577645571456 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.954379562702435 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 53.156859647387115 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.817073670484254 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.50435297732197 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.895895593604187 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.498740090190298 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.782507931644266 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.42491782030889 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.66383780900275 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 63.37433212408513 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 97.66063426754302 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.736521960433684 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.369992685003751 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.3031261939378 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.382196387567484 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.618001647366615 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.699192188369732 | |
