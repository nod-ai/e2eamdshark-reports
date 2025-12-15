# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.8378|101.6173|-0.2205|-0.22%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|284.6461|285.9389|1.2928|0.45%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.5896|57.4045|-0.1851|-0.32%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|75.3336|75.7502|0.4166|0.55%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|295.0061|295.2393|0.2332|0.08%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|40.2634|40.3639|0.1005|0.25%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6353|12.5899|-0.0454|-0.36%|
|migraphx_cadene__dpn92i1|Numerics|within tol|10.1416|10.1204|-0.0212|-0.21%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.8866|21.9275|0.0409|0.19%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.1036|6.097|-0.0065|-0.11%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2182|7.2295|0.0112|0.16%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.6713|19.7035|0.0322|0.16%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|14.8335|14.8608|0.0273|0.18%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8704|25.8418|-0.0286|-0.11%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.8104|112.7768|-0.0336|-0.03%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|14.5766|14.4628|-0.1139|-0.78%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.7406|17.7166|-0.0241|-0.14%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6755|4.645|-0.0305|-0.65%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.7169|3.7015|-0.0154|-0.41%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2506|20.285|0.0343|0.17%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.029|33.3168|0.2878|0.87%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.8849|52.5516|0.6667|1.28%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.748|11.7547|0.0068|0.06%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4656|12.4989|0.0333|0.27%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8433|12.853|0.0096|0.08%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4614|12.4587|-0.0026|-0.02%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7574|12.7996|0.0422|0.33%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.3671|14.3811|0.014|0.1%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.7479|32.3292|0.5812|1.83%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.5264|62.3983|0.872|1.42%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.4282|96.7129|1.2846|1.35%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.6743|12.6972|0.0229|0.18%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3316|14.3405|0.009|0.06%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.1998|20.3039|0.1041|0.52%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3197|14.3632|0.0434|0.3%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5596|20.6057|0.046|0.22%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.1078|29.4329|0.3251|1.12%|

## 8 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|ResNet18_vaiq|PASS|Numerics|
|ResNet34_vaiq|PASS|Numerics|
|sequencer2d_l_Opset16|PASS|Numerics|
|sequencer2d_m_Opset16|PASS|Numerics|
|sequencer2d_s_Opset16|PASS|Numerics|
|sequencer2d_s_Opset17_timm|PASS|Numerics|
|squeezenet1.0-9|PASS|Numerics|
|t5-decoder-with-lm-head-12|PASS|native_inference|

## 9 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|AlexNet_vaiq_int8|Numerics|PASS|
|alexnet_Opset18|Numerics|PASS|
|alexnet_Opset18_torch_hub|Numerics|PASS|
|sequencer2d_l_Opset17_timm|Numerics|PASS|
|sequencer2d_m_Opset16_timm|Numerics|PASS|
|sequencer2d_s_Opset16_timm|Numerics|PASS|
|squeezenet1.0-6|Numerics|PASS|
|squeezenet1_1_Opset17|Numerics|PASS|
|tf_efficientnetv2_s_Opset17_timm|compiled_inference|Numerics|

