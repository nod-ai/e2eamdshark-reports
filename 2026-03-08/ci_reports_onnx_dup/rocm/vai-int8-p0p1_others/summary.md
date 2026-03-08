## Passing Summary

**TOTAL TESTS = 59**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 59 | 100.0% | 100.0% |
| IREE Compilation | 18 | 30.5% | 30.5% |
| Gold Inference | 18 | 30.5% | 100.0% |
| IREE Inference Invocation | 18 | 30.5% | 100.0% |
| Inference Comparison (PASS) | 16 | 27.1% | 88.9% |
## Fail Summary

**TOTAL TESTS = 59**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 41 | 69.5% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 2 | 3.4% |
## Test Run Detail
Test was run with the following arguments:
Namespace(sources=['./e2eamdshark-reports/ci_reports_rocm_vai-int8-p0p1-shard1_others_onnx_json/vai-int8-p0p1-shard1_others.json', './e2eamdshark-reports/ci_reports_rocm_vai-int8-p0p1-shard2_others_onnx_json/vai-int8-p0p1-shard2_others.json', './e2eamdshark-reports/ci_reports_rocm_vai-int8-p0p1-shard3_others_onnx_json/vai-int8-p0p1-shard3_others.json'], output='./e2eamdshark-reports/vai-int8-p0p1_others.json', report=True, report_file='./e2eamdshark-reports/vai-int8-p0p1_others.md')

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| adv_inception_v3_vaiq | Numerics | None | |
| densenet121_vaiq | PASS | None | |
| efficientnet_el.ra_in1k_vaiq | PASS | None | |
| efficientnet_es.ra_in1k_vaiq | PASS | None | |
| gluon_inception_v3_vaiq | PASS | None | |
| gluon_resnet101_v1b_vaiq | compilation | None | |
| gluon_resnet152_v1b_vaiq | compilation | None | |
| gluon_resnet34_v1b_vaiq | compilation | None | |
| gluon_resnet50_v1b_vaiq | compilation | None | |
| gluon_resnext50_32x4d_vaiq | compilation | None | |
| ig_resnext101_32x32d_vaiq | compilation | None | |
| ig_resnext101_32x8d_vaiq | compilation | None | |
| inception_resnet_v2_vaiq | Numerics | None | |
| inception_v3_vaiq | PASS | None | |
| mobilenetv3_large_100.miil_in21k_ft_in1k_vaiq | PASS | None | |
| regnetx_008.tv2_in1k_vaiq | PASS | None | |
| regnetx_016.tv2_in1k_vaiq | PASS | None | |
| regnetx_032.tv2_in1k_vaiq | compilation | None | |
| regnetx_080.tv2_in1k_vaiq | compilation | None | |
| regnetx_160.tv2_in1k_vaiq | compilation | None | |
| regnetx_320.tv2_in1k_vaiq | compilation | None | |
| regnety_004.tv2_in1k_vaiq | PASS | None | |
| regnety_016.tv2_in1k_vaiq | PASS | None | |
| regnety_032.tv2_in1k_vaiq | compilation | None | |
| regnety_160.sw_in12k_ft_in1k_train_vaiq | compilation | None | |
| regnety_160.sw_in12k_ft_in1k_vaiq | compilation | None | |
| regnety_160.swag_ft_in1k_vaiq | compilation | None | |
| regnety_160.swag_lc_in1k_vaiq | compilation | None | |
| regnety_160.tv2_in1k_vaiq | compilation | None | |
| regnety_320.swag_ft_in1k_vaiq | compilation | None | |
| regnety_320.swag_lc_in1k_vaiq | compilation | None | |
| regnety_320.tv2_in1k_vaiq | compilation | None | |
| resmlp_12_224.fb_in1k_vaiq | PASS | None | |
| resmlp_24_224.fb_in1k_vaiq | PASS | None | |
| resmlp_36_224.fb_in1k_vaiq | PASS | None | |
| resnet101_vaiq | compilation | None | |
| resnet152_vaiq | compilation | None | |
| resnet18_vaiq | compilation | None | |
| resnet34_vaiq | compilation | None | |
| resnet50_vaiq | compilation | None | |
| resnet50d_vaiq | PASS | None | |
| resnetv2_152x2_bit.goog_teacher_in21k_ft_in1k_384_vaiq | compilation | None | |
| resnext101_32x8d_vaiq | compilation | None | |
| resnext50_32x4d_vaiq | compilation | None | |
| seresnext50_32x4d_vaiq | compilation | None | |
| ssl_resnet18_vaiq | compilation | None | |
| ssl_resnet50_vaiq | compilation | None | |
| ssl_resnext101_32x4d_vaiq | compilation | None | |
| ssl_resnext101_32x8d_vaiq | compilation | None | |
| ssl_resnext50_32x4d_vaiq | compilation | None | |
| swsl_resnet18_vaiq | compilation | None | |
| swsl_resnet50_vaiq | compilation | None | |
| swsl_resnext101_32x16d_vaiq | compilation | None | |
| swsl_resnext101_32x4d_vaiq | compilation | None | |
| swsl_resnext101_32x8d_vaiq | compilation | None | |
| swsl_resnext50_32x4d_vaiq | compilation | None | |
| tf_efficientnetv2_b3.in21k_ft_in1k_train_vaiq | PASS | None | |
| tf_efficientnetv2_b3.in21k_ft_in1k_vaiq | PASS | None | |
| xception_vaiq | compilation | None | |
