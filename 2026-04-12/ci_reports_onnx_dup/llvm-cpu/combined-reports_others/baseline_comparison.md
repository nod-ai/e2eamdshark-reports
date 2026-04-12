# Test Run Comparison Report

## Performance Comparison

regression tolerance: 10.0%

progression tolerance: 10.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|12599.4149|12634.7756|35.3607|0.28%|
|migraphx_torchvision__inceptioni32|PASS|within tol|9144.0816|9410.383|266.3014|2.91%|
|migraphx_torchvision__resnet50i64|PASS|within tol|10415.6569|9947.9222|-467.7347|-4.49%|

## 10 Regressions Found:

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

## 11 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|candy-8|Numerics|PASS|
|candy-9|compilation|Numerics|
|mosaic-8|Numerics|PASS|
|pointilism-8|Numerics|PASS|
|pointilism-9|compilation|Numerics|
|rain-princess-9|compilation|Numerics|
|regnetz_c16_evos_Opset17_timm|Numerics|PASS|
|regnetz_d8_evos_Opset17_timm|Numerics|PASS|
|resnetv2_50d_evos_Opset16_timm|Numerics|PASS|
|udnie-8|Numerics|PASS|
|udnie-9|compilation|Numerics|

