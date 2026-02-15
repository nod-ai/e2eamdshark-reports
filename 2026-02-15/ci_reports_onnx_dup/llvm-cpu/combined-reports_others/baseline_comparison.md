# Test Run Comparison Report

## Performance Comparison

regression tolerance: 10.0%

progression tolerance: 10.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|progression|12599.4149|2038.8361|-10560.5788|-83.82%|
|migraphx_torchvision__inceptioni32|PASS|progression|9144.0816|4250.0467|-4894.0349|-53.52%|
|migraphx_torchvision__resnet50i64|PASS|progression|10415.6569|4463.8239|-5951.833|-57.14%|

## 11 Regressions Found:

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
|regnetx_002_Opset18_timm|PASS|compiled_inference|

## No Progressions Found

