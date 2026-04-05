# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|11.5776|11.6299|0.0523|0.45%|
|migraphx_torchvision__inceptioni32|PASS|within tol|18.423|18.3406|-0.0824|-0.45%|
|migraphx_torchvision__resnet50i64|PASS|within tol|12.8826|12.6755|-0.2071|-1.61%|

## 3 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 39 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|gcresnet33ts_Opset18_timm|compilation|PASS|
|gcresnet50t_Opset18_timm|compilation|PASS|
|gcresnext26ts_Opset17_timm|compilation|PASS|
|gcresnext50ts_Opset17_timm|compilation|PASS|
|gluon_resnet101_v1b_vaiq|compilation|Numerics|
|gluon_resnet152_v1b_vaiq|compilation|Numerics|
|gluon_resnet34_v1b_vaiq|compilation|PASS|
|gluon_resnet50_v1b_vaiq|compilation|Numerics|
|gluon_resnext50_32x4d_vaiq|compilation|Numerics|
|ig_resnext101_32x32d_vaiq|compilation|Numerics|
|ig_resnext101_32x8d_vaiq|compilation|Numerics|
|regnetx_032.tv2_in1k_vaiq|compilation|PASS|
|regnety_032.tv2_in1k_vaiq|compilation|PASS|
|regnety_160.sw_in12k_ft_in1k_train_vaiq|compilation|PASS|
|regnety_160.swag_lc_in1k_vaiq|compilation|Numerics|
|regnety_160.tv2_in1k_vaiq|compilation|Numerics|
|resnet101_vaiq|compilation|Numerics|
|resnet152_vaiq|compilation|Numerics|
|resnet18_vaiq|compilation|PASS|
|resnet34_vaiq|compilation|PASS|
|resnet50_vaiq|compilation|Numerics|
|resnetv2_152x2_bit.goog_teacher_in21k_ft_in1k_384_vaiq|compilation|Numerics|
|resnext101_32x8d_vaiq|compilation|Numerics|
|resnext50_32x4d_vaiq|compilation|Numerics|
|seresnext50_32x4d_vaiq|compilation|Numerics|
|ssl_resnet18_vaiq|compilation|PASS|
|ssl_resnet50_vaiq|compilation|Numerics|
|ssl_resnext101_32x4d_vaiq|compilation|Numerics|
|ssl_resnext101_32x8d_vaiq|compilation|Numerics|
|ssl_resnext50_32x4d_vaiq|compilation|Numerics|
|swsl_resnet18_vaiq|compilation|PASS|
|swsl_resnet50_vaiq|compilation|Numerics|
|swsl_resnext101_32x16d_vaiq|compilation|Numerics|
|swsl_resnext101_32x4d_vaiq|compilation|Numerics|
|swsl_resnext101_32x8d_vaiq|compilation|Numerics|
|swsl_resnext50_32x4d_vaiq|compilation|Numerics|
|udnie-9|setup|compilation|
|xception_vaiq|compilation|PASS|
|xcit_medium_24_p8_224_Opset18_timm|setup|compilation|

