# Test Run Comparison Report

## Performance Comparison

regression tolerance: 10.0%

progression tolerance: 10.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|12599.4149|12497.9086|-101.5064|-0.81%|
|migraphx_torchvision__inceptioni32|PASS|within tol|9144.0816|8644.1678|-499.9139|-5.47%|
|migraphx_torchvision__resnet50i64|PASS|within tol|10415.6569|9473.0954|-942.5615|-9.05%|

## 14 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge.fb_in22k_ft_in1k_384|PASS|compiled_inference|
|deit3_large_patch16_384.fb_in22k_ft_in1k|PASS|compiled_inference|
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

## No Progressions Found

