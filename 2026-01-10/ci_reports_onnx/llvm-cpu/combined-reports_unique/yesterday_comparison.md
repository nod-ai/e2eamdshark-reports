# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1601.4551|1648.2867|46.8316|2.92%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1492.1076|1641.364|149.2564|10.0%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|12616.5074|25020.6048|12404.0974|98.32%|
|migraphx_ORT__distilgpt2_1|PASS|regression|688.0206|882.3965|194.3759|28.25%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2516.4532|2507.0348|-9.4183|-0.37%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|10134.1228|7411.2095|-2722.9133|-26.87%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|642.4682|562.6299|-79.8382|-12.43%|
|migraphx_cadene__dpn92i1|PASS|regression|436.0965|1029.3196|593.2231|136.03%|
|migraphx_cadene__inceptionv4i16|PASS|regression|8898.9589|19818.4857|10919.5268|122.71%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|819.3076|1045.7373|226.4297|27.64%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|9836.0614|11729.9797|1893.9183|19.25%|
|migraphx_mlperf__resnet50_v1|PASS|regression|203.9354|508.2631|304.3277|149.23%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|291.7781|610.2311|318.453|109.14%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1131.0182|2481.1636|1350.1454|119.37%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|56.4946|205.5243|149.0298|263.79%|
|migraphx_torchvision__densenet121i32|PASS|regression|4843.1162|6309.1939|1466.0777|30.27%|
|migraphx_torchvision__inceptioni1|PASS|regression|349.722|453.0504|103.3284|29.55%|
|migraphx_torchvision__resnet50i1|PASS|regression|194.1354|249.1856|55.0502|28.36%|

## 29 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384_Opset16|PASS|compiled_inference|
|beit_large_patch16_384_Opset17|PASS|compiled_inference|
|convnext_xlarge_384_in22ft1k_Opset16|PASS|compiled_inference|
|convnext_xlarge_384_in22ft1k_Opset17|PASS|compiled_inference|
|migx_bench_bert-large-uncased_1_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_1_384|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_384|PASS|compiled_inference|
|vit_large_patch16_384_Opset16|PASS|compiled_inference|
|vit_large_patch16_384_Opset17|PASS|compiled_inference|
|vit_large_patch16_384_Opset18|PASS|compiled_inference|
|xception41_Opset16|PASS|compiled_inference|
|xception41_Opset17|PASS|compiled_inference|
|xception41_Opset17_timm|PASS|compiled_inference|
|xception41_Opset18|PASS|compiled_inference|
|xception41p_Opset16|PASS|compiled_inference|
|xception41p_Opset17|PASS|compiled_inference|
|xception41p_Opset18|PASS|compiled_inference|
|xception65_Opset16|PASS|compiled_inference|
|xception65_Opset17|PASS|compiled_inference|
|xception65_Opset18|PASS|compiled_inference|
|xception65p_Opset16|PASS|compiled_inference|
|xception65p_Opset17|PASS|compiled_inference|
|xception65p_Opset18|PASS|compiled_inference|
|xception71_Opset16|PASS|compiled_inference|
|xception71_Opset17|PASS|compiled_inference|
|xception71_Opset17_timm|PASS|compiled_inference|
|xception71_Opset18|PASS|compiled_inference|

## 7 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384_Opset16_timm|compiled_inference|PASS|
|beit_large_patch16_384_Opset17_timm|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset16_timm|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17_timm|compiled_inference|PASS|
|regnetz_c16_evos_Opset16_timm|Numerics|PASS|
|vit_large_patch16_384_Opset16_timm|compiled_inference|PASS|
|vit_large_patch16_384_Opset17_timm|compiled_inference|PASS|

