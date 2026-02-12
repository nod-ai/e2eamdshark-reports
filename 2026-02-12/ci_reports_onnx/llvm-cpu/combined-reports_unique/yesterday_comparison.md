# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1520.8242|68.1064|-1452.7178|-95.52%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1553.3218|64.2639|-1489.0579|-95.86%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|12408.302|189.2076|-12219.0945|-98.48%|
|migraphx_ORT__distilgpt2_1|PASS|progression|723.0196|20.437|-702.5826|-97.17%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2456.7972|106.0274|-2350.7698|-95.68%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|10336.432|315.711|-10020.721|-96.95%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|663.5513|19.5853|-643.9661|-97.05%|
|migraphx_cadene__dpn92i1|PASS|progression|439.8399|200.3675|-239.4724|-54.45%|
|migraphx_cadene__inceptionv4i16|PASS|progression|9035.1272|4482.8994|-4552.2277|-50.38%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|816.3918|147.5251|-668.8667|-81.93%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|10195.0849|161.6065|-10033.4784|-98.41%|
|migraphx_mlperf__resnet50_v1|PASS|progression|196.581|119.8182|-76.7628|-39.05%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|297.8476|28.2265|-269.6211|-90.52%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|1383.1033|202.7579|-1180.3454|-85.34%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|56.8172|35.1977|-21.6195|-38.05%|
|migraphx_pytorch-examples__wlang_lstm|PASS|progression|32.5819|19.717|-12.8649|-39.48%|
|migraphx_torchvision__densenet121i32|PASS|progression|4939.5496|1763.7182|-3175.8314|-64.29%|
|migraphx_torchvision__inceptioni1|PASS|progression|356.6177|168.463|-188.1548|-52.76%|
|migraphx_torchvision__resnet50i1|PASS|progression|197.9196|134.2878|-63.6319|-32.15%|

## 13 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|model--albert-xxl-v2-finetuned-squad--anas-awadalla|PASS|compiled_inference|
|vit_large_patch16_384_Opset16|PASS|compiled_inference|

## 21 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset16_timm|compiled_inference|PASS|
|deit3_large_patch16_384_Opset16_timm|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17_timm|compiled_inference|PASS|
|longformer_Opset16|import_model|compiled_inference|
|longformer_Opset17|import_model|compiled_inference|
|longformer_Opset18|import_model|compiled_inference|
|migx_bench_bert-large-uncased_16_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_16_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_16_384|compiled_inference|Numerics|
|migx_bench_bert-large-uncased_32_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_32_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_32_384|compiled_inference|Numerics|
|migx_bench_bert-large-uncased_4_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_4_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_4_384|compiled_inference|PASS|
|migx_bench_bert-large-uncased_8_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_8_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_8_384|compiled_inference|PASS|
|vit_large_patch14_clip_336.laion2b_ft_in12k_in1k|compiled_inference|PASS|
|vit_large_patch16_384.augreg_in21k_ft_in1k|compiled_inference|PASS|
|vit_large_patch16_384_Opset16_timm|compiled_inference|PASS|

