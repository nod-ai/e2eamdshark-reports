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
| migraphx_bert__bert-large-uncased | PASS | 12.624835528965507 | |
| migraphx_cadene__dpn92i1 | PASS | 9.806926865043215 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 20.113582252746536 | |
| migraphx_cadene__resnext101_64x4di1 | Numerics | 3.292954461255544 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.2380280013346585 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.616067857929952 | |
| migraphx_mlperf__resnet50_v1 | PASS | 15.122263462863105 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.838652602684345 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.7854398348265 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.15893841499371 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 283.0060999840498 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.579529264734845 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 72.49730930974086 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 286.2312414993842 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 38.75953335039041 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 14.615683117881417 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.578087110693254 | |
| migraphx_torchvision__inceptioni1 | PASS | 3.431022541560963 | |
| migraphx_torchvision__resnet50i1 | PASS | 1.9012382270876262 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.277320540377072 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.8711811453104 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.54715889157393 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.769517097208235 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.524299079640988 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.869436779257022 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.509597032996162 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.758226331436271 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.443280606144137 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.614302431769442 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.31275308628876 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.00671390976225 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.714178386059674 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.370704272470505 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.294578728221712 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.388177708602273 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.595487134129392 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.010340700753858 | |
