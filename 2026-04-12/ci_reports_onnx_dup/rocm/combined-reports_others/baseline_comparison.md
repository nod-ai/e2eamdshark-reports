# Test Run Comparison Report

## Performance Comparison

regression tolerance: 10.0%

progression tolerance: 10.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_torchvision__resnet50i64|PASS|within tol|12.7626|13.4431|0.6804|5.33%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|regnet_x_3_2gf_Opset18_torch_hub|compilation|setup|
|regnet_x_800mf_Opset18_torch_hub|PASS|setup|

## 144 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|Yolov8n_vaiq|Numerics|PASS|
|adv_inception_v3_vaiq|setup|Numerics|
|beitv2_large_patch16_224.in1k_ft_in22k_in1k|setup|PASS|
|cait_m36_384_Opset18_timm|compilation|PASS|
|cait_s24_384_Opset17_timm|compilation|PASS|
|cait_s36_384_Opset18_timm|compilation|PASS|
|cait_xs24_384_Opset18_timm|compilation|PASS|
|cait_xxs24_384_Opset17_timm|compilation|PASS|
|cait_xxs36_384_Opset17_timm|compilation|PASS|
|candy-9|compilation|Numerics|
|convnext_base_384_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_base_Opset17_timm|compilation|PASS|
|convnext_base_Opset18_timm|compilation|PASS|
|convnext_base_Opset18_torch_hub|compilation|PASS|
|convnext_base_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_base_in22k_Opset18_timm|compilation|PASS|
|convnext_large_384_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_large_Opset17_timm|compilation|PASS|
|convnext_large_Opset17_torch_hub|compilation|PASS|
|convnext_large_Opset18_timm|compilation|PASS|
|convnext_large_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_large_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_large_in22k_Opset17_timm|compilation|PASS|
|convnext_nano_Opset18_timm|compilation|PASS|
|convnext_nano_ols_Opset17_timm|compilation|PASS|
|convnext_small_384_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_small_384_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_small_Opset18_timm|compilation|PASS|
|convnext_small_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_small_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_small_in22k_Opset18_timm|compilation|PASS|
|convnext_tiny_384_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_tiny_384_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_tiny_Opset17_timm|compilation|PASS|
|convnext_tiny_Opset17_torch_hub|compilation|PASS|
|convnext_tiny_Opset18_timm|compilation|PASS|
|convnext_tiny_hnf_Opset17_timm|compilation|PASS|
|convnext_tiny_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_tiny_in22k_Opset18_timm|compilation|PASS|
|convnext_xlarge_384_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_xlarge_384_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_xlarge_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_xlarge_in22k_Opset18_timm|compilation|PASS|
|densenet121_vaiq|setup|PASS|
|edgenext_x_small_Opset18_timm|compilation|PASS|
|gcresnet33ts_Opset18_timm|compilation|PASS|
|gcresnet50t_Opset18_timm|compilation|PASS|
|gcresnext26ts_Opset17_timm|compilation|PASS|
|gcresnext50ts_Opset17_timm|compilation|PASS|
|inception_v4_Opset17_timm|Numerics|PASS|
|inception_v4_Opset18_timm|Numerics|PASS|
|maxvit_base_tf_384.in21k_ft_in1k|compilation|PASS|
|maxvit_base_tf_512.in21k_ft_in1k|compilation|PASS|
|maxvit_large_tf_384.in21k_ft_in1k|compilation|PASS|
|maxvit_large_tf_512.in21k_ft_in1k|compilation|PASS|
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
|pointilism-9|compilation|Numerics|
|rain-princess-9|compilation|Numerics|
|regnetx_064_Opset18_timm|setup|PASS|
|repvgg_b3g4_Opset17_timm|setup|compilation|
|resnet34_vaiq|setup|PASS|
|resnetv2_152x2_bit.goog_teacher_in21k_ft_in1k_384_vaiq|compilation|Numerics|
|swinv2_base_window16_256.ms_in1k|compilation|PASS|
|udnie-9|compilation|Numerics|
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
|xcit_large_24_p8_384_dist_Opset18_timm|compilation|PASS|
|xcit_medium_24_p16_224_Opset17_timm|compilation|PASS|
|xcit_medium_24_p16_224_dist|compilation|PASS|
|xcit_medium_24_p16_224_dist_Opset17_timm|compilation|PASS|
|xcit_medium_24_p16_224_dist_Opset18_timm|compilation|PASS|
|xcit_medium_24_p16_384_dist_Opset18_timm|compilation|PASS|
|xcit_medium_24_p8_224_Opset18_timm|compilation|PASS|
|xcit_medium_24_p8_224_dist|compilation|PASS|
|xcit_medium_24_p8_224_dist_Opset17_timm|compilation|PASS|
|xcit_medium_24_p8_224_dist_Opset18_timm|compilation|PASS|
|xcit_medium_24_p8_384_dist_Opset18_timm|compilation|PASS|
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
|xcit_small_12_p8_384_dist_Opset18_timm|compilation|PASS|
|xcit_small_24_p16_224_Opset18_timm|compilation|PASS|
|xcit_small_24_p16_224_dist|compilation|PASS|
|xcit_small_24_p16_224_dist_Opset17_timm|compilation|PASS|
|xcit_small_24_p16_224_dist_Opset18_timm|compilation|PASS|
|xcit_small_24_p8_224_Opset17_timm|compilation|PASS|
|xcit_small_24_p8_224_dist|compilation|PASS|
|xcit_small_24_p8_224_dist_Opset17_timm|compilation|PASS|
|xcit_small_24_p8_224_dist_Opset18_timm|compilation|PASS|
|xcit_small_24_p8_384_dist_Opset17_timm|compilation|PASS|
|xcit_tiny_12_p16_224_Opset18_timm|compilation|PASS|
|xcit_tiny_12_p16_224_dist|compilation|PASS|
|xcit_tiny_12_p16_224_dist_Opset17_timm|compilation|PASS|
|xcit_tiny_12_p16_224_dist_Opset18_timm|compilation|PASS|
|xcit_tiny_12_p16_384_dist_Opset18_timm|compilation|PASS|
|xcit_tiny_12_p8_224_Opset18_timm|compilation|PASS|
|xcit_tiny_12_p8_224_dist|compilation|PASS|
|xcit_tiny_12_p8_224_dist_Opset17_timm|compilation|PASS|
|xcit_tiny_12_p8_224_dist_Opset18_timm|compilation|PASS|
|xcit_tiny_12_p8_384_dist_Opset18_timm|compilation|PASS|
|xcit_tiny_24_p16_224_Opset17_timm|compilation|PASS|
|xcit_tiny_24_p16_224_Opset18_timm|compilation|PASS|
|xcit_tiny_24_p16_224_dist|compilation|PASS|
|xcit_tiny_24_p16_224_dist_Opset17_timm|compilation|PASS|
|xcit_tiny_24_p16_384_dist_Opset17_timm|compilation|PASS|
|xcit_tiny_24_p8_224_Opset17_timm|compilation|PASS|
|xcit_tiny_24_p8_224_dist|compilation|PASS|
|xcit_tiny_24_p8_224_dist_Opset17_timm|compilation|PASS|
|xcit_tiny_24_p8_224_dist_Opset18_timm|compilation|PASS|
|xcit_tiny_24_p8_384_dist_Opset18_timm|compilation|PASS|
|yolov8n_vaiq_int8|Numerics|PASS|

