# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.6173|102.017|0.3997|0.39%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|285.9389|286.3973|0.4583|0.16%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.4045|58.4607|1.0561|1.84%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|75.7502|75.762|0.0118|0.02%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|295.2393|294.636|-0.6033|-0.2%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|40.3639|40.6352|0.2713|0.67%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.5899|12.696|0.1061|0.84%|
|migraphx_cadene__dpn92i1|Numerics|within tol|10.1204|10.2147|0.0942|0.93%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.9275|21.9714|0.0439|0.2%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.097|6.1477|0.0507|0.83%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2295|7.2733|0.0438|0.61%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.7035|20.6249|0.9214|4.68%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|14.8608|14.9098|0.0491|0.33%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8418|26.5269|0.6851|2.65%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.7768|113.6571|0.8803|0.78%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|14.4628|15.2395|0.7767|5.37%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.7166|17.8196|0.103|0.58%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.645|4.7138|0.0688|1.48%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.7015|3.7663|0.0648|1.75%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.285|20.3103|0.0253|0.12%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.3168|33.3268|0.01|0.03%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.5516|52.4735|-0.0781|-0.15%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7547|11.8494|0.0946|0.8%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4989|12.5051|0.0062|0.05%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.853|12.8942|0.0412|0.32%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4587|12.5495|0.0907|0.73%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7996|12.7971|-0.0026|-0.02%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.3811|14.4168|0.0357|0.25%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.3292|32.1325|-0.1967|-0.61%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.3983|62.2994|-0.0989|-0.16%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|96.7129|96.3268|-0.386|-0.4%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.6972|12.7527|0.0555|0.44%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3405|14.3792|0.0386|0.27%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3039|20.3345|0.0306|0.15%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3632|14.3828|0.0197|0.14%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6057|20.6193|0.0137|0.07%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.4329|29.4147|-0.0183|-0.06%|

## 9 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|AlexNet_vaiq_int8|PASS|Numerics|
|alexnet_Opset18|PASS|Numerics|
|alexnet_Opset18_torch_hub|PASS|Numerics|
|sequencer2d_l_Opset17_timm|PASS|Numerics|
|sequencer2d_m_Opset16_timm|PASS|Numerics|
|sequencer2d_m_Opset17_timm|PASS|Numerics|
|sequencer2d_s_Opset16_timm|PASS|Numerics|
|squeezenet1.0-6|PASS|Numerics|
|squeezenet1_1_Opset17|PASS|Numerics|

## 3 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|ResNet34_vaiq|Numerics|PASS|
|sequencer2d_s_Opset17_timm|Numerics|PASS|
|t5-decoder-with-lm-head-12|native_inference|PASS|

