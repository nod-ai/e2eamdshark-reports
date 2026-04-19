# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|progression|11.3953|10.7468|-0.6485|-5.69%|
|migraphx_torchvision__inceptioni32|PASS|progression|19.631|17.9905|-1.6405|-8.36%|
|migraphx_torchvision__resnet50i64|PASS|progression|13.4431|11.9539|-1.4891|-11.08%|

## 37 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|googlenet-3|PASS|compilation|
|googlenet-6|PASS|compilation|
|googlenet-8|PASS|compilation|
|googlenet-9|PASS|compilation|
|hrnet_w64_Opset17_timm|PASS|compilation|
|hrnet_w64_Opset18_timm|PASS|compilation|
|inception-v1-8|PASS|compilation|
|inception-v1-9|PASS|compilation|
|maxvit_base_tf_384.in21k_ft_in1k|PASS|compilation|
|maxvit_base_tf_512.in21k_ft_in1k|PASS|compilation|
|maxvit_large_tf_384.in21k_ft_in1k|PASS|compilation|
|nf_regnet_b1_Opset17_timm|Numerics|compilation|
|repvgg_b2g4_Opset17_timm|Numerics|compilation|
|repvgg_b2g4_Opset18_timm|Numerics|compilation|
|resmlp_12_224.fb_in1k_vaiq|PASS|compilation|
|resmlp_24_224.fb_in1k_vaiq|PASS|compilation|
|resmlp_36_224.fb_in1k_vaiq|PASS|compilation|
|resnest50d_4s2x40d_Opset17_timm|Numerics|compilation|
|resnetv2_101_Opset16_timm|PASS|compilation|
|resnetv2_101_Opset17_timm|PASS|compilation|
|resnetv2_50_Opset17_timm|PASS|compilation|
|resnetv2_50_Opset18_timm|PASS|compilation|
|squeezebert_Opset17_transformers|PASS|compilation|
|tf_efficientnet_b8.ra_in1k|PASS|compilation|
|tf_efficientnet_b8_Opset16_timm|PASS|compilation|
|tf_efficientnet_b8_Opset17_timm|PASS|compilation|
|tf_efficientnet_b8_ap_Opset16_timm|PASS|compilation|
|visformer_small_Opset16_timm|PASS|compilation|
|visformer_small_Opset18_timm|PASS|compilation|
|xception41_Opset16_timm|PASS|compilation|
|xception41_Opset18_timm|PASS|compilation|
|xception65_Opset16_timm|PASS|compilation|
|xception65_Opset17_timm|PASS|compilation|
|xception71_Opset16_timm|PASS|compilation|
|xception71_Opset18_timm|PASS|compilation|

## 49 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|bvlcalexnet-7|compilation|PASS|
|bvlcalexnet-9|compilation|PASS|
|dm_nfnet_f0_Opset17_timm|compilation|PASS|
|dm_nfnet_f1_Opset17_timm|compilation|PASS|
|dm_nfnet_f3_Opset17_timm|compilation|PASS|
|regnet_x_16gf_Opset16_torch_hub|compilation|PASS|
|regnet_x_16gf_Opset17_torch_hub|compilation|PASS|
|regnet_x_32gf_Opset17_torch_hub|compilation|PASS|
|regnet_x_32gf_Opset18_torch_hub|compilation|PASS|
|regnet_x_3_2gf_Opset17_torch_hub|compilation|PASS|
|regnet_x_3_2gf_Opset18_torch_hub|setup|PASS|
|regnet_x_800mf_Opset18_torch_hub|setup|PASS|
|regnet_x_8gf_Opset16_torch_hub|compilation|PASS|
|regnet_x_8gf_Opset17_torch_hub|compilation|PASS|
|regnet_y_16gf_Opset16_torch_hub|compilation|PASS|
|regnet_y_16gf_Opset18_torch_hub|compilation|PASS|
|regnet_y_32gf_Opset16_torch_hub|compilation|PASS|
|regnet_y_32gf_Opset17_torch_hub|compilation|PASS|
|regnetx_032_Opset16_timm|compilation|PASS|
|regnetx_032_Opset17_timm|compilation|PASS|
|regnetx_080.tv2_in1k_vaiq|compilation|PASS|
|regnetx_080_Opset16_timm|compilation|PASS|
|regnetx_080_Opset18_timm|compilation|PASS|
|regnetx_120_Opset17_timm|compilation|PASS|
|regnetx_120_Opset18_timm|compilation|PASS|
|regnetx_160.tv2_in1k_vaiq|compilation|Numerics|
|regnetx_160_Opset17_timm|compilation|PASS|
|regnetx_160_Opset18_timm|compilation|PASS|
|regnetx_320.tv2_in1k_vaiq|compilation|PASS|
|regnetx_320_Opset16_timm|compilation|PASS|
|regnetx_320_Opset18_timm|compilation|PASS|
|regnety_120_Opset16_timm|compilation|PASS|
|regnety_160.sw_in12k_ft_in1k_vaiq|compilation|PASS|
|regnety_160.swag_ft_in1k_vaiq|compilation|Numerics|
|regnety_160_Opset16_timm|compilation|PASS|
|regnety_320.swag_ft_in1k_vaiq|compilation|Numerics|
|regnety_320.swag_lc_in1k_vaiq|compilation|Numerics|
|regnety_320.tv2_in1k_vaiq|compilation|PASS|
|regnety_320_Opset16_timm|compilation|PASS|
|repvgg_b1g4_Opset16_timm|compilation|PASS|
|repvgg_b1g4_Opset18_timm|compilation|PASS|
|repvgg_b3g4_Opset17_timm|compilation|PASS|
|repvgg_b3g4_Opset18_timm|compilation|PASS|
|resnest14d_Opset16_timm|compilation|PASS|
|resnest200e_Opset16_timm|compilation|PASS|
|resnest269e_Opset16_timm|compilation|PASS|
|resnest26d_Opset16_timm|compilation|PASS|
|resnest50d_1s4x24d_Opset16_timm|compilation|PASS|
|resnest50d_Opset16_timm|compilation|PASS|

