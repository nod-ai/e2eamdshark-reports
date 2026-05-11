# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|1440.4937|1787.8006|347.3069|24.11%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1520.7448|1712.6862|191.9414|12.62%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|12945.693|20330.2152|7384.5222|57.04%|
|migraphx_ORT__distilgpt2_1|PASS|regression|718.6363|830.5963|111.96|15.58%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|1113.8021|988.607|-125.1951|-11.24%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|6405.8821|5319.3574|-1086.5247|-16.96%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|538.0672|495.6472|-42.42|-7.88%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|747.0342|776.5218|29.4875|3.95%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|10607.5015|11232.9684|625.467|5.9%|
|migraphx_mlperf__resnet50_v1|PASS|regression|189.9302|253.9998|64.0695|33.73%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|271.4562|441.2798|169.8236|62.56%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1351.7552|2899.1454|1547.3902|114.47%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|98.7592|261.8643|163.1051|165.15%|
|migraphx_pytorch-examples__wlang_lstm|PASS|regression|16.0301|22.1293|6.0992|38.05%|
|migraphx_torchvision__inceptioni1|PASS|regression|344.3221|412.4192|68.0971|19.78%|
|migraphx_torchvision__resnet50i1|PASS|regression|158.1097|188.5041|30.3944|19.22%|

## 21 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset18|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_384|PASS|compiled_inference|
|model--albert-xxl-v2-finetuned-squad--anas-awadalla|PASS|compiled_inference|
|resnet50-v1-12-qdq|PASS|Numerics|

## 20 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|coat_lite_small_Opset17_timm|compilation|PASS|
|coat_lite_tiny_Opset17_timm|compilation|PASS|
|coat_tiny_Opset18_timm|compilation|PASS|
|flaubert_Opset16_transformers|Numerics|PASS|
|flaubert_Opset17_transformers|Numerics|PASS|
|pit_s_distilled_224_Opset17_timm|compilation|PASS|
|pit_ti_distilled_224_Opset16_timm|compilation|PASS|
|pit_ti_distilled_224_Opset17_timm|compilation|PASS|
|umt5_Opset16_transformers|Numerics|PASS|
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
|xlmroberta_Opset16_transformers|Numerics|PASS|

