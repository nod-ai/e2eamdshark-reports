# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|99.8949|99.4585|-0.4364|-0.44%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|99.3439|99.4774|0.1335|0.13%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|293.2685|290.2603|-3.0083|-1.03%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.4727|57.2644|-0.2083|-0.36%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|70.6684|70.5366|-0.1318|-0.19%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|288.0876|287.8295|-0.2581|-0.09%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.9847|39.0014|0.0166|0.04%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.7226|12.741|0.0184|0.14%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.8998|2.9038|0.004|0.14%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|19.6004|19.6274|0.0271|0.14%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.3668|2.3443|-0.0225|-0.95%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.3076|7.2666|-0.0411|-0.56%|
|migraphx_mlperf__bert_large_mlperf|Numerics|progression|20.2645|19.1118|-1.1527|-5.69%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0148|14.9826|-0.0321|-0.21%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.9171|25.8958|-0.0213|-0.08%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|113.6689|112.6899|-0.979|-0.86%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.4321|17.3706|-0.0615|-0.35%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.3811|3.3202|-0.0609|-1.8%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8741|1.8683|-0.0058|-0.31%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.4252|20.3574|-0.0678|-0.33%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.2483|33.1001|-0.1483|-0.45%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.2084|52.0063|-0.2021|-0.39%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8198|11.7636|-0.0561|-0.47%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5419|12.4865|-0.0554|-0.44%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.9632|12.8936|-0.0695|-0.54%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.439|12.4515|0.0125|0.1%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8868|12.8455|-0.0413|-0.32%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4608|14.4569|-0.004|-0.03%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.9385|31.8454|-0.0932|-0.29%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.1761|61.5832|-0.5929|-0.95%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|96.0286|94.8011|-1.2274|-1.28%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7957|12.677|-0.1188|-0.93%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.4354|14.4222|-0.0132|-0.09%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3876|20.4005|0.0129|0.06%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.4311|14.4159|-0.0152|-0.11%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.7489|20.6976|-0.0513|-0.25%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.2772|29.0641|-0.213|-0.73%|

## No Regressions Found

## No Progressions Found

