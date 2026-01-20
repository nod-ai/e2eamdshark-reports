# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1610.9442|1515.1703|-95.7739|-5.95%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1447.3939|1463.853|16.4591|1.14%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12446.5602|12293.5211|-153.0391|-1.23%|
|migraphx_ORT__distilgpt2_1|PASS|progression|729.3772|683.2416|-46.1356|-6.33%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2508.789|2486.6412|-22.1478|-0.88%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|10018.537|10231.869|213.3321|2.13%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|653.1028|632.4529|-20.6499|-3.16%|
|migraphx_cadene__dpn92i1|Numerics|within tol|436.59|434.5477|-2.0422|-0.47%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8880.6809|8861.9528|-18.7281|-0.21%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|825.7871|817.6018|-8.1854|-0.99%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10164.6293|9699.4226|-465.2067|-4.58%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|208.8736|205.6265|-3.2471|-1.55%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|299.0157|300.4547|1.4389|0.48%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1078.0304|1145.554|67.5236|6.26%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|56.1748|57.0396|0.8647|1.54%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4855.4627|4775.4136|-80.049|-1.65%|
|migraphx_torchvision__inceptioni1|PASS|within tol|356.3414|348.1285|-8.2129|-2.3%|
|migraphx_torchvision__resnet50i1|PASS|within tol|199.0866|194.1425|-4.9441|-2.48%|

## 21 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384_Opset16|PASS|compiled_inference|
|beit_large_patch16_384_Opset17|PASS|compiled_inference|
|convnext_xlarge_384_in22ft1k_Opset16|PASS|compiled_inference|
|convnext_xlarge_384_in22ft1k_Opset17|PASS|compiled_inference|
|deit3_large_patch16_384_Opset16_timm|PASS|compiled_inference|
|model--albert-xxl-v2-finetuned-squad--anas-awadalla|PASS|compiled_inference|
|xception41_Opset16|PASS|compiled_inference|
|xception41_Opset17|PASS|compiled_inference|
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
|xception71_Opset18|PASS|compiled_inference|

## No Progressions Found

