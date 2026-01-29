# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|100.9819|101.5102|0.5283|0.52%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|282.329|282.5672|0.2382|0.08%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.6046|57.7004|0.0958|0.17%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|71.8512|72.2049|0.3537|0.49%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.046|286.1538|0.1078|0.04%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.8294|38.8707|0.0413|0.11%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.707|12.6693|-0.0377|-0.3%|
|migraphx_cadene__dpn92i1|PASS|within tol|3.0367|3.0625|0.0258|0.85%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.0271|19.9984|-0.0287|-0.14%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.4521|2.4631|0.011|0.45%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2633|7.2447|-0.0185|-0.25%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.7456|19.7585|0.0129|0.07%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.3767|15.1281|-0.2486|-1.62%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.5946|25.8102|0.2156|0.84%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.8623|112.6447|-0.2176|-0.19%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.5772|17.5883|0.0111|0.06%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.3997|3.4071|0.0074|0.22%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.9052|1.8964|-0.0087|-0.46%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2998|20.2737|-0.0261|-0.13%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.7904|32.989|0.1986|0.61%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.5342|51.7793|0.2452|0.48%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8096|11.7782|-0.0314|-0.27%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5107|12.511|0.0003|0.0%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.9016|12.8956|-0.006|-0.05%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.5162|12.3791|-0.1372|-1.1%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.812|12.8217|0.0097|0.08%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4432|14.4098|-0.0334|-0.23%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.4204|31.7443|0.3239|1.03%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|60.9276|61.606|0.6784|1.11%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|94.5665|95.4121|0.8456|0.89%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7479|12.7263|-0.0215|-0.17%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3863|14.3758|-0.0105|-0.07%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3697|20.3195|-0.0502|-0.25%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3849|14.3866|0.0016|0.01%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5845|20.6094|0.0249|0.12%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.0521|29.1041|0.052|0.18%|

## No Regressions Found

## No Progressions Found

