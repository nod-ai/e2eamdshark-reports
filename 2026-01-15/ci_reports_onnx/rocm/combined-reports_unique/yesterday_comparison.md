# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|100.9468|100.6267|-0.3201|-0.32%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|283.0463|283.0087|-0.0376|-0.01%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.7047|57.5936|-0.1111|-0.19%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|71.8353|72.0095|0.1742|0.24%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|285.3326|285.7729|0.4403|0.15%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.7834|38.4564|-0.327|-0.84%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6189|12.6338|0.0149|0.12%|
|migraphx_cadene__dpn92i1|Numerics|within tol|3.1013|3.1013|0.0|0.0%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.0826|20.0825|-0.0|-0.0%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.4787|2.4543|-0.0244|-0.98%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2334|7.223|-0.0104|-0.14%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.7318|19.328|-0.4037|-2.05%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0703|15.0678|-0.0024|-0.02%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.0645|25.1235|0.059|0.24%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.5587|112.4932|-0.0655|-0.06%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.5661|17.5142|-0.0519|-0.3%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.4352|3.4286|-0.0066|-0.19%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.9033|1.899|-0.0043|-0.23%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2299|20.2083|-0.0216|-0.11%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.8482|32.8096|-0.0386|-0.12%|
|migx_bench_bert-large-uncased_16_384|Numerics|within tol|51.5375|51.5148|-0.0227|-0.04%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7956|11.7809|-0.0148|-0.13%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5049|12.5092|0.0043|0.03%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8387|12.81|-0.0287|-0.22%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4068|12.3991|-0.0077|-0.06%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7631|12.7955|0.0325|0.25%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.386|14.3526|-0.0334|-0.23%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.632|31.6711|0.0391|0.12%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.3075|61.3308|0.0233|0.04%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.0262|95.0362|0.01|0.01%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7273|12.6976|-0.0296|-0.23%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3449|14.3671|0.0222|0.15%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3027|20.3019|-0.0008|-0.0%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3504|14.386|0.0355|0.25%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5328|20.5504|0.0176|0.09%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|28.9978|29.0199|0.0221|0.08%|

## No Regressions Found

## No Progressions Found

