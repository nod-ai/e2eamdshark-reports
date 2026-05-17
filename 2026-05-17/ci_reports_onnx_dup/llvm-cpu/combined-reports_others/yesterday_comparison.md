# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|10439.986|10441.566|1.58|0.02%|
|migraphx_torchvision__resnet50i64|PASS|within tol|8380.4303|8351.9812|-28.449|-0.34%|

## No Regressions Found

## 16 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset18_timm|compiled_inference|PASS|
|deit3_large_patch16_384_Opset17_timm|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset16_timm|compiled_inference|PASS|
|dpn107_Opset17_timm|compilation|PASS|
|dpn131_Opset16_timm|compilation|PASS|
|dpn131_Opset17_timm|compilation|PASS|
|dpn68_Opset16_timm|compilation|PASS|
|dpn68_Opset18_timm|compilation|PASS|
|dpn68b_Opset17_timm|compilation|PASS|
|dpn68b_Opset18_timm|compilation|PASS|
|dpn92_Opset16_timm|compilation|PASS|
|dpn92_Opset18_timm|compilation|PASS|
|dpn98_Opset16_timm|compilation|PASS|
|dpn98_Opset18_timm|compilation|PASS|
|migraphx_torchvision__inceptioni32|compilation|PASS|
|vit_large_patch16_384_Opset18_timm|compiled_inference|PASS|

