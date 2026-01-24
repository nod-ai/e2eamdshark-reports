# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1524.7377|1483.5008|-41.2369|-2.7%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1565.8597|1572.5095|6.6498|0.42%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12486.6549|12409.2135|-77.4414|-0.62%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|744.9039|711.2601|-33.6439|-4.52%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2521.2953|2499.1177|-22.1776|-0.88%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|10263.3798|10073.1239|-190.2559|-1.85%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|627.6207|627.5924|-0.0283|-0.0%|
|migraphx_cadene__dpn92i1|PASS|within tol|438.8148|438.5726|-0.2422|-0.06%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8875.1283|8910.0431|34.9148|0.39%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|823.7375|824.5096|0.7721|0.09%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10301.765|10132.9389|-168.8261|-1.64%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|204.1768|206.5428|2.3661|1.16%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|293.0406|293.6896|0.649|0.22%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1071.0626|1278.5834|207.5208|19.38%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|56.4949|57.2008|0.7058|1.25%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4796.69|4798.4239|1.7338|0.04%|
|migraphx_torchvision__inceptioni1|PASS|within tol|358.5608|355.3559|-3.2049|-0.89%|
|migraphx_torchvision__resnet50i1|PASS|within tol|192.9886|199.9464|6.9579|3.61%|

## 7 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|model--s2t-medium-librispeech-asr--facebook|PASS|Numerics|
|regnetx_002_Opset17_timm|PASS|compiled_inference|
|xception41p_Opset16_timm|PASS|compiled_inference|

## 2 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset16_timm|import_model|PASS|
|migraphx_pytorch-examples__wlang_lstm|compiled_inference|PASS|

