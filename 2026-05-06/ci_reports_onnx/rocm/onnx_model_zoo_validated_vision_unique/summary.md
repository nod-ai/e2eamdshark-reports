## Passing Summary

**TOTAL TESTS = 71**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 71 | 100.0% | 100.0% |
| IREE Compilation | 61 | 85.9% | 85.9% |
| Gold Inference | 61 | 85.9% | 100.0% |
| IREE Inference Invocation | 60 | 84.5% | 98.4% |
| Inference Comparison (PASS) | 34 | 47.9% | 56.7% |
## Fail Summary

**TOTAL TESTS = 71**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 10 | 14.1% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 1.4% |
| Inference Comparison | 26 | 36.6% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/onnx_model_zoo_validated_vision_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/onnx_model_zoo_validated_vision_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| arcfaceresnet100-8 | compilation | None | |
| bvlcalexnet-12 | PASS | None | |
| bvlcalexnet-12-qdq | Numerics | None | |
| bvlcalexnet-8 | PASS | None | |
| caffenet-12 | PASS | None | |
| caffenet-12-qdq | Numerics | None | |
| caffenet-9 | PASS | None | |
| densenet-12 | PASS | None | |
| densenet-6 | PASS | None | |
| efficientnet-lite4-11 | PASS | None | |
| efficientnet-lite4-11-qdq | Numerics | None | |
| emotion-ferplus-12-int8 | PASS | None | |
| emotion-ferplus-8 | PASS | None | |
| fcn-resnet101-11 | Numerics | None | |
| fcn-resnet50-11 | Numerics | None | |
| fcn-resnet50-12 | Numerics | None | |
| fcn-resnet50-12-qdq | Numerics | None | |
| googlenet-12 | compilation | None | |
| googlenet-12-qdq | Numerics | None | |
| googlenet-7 | compilation | None | |
| inception-v1-12 | compilation | None | |
| inception-v1-12-qdq | Numerics | None | |
| inception-v1-7 | compilation | None | |
| inception-v2-9 | PASS | None | |
| mnist-12 | PASS | None | |
| mnist-8 | PASS | None | |
| mobilenetv2-10 | PASS | None | |
| mobilenetv2-12 | PASS | None | |
| mobilenetv2-12-qdq | Numerics | None | |
| mobilenetv2-7 | PASS | None | |
| rain-princess-8 | Numerics | None | |
| rcnn-ilsvrc13-7 | PASS | None | |
| resnet101-v1-7 | Numerics | None | |
| resnet101-v2-7 | Numerics | None | |
| resnet152-v1-7 | Numerics | None | |
| resnet152-v2-7 | Numerics | None | |
| resnet18-v1-7 | Numerics | None | |
| resnet18-v2-7 | Numerics | None | |
| resnet34-v1-7 | Numerics | None | |
| resnet34-v2-7 | Numerics | None | |
| resnet50-caffe2-v1-7 | Numerics | None | |
| resnet50-v1-12 | Numerics | None | |
| resnet50-v1-12-qdq | PASS | None | |
| resnet50-v1-7 | Numerics | None | |
| resnet50-v2-7 | Numerics | None | |
| retinanet-9 | compilation | None | |
| shufflenet-7 | PASS | None | |
| shufflenet-v2-10 | PASS | None | |
| shufflenet-v2-12 | PASS | None | |
| shufflenet-v2-12-qdq | Numerics | None | |
| squeezenet1.0-12 | PASS | None | |
| squeezenet1.0-13-qdq | compilation | None | |
| squeezenet1.0-6 | PASS | None | |
| squeezenet1.0-9 | PASS | None | |
| squeezenet1.1-7 | PASS | None | |
| super-resolution-10 | PASS | None | |
| tinyyolov2-7 | compiled_inference | None | |
| version-RFB-320 | PASS | None | |
| version-RFB-640 | PASS | None | |
| vgg16-12 | PASS | None | |
| vgg16-12-qdq | Numerics | None | |
| vgg16-7 | PASS | None | |
| vgg16-bn-7 | import_model | None | |
| vgg19-7 | PASS | None | |
| vgg19-bn-7 | import_model | None | |
| vgg19-caffe2-8 | PASS | None | |
| yolov2-coco-9 | PASS | None | |
| yolov4 | compilation | None | |
| zfnet512-12 | PASS | None | |
| zfnet512-12-qdq | Numerics | None | |
| zfnet512-9 | PASS | None | |
