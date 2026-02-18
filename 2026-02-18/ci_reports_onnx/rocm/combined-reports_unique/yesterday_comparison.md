# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|99.4585|99.6823|0.2239|0.23%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|99.4774|99.9973|0.5199|0.52%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|290.2603|290.2606|0.0003|0.0%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.2644|56.977|-0.2874|-0.5%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|70.5366|70.3648|-0.1718|-0.24%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|287.8295|287.1878|-0.6417|-0.22%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|39.0014|38.5148|-0.4866|-1.25%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.741|12.6847|-0.0563|-0.44%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.9038|2.9096|0.0058|0.2%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|19.6274|19.6234|-0.004|-0.02%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.3443|2.3557|0.0114|0.49%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2666|7.2335|-0.0331|-0.45%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.1118|19.3823|0.2705|1.42%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|14.9826|14.9833|0.0006|0.0%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8958|25.2154|-0.6805|-2.63%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.6899|112.5726|-0.1173|-0.1%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.3706|17.3217|-0.0489|-0.28%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.3202|3.3323|0.0121|0.36%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8683|1.8502|-0.018|-0.97%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.3574|20.3751|0.0177|0.09%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.1001|32.9118|-0.1883|-0.57%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.0063|51.6235|-0.3829|-0.74%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7636|11.7861|0.0225|0.19%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4865|12.4851|-0.0014|-0.01%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8936|12.8853|-0.0084|-0.06%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4515|12.5149|0.0634|0.51%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8455|12.8395|-0.006|-0.05%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4569|14.4332|-0.0237|-0.16%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.8454|31.6928|-0.1526|-0.48%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.5832|61.6282|0.0451|0.07%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|94.8011|95.1633|0.3622|0.38%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.677|12.7172|0.0403|0.32%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.4222|14.409|-0.0133|-0.09%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.4005|20.3972|-0.0032|-0.02%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.4159|14.3807|-0.0352|-0.24%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6976|20.6951|-0.0025|-0.01%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.0641|29.1217|0.0576|0.2%|

## No Regressions Found

## One Progression Found:

|model name|old_status|new_status|
|---|---|---|
|t5-decoder-with-lm-head-12|native_inference|PASS|

