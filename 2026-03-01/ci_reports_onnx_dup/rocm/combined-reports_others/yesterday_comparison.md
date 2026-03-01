# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_cadene__resnext101_64x4di16|PASS|within tol|10.9685|10.9412|-0.0273|-0.25%|
|migraphx_torchvision__inceptioni32|PASS|within tol|18.4112|18.3684|-0.0429|-0.23%|
|migraphx_torchvision__resnet50i64|PASS|within tol|12.648|12.6636|0.0156|0.12%|

## 7 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|mobilevitv2_125_Opset17_timm|PASS|setup|
|regnetx_032.tv2_in1k_vaiq|PASS|compilation|
|regnety_032.tv2_in1k_vaiq|PASS|compilation|
|regnety_160.sw_in12k_ft_in1k_train_vaiq|PASS|compilation|
|regnety_160.swag_lc_in1k_vaiq|Numerics|compilation|
|regnety_160.tv2_in1k_vaiq|Numerics|compilation|
|resnext101_32x4d_Opset16_timm|PASS|setup|

## 14 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|cait_m36_384_Opset18_timm|setup|compilation|
|convnext_base_Opset18_torch_hub|setup|compilation|
|convnext_large_Opset17_torch_hub|setup|compilation|
|convnext_small_384_in22ft1k_Opset17_timm|setup|compilation|
|gluon_resnet50_v1b_Opset18_timm|setup|PASS|
|mobilenetv2_110d_Opset16_timm|setup|PASS|
|mobilenetv2_110d_Opset17_timm|setup|PASS|
|model--mobilebert-uncased-finetuned-squadv2--mrm8488|compilation|PASS|
|model--mobilebert_mrpc--Alireza1044|compilation|PASS|
|model--mobilebert_rte--Alireza1044|compilation|PASS|
|model--mobilebert_sst2--Alireza1044|compilation|PASS|
|resnet152_Opset16_torch_hub|setup|PASS|
|vit_base_patch8_224_in21k_Opset18_timm|setup|PASS|
|vit_relpos_medium_patch16_cls_224_Opset18_timm|setup|PASS|

