# Test Run Comparison Report

## Performance Comparison

regression tolerance: 10.0%

progression tolerance: 10.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_torchvision__resnet50i64|PASS|within tol|12.7626|12.8826|0.12|0.94%|

## 39 Regressions Found:

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
|regnetx_032.tv2_in1k_vaiq|PASS|compilation|
|regnety_032.tv2_in1k_vaiq|PASS|compilation|
|regnety_160.sw_in12k_ft_in1k_train_vaiq|PASS|compilation|
|regnety_160.swag_lc_in1k_vaiq|Numerics|compilation|
|regnety_160.tv2_in1k_vaiq|Numerics|compilation|
|resnet101_vaiq|PASS|compilation|
|resnet152_vaiq|PASS|compilation|
|resnet18_vaiq|PASS|compilation|
|resnet50_vaiq|PASS|compilation|
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
|udnie-9|compilation|setup|
|xception_vaiq|PASS|compilation|
|xcit_medium_24_p8_224_Opset18_timm|compilation|setup|

## 103 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|Yolov8n_vaiq|Numerics|PASS|
|adv_inception_v3_vaiq|setup|Numerics|
|beitv2_large_patch16_224.in1k_ft_in22k_in1k|setup|PASS|
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
|densenet121_vaiq|setup|PASS|
|edgenext_x_small_Opset18_timm|compilation|PASS|
|inception_v4_Opset17_timm|Numerics|PASS|
|inception_v4_Opset18_timm|Numerics|PASS|
|migraphx_cadene__resnext101_64x4di16|setup|PASS|
|migraphx_torchvision__inceptioni32|setup|PASS|
|mobilevit_s_Opset17_timm|compilation|PASS|
|mobilevit_xxs_Opset17_timm|compilation|PASS|
|model--bert-base-uncased-finetuned-squad--harveyagraphcore|setup|PASS|
|model--finetuning-sentiment-model-3000-samples--nachowdh|setup|PASS|
|model--mobilebert-uncased-finetuned-squadv2--mrm8488|compilation|PASS|
|model--mobilebert_mrpc--Alireza1044|compilation|PASS|
|model--mobilebert_rte--Alireza1044|compilation|PASS|
|model--mobilebert_sst2--Alireza1044|compilation|PASS|
|regnetx_064_Opset18_timm|setup|PASS|
|repvgg_b3g4_Opset17_timm|setup|compilation|
|resnet34_vaiq|setup|compilation|
|swinv2_base_window16_256.ms_in1k|compilation|PASS|
|vit_l_16_Opset18_torch_hub|setup|PASS|
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
|yolov8n_vaiq_int8|Numerics|PASS|

