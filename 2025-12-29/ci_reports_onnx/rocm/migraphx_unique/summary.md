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
| migraphx_bert__bert-large-uncased | PASS | 12.693372470411388 | |
| migraphx_cadene__dpn92i1 | PASS | 10.159980971366167 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.974764803114038 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.141107101864807 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.28878331501869 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.503165830104123 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.138096574262 | |
| migraphx_models__whisper-tiny-decoder | PASS | 26.34610380563471 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 113.33567255900965 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 100.7180454741631 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 284.47258969148 | |
| migraphx_ORT__distilgpt2_1 | PASS | 58.064559396977224 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.12222488597035 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.0646415501833 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.88281969422543 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 15.447689828519918 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.778935882016125 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.665221613944892 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.767265929877223 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.29026151590404 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.88523471426396 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.528134144460545 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.842546889842568 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.538172171584195 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.927588707778924 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.541474430777484 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.846844569977485 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.488953075164721 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.636818918879282 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.380172741006724 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.15731351538783 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.767471147306034 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.430334747192404 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.333601043139602 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.436734346102694 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.64610896266851 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.070865944959223 | |
