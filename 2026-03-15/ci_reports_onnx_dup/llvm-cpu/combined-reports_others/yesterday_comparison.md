# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|12497.9086|12475.0554|-22.8531|-0.18%|
|migraphx_torchvision__inceptioni32|PASS|within tol|8644.1678|8884.3592|240.1914|2.78%|
|migraphx_torchvision__resnet50i64|PASS|within tol|9473.0954|9733.8612|260.7657|2.75%|

## 6 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 6 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|candy-8|Numerics|PASS|
|convnext_xlarge.fb_in22k_ft_in1k_384|compiled_inference|PASS|
|deit3_large_patch16_384.fb_in22k_ft_in1k|compiled_inference|PASS|
|mosaic-8|Numerics|PASS|
|pointilism-8|Numerics|PASS|
|udnie-8|Numerics|PASS|

