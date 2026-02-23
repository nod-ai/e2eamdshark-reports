# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1528.8187|1550.0473|21.2286|1.39%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1526.735|1533.8951|7.1601|0.47%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12559.9933|12499.4884|-60.5049|-0.48%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|755.7574|740.1027|-15.6547|-2.07%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2454.6643|2330.8364|-123.8279|-5.04%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|10024.5964|10176.8162|152.2198|1.52%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|643.3612|634.4452|-8.9161|-1.39%|
|migraphx_cadene__dpn92i1|PASS|within tol|438.2549|442.1874|3.9325|0.9%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|9071.9118|9073.667|1.7552|0.02%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|815.4727|819.8659|4.3932|0.54%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10432.0484|10097.3131|-334.7353|-3.21%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|162.9372|164.6277|1.6905|1.04%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|296.6431|298.3522|1.7092|0.58%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|1614.6958|1436.6702|-178.0256|-11.03%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|55.6512|54.694|-0.9572|-1.72%|
|migraphx_pytorch-examples__wlang_lstm|PASS|within tol|32.9346|32.8873|-0.0473|-0.14%|
|migraphx_torchvision__densenet121i32|PASS|within tol|3510.1661|3511.4264|1.2603|0.04%|
|migraphx_torchvision__inceptioni1|PASS|within tol|352.3734|364.1066|11.7333|3.33%|
|migraphx_torchvision__resnet50i1|PASS|within tol|208.2448|210.9487|2.7039|1.3%|

## 7 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384.in22k_ft_in22k_in1k|PASS|compiled_inference|
|convnext_xlarge.fb_in22k_ft_in1k|PASS|compiled_inference|
|deit3_large_patch16_384.fb_in1k|PASS|compiled_inference|
|dm_nfnet_f4.dm_in1k|PASS|compiled_inference|
|longformer_Opset16|compiled_inference|import_model|
|longformer_Opset17|compiled_inference|import_model|
|longformer_Opset18|compiled_inference|import_model|

## 6 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset16|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset16|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset18|compiled_inference|PASS|
|vit_large_patch14_clip_336.laion2b_ft_in12k_in1k|compiled_inference|PASS|
|vit_large_patch16_384.augreg_in21k_ft_in1k|compiled_inference|PASS|

