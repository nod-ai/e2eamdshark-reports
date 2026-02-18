# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1543.6087|1612.7657|69.1569|4.48%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1540.3903|1591.2633|50.873|3.3%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12381.0605|12470.9379|89.8773|0.73%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|745.676|750.6607|4.9847|0.67%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2555.1128|2537.6557|-17.4571|-0.68%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|10210.887|8706.8074|-1504.0797|-14.73%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|635.2895|637.9|2.6105|0.41%|
|migraphx_cadene__dpn92i1|PASS|regression|437.9408|489.7452|51.8045|11.83%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8801.6289|9059.12|257.4911|2.93%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|825.0119|925.3463|100.3344|12.16%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10181.1054|10310.3577|129.2523|1.27%|
|migraphx_mlperf__resnet50_v1|PASS|regression|166.6493|197.5828|30.9335|18.56%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|297.9207|326.0105|28.0898|9.43%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1397.9512|1473.795|75.8438|5.43%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|56.6477|78.6147|21.967|38.78%|
|migraphx_pytorch-examples__wlang_lstm|PASS|regression|32.2725|56.2016|23.9291|74.15%|
|migraphx_torchvision__densenet121i32|PASS|within tol|3619.056|3751.1486|132.0927|3.65%|
|migraphx_torchvision__inceptioni1|PASS|regression|364.6126|403.1043|38.4917|10.56%|
|migraphx_torchvision__resnet50i1|PASS|regression|197.6261|233.719|36.0929|18.26%|

## 12 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|regnetz_c16_evos_Opset16_timm|PASS|Numerics|

## 10 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|RDN_pytorch_vaiq_int8|compiled_inference|Numerics|
|deit3_large_patch16_384_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_Opset18|compiled_inference|PASS|
|regnetz_c16_evos_Opset16|Numerics|PASS|
|regnetz_c16_evos_Opset17|Numerics|PASS|
|regnetz_d8_evos_Opset16|Numerics|PASS|
|regnetz_d8_evos_Opset17|Numerics|PASS|
|xception41_Opset17_timm|compiled_inference|PASS|
|xception65_Opset18_timm|compiled_inference|PASS|
|xception71_Opset17_timm|compiled_inference|PASS|

