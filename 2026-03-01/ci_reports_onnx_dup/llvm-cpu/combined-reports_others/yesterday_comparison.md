# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|progression|16264.7518|12475.1176|-3789.6342|-23.3%|
|migraphx_torchvision__inceptioni32|PASS|progression|12060.6496|8557.847|-3502.8026|-29.04%|
|migraphx_torchvision__resnet50i64|PASS|progression|13402.4272|10114.6874|-3287.7398|-24.53%|

## 4 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 2 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|vit_large_patch14_clip_336.laion2b_ft_in1k|compiled_inference|PASS|
|vit_large_patch14_clip_336.openai_ft_in12k_in1k|compiled_inference|PASS|

