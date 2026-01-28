# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1553.1071|1564.69|11.5829|0.75%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1574.9518|1483.7105|-91.2413|-5.79%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12562.6251|12213.4469|-349.1782|-2.78%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|789.6654|758.8314|-30.834|-3.9%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2431.7581|2544.6871|112.929|4.64%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|8379.0526|10002.99|1623.9373|19.38%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|589.8358|668.2016|78.3658|13.29%|
|migraphx_cadene__dpn92i1|PASS|within tol|463.1181|453.9682|-9.15|-1.98%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8978.7204|8966.2586|-12.4617|-0.14%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|845.5736|842.5768|-2.9968|-0.35%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10005.7121|9957.4861|-48.226|-0.48%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|217.6015|209.7407|-7.8608|-3.61%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|325.5798|302.1082|-23.4716|-7.21%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1165.8648|1143.6973|-22.1675|-1.9%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|75.987|56.6348|-19.3522|-25.47%|
|migraphx_pytorch-examples__wlang_lstm|PASS|progression|54.5817|33.8712|-20.7105|-37.94%|
|migraphx_torchvision__densenet121i32|PASS|within tol|5065.9845|4836.7173|-229.2671|-4.53%|
|migraphx_torchvision__inceptioni1|PASS|progression|375.3602|356.418|-18.9423|-5.05%|
|migraphx_torchvision__resnet50i1|PASS|progression|207.343|195.386|-11.957|-5.77%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 5 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset16_timm|compiled_inference|PASS|
|deit3_large_patch16_384_Opset16_timm|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17_timm|compiled_inference|PASS|
|regnetz_d8_evos_Opset16_timm|Numerics|PASS|
|vit_large_patch16_384_Opset16_timm|compiled_inference|PASS|

