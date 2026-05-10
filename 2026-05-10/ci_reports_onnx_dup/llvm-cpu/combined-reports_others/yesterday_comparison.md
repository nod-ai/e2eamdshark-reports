# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|10417.0985|10439.986|22.8876|0.22%|
|migraphx_torchvision__resnet50i64|PASS|within tol|8334.5957|8380.4303|45.8345|0.55%|

## 16 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|dpn107_Opset17_timm|PASS|compilation|
|dpn131_Opset16_timm|PASS|compilation|
|dpn131_Opset17_timm|PASS|compilation|
|dpn68_Opset16_timm|PASS|compilation|
|dpn68_Opset18_timm|PASS|compilation|
|dpn68b_Opset17_timm|PASS|compilation|
|dpn68b_Opset18_timm|PASS|compilation|
|dpn92_Opset16_timm|PASS|compilation|
|dpn92_Opset18_timm|PASS|compilation|
|dpn98_Opset16_timm|PASS|compilation|
|dpn98_Opset18_timm|PASS|compilation|
|migraphx_torchvision__inceptioni32|PASS|compilation|

## No Progressions Found

