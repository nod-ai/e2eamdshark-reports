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
| migraphx_bert__bert-large-uncased | PASS | 12.70685770520658 | |
| migraphx_cadene__dpn92i1 | PASS | 2.9103492926368237 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 19.701665094881143 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.356253466702521 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.237405986669137 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 20.368587993154367 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.995121350842163 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.12156733392197 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.80410731625226 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 99.00294940563894 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 290.426019889613 | |
| migraphx_ORT__distilgpt2_1 | PASS | 56.809501981155734 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 70.32586460312207 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.9979147799313 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.96194618816177 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.429713904857635 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.3386946907119146 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8655591370234037 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.33919129776312 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.1416746217107 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.99513816012021 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.794531486381246 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.486455684882543 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.897867623164695 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.428779177190291 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.830406342717735 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.441102361565248 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.966614014835965 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.9953917621663 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.72854416356199 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.759925989490563 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.399548733813894 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.346898110766038 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.340357132712187 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.64650059294175 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.156329446575707 | |
