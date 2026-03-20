# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1550.0473|1580.8284|30.7811|1.99%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1533.8951|1554.7037|20.8086|1.36%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12499.4884|12244.1396|-255.3488|-2.04%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|740.1027|728.7059|-11.3969|-1.54%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2330.8364|1249.8873|-1080.9491|-46.38%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|10176.8162|6994.2266|-3182.5896|-31.27%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|634.4452|623.1345|-11.3107|-1.78%|
|migraphx_cadene__dpn92i1|PASS|within tol|442.1874|437.5316|-4.6558|-1.05%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|9073.667|9331.1994|257.5325|2.84%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|819.8659|815.4423|-4.4237|-0.54%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10097.3131|9731.4014|-365.9117|-3.62%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|164.6277|164.277|-0.3507|-0.21%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|298.3522|302.5713|4.219|1.41%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1436.6702|1436.8228|0.1526|0.01%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|54.694|55.5935|0.8995|1.64%|
|migraphx_pytorch-examples__wlang_lstm|PASS|within tol|32.8873|32.0338|-0.8534|-2.6%|
|migraphx_torchvision__densenet121i32|PASS|within tol|3511.4264|3574.453|63.0266|1.79%|
|migraphx_torchvision__inceptioni1|PASS|within tol|364.1066|368.2478|4.1412|1.14%|
|migraphx_torchvision__resnet50i1|PASS|progression|210.9487|196.3842|-14.5645|-6.9%|

## No Regressions Found

## 22 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|RRDB_ESRGAN_vaiq_int8|compilation|Numerics|
|beit_large_patch16_384.in22k_ft_in22k_in1k|compiled_inference|PASS|
|beit_large_patch16_384_Opset16|compiled_inference|PASS|
|beit_large_patch16_384_Opset17|compiled_inference|PASS|
|convnext_xlarge.fb_in22k_ft_in1k|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset16|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384.fb_in1k|compiled_inference|PASS|
|dm_nfnet_f0_Opset16|Numerics|PASS|
|dm_nfnet_f0_Opset17|Numerics|PASS|
|dm_nfnet_f1_Opset16|Numerics|PASS|
|dm_nfnet_f2_Opset16|Numerics|PASS|
|dm_nfnet_f2_Opset17|Numerics|PASS|
|dm_nfnet_f4.dm_in1k|compiled_inference|PASS|
|fcn-resnet101-11|Numerics|PASS|
|fcn-resnet50-11|Numerics|PASS|
|fcn-resnet50-12|Numerics|PASS|
|longformer_Opset16|import_model|compiled_inference|
|longformer_Opset17|import_model|compiled_inference|
|longformer_Opset18|import_model|compiled_inference|
|model--s2t-medium-librispeech-asr--facebook|Numerics|PASS|
|rain-princess-8|Numerics|PASS|

