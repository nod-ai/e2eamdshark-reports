# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1497.1732|1470.3148|-26.8584|-1.79%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1495.7937|1572.0663|76.2726|5.1%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12233.4604|12426.901|193.4406|1.58%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|739.0513|742.1546|3.1033|0.42%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2504.7886|2538.5637|33.7751|1.35%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|9975.5093|10070.7031|95.1938|0.95%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|622.8967|602.8655|-20.0312|-3.22%|
|migraphx_cadene__dpn92i1|Numerics|within tol|436.493|438.4559|1.9628|0.45%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8867.4966|8896.8254|29.3287|0.33%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|819.0862|821.6452|2.559|0.31%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10431.5791|10181.4235|-250.1556|-2.4%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|202.9991|206.6969|3.6978|1.82%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|292.2656|292.1236|-0.142|-0.05%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1075.6681|1094.418|18.7499|1.74%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|56.4495|57.4766|1.0271|1.82%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4779.1664|4815.3498|36.1834|0.76%|
|migraphx_torchvision__inceptioni1|PASS|within tol|358.817|355.5206|-3.2964|-0.92%|
|migraphx_torchvision__resnet50i1|PASS|within tol|193.9243|195.2303|1.306|0.67%|

## 3 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 10 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384_Opset16|compiled_inference|PASS|
|beit_large_patch16_384_Opset17|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset16|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_Opset16|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset16|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset18|compiled_inference|PASS|
|model--albert-xxl-v2-finetuned-squad--anas-awadalla|compiled_inference|PASS|
|regnetz_d8_evos_Opset16_timm|Numerics|PASS|

