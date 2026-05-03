# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|regression|2486.7802|10417.0985|7930.3182|318.9%|
|migraphx_torchvision__inceptioni32|PASS|regression|4188.2085|7826.9888|3638.7803|86.88%|
|migraphx_torchvision__resnet50i64|PASS|regression|4567.4445|8334.5957|3767.1512|82.48%|

## 4 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|candy-9|Numerics|compilation|
|pointilism-9|Numerics|compilation|
|rain-princess-9|Numerics|compilation|
|udnie-9|Numerics|compilation|

## 2 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|flaubert_Opset18_transformers|Numerics|PASS|
|umt5_Opset17_transformers|Numerics|PASS|

