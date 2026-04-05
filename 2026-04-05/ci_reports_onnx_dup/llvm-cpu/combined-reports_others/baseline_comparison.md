# Test Run Comparison Report

## Performance Comparison

regression tolerance: 10.0%

progression tolerance: 10.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|12599.4149|12470.2987|-129.1163|-1.02%|
|migraphx_torchvision__inceptioni32|PASS|within tol|9144.0816|9273.819|129.7374|1.42%|
|migraphx_torchvision__resnet50i64|PASS|within tol|10415.6569|10004.6696|-410.9873|-3.95%|

## 15 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset18_timm|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset16_timm|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset18_timm|PASS|compiled_inference|
|mobilevitv2_150_384_in22ft1k|PASS|Numerics|
|mobilevitv2_150_384_in22ft1k_Opset17_timm|PASS|Numerics|
|mobilevitv2_150_384_in22ft1k_Opset18_timm|PASS|Numerics|
|mobilevitv2_175_384_in22ft1k|PASS|Numerics|
|mobilevitv2_175_384_in22ft1k_Opset16_timm|PASS|Numerics|
|mobilevitv2_175_384_in22ft1k_Opset18_timm|PASS|Numerics|
|mobilevitv2_200_384_in22ft1k|PASS|Numerics|
|mobilevitv2_200_384_in22ft1k_Opset16_timm|PASS|Numerics|
|mobilevitv2_200_384_in22ft1k_Opset17_timm|PASS|Numerics|
|model--bart-large-cnn--facebook|PASS|Numerics|
|vit_large_patch14_clip_336.laion2b_ft_in1k|PASS|compiled_inference|
|vit_large_patch14_clip_336.openai_ft_in12k_in1k|PASS|compiled_inference|

## 4 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|candy-8|Numerics|PASS|
|mosaic-8|Numerics|PASS|
|pointilism-8|Numerics|PASS|
|udnie-8|Numerics|PASS|

