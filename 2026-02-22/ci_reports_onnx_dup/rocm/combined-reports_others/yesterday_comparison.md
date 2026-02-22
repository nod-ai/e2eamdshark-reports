# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|10.9432|10.9685|0.0253|0.23%|
|migraphx_torchvision__inceptioni32|PASS|within tol|18.4085|18.4112|0.0028|0.01%|
|migraphx_torchvision__resnet50i64|PASS|within tol|12.6332|12.648|0.0148|0.12%|

## 10 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|gluon_resnet50_v1b_Opset18_timm|PASS|setup|
|mobilenetv2_110d_Opset16_timm|PASS|setup|
|mobilenetv2_110d_Opset17_timm|PASS|setup|
|resnet152_Opset16_torch_hub|PASS|setup|
|vit_relpos_medium_patch16_cls_224_Opset18_timm|PASS|setup|

## One Progression Found:

|model name|old_status|new_status|
|---|---|---|
|mixer_l16_224_Opset16_timm|setup|PASS|

