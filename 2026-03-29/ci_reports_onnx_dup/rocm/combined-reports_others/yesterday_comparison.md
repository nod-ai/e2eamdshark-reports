# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|regression|10.9379|11.5776|0.6397|5.85%|
|migraphx_torchvision__inceptioni32|PASS|within tol|18.4167|18.423|0.0064|0.03%|
|migraphx_torchvision__resnet50i64|PASS|within tol|12.6712|12.8826|0.2114|1.67%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 2 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|leconv_Opset18_graph_convolutions|setup|PASS|
|seresnext26tn_32x4d_Opset16_timm|setup|PASS|

