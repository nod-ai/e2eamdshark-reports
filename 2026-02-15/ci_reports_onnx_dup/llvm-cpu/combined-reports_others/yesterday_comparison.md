# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|progression|12961.6837|2038.8361|-10922.8476|-84.27%|
|migraphx_torchvision__inceptioni32|PASS|progression|9079.3792|4250.0467|-4829.3325|-53.19%|
|migraphx_torchvision__resnet50i64|PASS|progression|10898.2773|4463.8239|-6434.4534|-59.04%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|
|regnetx_002_Opset18_timm|PASS|compiled_inference|

## 4 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset17_timm|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset18_timm|compiled_inference|PASS|
|deit3_large_patch16_384_Opset18_timm|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset16_timm|compiled_inference|PASS|

