# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|12599.4149|12961.6837|362.2687|2.88%|
|migraphx_torchvision__inceptioni32|PASS|within tol|9144.0816|9079.3792|-64.7024|-0.71%|
|migraphx_torchvision__resnet50i64|PASS|within tol|10415.6569|10898.2773|482.6204|4.63%|

## 14 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset17_timm|PASS|compiled_inference|
|convnext_xlarge_384_in22ft1k_Opset18_timm|PASS|compiled_inference|
|deit3_large_patch16_384_Opset18_timm|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset16_timm|PASS|compiled_inference|
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

## No Progressions Found

