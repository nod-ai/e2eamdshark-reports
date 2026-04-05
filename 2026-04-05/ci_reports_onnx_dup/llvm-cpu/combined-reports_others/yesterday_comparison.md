# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|12461.4383|12470.2987|8.8604|0.07%|
|migraphx_torchvision__inceptioni32|PASS|within tol|9294.5249|9273.819|-20.7059|-0.22%|
|migraphx_torchvision__resnet50i64|PASS|within tol|9997.6577|10004.6696|7.012|0.07%|

## 3 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 2 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge.fb_in22k_ft_in1k_384|compiled_inference|PASS|
|deit3_large_patch16_384.fb_in22k_ft_in1k|compiled_inference|PASS|

