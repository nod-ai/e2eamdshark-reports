# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|1283.4886|1601.4551|317.9665|24.77%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1257.9089|1492.1076|234.1987|18.62%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|10743.2275|12616.5074|1873.28|17.44%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|680.6086|688.0206|7.412|1.09%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|2260.6606|2516.4532|255.7926|11.31%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|7583.0263|10134.1228|2551.0965|33.64%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|484.4023|642.4682|158.0658|32.63%|
|migraphx_cadene__dpn92i1|PASS|regression|401.6197|436.0965|34.4768|8.58%|
|migraphx_cadene__inceptionv4i16|PASS|progression|9472.415|8898.9589|-573.4562|-6.05%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|882.0449|819.3076|-62.7372|-7.11%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|7385.5996|9836.0614|2450.4618|33.18%|
|migraphx_mlperf__resnet50_v1|PASS|progression|222.1224|203.9354|-18.187|-8.19%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|242.771|291.7781|49.0071|20.19%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|768.9912|1131.0182|362.0269|47.08%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|49.7085|56.4946|6.7861|13.65%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4901.5753|4843.1162|-58.4591|-1.19%|
|migraphx_torchvision__inceptioni1|PASS|within tol|347.9145|349.722|1.8075|0.52%|
|migraphx_torchvision__resnet50i1|PASS|progression|233.3967|194.1354|-39.2613|-16.82%|

## 6 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384_Opset16_timm|PASS|compiled_inference|
|beit_large_patch16_384_Opset17_timm|PASS|compiled_inference|
|convnext_xlarge_384_in22ft1k_Opset16_timm|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset17_timm|PASS|compiled_inference|
|vit_large_patch16_384_Opset16_timm|PASS|compiled_inference|
|vit_large_patch16_384_Opset17_timm|PASS|compiled_inference|

## No Progressions Found

