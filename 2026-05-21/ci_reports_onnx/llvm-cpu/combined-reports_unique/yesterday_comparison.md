# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1535.6861|1559.8958|24.2097|1.58%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1490.3083|1533.6338|43.3254|2.91%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12919.2608|13166.1211|246.8604|1.91%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|709.4114|710.9848|1.5734|0.22%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|1130.4596|1115.3593|-15.1002|-1.34%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|6439.0221|6518.3284|79.3063|1.23%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|544.3907|526.0833|-18.3074|-3.36%|
|migraphx_cadene__dpn92i1|PASS|within tol|366.2835|367.8794|1.596|0.44%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8471.8878|8516.9397|45.0519|0.53%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|724.3481|731.073|6.7249|0.93%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10489.5383|10505.4507|15.9124|0.15%|
|migraphx_mlperf__resnet50_v1|PASS|regression|155.6883|230.707|75.0186|48.19%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|272.5608|257.7966|-14.7643|-5.42%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|1501.9855|1377.5259|-124.4596|-8.29%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|95.3506|97.0172|1.6665|1.75%|
|migraphx_pytorch-examples__wlang_lstm|PASS|within tol|16.1689|16.1351|-0.0338|-0.21%|
|migraphx_torchvision__densenet121i32|PASS|within tol|3030.7158|3075.1068|44.391|1.46%|
|migraphx_torchvision__inceptioni1|PASS|within tol|323.591|325.5299|1.9389|0.6%|
|migraphx_torchvision__resnet50i1|PASS|within tol|147.5334|149.1808|1.6473|1.12%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|
|RDN_pytorch_vaiq_int8|Numerics|compiled_inference|

## 12 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384_Opset16|compiled_inference|PASS|
|beit_large_patch16_384_Opset17|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset16|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset17|compiled_inference|PASS|
|flaubert_Opset16|Numerics|PASS|
|flaubert_Opset17|Numerics|PASS|
|flaubert_Opset18|Numerics|PASS|
|umt5_Opset16|Numerics|PASS|
|umt5_Opset17|Numerics|PASS|
|vit_large_patch14_clip_336.laion2b_ft_in12k_in1k|compiled_inference|PASS|
|vit_large_patch16_384.augreg_in21k_ft_in1k|compiled_inference|PASS|
|xlmroberta_Opset16|Numerics|PASS|

