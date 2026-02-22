# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|regression|2038.8361|16264.7518|14225.9157|697.75%|
|migraphx_torchvision__inceptioni32|PASS|regression|4250.0467|12060.6496|7810.6029|183.78%|
|migraphx_torchvision__resnet50i64|PASS|regression|4463.8239|13402.4272|8938.6033|200.25%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## One Progression Found:

|model name|old_status|new_status|
|---|---|---|
|regnetx_002_Opset18_timm|compiled_inference|PASS|

