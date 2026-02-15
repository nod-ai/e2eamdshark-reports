# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|10.9617|10.9432|-0.0185|-0.17%|
|migraphx_torchvision__inceptioni32|PASS|within tol|18.3954|18.4085|0.0131|0.07%|
|migraphx_torchvision__resnet50i64|PASS|within tol|12.6403|12.6332|-0.0071|-0.06%|

## No Regressions Found

## 17 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit_base_patch16_384_Opset18_timm|setup|PASS|
|dpn68_Opset16_timm|setup|PASS|
|eca_resnext26ts_Opset16_timm|setup|PASS|
|gluon_resnet101_v1s_Opset18_timm|setup|PASS|
|gluon_resnet152_v1d_Opset17_timm|setup|PASS|
|hrnet_w32_Opset18_timm|setup|PASS|
|resnet152_Opset17_torch_hub|setup|PASS|
|resnetv2_50d_gn_Opset18_timm|setup|PASS|
|ssl_resnet18_Opset18_timm|setup|PASS|
|tf_efficientnet_b5_Opset17_timm|setup|PASS|
|tf_efficientnetv2_b1_Opset17_timm|setup|PASS|
|tf_efficientnetv2_m_in21k_Opset17_timm|setup|PASS|
|umt5encoder_Opset17_transformers|setup|PASS|
|visformer_small_Opset16_timm|setup|PASS|
|vit_large_patch32_384_Opset18_timm|setup|PASS|
|wide_resnet101_2_Opset17_timm|setup|PASS|
|xcit_small_24_p8_224_dist_Opset18_timm|setup|compilation|

