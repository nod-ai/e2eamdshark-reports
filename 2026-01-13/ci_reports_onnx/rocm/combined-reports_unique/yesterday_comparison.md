# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|100.9585|100.4891|-0.4694|-0.46%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|284.081|282.7743|-1.3067|-0.46%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.477|58.1723|0.6953|1.21%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.0148|72.044|0.0293|0.04%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.3314|285.7104|-0.6211|-0.22%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.6517|38.7413|0.0896|0.23%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6263|12.6314|0.0051|0.04%|
|migraphx_cadene__dpn92i1|PASS|within tol|9.8452|9.6819|-0.1634|-1.66%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.1507|20.1166|-0.0341|-0.17%|
|migraphx_cadene__resnext101_64x4di1|Numerics|within tol|3.3189|3.3174|-0.0014|-0.04%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2407|7.2363|-0.0044|-0.06%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.6949|19.8524|0.1575|0.8%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1148|15.1172|0.0024|0.02%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8644|25.2642|-0.6002|-2.32%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.9216|112.8722|-0.0494|-0.04%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|14.7369|14.2556|-0.4813|-3.27%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.608|17.6077|-0.0003|-0.0%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.4409|3.4325|-0.0084|-0.24%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.9064|1.9037|-0.0027|-0.14%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2416|20.2727|0.0311|0.15%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.2705|32.8424|-0.4281|-1.29%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.09|51.5617|-0.5283|-1.01%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7693|11.7709|0.0016|0.01%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4676|12.4931|0.0255|0.2%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8443|12.8163|-0.028|-0.22%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4254|12.4719|0.0466|0.37%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8236|12.7244|-0.0992|-0.77%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4171|14.3503|-0.0669|-0.46%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.017|31.6717|-0.3453|-1.08%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.0724|61.4305|-0.6419|-1.03%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|96.0893|95.0823|-1.0069|-1.05%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7418|12.7321|-0.0097|-0.08%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.401|14.3906|-0.0104|-0.07%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3068|20.2862|-0.0207|-0.1%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3918|14.3888|-0.003|-0.02%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5925|20.5897|-0.0027|-0.01%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.2397|29.0039|-0.2358|-0.81%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|
|t5-decoder-with-lm-head-12|PASS|native_inference|

## 2 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|efficientformerv2_s0.snap_dist_in1k|compiled_inference|PASS|
|tf_efficientnetv2_b1.in1k_vaiq|Numerics|PASS|

