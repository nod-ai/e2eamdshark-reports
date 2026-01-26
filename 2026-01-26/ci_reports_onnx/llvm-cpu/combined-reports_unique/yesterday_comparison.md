# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1483.5008|1396.2521|-87.2487|-5.88%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1572.5095|1552.1987|-20.3108|-1.29%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12409.2135|12353.6958|-55.5178|-0.45%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|711.2601|739.1835|27.9234|3.93%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2499.1177|2467.9484|-31.1693|-1.25%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|10073.1239|10012.3254|-60.7984|-0.6%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|627.5924|678.3723|50.7799|8.09%|
|migraphx_cadene__dpn92i1|PASS|within tol|438.5726|438.4495|-0.1231|-0.03%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8910.0431|8851.5166|-58.5265|-0.66%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|824.5096|822.0821|-2.4274|-0.29%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10132.9389|10488.4946|355.5557|3.51%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|206.5428|202.0378|-4.505|-2.18%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|293.6896|293.4156|-0.274|-0.09%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1278.5834|1292.7896|14.2062|1.11%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|57.2008|55.9257|-1.2751|-2.23%|
|migraphx_pytorch-examples__wlang_lstm|PASS|progression|34.0283|32.2031|-1.8251|-5.36%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4798.4239|4809.499|11.0751|0.23%|
|migraphx_torchvision__inceptioni1|PASS|within tol|355.3559|350.5243|-4.8316|-1.36%|
|migraphx_torchvision__resnet50i1|PASS|within tol|199.9464|194.108|-5.8384|-2.92%|

## 4 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset16|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset16|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset17|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset18|PASS|compiled_inference|

## 9 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_Opset18|compiled_inference|PASS|
|longformer_Opset16|import_model|compiled_inference|
|longformer_Opset17|import_model|compiled_inference|
|longformer_Opset18|import_model|compiled_inference|
|regnetx_002_Opset17_timm|compiled_inference|PASS|
|vit_large_patch14_clip_336.laion2b_ft_in12k_in1k|compiled_inference|PASS|
|vit_large_patch16_384.augreg_in21k_ft_in1k|compiled_inference|PASS|
|xception41p_Opset16_timm|compiled_inference|PASS|

