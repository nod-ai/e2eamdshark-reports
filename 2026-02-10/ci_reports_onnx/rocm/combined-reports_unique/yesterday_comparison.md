# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|98.7676|99.1428|0.3752|0.38%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|99.6347|99.5796|-0.055|-0.06%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|289.1901|290.2472|1.0571|0.37%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.3403|57.3226|-0.0177|-0.03%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|70.3314|70.2704|-0.061|-0.09%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|287.6684|287.7479|0.0795|0.03%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.7049|38.9166|0.2117|0.55%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6668|12.7247|0.0579|0.46%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.8941|2.9167|0.0226|0.78%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|19.5912|19.644|0.0528|0.27%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.3282|2.3354|0.0072|0.31%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2204|7.2311|0.0106|0.15%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.327|19.7298|0.4028|2.08%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|14.8445|14.886|0.0415|0.28%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.5261|25.8704|0.3443|1.35%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.3281|112.7107|0.3826|0.34%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.2955|17.394|0.0985|0.57%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.3278|3.3341|0.0062|0.19%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.861|1.8552|-0.0058|-0.31%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.3207|20.366|0.0453|0.22%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.2309|33.2495|0.0186|0.06%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.1802|52.0967|-0.0835|-0.16%|
|migx_bench_bert-large-uncased_1_128|PASS|progression|13.338|11.7966|-1.5414|-11.56%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4345|12.538|0.1035|0.83%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8774|12.9067|0.0293|0.23%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4872|12.4339|-0.0532|-0.43%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7885|12.8081|0.0197|0.15%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4603|14.4691|0.0088|0.06%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.9604|31.9668|0.0065|0.02%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.227|62.0671|-0.1599|-0.26%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.9753|95.6584|-0.317|-0.33%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7017|12.7474|0.0457|0.36%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.41|14.3947|-0.0153|-0.11%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3743|20.3574|-0.0169|-0.08%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3869|14.403|0.0162|0.11%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6627|20.6813|0.0186|0.09%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.1968|29.208|0.0112|0.04%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|

## 5 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|res2net50_26w_4s_Opset16_timm|setup|PASS|
|tf_efficientnet_b5_Opset16_timm|setup|PASS|
|tf_mixnet_s_Opset16_timm|setup|PASS|
|twins_svt_base_Opset17_timm|setup|PASS|
|xcit_tiny_24_p16_224_dist_Opset16_timm|setup|PASS|

