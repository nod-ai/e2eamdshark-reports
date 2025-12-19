# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.115|101.9597|0.8446|0.84%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|285.1791|284.289|-0.8901|-0.31%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.7591|57.4163|-0.3429|-0.59%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|75.5473|75.5444|-0.003|-0.0%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|295.239|294.7195|-0.5195|-0.18%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|40.1991|40.3183|0.1192|0.3%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6086|12.6355|0.0268|0.21%|
|migraphx_cadene__dpn92i1|Numerics|within tol|10.0989|9.9095|-0.1894|-1.88%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.9672|21.9033|-0.0639|-0.29%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.0458|6.0859|0.04|0.66%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2165|7.2333|0.0168|0.23%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.6668|19.503|-0.1638|-0.83%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0856|15.0851|-0.0004|-0.0%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.0822|25.7492|-0.3329|-1.28%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.9078|112.8573|-0.0506|-0.04%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|14.5949|14.4334|-0.1615|-1.11%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.7373|17.7455|0.0082|0.05%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6584|4.6376|-0.0208|-0.45%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.6949|3.6872|-0.0077|-0.21%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2847|20.2951|0.0105|0.05%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.3187|33.2121|-0.1066|-0.32%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.2661|52.0397|-0.2264|-0.43%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.795|11.7932|-0.0017|-0.01%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.49|12.4719|-0.0182|-0.15%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8445|12.8658|0.0213|0.17%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.3902|12.4083|0.0181|0.15%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8253|12.7663|-0.059|-0.46%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4289|14.3831|-0.0458|-0.32%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.0723|31.9751|-0.0972|-0.3%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.1197|62.2351|0.1154|0.19%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|96.1747|95.971|-0.2037|-0.21%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7101|12.7199|0.0098|0.08%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.4056|14.3932|-0.0124|-0.09%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3113|20.3007|-0.0107|-0.05%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3746|14.3908|0.0163|0.11%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5733|20.5852|0.0119|0.06%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.2104|29.1944|-0.016|-0.05%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|
|sequencer2d_s_Opset16|PASS|Numerics|

## 10 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|AlexNet_vaiq_int8|Numerics|PASS|
|ResNet18_vaiq|Numerics|PASS|
|ResNet34_vaiq|Numerics|PASS|
|alexnet_Opset18|Numerics|PASS|
|coatnet_2_rw_224.sw_in12k|compilation|PASS|
|sequencer2d_l_Opset16_timm|Numerics|PASS|
|squeezenet1.1-7|Numerics|PASS|
|swin_base_patch4_window12_384_in22k_Opset17_timm|compilation|PASS|
|xcit_small_12_p8_384_dist_Opset16_timm|compiled_inference|Numerics|
|xcit_small_24_p8_384_dist_Opset16_timm|compiled_inference|Numerics|

