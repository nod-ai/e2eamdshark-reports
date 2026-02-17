# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1597.9898|1543.6087|-54.3811|-3.4%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1589.3946|1540.3903|-49.0043|-3.08%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12896.7411|12381.0605|-515.6805|-4.0%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|738.1373|745.676|7.5387|1.02%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2507.9459|2555.1128|47.1669|1.88%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|10140.8748|10210.887|70.0122|0.69%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|615.5751|635.2895|19.7144|3.2%|
|migraphx_cadene__dpn92i1|PASS|within tol|437.0882|437.9408|0.8525|0.2%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8760.5088|8801.6289|41.1201|0.47%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|807.1926|825.0119|17.8193|2.21%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10474.3753|10181.1054|-293.2699|-2.8%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|163.1392|166.6493|3.5102|2.15%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|294.4752|297.9207|3.4455|1.17%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1432.1454|1397.9512|-34.1942|-2.39%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|55.4166|56.6477|1.2311|2.22%|
|migraphx_pytorch-examples__wlang_lstm|PASS|progression|35.5753|32.2725|-3.3028|-9.28%|
|migraphx_torchvision__densenet121i32|PASS|within tol|3541.0458|3619.056|78.0102|2.2%|
|migraphx_torchvision__inceptioni1|PASS|within tol|357.2608|364.6126|7.3518|2.06%|
|migraphx_torchvision__resnet50i1|PASS|within tol|200.3825|197.6261|-2.7564|-1.38%|

## 9 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|regnetz_c16_evos_Opset16|PASS|Numerics|
|regnetz_c16_evos_Opset17|PASS|Numerics|
|regnetz_d8_evos_Opset16|PASS|Numerics|
|regnetz_d8_evos_Opset17|PASS|Numerics|

## 12 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|RRDB_ESRGAN_vaiq_int8|compilation|Numerics|
|regnetx_002_Opset16|compiled_inference|PASS|
|regnetx_002_Opset17|compiled_inference|PASS|
|regnetx_002_Opset17_timm|compiled_inference|PASS|
|regnetx_002_Opset18|compiled_inference|PASS|
|regnety_002_Opset16|compiled_inference|PASS|
|regnety_002_Opset16_timm|compiled_inference|PASS|
|regnety_002_Opset17|compiled_inference|PASS|
|regnetz_c16_evos_Opset16_timm|Numerics|PASS|
|regnetz_d8_evos_Opset16_timm|Numerics|PASS|
|xception41p_Opset16_timm|compiled_inference|PASS|
|xception65p_Opset18_timm|compiled_inference|PASS|

