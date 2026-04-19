## Passing Summary

**TOTAL TESTS = 38**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 38 | 100.0% | 100.0% |
| IREE Compilation | 38 | 100.0% | 100.0% |
| Gold Inference | 38 | 100.0% | 100.0% |
| IREE Inference Invocation | 37 | 97.4% | 97.4% |
| Inference Comparison (PASS) | 33 | 86.8% | 89.2% |
## Fail Summary

**TOTAL TESTS = 38**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 0 | 0.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 2.6% |
| Inference Comparison | 4 | 10.5% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/onnx_model_zoo_validated_vision_others.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/onnx_model_zoo_validated_vision_others.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| bvlcalexnet-7 | PASS | None | |
| bvlcalexnet-9 | PASS | None | |
| caffenet-7 | PASS | None | |
| caffenet-8 | PASS | None | |
| candy-8 | PASS | None | |
| candy-9 | Numerics | None | |
| densenet-7 | PASS | None | |
| densenet-8 | PASS | None | |
| densenet-9 | PASS | None | |
| emotion-ferplus-7 | PASS | None | |
| googlenet-3 | PASS | None | |
| googlenet-6 | PASS | None | |
| googlenet-8 | PASS | None | |
| googlenet-9 | PASS | None | |
| inception-v1-8 | PASS | None | |
| inception-v1-9 | PASS | None | |
| inception-v2-7 | PASS | None | |
| inception-v2-8 | PASS | None | |
| mnist-7 | PASS | None | |
| mosaic-8 | PASS | None | |
| pointilism-8 | PASS | None | |
| pointilism-9 | Numerics | None | |
| rain-princess-9 | Numerics | None | |
| rcnn-ilsvrc13-8 | PASS | None | |
| rcnn-ilsvrc13-9 | PASS | None | |
| resnet50-caffe2-v1-8 | PASS | None | |
| resnet50-caffe2-v1-9 | PASS | None | |
| shufflenet-8 | PASS | None | |
| shufflenet-9 | PASS | None | |
| squeezenet1.0-7 | PASS | None | |
| squeezenet1.0-8 | PASS | None | |
| tinyyolov2-8 | compiled_inference | None | |
| udnie-8 | PASS | None | |
| udnie-9 | Numerics | None | |
| vgg19-caffe2-7 | PASS | None | |
| vgg19-caffe2-9 | PASS | None | |
| zfnet512-7 | PASS | None | |
| zfnet512-8 | PASS | None | |
