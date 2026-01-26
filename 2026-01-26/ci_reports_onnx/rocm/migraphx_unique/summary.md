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
| migraphx_bert__bert-large-uncased | PASS | 12.696331299164079 | |
| migraphx_cadene__dpn92i1 | PASS | 2.9896287782410695 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.02962531433219 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 2.446664451667062 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.256974565358096 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.397237701784995 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.386064766325811 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.873081689631494 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.96154506918457 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.66939285894233 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 284.0801052128275 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.79189709573984 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.33199918021758 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.6351278498769 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.7940795885192 | |
| migraphx_pytorch-examples__wlang_gru | compiled_inference | None | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.585674254223704 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.3982462915787806 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.8962368067051913 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.330266004391746 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 33.19870905270652 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 52.175360564620064 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.810350759575764 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.499400325829072 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.859641523523763 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.411701326657615 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.806661799550055 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.431111425870938 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 32.08794298045562 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 62.111809059525974 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 96.31850029386224 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.732515585693443 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.385210312142663 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.360086697573756 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.412922594620257 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.62303720809081 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.236204016746743 | |
