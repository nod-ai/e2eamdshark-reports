# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|10.9412|10.8913|-0.0499|-0.46%|
|migraphx_torchvision__inceptioni32|PASS|within tol|18.3684|18.3348|-0.0336|-0.18%|
|migraphx_torchvision__resnet50i64|PASS|within tol|12.6636|12.6101|-0.0534|-0.42%|

## 34 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|gluon_resnet101_v1b_vaiq|PASS|compilation|
|gluon_resnet152_v1b_vaiq|PASS|compilation|
|gluon_resnet34_v1b_vaiq|PASS|compilation|
|gluon_resnet50_v1b_vaiq|PASS|compilation|
|gluon_resnext50_32x4d_vaiq|PASS|compilation|
|ig_resnext101_32x32d_vaiq|PASS|compilation|
|ig_resnext101_32x8d_vaiq|PASS|compilation|
|model--bart-base-cnn--ainize|PASS|compiled_inference|
|model--bart-base-samsum--philschmid|PASS|compiled_inference|
|model--bart-base-xsum--harouzie|PASS|compiled_inference|
|model--bart-base-xsum--morenolq|PASS|compiled_inference|
|model--bart-german--Shahm|PASS|compiled_inference|
|model--bart_lfqa_sqaud--Shubham09|PASS|compiled_inference|
|resnet101_vaiq|PASS|compilation|
|resnet152_vaiq|PASS|compilation|
|resnet18_vaiq|PASS|compilation|
|resnet34_vaiq|PASS|compilation|
|resnet50_vaiq|PASS|compilation|
|resnetv2_101_Opset17_timm|PASS|setup|
|resnext101_32x8d_vaiq|PASS|compilation|
|resnext50_32x4d_vaiq|PASS|compilation|
|seresnext50_32x4d_vaiq|PASS|compilation|
|ssl_resnet18_vaiq|PASS|compilation|
|ssl_resnet50_vaiq|PASS|compilation|
|ssl_resnext101_32x4d_vaiq|PASS|compilation|
|ssl_resnext101_32x8d_vaiq|PASS|compilation|
|ssl_resnext50_32x4d_vaiq|PASS|compilation|
|swsl_resnet18_vaiq|PASS|compilation|
|swsl_resnet50_vaiq|PASS|compilation|
|swsl_resnext101_32x16d_vaiq|PASS|compilation|
|swsl_resnext101_32x4d_vaiq|PASS|compilation|
|swsl_resnext101_32x8d_vaiq|PASS|compilation|
|swsl_resnext50_32x4d_vaiq|PASS|compilation|
|xception_vaiq|PASS|compilation|

## 86 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|cait_m36_384_Opset18_timm|compilation|PASS|
|cait_s24_384_Opset17_timm|compilation|PASS|
|cait_s36_384_Opset18_timm|compilation|PASS|
|cait_xxs24_384_Opset17_timm|compilation|PASS|
|cait_xxs36_384_Opset17_timm|compilation|PASS|
|convnext_base_Opset17_timm|compilation|PASS|
|convnext_base_Opset18_timm|compilation|PASS|
|convnext_base_Opset18_torch_hub|compilation|PASS|
|convnext_base_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_base_in22k_Opset18_timm|compilation|PASS|
|convnext_nano_Opset18_timm|compilation|PASS|
|convnext_nano_ols_Opset17_timm|compilation|PASS|
|convnext_small_Opset18_timm|compilation|PASS|
|convnext_small_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_small_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_small_in22k_Opset18_timm|compilation|PASS|
|convnext_tiny_Opset17_timm|compilation|PASS|
|convnext_tiny_Opset17_torch_hub|compilation|PASS|
|convnext_tiny_Opset18_timm|compilation|PASS|
|convnext_tiny_hnf_Opset17_timm|compilation|PASS|
|convnext_tiny_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_tiny_in22k_Opset18_timm|compilation|PASS|
|edgenext_x_small_Opset18_timm|compilation|PASS|
|mobilevit_s_Opset17_timm|compilation|PASS|
|mobilevit_xxs_Opset17_timm|compilation|PASS|
|mobilevitv2_125_Opset17_timm|setup|PASS|
|resnext101_32x4d_Opset16_timm|setup|PASS|
|swinv2_base_window16_256.ms_in1k|compilation|PASS|
|xcit_large_24_p16_224_Opset18_timm|compilation|PASS|
|xcit_large_24_p16_224_dist|compilation|PASS|
|xcit_large_24_p16_224_dist_Opset17_timm|compilation|PASS|
|xcit_large_24_p16_224_dist_Opset18_timm|compilation|PASS|
|xcit_large_24_p16_384_dist_Opset18_timm|compilation|PASS|
|xcit_large_24_p8_224_Opset18_timm|compilation|PASS|
|xcit_large_24_p8_224_dist|compilation|PASS|
|xcit_large_24_p8_224_dist_Opset17_timm|compilation|PASS|
|xcit_large_24_p8_224_dist_Opset18_timm|compilation|PASS|
|xcit_medium_24_p16_224_Opset17_timm|compilation|PASS|
|xcit_medium_24_p16_224_dist|compilation|PASS|
|xcit_medium_24_p16_224_dist_Opset17_timm|compilation|PASS|
|xcit_medium_24_p16_224_dist_Opset18_timm|compilation|PASS|
|xcit_nano_12_p16_224_Opset17_timm|compilation|PASS|
|xcit_nano_12_p16_224_dist|compilation|PASS|
|xcit_nano_12_p16_224_dist_Opset17_timm|compilation|PASS|
|xcit_nano_12_p16_224_dist_Opset18_timm|compilation|PASS|
|xcit_nano_12_p16_384_dist_Opset18_timm|compilation|PASS|
|xcit_nano_12_p8_224_Opset17_timm|compilation|PASS|
|xcit_nano_12_p8_224_Opset18_timm|compilation|PASS|
|xcit_nano_12_p8_224_dist|compilation|PASS|
|xcit_nano_12_p8_224_dist_Opset17_timm|compilation|PASS|
|xcit_nano_12_p8_384_dist_Opset17_timm|compilation|PASS|
|xcit_small_12_p16_224_Opset18_timm|compilation|PASS|
|xcit_small_12_p16_224_dist|compilation|PASS|
|xcit_small_12_p16_224_dist_Opset17_timm|compilation|PASS|
|xcit_small_12_p16_224_dist_Opset18_timm|compilation|PASS|
|xcit_small_12_p16_384_dist_Opset18_timm|compilation|PASS|
|xcit_small_12_p8_224_Opset17_timm|compilation|PASS|
|xcit_small_12_p8_224_Opset18_timm|compilation|PASS|
|xcit_small_12_p8_224_dist|compilation|PASS|
|xcit_small_12_p8_224_dist_Opset18_timm|compilation|PASS|
|xcit_small_24_p16_224_Opset18_timm|compilation|PASS|
|xcit_small_24_p16_224_dist|compilation|PASS|
|xcit_small_24_p16_224_dist_Opset17_timm|compilation|PASS|
|xcit_small_24_p16_224_dist_Opset18_timm|compilation|PASS|
|xcit_small_24_p8_224_Opset17_timm|compilation|PASS|
|xcit_small_24_p8_224_dist|compilation|PASS|
|xcit_small_24_p8_224_dist_Opset17_timm|compilation|PASS|
|xcit_small_24_p8_224_dist_Opset18_timm|compilation|PASS|
|xcit_tiny_12_p16_224_Opset18_timm|compilation|PASS|
|xcit_tiny_12_p16_224_dist|compilation|PASS|
|xcit_tiny_12_p16_224_dist_Opset17_timm|compilation|PASS|
|xcit_tiny_12_p16_224_dist_Opset18_timm|compilation|PASS|
|xcit_tiny_12_p16_384_dist_Opset18_timm|compilation|PASS|
|xcit_tiny_12_p8_224_Opset18_timm|compilation|PASS|
|xcit_tiny_12_p8_224_dist|compilation|PASS|
|xcit_tiny_12_p8_224_dist_Opset17_timm|compilation|PASS|
|xcit_tiny_12_p8_224_dist_Opset18_timm|compilation|PASS|
|xcit_tiny_24_p16_224_Opset17_timm|compilation|PASS|
|xcit_tiny_24_p16_224_Opset18_timm|compilation|PASS|
|xcit_tiny_24_p16_224_dist|compilation|PASS|
|xcit_tiny_24_p16_224_dist_Opset17_timm|compilation|PASS|
|xcit_tiny_24_p16_384_dist_Opset17_timm|compilation|PASS|
|xcit_tiny_24_p8_224_Opset17_timm|compilation|PASS|
|xcit_tiny_24_p8_224_dist|compilation|PASS|
|xcit_tiny_24_p8_224_dist_Opset17_timm|compilation|PASS|
|xcit_tiny_24_p8_224_dist_Opset18_timm|compilation|PASS|

