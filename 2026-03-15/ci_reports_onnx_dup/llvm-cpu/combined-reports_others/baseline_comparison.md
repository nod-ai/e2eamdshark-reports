# Test Run Comparison Report

## Performance Comparison

regression tolerance: 10.0%

progression tolerance: 10.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|12599.4149|12475.0554|-124.3595|-0.99%|
|migraphx_torchvision__inceptioni32|PASS|within tol|9144.0816|8884.3592|-259.7224|-2.84%|
|migraphx_torchvision__resnet50i64|PASS|within tol|10415.6569|9733.8612|-681.7957|-6.55%|

## 18 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset17_timm|PASS|compiled_inference|
|convnext_xlarge_384_in22ft1k_Opset18_timm|PASS|compiled_inference|
|deit3_large_patch16_384_Opset18_timm|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset16_timm|PASS|compiled_inference|
|eva_large_patch14_336.in22k_ft_in22k_in1k|PASS|compiled_inference|
|maxvit_large_tf_512.in21k_ft_in1k|PASS|compiled_inference|
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

