# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1564.69|1470.6428|-94.0471|-6.01%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1483.7105|1561.5465|77.836|5.25%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12213.4469|12410.1472|196.7002|1.61%|
|migraphx_ORT__distilgpt2_1|PASS|progression|758.8314|714.2068|-44.6246|-5.88%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2544.6871|2448.149|-96.5381|-3.79%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|10002.99|9771.6172|-231.3727|-2.31%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|668.2016|662.6366|-5.565|-0.83%|
|migraphx_cadene__dpn92i1|PASS|within tol|453.9682|433.9049|-20.0632|-4.42%|
|migraphx_cadene__inceptionv4i16|PASS|progression|8966.2586|8346.4987|-619.7599|-6.91%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|842.5768|810.8561|-31.7207|-3.76%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|9957.4861|10322.431|364.9449|3.67%|
|migraphx_mlperf__resnet50_v1|PASS|progression|209.7407|192.6873|-17.0533|-8.13%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|302.1082|292.7868|-9.3214|-3.09%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1143.6973|1094.1743|-49.523|-4.33%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|56.6348|56.5281|-0.1067|-0.19%|
|migraphx_pytorch-examples__wlang_lstm|PASS|within tol|33.8712|32.2507|-1.6206|-4.78%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4836.7173|4829.1118|-7.6056|-0.16%|
|migraphx_torchvision__inceptioni1|PASS|within tol|356.418|349.0585|-7.3595|-2.06%|
|migraphx_torchvision__resnet50i1|PASS|within tol|195.386|196.1677|0.7817|0.4%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|
|regnetz_d8_evos_Opset16_timm|PASS|Numerics|

## 5 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|RRDB_ESRGAN_vaiq_int8|compilation|Numerics|
|longformer_Opset16|import_model|compiled_inference|
|longformer_Opset17|import_model|compiled_inference|
|longformer_Opset18|import_model|compiled_inference|
|xception65_Opset18_timm|compiled_inference|PASS|

