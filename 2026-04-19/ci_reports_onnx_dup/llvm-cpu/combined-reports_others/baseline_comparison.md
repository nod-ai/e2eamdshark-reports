# Test Run Comparison Report

## Performance Comparison

regression tolerance: 10.0%

progression tolerance: 10.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|progression|12599.4149|2442.3853|-10157.0296|-80.62%|
|migraphx_torchvision__inceptioni32|PASS|progression|9144.0816|4207.9859|-4936.0957|-53.98%|
|migraphx_torchvision__resnet50i64|PASS|progression|10415.6569|4559.5564|-5856.1005|-56.22%|

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
|squeezebert_Opset17_transformers|PASS|compilation|

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

