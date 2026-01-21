# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1515.1703|1469.5395|-45.6308|-3.01%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1463.853|1460.5515|-3.3015|-0.23%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12293.5211|12297.5318|4.0106|0.03%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|683.2416|714.8756|31.634|4.63%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2486.6412|2495.2957|8.6545|0.35%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|10231.869|10491.4162|259.5471|2.54%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|632.4529|635.6109|3.158|0.5%|
|migraphx_cadene__dpn92i1|Numerics|within tol|434.5477|435.624|1.0762|0.25%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8861.9528|8887.8818|25.929|0.29%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|817.6018|816.9123|-0.6895|-0.08%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|9699.4226|10669.2582|969.8355|10.0%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|205.6265|203.1197|-2.5068|-1.22%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|300.4547|292.263|-8.1916|-2.73%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|1145.554|1038.5026|-107.0514|-9.34%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|57.0396|57.9958|0.9563|1.68%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4775.4136|4790.0668|14.6532|0.31%|
|migraphx_torchvision__inceptioni1|PASS|within tol|348.1285|349.8034|1.6749|0.48%|
|migraphx_torchvision__resnet50i1|PASS|within tol|194.1425|194.6778|0.5353|0.28%|

## 4 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 20 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384_Opset16|compiled_inference|PASS|
|beit_large_patch16_384_Opset17|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset16|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_Opset16_timm|compiled_inference|PASS|
|xception41_Opset16|compiled_inference|PASS|
|xception41_Opset17|compiled_inference|PASS|
|xception41_Opset18|compiled_inference|PASS|
|xception41p_Opset16|compiled_inference|PASS|
|xception41p_Opset17|compiled_inference|PASS|
|xception41p_Opset18|compiled_inference|PASS|
|xception65_Opset16|compiled_inference|PASS|
|xception65_Opset17|compiled_inference|PASS|
|xception65_Opset18|compiled_inference|PASS|
|xception65p_Opset16|compiled_inference|PASS|
|xception65p_Opset17|compiled_inference|PASS|
|xception65p_Opset18|compiled_inference|PASS|
|xception71_Opset16|compiled_inference|PASS|
|xception71_Opset17|compiled_inference|PASS|
|xception71_Opset18|compiled_inference|PASS|

