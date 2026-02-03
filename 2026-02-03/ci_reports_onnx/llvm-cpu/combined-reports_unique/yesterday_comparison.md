# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1631.1848|1572.7722|-58.4126|-3.58%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1660.1295|1532.2188|-127.9107|-7.7%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|24699.281|12317.9899|-12381.2911|-50.13%|
|migraphx_ORT__distilgpt2_1|PASS|progression|866.668|719.9918|-146.6762|-16.92%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2513.6156|2460.4569|-53.1587|-2.11%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|7411.1645|10345.6322|2934.4677|39.6%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|563.3219|639.5305|76.2085|13.53%|
|migraphx_cadene__dpn92i1|PASS|progression|1040.0101|436.5646|-603.4455|-58.02%|
|migraphx_cadene__inceptionv4i16|PASS|progression|12507.322|8863.5325|-3643.7895|-29.13%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|1065.3922|816.9011|-248.4912|-23.32%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|11767.871|9938.564|-1829.307|-15.54%|
|migraphx_mlperf__resnet50_v1|PASS|progression|385.6434|202.1256|-183.5178|-47.59%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|563.9932|298.3092|-265.684|-47.11%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|2418.2852|1115.0397|-1303.2455|-53.89%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|178.5608|57.0833|-121.4775|-68.03%|
|migraphx_torchvision__densenet121i32|PASS|progression|6895.2537|4761.0335|-2134.2202|-30.95%|
|migraphx_torchvision__inceptioni1|PASS|progression|436.9137|349.8965|-87.0172|-19.92%|
|migraphx_torchvision__resnet50i1|PASS|progression|253.7962|194.3403|-59.456|-23.43%|

## 144 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384.in22k_ft_in22k_in1k|PASS|compiled_inference|
|convnext_xlarge.fb_in22k_ft_in1k|PASS|compiled_inference|
|deit3_large_patch16_384.fb_in1k|PASS|compiled_inference|
|dm_nfnet_f0_Opset16|PASS|compilation|
|dm_nfnet_f0_Opset17|PASS|compilation|
|dm_nfnet_f1_Opset16|PASS|compilation|
|dm_nfnet_f2_Opset16|PASS|compilation|
|dm_nfnet_f2_Opset17|PASS|compilation|
|dm_nfnet_f4.dm_in1k|PASS|compiled_inference|
|longformer_Opset16|compiled_inference|compilation|
|longformer_Opset17|compiled_inference|compilation|
|longformer_Opset18|compiled_inference|compilation|

## 13 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset16_timm|compiled_inference|PASS|
|deit3_large_patch16_384_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_Opset18|compiled_inference|PASS|
|migx_bench_bert-large-uncased_1_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_1_384|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_384|compiled_inference|PASS|
|model--s2t-medium-librispeech-asr--facebook|Numerics|PASS|
|regnetz_c16_evos_Opset16_timm|Numerics|PASS|
|vit_large_patch16_384_Opset16|compiled_inference|PASS|
|vit_large_patch16_384_Opset17|compiled_inference|PASS|
|vit_large_patch16_384_Opset18|compiled_inference|PASS|

