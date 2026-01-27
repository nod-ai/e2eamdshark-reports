# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.6694|100.6265|-1.0429|-1.03%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|284.0801|282.167|-1.9131|-0.67%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.7919|57.3743|-0.4176|-0.72%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.332|72.1081|-0.2239|-0.31%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.6351|285.9409|-0.6942|-0.24%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.7941|38.8128|0.0187|0.05%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6963|12.634|-0.0623|-0.49%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.9896|2.989|-0.0006|-0.02%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.0296|19.9561|-0.0735|-0.37%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.4467|2.4573|0.0106|0.43%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.257|7.2371|-0.0198|-0.27%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.3972|19.7029|0.3057|1.58%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.3861|15.2963|-0.0898|-0.58%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8731|25.22|-0.6531|-2.52%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.9615|112.3907|-0.5709|-0.51%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.5857|17.5462|-0.0394|-0.22%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.3982|3.3948|-0.0034|-0.1%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8962|1.8958|-0.0004|-0.02%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.3303|20.1829|-0.1474|-0.72%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.1987|32.9879|-0.2108|-0.63%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.1754|51.8757|-0.2996|-0.57%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8104|11.7804|-0.0299|-0.25%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4994|12.4774|-0.022|-0.18%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8596|12.8384|-0.0213|-0.17%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4117|12.4009|-0.0108|-0.09%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8067|12.7719|-0.0348|-0.27%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4311|14.4166|-0.0145|-0.1%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.0879|31.7334|-0.3545|-1.1%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.1118|61.564|-0.5478|-0.88%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|96.3185|95.604|-0.7145|-0.74%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7325|12.6942|-0.0383|-0.3%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3852|14.3671|-0.0181|-0.13%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3601|20.2906|-0.0695|-0.34%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.4129|14.3516|-0.0613|-0.43%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.623|20.5739|-0.0491|-0.24%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.2362|29.1105|-0.1258|-0.43%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|
|t5-decoder-with-lm-head-12|PASS|native_inference|

## No Progressions Found

