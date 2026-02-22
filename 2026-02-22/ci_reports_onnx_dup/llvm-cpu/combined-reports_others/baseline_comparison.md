# Test Run Comparison Report

## Performance Comparison

regression tolerance: 10.0%

progression tolerance: 10.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|regression|12599.4149|16264.7518|3665.3368|29.09%|
|migraphx_torchvision__inceptioni32|PASS|regression|9144.0816|12060.6496|2916.568|31.9%|
|migraphx_torchvision__resnet50i64|PASS|regression|10415.6569|13402.4272|2986.7703|28.68%|

## 12 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
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

