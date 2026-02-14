# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|99.9323|99.5525|-0.3798|-0.38%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|99.7328|99.7972|0.0644|0.06%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|294.6554|290.0691|-4.5863|-1.56%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.7035|57.3442|-0.3593|-0.62%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|70.816|70.1934|-0.6226|-0.88%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|288.3156|287.9764|-0.3392|-0.12%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|39.4356|38.8426|-0.593|-1.5%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.736|12.7|-0.036|-0.28%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.9524|2.9123|-0.0401|-1.36%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|19.6924|19.6434|-0.0491|-0.25%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.3907|2.3538|-0.037|-1.55%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.3219|7.2332|-0.0887|-1.21%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|20.6123|19.6167|-0.9956|-4.83%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0136|14.9963|-0.0173|-0.12%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.6423|25.806|-0.8363|-3.14%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|113.3752|112.6654|-0.7098|-0.63%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.4128|17.3881|-0.0247|-0.14%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.3171|3.3364|0.0193|0.58%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8737|1.8642|-0.0095|-0.51%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.3694|20.3561|-0.0133|-0.07%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.3811|33.1351|-0.246|-0.74%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.4232|51.9266|-0.4966|-0.95%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8622|11.785|-0.0772|-0.65%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5079|12.4837|-0.0242|-0.19%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.922|12.9137|-0.0082|-0.06%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.5185|12.4531|-0.0654|-0.52%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8776|12.8444|-0.0332|-0.26%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.5123|14.4518|-0.0605|-0.42%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.893|31.8972|0.0042|0.01%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.1727|61.9218|-0.2509|-0.4%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|96.1582|95.5165|-0.6417|-0.67%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7974|12.7685|-0.0289|-0.23%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.437|14.4147|-0.0223|-0.15%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.4607|20.3807|-0.0801|-0.39%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.4119|14.4033|-0.0086|-0.06%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.7901|20.6833|-0.1069|-0.51%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.357|29.2174|-0.1397|-0.48%|

## No Regressions Found

## No Progressions Found

