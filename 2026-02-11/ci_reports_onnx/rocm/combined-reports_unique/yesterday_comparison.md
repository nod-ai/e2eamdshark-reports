# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|99.1428|99.5626|0.4198|0.42%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|99.5796|99.6166|0.0369|0.04%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|290.2472|292.7853|2.5381|0.87%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.3226|57.3287|0.0061|0.01%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|70.2704|70.6721|0.4017|0.57%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|287.7479|288.2355|0.4876|0.17%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.9166|38.6902|-0.2264|-0.58%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.7247|12.6922|-0.0325|-0.26%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.9167|2.9091|-0.0076|-0.26%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|19.644|19.6545|0.0105|0.05%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.3354|2.3535|0.0181|0.77%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2311|7.2443|0.0133|0.18%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.7298|19.589|-0.1408|-0.71%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|14.886|14.901|0.015|0.1%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8704|25.8755|0.0051|0.02%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.7107|112.9479|0.2372|0.21%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.394|17.4279|0.0339|0.2%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.3341|3.329|-0.0051|-0.15%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8552|1.8535|-0.0017|-0.09%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.366|20.405|0.0389|0.19%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.2495|33.877|0.6276|1.89%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.0967|53.1341|1.0374|1.99%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7966|11.792|-0.0046|-0.04%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.538|12.5361|-0.0019|-0.02%|
|migx_bench_bert-large-uncased_1_384|PASS|regression|12.9067|24.389|11.4823|88.96%|
|migx_bench_bert-large-uncased_2_128|PASS|regression|12.4339|29.4752|17.0413|137.05%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8081|12.768|-0.0401|-0.31%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4691|14.4497|-0.0194|-0.13%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.9668|32.5954|0.6286|1.97%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.0671|62.8399|0.7728|1.25%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.6584|97.1362|1.4778|1.54%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7474|12.7203|-0.0272|-0.21%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3947|14.3783|-0.0164|-0.11%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3574|20.4355|0.0781|0.38%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.403|14.3867|-0.0163|-0.11%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6813|20.7521|0.0707|0.34%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.208|29.6535|0.4455|1.53%|

## No Regressions Found

## No Progressions Found

