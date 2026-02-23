# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|100.0904|100.1573|0.0669|0.07%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|100.0669|99.3947|-0.6722|-0.67%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|292.2382|293.6626|1.4243|0.49%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.3156|58.2308|0.9152|1.6%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|70.4742|70.8811|0.4069|0.58%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|287.6156|288.4484|0.8328|0.29%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|39.2464|39.3703|0.1239|0.32%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6995|12.6967|-0.0028|-0.02%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.9165|2.9413|0.0248|0.85%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|19.6194|19.6659|0.0465|0.24%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.3646|2.3637|-0.0009|-0.04%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2951|7.2705|-0.0246|-0.34%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.936|20.6517|0.7157|3.59%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0003|15.0023|0.002|0.01%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.7388|26.2679|-0.4709|-1.76%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.933|113.4864|0.5534|0.49%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.416|17.4372|0.0213|0.12%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.3736|3.3469|-0.0267|-0.79%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8795|1.8772|-0.0023|-0.12%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.3989|20.4473|0.0485|0.24%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.4086|33.5088|0.1001|0.3%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.4037|52.4146|0.0109|0.02%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8207|11.8658|0.045|0.38%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4872|12.4715|-0.0157|-0.13%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8974|12.9143|0.0169|0.13%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4506|12.5601|0.1095|0.88%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8561|12.8593|0.0031|0.02%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4712|14.5095|0.0383|0.26%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.1534|32.2145|0.0611|0.19%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.6395|62.6331|-0.0064|-0.01%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|96.5645|96.8174|0.2529|0.26%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7942|12.7869|-0.0072|-0.06%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3505|14.438|0.0876|0.61%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.438|20.4842|0.0462|0.23%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3871|14.444|0.0569|0.4%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6723|20.7787|0.1064|0.51%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.3792|29.3526|-0.0266|-0.09%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|

## One Progression Found:

|model name|old_status|new_status|
|---|---|---|
|esm_Opset16_transformers|setup|PASS|

