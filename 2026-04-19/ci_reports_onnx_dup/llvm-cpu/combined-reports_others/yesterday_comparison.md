# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|progression|12634.7756|2442.3853|-10192.3903|-80.67%|
|migraphx_torchvision__inceptioni32|PASS|progression|9410.383|4207.9859|-5202.3971|-55.28%|
|migraphx_torchvision__resnet50i64|PASS|progression|9947.9222|4559.5564|-5388.3658|-54.17%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|
|squeezebert_Opset17_transformers|PASS|compilation|

## No Progressions Found

