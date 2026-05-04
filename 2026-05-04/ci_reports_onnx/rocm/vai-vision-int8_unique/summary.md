## Passing Summary

**TOTAL TESTS = 73**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 73 | 100.0% | 100.0% |
| IREE Compilation | 70 | 95.9% | 95.9% |
| Gold Inference | 70 | 95.9% | 100.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 73**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 3 | 4.1% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 70 | 95.9% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/vai-vision-int8_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/vai-vision-int8_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| dla169_vaiq | compiled_inference | None | |
| efficientnet_b0.ra_in1k_vaiq | compiled_inference | None | |
| EfficientNet_b0_vaiq | compiled_inference | None | |
| efficientnet_b1.ft_in1k_vaiq | compiled_inference | None | |
| EfficientNet_b1_vaiq | compiled_inference | None | |
| efficientnet_b2.ra_in1k_vaiq | compiled_inference | None | |
| EfficientNet_b2_vaiq | compiled_inference | None | |
| efficientnet_b3.ra2_in1k_vaiq | compiled_inference | None | |
| EfficientNet_b3_vaiq | compiled_inference | None | |
| efficientnet_b4.ra2_in1k_vaiq | compiled_inference | None | |
| EfficientNet_b4_vaiq | compiled_inference | None | |
| efficientnet_b5.sw_in12k_vaiq | compiled_inference | None | |
| EfficientNet_b5_vaiq | compiled_inference | None | |
| EfficientNet_b6_vaiq | compiled_inference | None | |
| EfficientNet_b7_vaiq | compiled_inference | None | |
| efficientnet_el_pruned.in1k_vaiq | compiled_inference | None | |
| efficientnet_em.ra2_in1k_vaiq | compiled_inference | None | |
| efficientnet_es_pruned.in1k_vaiq | compiled_inference | None | |
| efficientnet_lite0.ra_in1k_vaiq | compiled_inference | None | |
| EfficientNet_v2_l_vaiq | compiled_inference | None | |
| EfficientNet_v2_m_vaiq | compiled_inference | None | |
| EfficientNet_v2_s_vaiq | compiled_inference | None | |
| efficientnetv2_rw_m.agc_in1k_vaiq | compiled_inference | None | |
| efficientnetv2_rw_s.ra2_in1k_vaiq | compiled_inference | None | |
| efficientnetv2_rw_t.ra2_in1k_vaiq | compiled_inference | None | |
| fbnetc_100.rmsp_in1k_vaiq | compiled_inference | None | |
| gernet_l.idstcv_in1k_vaiq | compiled_inference | None | |
| gernet_m.idstcv_in1k_vaiq | compiled_inference | None | |
| gernet_s.idstcv_in1k_vaiq | compiled_inference | None | |
| GoogLeNet_vaiq | compiled_inference | None | |
| inception_v3.tf_in1k_vaiq | compiled_inference | None | |
| Inception_v3_vaiq | compiled_inference | None | |
| inception_v4.tf_in1k_vaiq | compiled_inference | None | |
| lcnet_050.ra2_in1k_vaiq | compiled_inference | None | |
| lcnet_075.ra2_in1k_vaiq | compiled_inference | None | |
| lcnet_100.ra2_in1k_vaiq | compiled_inference | None | |
| mnasnet_100.rmsp_in1k_vaiq | compiled_inference | None | |
| mnasnet_small.lamb_in1k_vaiq | compiled_inference | None | |
| mobilenetv2_050.lamb_in1k_vaiq | compiled_inference | None | |
| mobilenetv2_100.ra_in1k_vaiq | compiled_inference | None | |
| mobilenetv2_110d.ra_in1k_vaiq | compiled_inference | None | |
| mobilenetv2_120d.ra_in1k_vaiq | compiled_inference | None | |
| mobilenetv2_140.ra_in1k_vaiq | compiled_inference | None | |
| MobileNetV2_vaiq | compiled_inference | None | |
| mobilenetv3_large_100.ra_in1k_vaiq | compiled_inference | None | |
| MobileNetV3_large_vaiq | compiled_inference | None | |
| mobilenetv3_small_050.lamb_in1k_vaiq | compiled_inference | None | |
| mobilenetv3_small_075.lamb_in1k_vaiq | compiled_inference | None | |
| mobilenetv3_small_100.lamb_in1k_vaiq | compiled_inference | None | |
| MobileNetV3_small_vaiq | compiled_inference | None | |
| ResNet101_vaiq | compiled_inference | None | |
| ResNet152_vaiq | compiled_inference | None | |
| ResNet18_vaiq | compiled_inference | None | |
| resnet32ts.ra2_in1k_vaiq | compiled_inference | None | |
| resnet33ts.ra2_in1k_vaiq | compiled_inference | None | |
| ResNet34_vaiq | compiled_inference | None | |
| resnet50.a1_in1k_vaiq | compiled_inference | None | |
| ResNet50_vaiq | compiled_inference | None | |
| RRDB_ESRGAN_pro_vaiq | compilation | None | |
| RRDB_ESRGAN_vaiq | compilation | None | |
| SqueezeNet_1_0_vaiq | compiled_inference | None | |
| VGG11_bn_vaiq | compiled_inference | None | |
| VGG11_vaiq | compiled_inference | None | |
| VGG13_bn_vaiq | compiled_inference | None | |
| VGG13_vaiq | compiled_inference | None | |
| VGG16_bn_vaiq | compiled_inference | None | |
| VGG16_vaiq | compiled_inference | None | |
| VGG19_bn_vaiq | compiled_inference | None | |
| VGG19_vaiq | compiled_inference | None | |
| WideResNet_101_2_vaiq | compiled_inference | None | |
| WideResNet_50_2_vaiq | compiled_inference | None | |
| YoloNetV3_vaiq | compiled_inference | None | |
| Yolov8m_vaiq | compilation | None | |
