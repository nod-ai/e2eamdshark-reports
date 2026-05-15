# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1561.1915|1535.6861|-25.5054|-1.63%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1473.3754|1490.3083|16.933|1.15%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|13276.0732|12919.2608|-356.8125|-2.69%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|719.4032|709.4114|-9.9918|-1.39%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|1111.315|1130.4596|19.1446|1.72%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|6332.7032|6439.0221|106.3189|1.68%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|539.2069|544.3907|5.1838|0.96%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|732.2364|724.3481|-7.8883|-1.08%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10624.837|10489.5383|-135.2987|-1.27%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|159.1014|155.6883|-3.4131|-2.15%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|257.283|272.5608|15.2778|5.94%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1302.6037|1501.9855|199.3818|15.31%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|94.8337|95.3506|0.517|0.55%|
|migraphx_pytorch-examples__wlang_lstm|PASS|within tol|15.8554|16.1689|0.3135|1.98%|
|migraphx_torchvision__inceptioni1|PASS|within tol|335.1767|323.591|-11.5857|-3.46%|
|migraphx_torchvision__resnet50i1|PASS|within tol|149.6829|147.5334|-2.1495|-1.44%|

## 8 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 37 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|RDN_pytorch_vaiq_int8|compiled_inference|Numerics|
|convnext_xlarge_384_in22ft1k_Opset16_timm|compiled_inference|PASS|
|deit3_large_patch16_384_Opset16|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset16|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17_timm|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset18|compiled_inference|PASS|
|dpn107_Opset16|compilation|PASS|
|dpn107_Opset16_timm|compilation|PASS|
|dpn107_Opset17|compilation|PASS|
|dpn107_Opset18|compilation|PASS|
|dpn107_Opset18_timm|compilation|PASS|
|dpn131_Opset16|compilation|PASS|
|dpn131_Opset17|compilation|PASS|
|dpn131_Opset18|compilation|PASS|
|dpn131_Opset18_timm|compilation|PASS|
|dpn68_Opset16|compilation|PASS|
|dpn68_Opset17|compilation|PASS|
|dpn68_Opset17_timm|compilation|PASS|
|dpn68_Opset18|compilation|PASS|
|dpn68b_Opset16|compilation|PASS|
|dpn68b_Opset16_timm|compilation|PASS|
|dpn68b_Opset17|compilation|PASS|
|dpn68b_Opset18|compilation|PASS|
|dpn92_Opset16|compilation|PASS|
|dpn92_Opset17|compilation|PASS|
|dpn92_Opset17_timm|compilation|PASS|
|dpn92_Opset18|compilation|PASS|
|dpn98_Opset16|compilation|PASS|
|dpn98_Opset17|compilation|PASS|
|dpn98_Opset17_timm|compilation|PASS|
|dpn98_Opset18|compilation|PASS|
|migraphx_cadene__dpn92i1|compilation|PASS|
|migraphx_cadene__inceptionv4i16|compilation|PASS|
|migraphx_torchvision__densenet121i32|compilation|PASS|
|vit_large_patch16_384_Opset16_timm|compiled_inference|PASS|
|yolov4|compilation|Numerics|

