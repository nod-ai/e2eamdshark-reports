# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|12475.0554|12461.4383|-13.6171|-0.11%|
|migraphx_torchvision__inceptioni32|PASS|within tol|8884.3592|9294.5249|410.1657|4.62%|
|migraphx_torchvision__resnet50i64|PASS|within tol|9733.8612|9997.6577|263.7965|2.71%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 6 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset17_timm|compiled_inference|PASS|
|deit3_large_patch16_384_Opset18_timm|compiled_inference|PASS|
|eva_large_patch14_336.in22k_ft_in22k_in1k|compiled_inference|PASS|
|maxvit_large_tf_512.in21k_ft_in1k|compiled_inference|PASS|
|vit_large_patch14_clip_336.laion2b_ft_in1k|compiled_inference|PASS|
|vit_large_patch14_clip_336.openai_ft_in12k_in1k|compiled_inference|PASS|

