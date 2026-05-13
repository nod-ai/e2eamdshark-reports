# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1543.6179|1561.1915|17.5737|1.14%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1484.2813|1473.3754|-10.9059|-0.73%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|13127.6535|13276.0732|148.4198|1.13%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|701.0169|719.4032|18.3864|2.62%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|1114.451|1111.315|-3.136|-0.28%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|6493.4566|6332.7032|-160.7534|-2.48%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|569.5658|539.2069|-30.3589|-5.33%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|740.8481|732.2364|-8.6117|-1.16%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10478.8012|10624.837|146.0358|1.39%|
|migraphx_mlperf__resnet50_v1|PASS|progression|213.1874|159.1014|-54.086|-25.37%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|262.7563|257.283|-5.4733|-2.08%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1297.4921|1302.6037|5.1116|0.39%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|95.3955|94.8337|-0.5618|-0.59%|
|migraphx_pytorch-examples__wlang_lstm|PASS|within tol|16.18|15.8554|-0.3246|-2.01%|
|migraphx_torchvision__inceptioni1|PASS|within tol|340.7727|335.1767|-5.596|-1.64%|
|migraphx_torchvision__resnet50i1|PASS|within tol|150.8002|149.6829|-1.1173|-0.74%|

## 13 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset16_timm|PASS|compiled_inference|
|deit3_large_patch16_384_Opset16|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset16|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset17|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset17_timm|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset18|PASS|compiled_inference|
|vit_large_patch16_384_Opset16_timm|PASS|compiled_inference|

## 17 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|model--albert-xxl-v2-finetuned-squad--anas-awadalla|compiled_inference|PASS|
|pit_b_224|compilation|PASS|
|pit_b_distilled_224|compilation|PASS|
|pit_s_distilled_224|compilation|PASS|
|pit_ti_distilled_224|compilation|PASS|
|pit_xs_distilled_224|compilation|PASS|
|resnet50-v1-12-qdq|Numerics|PASS|
|vit_base_patch8_224_Opset16|compilation|PASS|
|vit_base_patch8_224_dino_Opset16|compilation|PASS|
|vit_base_patch8_224_dino_Opset17|compilation|PASS|
|vit_base_patch8_224_dino_Opset18|compilation|PASS|
|vit_base_patch8_224_in21k_Opset16|compilation|PASS|
|vit_base_patch8_224_in21k_Opset17|compilation|PASS|
|vit_base_patch8_224_in21k_Opset18|compilation|PASS|
|vit_small_patch8_224_dino_Opset16|compilation|PASS|
|vit_small_patch8_224_dino_Opset17|compilation|PASS|
|vit_small_patch8_224_dino_Opset18|compilation|PASS|

