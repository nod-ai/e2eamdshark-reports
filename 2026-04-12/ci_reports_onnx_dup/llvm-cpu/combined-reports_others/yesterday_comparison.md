# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|12470.2987|12634.7756|164.4769|1.32%|
|migraphx_torchvision__inceptioni32|PASS|within tol|9273.819|9410.383|136.564|1.47%|
|migraphx_torchvision__resnet50i64|PASS|within tol|10004.6696|9947.9222|-56.7475|-0.57%|

## No Regressions Found

## 12 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|candy-9|compilation|Numerics|
|convnext_xlarge_384_in22ft1k_Opset18_timm|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset16_timm|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset18_timm|compiled_inference|PASS|
|pointilism-9|compilation|Numerics|
|rain-princess-9|compilation|Numerics|
|regnetz_c16_evos_Opset17_timm|Numerics|PASS|
|regnetz_d8_evos_Opset17_timm|Numerics|PASS|
|resnetv2_50d_evos_Opset16_timm|Numerics|PASS|
|udnie-9|compilation|Numerics|
|vit_large_patch14_clip_336.laion2b_ft_in1k|compiled_inference|PASS|
|vit_large_patch14_clip_336.openai_ft_in12k_in1k|compiled_inference|PASS|

