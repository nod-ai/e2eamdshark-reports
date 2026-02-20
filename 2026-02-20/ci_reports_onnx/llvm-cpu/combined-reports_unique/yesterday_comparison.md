# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1612.7657|1528.8187|-83.947|-5.21%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1591.2633|1526.735|-64.5283|-4.06%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12470.9379|12559.9933|89.0554|0.71%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|750.6607|755.7574|5.0967|0.68%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2537.6557|2454.6643|-82.9913|-3.27%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|8706.8074|10024.5964|1317.7891|15.14%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|637.9|643.3612|5.4612|0.86%|
|migraphx_cadene__dpn92i1|PASS|progression|489.7452|438.2549|-51.4903|-10.51%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|9059.12|9071.9118|12.7918|0.14%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|925.3463|815.4727|-109.8736|-11.87%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10310.3577|10432.0484|121.6907|1.18%|
|migraphx_mlperf__resnet50_v1|PASS|progression|197.5828|162.9372|-34.6456|-17.53%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|326.0105|296.6431|-29.3675|-9.01%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1473.795|1614.6958|140.9007|9.56%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|78.6147|55.6512|-22.9635|-29.21%|
|migraphx_pytorch-examples__wlang_lstm|PASS|progression|56.2016|32.9346|-23.267|-41.4%|
|migraphx_torchvision__densenet121i32|PASS|progression|3751.1486|3510.1661|-240.9826|-6.42%|
|migraphx_torchvision__inceptioni1|PASS|progression|403.1043|352.3734|-50.7309|-12.59%|
|migraphx_torchvision__resnet50i1|PASS|progression|233.719|208.2448|-25.4742|-10.9%|

## 13 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|RDN_pytorch_vaiq_int8|Numerics|compiled_inference|
|RRDB_ESRGAN_vaiq_int8|Numerics|compilation|
|beit_large_patch16_384_Opset16|PASS|compiled_inference|
|beit_large_patch16_384_Opset17|PASS|compiled_inference|
|convnext_xlarge_384_in22ft1k_Opset16|PASS|compiled_inference|
|convnext_xlarge_384_in22ft1k_Opset17|PASS|compiled_inference|
|regnetz_c16_evos_Opset16|PASS|Numerics|
|regnetz_c16_evos_Opset17|PASS|Numerics|
|regnetz_d8_evos_Opset16|PASS|Numerics|
|regnetz_d8_evos_Opset16_timm|PASS|Numerics|
|regnetz_d8_evos_Opset17|PASS|Numerics|
|vit_large_patch14_clip_336.laion2b_ft_in12k_in1k|PASS|compiled_inference|
|vit_large_patch16_384.augreg_in21k_ft_in1k|PASS|compiled_inference|

## 7 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384.in22k_ft_in22k_in1k|compiled_inference|PASS|
|convnext_xlarge.fb_in22k_ft_in1k|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset16_timm|compiled_inference|PASS|
|deit3_large_patch16_384.fb_in1k|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17_timm|compiled_inference|PASS|
|dm_nfnet_f4.dm_in1k|compiled_inference|PASS|
|vit_large_patch16_384_Opset16_timm|compiled_inference|PASS|

