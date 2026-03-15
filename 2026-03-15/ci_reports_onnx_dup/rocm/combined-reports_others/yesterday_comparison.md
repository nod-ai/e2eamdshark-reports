# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|10.8913|10.9379|0.0466|0.43%|
|migraphx_torchvision__inceptioni32|PASS|within tol|18.3348|18.4167|0.0819|0.45%|
|migraphx_torchvision__resnet50i64|PASS|within tol|12.6101|12.6712|0.0611|0.48%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|leconv_Opset18_graph_convolutions|PASS|setup|

## One Progression Found:

|model name|old_status|new_status|
|---|---|---|
|resnetv2_101_Opset17_timm|setup|PASS|

