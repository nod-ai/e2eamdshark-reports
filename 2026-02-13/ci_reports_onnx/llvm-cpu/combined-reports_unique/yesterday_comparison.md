# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|68.1064|1564.1408|1496.0344|2196.61%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|64.2639|1542.745|1478.4811|2300.64%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|189.2076|12481.4681|12292.2605|6496.71%|
|migraphx_ORT__distilgpt2_1|PASS|regression|20.437|745.6582|725.2212|3548.56%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|106.0274|2475.8384|2369.811|2235.09%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|315.711|9930.1176|9614.4066|3045.32%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|19.5853|626.1884|606.6032|3097.24%|
|migraphx_cadene__dpn92i1|PASS|regression|200.3675|440.645|240.2775|119.92%|
|migraphx_cadene__inceptionv4i16|PASS|regression|4482.8994|8808.6188|4325.7193|96.49%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|147.5251|810.5485|663.0234|449.43%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|161.6065|10503.8937|10342.2872|6399.67%|
|migraphx_mlperf__resnet50_v1|PASS|regression|119.8182|165.1387|45.3206|37.82%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|28.2265|299.992|271.7655|962.8%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|202.7579|1416.3181|1213.5602|598.53%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|35.1977|58.2469|23.0491|65.48%|
|migraphx_pytorch-examples__wlang_lstm|PASS|regression|19.717|33.2865|13.5694|68.82%|
|migraphx_torchvision__densenet121i32|PASS|regression|1763.7182|3560.1576|1796.4394|101.86%|
|migraphx_torchvision__inceptioni1|PASS|regression|168.463|358.075|189.612|112.55%|
|migraphx_torchvision__resnet50i1|PASS|regression|134.2878|197.458|63.1702|47.04%|

## 21 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|dm_nfnet_f0_Opset16|PASS|Numerics|
|dm_nfnet_f0_Opset17|PASS|Numerics|
|dm_nfnet_f1_Opset16|PASS|Numerics|
|dm_nfnet_f2_Opset16|PASS|Numerics|
|dm_nfnet_f2_Opset17|PASS|Numerics|
|fcn-resnet101-11|PASS|Numerics|
|fcn-resnet50-11|PASS|Numerics|
|fcn-resnet50-12|PASS|Numerics|

## 7 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384.in22k_ft_in22k_in1k|compiled_inference|PASS|
|beit_large_patch16_384_Opset16_timm|compiled_inference|PASS|
|beit_large_patch16_384_Opset17_timm|compiled_inference|PASS|
|convnext_xlarge.fb_in22k_ft_in1k|compiled_inference|PASS|
|deit3_large_patch16_384.fb_in1k|compiled_inference|PASS|
|dm_nfnet_f4.dm_in1k|compiled_inference|PASS|
|vit_large_patch16_384_Opset17_timm|compiled_inference|PASS|

