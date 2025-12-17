## Passing Summary

**TOTAL TESTS = 41**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 40 | 97.6% | 97.6% |
| IREE Compilation | 38 | 92.7% | 95.0% |
| Gold Inference | 38 | 92.7% | 100.0% |
| IREE Inference Invocation | 37 | 90.2% | 97.4% |
| Inference Comparison (PASS) | 28 | 68.3% | 75.7% |
## Fail Summary

**TOTAL TESTS = 41**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 2.4% |
| IREE Compilation | 2 | 4.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.4% |
| Inference Comparison | 9 | 22.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=True, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/migraphx_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/migraphx_unique.md', get_metadata=True)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| migraphx_bert__bert-large-uncased | PASS | 12.636320460365994 | |
| migraphx_cadene__dpn92i1 | Numerics | 10.193539261458 | |
| migraphx_cadene__inceptionv4i16 | Numerics | 21.87051569732527 | |
| migraphx_cadene__resnext101_64x4di1 | PASS | 6.081514835249686 | |
| migraphx_huggingface-transformers__bert_mrpc8 | PASS | 7.228961467256457 | |
| migraphx_mlperf__bert_large_mlperf | Numerics | 19.539885861040265 | |
| migraphx_mlperf__resnet50_v1 | PASS | 14.836908681384214 | |
| migraphx_models__whisper-tiny-decoder | PASS | 25.61968307436248 | |
| migraphx_models__whisper-tiny-encoder | Numerics | 112.3598893173039 | |
| migraphx_ORT__bert_base_cased_1 | PASS | 101.4802030154637 | |
| migraphx_ORT__bert_base_uncased_1 | setup | None | |
| migraphx_ORT__bert_large_uncased_1 | PASS | 284.2378586841126 | |
| migraphx_ORT__distilgpt2_1 | PASS | 57.73789585671491 | |
| migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu | Numerics | 75.49639166919168 | |
| migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu | Numerics | 294.6991121085981 | |
| migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu | Numerics | 40.324042058166334 | |
| migraphx_pytorch-examples__wlang_gru | PASS | 13.91682683283256 | |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | None | |
| migraphx_sd__unet__model | import_model | None | |
| migraphx_sdxl__unet__model | import_model | None | |
| migraphx_torchvision__densenet121i32 | PASS | 17.73539502173662 | |
| migraphx_torchvision__inceptioni1 | Numerics | 4.634293809812721 | |
| migraphx_torchvision__resnet50i1 | PASS | 3.725142365136573 | |
| migx_bench_bert-large-uncased_16_128 | PASS | 20.284731366804667 | |
| migx_bench_bert-large-uncased_16_256 | PASS | 32.929700917549546 | |
| migx_bench_bert-large-uncased_16_384 | PASS | 51.842621957453396 | |
| migx_bench_bert-large-uncased_1_128 | PASS | 11.738376552239062 | |
| migx_bench_bert-large-uncased_1_256 | PASS | 12.43318264217426 | |
| migx_bench_bert-large-uncased_1_384 | PASS | 12.836666467289128 | |
| migx_bench_bert-large-uncased_2_128 | PASS | 12.453087383792514 | |
| migx_bench_bert-large-uncased_2_256 | PASS | 12.723986369868117 | |
| migx_bench_bert-large-uncased_2_384 | PASS | 14.38960732043195 | |
| migx_bench_bert-large-uncased_32_128 | PASS | 31.604624804899544 | |
| migx_bench_bert-large-uncased_32_256 | PASS | 61.40733747319741 | |
| migx_bench_bert-large-uncased_32_384 | Numerics | 95.35789884449468 | |
| migx_bench_bert-large-uncased_4_128 | PASS | 12.656172268995732 | |
| migx_bench_bert-large-uncased_4_256 | PASS | 14.369929107983095 | |
| migx_bench_bert-large-uncased_4_384 | PASS | 20.313559401342097 | |
| migx_bench_bert-large-uncased_8_128 | PASS | 14.343486908747225 | |
| migx_bench_bert-large-uncased_8_256 | PASS | 20.603602551216003 | |
| migx_bench_bert-large-uncased_8_384 | PASS | 29.03524460271001 | |
