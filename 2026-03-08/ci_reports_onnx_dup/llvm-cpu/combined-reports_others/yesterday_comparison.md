# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|12475.1176|12497.9086|22.791|0.18%|
|migraphx_torchvision__inceptioni32|PASS|within tol|8557.847|8644.1678|86.3208|1.01%|
|migraphx_torchvision__resnet50i64|PASS|progression|10114.6874|9473.0954|-641.592|-6.34%|

## 4 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 4 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset18_timm|compiled_inference|PASS|
|deit3_large_patch16_384_Opset17_timm|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset16_timm|compiled_inference|PASS|
|vit_large_patch16_384_Opset18_timm|compiled_inference|PASS|

