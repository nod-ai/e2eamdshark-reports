# Test Run Comparison Report

## Performance Comparison

regression tolerance: 10.0%

progression tolerance: 10.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_torchvision__resnet50i64|PASS|within tol|12.7626|12.6636|-0.099|-0.78%|

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

## 19 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|Yolov8n_vaiq|Numerics|PASS|
|adv_inception_v3_vaiq|setup|Numerics|
|beitv2_large_patch16_224.in1k_ft_in22k_in1k|setup|PASS|
|densenet121_vaiq|setup|PASS|
|inception_v4_Opset17_timm|Numerics|PASS|
|inception_v4_Opset18_timm|Numerics|PASS|
|migraphx_cadene__resnext101_64x4di16|setup|PASS|
|migraphx_torchvision__inceptioni32|setup|PASS|
|model--bert-base-uncased-finetuned-squad--harveyagraphcore|setup|PASS|
|model--finetuning-sentiment-model-3000-samples--nachowdh|setup|PASS|
|model--mobilebert-uncased-finetuned-squadv2--mrm8488|compilation|PASS|
|model--mobilebert_mrpc--Alireza1044|compilation|PASS|
|model--mobilebert_rte--Alireza1044|compilation|PASS|
|model--mobilebert_sst2--Alireza1044|compilation|PASS|
|regnetx_064_Opset18_timm|setup|PASS|
|repvgg_b3g4_Opset17_timm|setup|compilation|
|resnet34_vaiq|setup|PASS|
|vit_l_16_Opset18_torch_hub|setup|PASS|
|yolov8n_vaiq_int8|Numerics|PASS|

