# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|100.6989|101.1638|0.4649|0.46%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|282.3085|286.4025|4.094|1.45%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.6294|58.1939|0.5645|0.98%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|71.8174|72.2721|0.4547|0.63%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|285.7505|286.2244|0.474|0.17%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.8225|38.9633|0.1408|0.36%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.686|12.7018|0.0157|0.12%|
|migraphx_cadene__dpn92i1|Numerics|within tol|3.1085|3.1447|0.0363|1.17%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.1345|20.2085|0.074|0.37%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.4753|2.5082|0.0329|1.33%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2463|7.2924|0.0461|0.64%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.7742|20.534|0.7599|3.84%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1044|15.1531|0.0487|0.32%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8874|26.5793|0.6919|2.67%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|113.0416|114.2438|1.2021|1.06%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.6229|17.6514|0.0284|0.16%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.4377|3.4744|0.0367|1.07%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.9043|1.9194|0.0151|0.79%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2806|20.2888|0.0083|0.04%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.1145|34.0365|0.9219|2.78%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.0303|53.5103|1.48|2.84%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7943|11.8445|0.0502|0.43%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5332|12.5061|-0.0271|-0.22%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8927|12.9046|0.0119|0.09%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4165|12.4498|0.0333|0.27%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7881|12.8422|0.0541|0.42%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4521|14.4866|0.0345|0.24%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.8574|32.8016|0.9442|2.96%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.8907|63.3542|1.4635|2.36%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.9698|98.2976|2.3278|2.43%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.738|12.7621|0.0242|0.19%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3929|14.3852|-0.0077|-0.05%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3245|20.3322|0.0077|0.04%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3947|14.374|-0.0207|-0.14%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5748|20.5862|0.0114|0.06%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.127|29.8492|0.7223|2.48%|

## No Regressions Found

## 8 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|nf_regnet_b1_Opset16|compilation|Numerics|
|nf_regnet_b1_Opset16_timm|compilation|Numerics|
|nf_regnet_b1_Opset17|compilation|Numerics|
|repvgg_b3g4_Opset16|compilation|PASS|
|repvgg_b3g4_Opset16_timm|compilation|PASS|
|repvgg_b3g4_Opset17|compilation|PASS|
|repvgg_b3g4_Opset18|compilation|PASS|
|t5-decoder-with-lm-head-12|native_inference|PASS|

