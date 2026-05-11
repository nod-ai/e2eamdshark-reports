## Passing Summary

**TOTAL TESTS = 71**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 71 | 100.0% | 100.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 71**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 71 | 100.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/onnx_model_zoo_validated_vision_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/onnx_model_zoo_validated_vision_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| arcfaceresnet100-8 | compilation | None | |
| bvlcalexnet-12 | compilation | None | |
| bvlcalexnet-12-qdq | compilation | None | |
| bvlcalexnet-8 | compilation | None | |
| caffenet-12 | compilation | None | |
| caffenet-12-qdq | compilation | None | |
| caffenet-9 | compilation | None | |
| densenet-12 | compilation | None | |
| densenet-6 | compilation | None | |
| efficientnet-lite4-11 | compilation | None | |
| efficientnet-lite4-11-qdq | compilation | None | |
| emotion-ferplus-12-int8 | compilation | None | |
| emotion-ferplus-8 | compilation | None | |
| fcn-resnet101-11 | compilation | None | |
| fcn-resnet50-11 | compilation | None | |
| fcn-resnet50-12 | compilation | None | |
| fcn-resnet50-12-qdq | compilation | None | |
| googlenet-12 | compilation | None | |
| googlenet-12-qdq | compilation | None | |
| googlenet-7 | compilation | None | |
| inception-v1-12 | compilation | None | |
| inception-v1-12-qdq | compilation | None | |
| inception-v1-7 | compilation | None | |
| inception-v2-9 | compilation | None | |
| mnist-12 | compilation | None | |
| mnist-8 | compilation | None | |
| mobilenetv2-10 | compilation | None | |
| mobilenetv2-12 | compilation | None | |
| mobilenetv2-12-qdq | compilation | None | |
| mobilenetv2-7 | compilation | None | |
| rain-princess-8 | compilation | None | |
| rcnn-ilsvrc13-7 | compilation | None | |
| resnet101-v1-7 | compilation | None | |
| resnet101-v2-7 | compilation | None | |
| resnet152-v1-7 | compilation | None | |
| resnet152-v2-7 | compilation | None | |
| resnet18-v1-7 | compilation | None | |
| resnet18-v2-7 | compilation | None | |
| resnet34-v1-7 | compilation | None | |
| resnet34-v2-7 | compilation | None | |
| resnet50-caffe2-v1-7 | compilation | None | |
| resnet50-v1-12 | compilation | None | |
| resnet50-v1-12-qdq | compilation | None | |
| resnet50-v1-7 | compilation | None | |
| resnet50-v2-7 | compilation | None | |
| retinanet-9 | compilation | None | |
| shufflenet-7 | compilation | None | |
| shufflenet-v2-10 | compilation | None | |
| shufflenet-v2-12 | compilation | None | |
| shufflenet-v2-12-qdq | compilation | None | |
| squeezenet1.0-12 | compilation | None | |
| squeezenet1.0-13-qdq | compilation | None | |
| squeezenet1.0-6 | compilation | None | |
| squeezenet1.0-9 | compilation | None | |
| squeezenet1.1-7 | compilation | None | |
| super-resolution-10 | compilation | None | |
| tinyyolov2-7 | compilation | None | |
| version-RFB-320 | compilation | None | |
| version-RFB-640 | compilation | None | |
| vgg16-12 | compilation | None | |
| vgg16-12-qdq | compilation | None | |
| vgg16-7 | compilation | None | |
| vgg16-bn-7 | import_model | None | |
| vgg19-7 | compilation | None | |
| vgg19-bn-7 | import_model | None | |
| vgg19-caffe2-8 | compilation | None | |
| yolov2-coco-9 | compilation | None | |
| yolov4 | compilation | None | |
| zfnet512-12 | compilation | None | |
| zfnet512-12-qdq | compilation | None | |
| zfnet512-9 | compilation | None | |
