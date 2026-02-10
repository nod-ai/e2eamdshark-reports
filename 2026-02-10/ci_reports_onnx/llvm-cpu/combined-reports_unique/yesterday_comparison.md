# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1526.5667|1565.5326|38.9659|2.55%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1520.2143|1589.888|69.6737|4.58%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12450.6361|12844.4383|393.8022|3.16%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|752.8726|771.6817|18.8091|2.5%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2523.982|2426.1554|-97.8267|-3.88%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|10243.3061|8349.5829|-1893.7232|-18.49%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|671.5233|607.9351|-63.5882|-9.47%|
|migraphx_cadene__dpn92i1|PASS|regression|438.7368|462.3788|23.642|5.39%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|9021.5812|9161.8075|140.2263|1.55%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|815.5667|841.3635|25.7968|3.16%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10152.965|10322.6502|169.6853|1.67%|
|migraphx_mlperf__resnet50_v1|PASS|regression|196.4572|208.9116|12.4545|6.34%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|296.6689|323.271|26.6021|8.97%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1423.1732|1446.9088|23.7356|1.67%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|57.0445|75.0763|18.0318|31.61%|
|migraphx_pytorch-examples__wlang_lstm|PASS|regression|32.2439|53.6162|21.3723|66.28%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4948.394|4877.4135|-70.9805|-1.43%|
|migraphx_torchvision__inceptioni1|PASS|regression|355.3275|373.9647|18.6372|5.25%|
|migraphx_torchvision__resnet50i1|PASS|regression|198.3432|211.7298|13.3867|6.75%|

## 5 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 3 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset16_timm|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17_timm|compiled_inference|PASS|
|vit_large_patch16_384_Opset16_timm|compiled_inference|PASS|

