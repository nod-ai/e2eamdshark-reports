# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|99.4181|99.9323|0.5141|0.52%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|99.3549|99.7328|0.3779|0.38%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|290.7916|294.6554|3.8638|1.33%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.1321|57.7035|0.5714|1.0%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|70.5927|70.816|0.2233|0.32%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|287.3033|288.3156|1.0123|0.35%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.8813|39.4356|0.5543|1.43%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6843|12.736|0.0516|0.41%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.9082|2.9524|0.0442|1.52%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|19.6081|19.6924|0.0843|0.43%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.3522|2.3907|0.0386|1.64%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2563|7.3219|0.0656|0.9%|
|migraphx_mlperf__bert_large_mlperf|Numerics|regression|19.6156|20.6123|0.9967|5.08%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|14.8981|15.0136|0.1155|0.78%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.4649|26.6423|1.1775|4.62%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.4255|113.3752|0.9497|0.84%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.3609|17.4128|0.0519|0.3%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.3014|3.3171|0.0157|0.48%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8599|1.8737|0.0138|0.74%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.347|20.3694|0.0224|0.11%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.0607|33.3811|0.3204|0.97%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.8357|52.4232|0.5875|1.13%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7346|11.8622|0.1276|1.09%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4687|12.5079|0.0393|0.31%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8747|12.922|0.0473|0.37%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4024|12.5185|0.1161|0.94%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8251|12.8776|0.0525|0.41%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4612|14.5123|0.0512|0.35%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.8031|31.893|0.0899|0.28%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.9361|62.1727|0.2367|0.38%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.6855|96.1582|0.4727|0.49%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7241|12.7974|0.0732|0.58%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3802|14.437|0.0568|0.4%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.4113|20.4607|0.0495|0.24%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3849|14.4119|0.027|0.19%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.7196|20.7901|0.0705|0.34%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.1804|29.357|0.1767|0.61%|

## No Regressions Found

## No Progressions Found

