# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|99.5525|99.8949|0.3423|0.34%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|99.7972|99.3439|-0.4533|-0.45%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|290.0691|293.2685|3.1994|1.1%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.3442|57.4727|0.1286|0.22%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|70.1934|70.6684|0.4751|0.68%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|287.9764|288.0876|0.1112|0.04%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.8426|38.9847|0.1421|0.37%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.7|12.7226|0.0226|0.18%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.9123|2.8998|-0.0125|-0.43%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|19.6434|19.6004|-0.043|-0.22%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.3538|2.3668|0.013|0.55%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2332|7.3076|0.0744|1.03%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.6167|20.2645|0.6478|3.3%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|14.9963|15.0148|0.0185|0.12%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.806|25.9171|0.1111|0.43%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.6654|113.6689|1.0034|0.89%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.3881|17.4321|0.044|0.25%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.3364|3.3811|0.0446|1.34%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8642|1.8741|0.0099|0.53%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.3561|20.4252|0.0691|0.34%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.1351|33.2483|0.1132|0.34%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.9266|52.2084|0.2818|0.54%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.785|11.8198|0.0348|0.3%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4837|12.5419|0.0582|0.47%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.9137|12.9632|0.0494|0.38%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4531|12.439|-0.0141|-0.11%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8444|12.8868|0.0424|0.33%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4518|14.4608|0.009|0.06%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.8972|31.9385|0.0413|0.13%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.9218|62.1761|0.2543|0.41%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.5165|96.0286|0.5121|0.54%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7685|12.7957|0.0272|0.21%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.4147|14.4354|0.0207|0.14%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3807|20.3876|0.0069|0.03%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.4033|14.4311|0.0278|0.19%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6833|20.7489|0.0657|0.32%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.2174|29.2772|0.0598|0.2%|

## No Regressions Found

## No Progressions Found

