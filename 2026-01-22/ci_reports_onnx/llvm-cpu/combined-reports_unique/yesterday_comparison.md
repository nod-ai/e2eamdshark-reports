# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1490.9669|57.6861|-1433.2808|-96.13%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1486.7927|55.7779|-1431.0148|-96.25%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|12232.4322|196.059|-12036.3733|-98.4%|
|migraphx_ORT__distilgpt2_1|PASS|progression|736.2612|20.1132|-716.148|-97.27%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2534.3143|96.8481|-2437.4661|-96.18%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|10092.2876|293.1291|-9799.1584|-97.1%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|668.7756|18.0354|-650.7402|-97.3%|
|migraphx_cadene__dpn92i1|PASS|progression|438.7833|200.3524|-238.4309|-54.34%|
|migraphx_cadene__inceptionv4i16|PASS|progression|8838.7029|4389.8409|-4448.8619|-50.33%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|819.0862|135.5174|-683.5688|-83.46%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|9878.8026|153.2448|-9725.5578|-98.45%|
|migraphx_mlperf__resnet50_v1|PASS|progression|203.2532|121.7012|-81.5519|-40.12%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|299.7416|26.8932|-272.8484|-91.03%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|1084.6987|53.0555|-1031.6432|-95.11%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|55.6221|35.629|-19.993|-35.94%|
|migraphx_torchvision__densenet121i32|PASS|progression|4822.3876|1525.2894|-3297.0982|-68.37%|
|migraphx_torchvision__inceptioni1|PASS|progression|348.1874|150.4832|-197.7041|-56.78%|
|migraphx_torchvision__resnet50i1|PASS|progression|192.4547|125.7994|-66.6554|-34.63%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|

## 70 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|crossvit_15_240|Numerics|PASS|
|crossvit_15_dagger_240|Numerics|PASS|
|crossvit_15_dagger_408|Numerics|PASS|
|crossvit_18_240|Numerics|PASS|
|crossvit_18_dagger_240|Numerics|PASS|
|crossvit_18_dagger_408|Numerics|PASS|
|crossvit_9_240|Numerics|PASS|
|crossvit_9_dagger_240|Numerics|PASS|
|crossvit_base_240|Numerics|PASS|
|crossvit_small_240|Numerics|PASS|
|crossvit_tiny_240|Numerics|PASS|
|cs3se_edgenet_x_Opset16_timm|Numerics|PASS|
|cs3sedarknet_l_Opset16_timm|Numerics|PASS|
|cs3sedarknet_x_Opset17_timm|Numerics|PASS|
|dpn92_Opset17_timm|Numerics|PASS|
|edgenext_base|Numerics|PASS|
|edgenext_small|Numerics|PASS|
|edgenext_small_rw|Numerics|PASS|
|edgenext_small_rw_Opset18_timm|Numerics|PASS|
|edgenext_x_small|Numerics|PASS|
|edgenext_xx_small|Numerics|PASS|
|migraphx_cadene__dpn92i1|Numerics|PASS|
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
|res2net50_48w_2s_Opset18_timm|Numerics|PASS|
|t5_Opset16|Numerics|PASS|
|t5_Opset17|Numerics|PASS|
|xcit_large_24_p16_224|Numerics|PASS|
|xcit_large_24_p16_384_dist|Numerics|PASS|
|xcit_large_24_p8_224|Numerics|PASS|
|xcit_large_24_p8_224_Opset16_timm|Numerics|PASS|
|xcit_large_24_p8_384_dist|Numerics|PASS|
|xcit_medium_24_p16_224|Numerics|PASS|
|xcit_medium_24_p16_384_dist|Numerics|PASS|
|xcit_medium_24_p8_224|Numerics|PASS|
|xcit_medium_24_p8_384_dist|Numerics|PASS|
|xcit_nano_12_p16_224|Numerics|PASS|
|xcit_nano_12_p16_384_dist|Numerics|PASS|
|xcit_nano_12_p8_224|Numerics|PASS|
|xcit_nano_12_p8_384_dist|Numerics|PASS|
|xcit_small_12_p16_224|Numerics|PASS|
|xcit_small_12_p16_384_dist|Numerics|PASS|
|xcit_small_12_p8_224|Numerics|PASS|
|xcit_small_12_p8_224_dist_Opset17_timm|Numerics|PASS|
|xcit_small_12_p8_384_dist|Numerics|PASS|
|xcit_small_24_p16_224|Numerics|PASS|
|xcit_small_24_p16_384_dist|Numerics|PASS|
|xcit_small_24_p8_224|Numerics|PASS|
|xcit_small_24_p8_384_dist|Numerics|PASS|
|xcit_tiny_12_p16_224|Numerics|PASS|
|xcit_tiny_12_p16_224_Opset17_timm|Numerics|PASS|
|xcit_tiny_12_p16_384_dist|Numerics|PASS|
|xcit_tiny_12_p8_224|Numerics|PASS|
|xcit_tiny_12_p8_384_dist|Numerics|PASS|
|xcit_tiny_24_p16_224|Numerics|PASS|
|xcit_tiny_24_p16_384_dist|Numerics|PASS|
|xcit_tiny_24_p8_224|Numerics|PASS|
|xcit_tiny_24_p8_384_dist|Numerics|PASS|
|xcit_tiny_24_p8_384_dist_Opset16_timm|Numerics|PASS|
|xlmroberta_Opset16|Numerics|PASS|

