# Test Run Comparison Report

## Performance Comparison

regression tolerance: 10.0%

progression tolerance: 10.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_torchvision__resnet50i64|PASS|within tol|12.7626|12.6403|-0.1223|-0.96%|

## 18 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit_base_patch16_384_Opset18_timm|PASS|setup|
|dpn68_Opset16_timm|PASS|setup|
|eca_resnext26ts_Opset16_timm|PASS|setup|
|gluon_resnet101_v1s_Opset18_timm|PASS|setup|
|gluon_resnet152_v1d_Opset17_timm|PASS|setup|
|hrnet_w32_Opset18_timm|PASS|setup|
|mixer_l16_224_Opset16_timm|PASS|setup|
|resnet152_Opset17_torch_hub|PASS|setup|
|resnetv2_50d_gn_Opset18_timm|PASS|setup|
|ssl_resnet18_Opset18_timm|PASS|setup|
|tf_efficientnet_b5_Opset17_timm|PASS|setup|
|tf_efficientnetv2_b1_Opset17_timm|PASS|setup|
|tf_efficientnetv2_m_in21k_Opset17_timm|PASS|setup|
|umt5encoder_Opset17_transformers|PASS|setup|
|visformer_small_Opset16_timm|PASS|setup|
|vit_large_patch32_384_Opset18_timm|PASS|setup|
|wide_resnet101_2_Opset17_timm|PASS|setup|
|xcit_small_24_p8_224_dist_Opset18_timm|compilation|setup|

## 15 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|Yolov8n_vaiq|Numerics|PASS|
|adv_inception_v3_vaiq|setup|Numerics|
|beitv2_large_patch16_224.in1k_ft_in22k_in1k|setup|PASS|
|densenet121_vaiq|setup|PASS|
|inception_v4_Opset17_timm|Numerics|PASS|
|inception_v4_Opset18_timm|Numerics|PASS|
|migraphx_cadene__resnext101_64x4di16|setup|PASS|
|migraphx_torchvision__inceptioni32|setup|PASS|
|model--bert-base-uncased-finetuned-squad--harveyagraphcore|setup|PASS|
|model--finetuning-sentiment-model-3000-samples--nachowdh|setup|PASS|
|regnetx_064_Opset18_timm|setup|PASS|
|repvgg_b3g4_Opset17_timm|setup|compilation|
|resnet34_vaiq|setup|PASS|
|vit_l_16_Opset18_torch_hub|setup|PASS|
|yolov8n_vaiq_int8|Numerics|PASS|

