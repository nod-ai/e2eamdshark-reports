## Passing Summary

**TOTAL TESTS = 71**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 70 | 98.6% | 98.6% |
| IREE Compilation | 59 | 83.1% | 84.3% |
| Gold Inference | 57 | 80.3% | 96.6% |
| IREE Inference Invocation | 57 | 80.3% | 100.0% |
| Inference Comparison (PASS) | 53 | 74.6% | 93.0% |
## Fail Summary

**TOTAL TESTS = 71**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 1.4% |
| IREE Compilation | 11 | 15.5% |
| Gold Inference | 2 | 2.8% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 4 | 5.6% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-image-classification-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-image-classification-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_beit-base-patch16-224-pt22k | PASS | None | |
| hf_beit-base-patch16-224-pt22k-ft22k | PASS | None | |
| hf_beit_base_patch16_224.in22k_ft_in22k_in1k | PASS | None | |
| hf_beitv2_base_patch16_224.in1k_ft_in22k | PASS | None | |
| hf_convnext_base.fb_in22k_ft_in1k | compilation | None | |
| hf_convnext_large_mlp.clip_laion2b_soup_ft_in12k_in1k_320 | compilation | None | |
| hf_convnextv2_base.fcmae_ft_in22k_in1k | compilation | None | |
| hf_cspdarknet53.ra_in1k | PASS | None | |
| hf_deit-base-patch16-224 | PASS | None | |
| hf_deit-tiny-patch16-224 | PASS | None | |
| hf_deit_base_distilled_patch16_224.fb_in1k | PASS | None | |
| hf_densenet121.ra_in1k | PASS | None | |
| hf_efficientnet_b0.ra_in1k | Numerics | None | |
| hf_efficientnet_b3.ra2_in1k | Numerics | None | |
| hf_efficientnet_b4.ra2_in1k | Numerics | None | |
| hf_ese_vovnet19b_dw.ra_in1k | PASS | None | |
| hf_eva_large_patch14_196.in22k_ft_in22k_in1k | native_inference | None | |
| hf_gender-classification | PASS | None | |
| hf_hrnet_w18.ms_aug_in1k | PASS | None | |
| hf_inception_resnet_v2.tf_in1k | PASS | None | |
| hf_inception_v3.tf_adv_in1k | PASS | None | |
| hf_inception_v3.tv_in1k | PASS | None | |
| hf_lcnet_050.ra2_in1k | PASS | None | |
| hf_mit-b0 | compilation | None | |
| hf_mit-b5 | compilation | None | |
| hf_mobilenet_v1_0.75_192 | native_inference | None | |
| hf_mobilenet_v2_1.0_224 | PASS | None | |
| hf_mobilenetv2_100.ra_in1k | PASS | None | |
| hf_mobilenetv3_large_100.miil_in21k_ft_in1k | PASS | None | |
| hf_mobilenetv3_large_100.ra_in1k | PASS | None | |
| hf_mobilevit-small | compilation | None | |
| hf_nfnet_l0.ra2_in1k | compilation | None | |
| hf_nsfw-classifier | PASS | None | |
| hf_nsfw_image_detection | PASS | None | |
| hf_pedestrian_gender_recognition | PASS | None | |
| hf_pnasnet5large.tf_in1k | compilation | None | |
| hf_regnety_002.pycls_in1k | PASS | None | |
| hf_resnet-18 | PASS | None | |
| hf_resnet-50 | PASS | None | |
| hf_resnet101.a1h_in1k | PASS | None | |
| hf_resnet18.a1_in1k | PASS | None | |
| hf_resnet34.a1_in1k | PASS | None | |
| hf_resnet50.a1_in1k | PASS | None | |
| hf_resnext50_32x4d.fb_swsl_ig1b_ft_in1k | PASS | None | |
| hf_roramdshark-vit-base | setup | None | |
| hf_swin-tiny-patch4-window7-224 | compilation | None | |
| hf_swin_base_patch4_window7_224.ms_in22k_ft_in1k | compilation | None | |
| hf_tf_efficientnet_b0.ns_jft_in1k | Numerics | None | |
| hf_tf_efficientnetv2_s.in21k | PASS | None | |
| hf_tf_mobilenetv3_large_minimal_100.in1k | PASS | None | |
| hf_tf_mobilenetv3_small_minimal_100.in1k | PASS | None | |
| hf_UL_base_classification | PASS | None | |
| hf_vgg16.tv_in1k | PASS | None | |
| hf_vgg19.tv_in1k | PASS | None | |
| hf_vit-age-classifier | PASS | None | |
| hf_vit-base-patch16-224 | PASS | None | |
| hf_vit-base-uppercase-english-characters | PASS | None | |
| hf_vit-face-expression | PASS | None | |
| hf_vit-large-patch16-224 | PASS | None | |
| hf_vit-small-patch16-224 | PASS | None | |
| hf_vit-tiny-patch16-224 | PASS | None | |
| hf_vit_base_patch16_224.augreg2_in21k_ft_in1k | PASS | None | |
| hf_vit_base_patch16_224.augreg_in21k | PASS | None | |
| hf_vit_base_patch32_224.augreg_in21k_ft_in1k | PASS | None | |
| hf_vit_base_patch8_224.augreg2_in21k_ft_in1k | PASS | None | |
| hf_vit_large_patch16_224.augreg_in21k_ft_in1k | PASS | None | |
| hf_vit_small_patch16_224.augreg_in21k_ft_in1k | PASS | None | |
| hf_vit_tiny_patch16_224.augreg_in21k_ft_in1k | PASS | None | |
| hf_watermark_detector | PASS | None | |
| hf_wide_resnet50_2.racm_in1k | PASS | None | |
| hf_xcit_tiny_24_p8_384.fb_dist_in1k | compilation | None | |
