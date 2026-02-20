# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|99.6823|100.0904|0.4081|0.41%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|99.9973|100.0669|0.0696|0.07%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|290.2606|292.2382|1.9777|0.68%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|56.977|57.3156|0.3385|0.59%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|70.3648|70.4742|0.1094|0.16%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|287.1878|287.6156|0.4278|0.15%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.5148|39.2464|0.7316|1.9%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6847|12.6995|0.0149|0.12%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.9096|2.9165|0.0069|0.24%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|19.6234|19.6194|-0.004|-0.02%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.3557|2.3646|0.0089|0.38%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2335|7.2951|0.0616|0.85%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.3823|19.936|0.5537|2.86%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|14.9833|15.0003|0.017|0.11%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|25.2154|26.7388|1.5234|6.04%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.5726|112.933|0.3604|0.32%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.3217|17.416|0.0943|0.54%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.3323|3.3736|0.0413|1.24%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8502|1.8795|0.0293|1.58%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.3751|20.3989|0.0238|0.12%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.9118|33.4086|0.4969|1.51%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.6235|52.4037|0.7803|1.51%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7861|11.8207|0.0346|0.29%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4851|12.4872|0.0021|0.02%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8853|12.8974|0.0121|0.09%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.5149|12.4506|-0.0643|-0.51%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8395|12.8561|0.0167|0.13%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4332|14.4712|0.038|0.26%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.6928|32.1534|0.4606|1.45%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.6282|62.6395|1.0113|1.64%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.1633|96.5645|1.4012|1.47%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7172|12.7942|0.0769|0.61%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.409|14.3505|-0.0585|-0.41%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3972|20.438|0.0408|0.2%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3807|14.3871|0.0064|0.04%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6951|20.6723|-0.0228|-0.11%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.1217|29.3792|0.2575|0.88%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|esm_Opset16_transformers|PASS|setup|
|t5-decoder-with-lm-head-12|PASS|native_inference|

## No Progressions Found

