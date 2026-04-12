# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|11.6299|11.3953|-0.2346|-2.02%|
|migraphx_torchvision__inceptioni32|PASS|regression|18.3406|19.631|1.2903|7.04%|
|migraphx_torchvision__resnet50i64|PASS|regression|12.6755|13.4431|0.7675|6.06%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 66 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|cait_xs24_384_Opset18_timm|compilation|PASS|
|candy-9|compilation|Numerics|
|convnext_base_384_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_large_384_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_large_Opset17_timm|compilation|PASS|
|convnext_large_Opset17_torch_hub|compilation|PASS|
|convnext_large_Opset18_timm|compilation|PASS|
|convnext_large_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_large_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_large_in22k_Opset17_timm|compilation|PASS|
|convnext_small_384_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_small_384_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_tiny_384_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_tiny_384_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_xlarge_384_in22ft1k_Opset17_timm|compilation|PASS|
|convnext_xlarge_384_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_xlarge_in22ft1k_Opset18_timm|compilation|PASS|
|convnext_xlarge_in22k_Opset18_timm|compilation|PASS|
|flaubert_Opset18_transformers|setup|Numerics|
|gluon_resnet101_v1b_vaiq|Numerics|PASS|
|gluon_resnet152_v1b_vaiq|Numerics|PASS|
|gluon_resnet50_v1b_vaiq|Numerics|PASS|
|gluon_resnext50_32x4d_vaiq|Numerics|PASS|
|ig_resnext101_32x32d_vaiq|Numerics|PASS|
|ig_resnext101_32x8d_vaiq|Numerics|PASS|
|marian_Opset17_transformers|setup|PASS|
|markuplm_Opset17_transformers|setup|PASS|
|maxvit_base_tf_384.in21k_ft_in1k|compilation|PASS|
|maxvit_base_tf_512.in21k_ft_in1k|compilation|PASS|
|maxvit_large_tf_384.in21k_ft_in1k|compilation|PASS|
|maxvit_large_tf_512.in21k_ft_in1k|compilation|PASS|
|model--bart-base-cnn--ainize|compiled_inference|PASS|
|model--bart-base-samsum--philschmid|compiled_inference|PASS|
|model--bart-base-xsum--harouzie|compiled_inference|PASS|
|model--bart-base-xsum--morenolq|compiled_inference|PASS|
|model--bart-german--Shahm|compiled_inference|PASS|
|model--bart_lfqa_sqaud--Shubham09|compiled_inference|PASS|
|pointilism-9|compilation|Numerics|
|rain-princess-9|compilation|Numerics|
|resnet101_vaiq|Numerics|PASS|
|resnet152_vaiq|Numerics|PASS|
|resnet50_vaiq|Numerics|PASS|
|resnext101_32x8d_vaiq|Numerics|PASS|
|resnext50_32x4d_vaiq|Numerics|PASS|
|seresnext50_32x4d_vaiq|Numerics|PASS|
|ssl_resnet50_vaiq|Numerics|PASS|
|ssl_resnext101_32x4d_vaiq|Numerics|PASS|
|ssl_resnext101_32x8d_vaiq|Numerics|PASS|
|ssl_resnext50_32x4d_vaiq|Numerics|PASS|
|swsl_resnet50_vaiq|Numerics|PASS|
|swsl_resnext101_32x16d_vaiq|Numerics|PASS|
|swsl_resnext101_32x4d_vaiq|Numerics|PASS|
|swsl_resnext101_32x8d_vaiq|Numerics|PASS|
|swsl_resnext50_32x4d_vaiq|Numerics|PASS|
|udnie-9|compilation|Numerics|
|xcit_large_24_p8_384_dist_Opset18_timm|compilation|PASS|
|xcit_medium_24_p16_384_dist_Opset18_timm|compilation|PASS|
|xcit_medium_24_p8_224_Opset18_timm|compilation|PASS|
|xcit_medium_24_p8_224_dist|compilation|PASS|
|xcit_medium_24_p8_224_dist_Opset17_timm|compilation|PASS|
|xcit_medium_24_p8_224_dist_Opset18_timm|compilation|PASS|
|xcit_medium_24_p8_384_dist_Opset18_timm|compilation|PASS|
|xcit_small_12_p8_384_dist_Opset18_timm|compilation|PASS|
|xcit_small_24_p8_384_dist_Opset17_timm|compilation|PASS|
|xcit_tiny_12_p8_384_dist_Opset18_timm|compilation|PASS|
|xcit_tiny_24_p8_384_dist_Opset18_timm|compilation|PASS|

