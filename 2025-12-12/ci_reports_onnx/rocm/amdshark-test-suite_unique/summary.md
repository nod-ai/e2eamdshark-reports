## Passing Summary

**TOTAL TESTS = 28**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 0 | 0.0% | 0.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 28**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 28 | 100.0% |
| IREE Compilation | 0 | 0.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/amdshark-test-suite_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/amdshark-test-suite_unique.md', get_metadata=True)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| AlexNet_vaiq_int8 | setup | None | |
| ConvNeXt_vaiq_int8 | setup | None | |
| CSP-DarkNet_vaiq_int8 | setup | None | |
| DarkNet53_vaiq_int8 | setup | None | |
| DeepLabV3_resnet50_vaiq_int8 | setup | None | |
| DenseNet201_vaiq_int8 | setup | None | |
| EfficientNet_v2_s_vaiq_int8 | setup | None | |
| FCN_vaiq_int8 | setup | None | |
| GoogLeNet_vaiq_int8 | setup | None | |
| Inception_v4_vaiq_int8 | setup | None | |
| LRASPP_vaiq_int8 | setup | None | |
| MNASNet_1_3_vaiq_int8 | setup | None | |
| MobileNetV3_small_vaiq_int8 | setup | None | |
| pytorch-3dunet_vaiq_int8 | setup | None | |
| RAFT_vaiq_int8 | setup | None | |
| RDN_pytorch_vaiq_int8 | setup | None | |
| RegNet_y_8gf_vaiq_int8 | setup | None | |
| ResNet152_vaiq_int8 | setup | None | |
| RRDB_ESRGAN_vaiq_int8 | setup | None | |
| ShuffleNet_v2_x2_0_vaiq_int8 | setup | None | |
| SqueezeNet_1_1_vaiq_int8 | setup | None | |
| U-2-Net_vaiq_int8 | setup | None | |
| u-net_brain_mri_vaiq_int8 | setup | None | |
| VGG11_bn_vaiq_int8 | setup | None | |
| VGG19_vaiq_int8 | setup | None | |
| VideoResNet_vaiq_int8 | setup | None | |
| WideResNet_50_2_vaiq_int8 | setup | None | |
| YoloNetV3_vaiq_int8 | setup | None | |
