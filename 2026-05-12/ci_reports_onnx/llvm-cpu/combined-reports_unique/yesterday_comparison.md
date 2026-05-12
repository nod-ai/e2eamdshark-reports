# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1787.8006|1543.6179|-244.1828|-13.66%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1712.6862|1484.2813|-228.4049|-13.34%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|20330.2152|13127.6535|-7202.5618|-35.43%|
|migraphx_ORT__distilgpt2_1|PASS|progression|830.5963|701.0169|-129.5794|-15.6%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|988.607|1114.451|125.8439|12.73%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|5319.3574|6493.4566|1174.0992|22.07%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|495.6472|569.5658|73.9185|14.91%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|776.5218|740.8481|-35.6737|-4.59%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|11232.9684|10478.8012|-754.1672|-6.71%|
|migraphx_mlperf__resnet50_v1|PASS|progression|253.9998|213.1874|-40.8124|-16.07%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|441.2798|262.7563|-178.5235|-40.46%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|2899.1454|1297.4921|-1601.6533|-55.25%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|261.8643|95.3955|-166.4688|-63.57%|
|migraphx_pytorch-examples__wlang_lstm|PASS|progression|22.1293|16.18|-5.9493|-26.88%|
|migraphx_torchvision__inceptioni1|PASS|progression|412.4192|340.7727|-71.6465|-17.37%|
|migraphx_torchvision__resnet50i1|PASS|progression|188.5041|150.8002|-37.7039|-20.0%|

## 15 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 19 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|coat_lite_mini_Opset18_timm|compilation|PASS|
|coat_tiny_Opset16_timm|compilation|PASS|
|convnext_xlarge_384_in22ft1k_Opset18|compiled_inference|PASS|
|crossvit_18_240_Opset16_timm|compilation|PASS|
|crossvit_18_240_Opset17_timm|compilation|PASS|
|migx_bench_bert-large-uncased_1_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_1_384|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_384|compiled_inference|PASS|
|pit_b_distilled_224_Opset16_timm|compilation|PASS|
|pit_b_distilled_224_Opset18_timm|compilation|PASS|
|vit_base_patch8_224_Opset17|compilation|PASS|
|vit_base_patch8_224_dino_Opset16_timm|compilation|PASS|
|vit_base_patch8_224_dino_Opset18_timm|compilation|PASS|
|vit_base_patch8_224_in21k_Opset16_timm|compilation|PASS|
|vit_base_patch8_224_in21k_Opset17_timm|compilation|PASS|
|vit_small_patch8_224_dino_Opset16_timm|compilation|PASS|
|vit_small_patch8_224_dino_Opset18_timm|compilation|PASS|

