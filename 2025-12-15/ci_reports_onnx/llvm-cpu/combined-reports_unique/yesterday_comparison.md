# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1824.6712|1777.795|-46.8762|-2.57%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1751.1814|1794.1761|42.9947|2.46%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|20195.6748|19503.2769|-692.3979|-3.43%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|837.1258|841.9634|4.8376|0.58%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2609.3986|2583.0912|-26.3074|-1.01%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|14059.8558|14066.9943|7.1385|0.05%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|642.4111|617.2811|-25.1299|-3.91%|
|migraphx_cadene__dpn92i1|PASS|within tol|861.5502|825.6118|-35.9384|-4.17%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|9549.7418|9545.7038|-4.038|-0.04%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|1016.7835|1017.1637|0.3802|0.04%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|13755.6168|14168.4835|412.8668|3.0%|
|migraphx_mlperf__resnet50_v1|PASS|progression|413.3813|358.8715|-54.5099|-13.19%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|489.6272|557.3747|67.7475|13.84%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|2454.5918|2349.4241|-105.1677|-4.28%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|99.2259|103.5409|4.3151|4.35%|
|migraphx_torchvision__densenet121i32|PASS|within tol|5088.2565|5053.6158|-34.6406|-0.68%|
|migraphx_torchvision__inceptioni1|PASS|within tol|369.1837|370.9709|1.7872|0.48%|
|migraphx_torchvision__resnet50i1|PASS|within tol|216.9016|213.9783|-2.9233|-1.35%|

## No Regressions Found

## 7 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384_Opset16_timm|compiled_inference|PASS|
|beit_large_patch16_384_Opset17_timm|compiled_inference|PASS|
|deit3_large_patch16_384_Opset16_timm|compiled_inference|PASS|
|longformer_Opset16|import_model|compilation|
|longformer_Opset17|import_model|compilation|
|longformer_Opset18|import_model|compilation|
|vit_large_patch16_384_Opset17_timm|compiled_inference|PASS|

