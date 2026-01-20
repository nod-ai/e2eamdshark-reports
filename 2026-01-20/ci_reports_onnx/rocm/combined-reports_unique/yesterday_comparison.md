# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|100.9462|101.2177|0.2714|0.27%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|286.8793|282.8731|-4.0062|-1.4%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.5762|57.8061|0.23|0.4%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.2903|71.8873|-0.403|-0.56%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.4163|285.8049|-0.6115|-0.21%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.8522|38.8023|-0.0499|-0.13%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.734|12.67|-0.064|-0.5%|
|migraphx_cadene__dpn92i1|Numerics|within tol|3.1397|3.1091|-0.0306|-0.97%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.197|20.076|-0.121|-0.6%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.4805|2.4803|-0.0002|-0.01%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2945|7.2402|-0.0543|-0.74%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|20.6656|19.779|-0.8866|-4.29%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1027|15.0855|-0.0172|-0.11%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.527|25.9129|-0.6142|-2.32%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|114.1607|112.6652|-1.4955|-1.31%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.6838|17.5916|-0.0922|-0.52%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.4956|3.4332|-0.0624|-1.78%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.9125|1.9044|-0.0081|-0.42%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.3274|20.2205|-0.1069|-0.53%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|34.078|32.9886|-1.0894|-3.2%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|53.5601|51.8741|-1.686|-3.15%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.803|11.8034|0.0004|0.0%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5757|12.4597|-0.116|-0.92%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.94|12.8131|-0.1269|-0.98%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4754|12.5021|0.0267|0.21%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8379|12.8048|-0.0331|-0.26%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4525|14.4132|-0.0392|-0.27%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.792|31.7576|-1.0344|-3.15%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|63.461|61.5332|-1.9278|-3.04%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|98.0755|95.2969|-2.7786|-2.83%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7561|12.6959|-0.0602|-0.47%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.4343|14.3389|-0.0954|-0.66%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3984|20.3203|-0.0781|-0.38%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.4038|14.3886|-0.0152|-0.11%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.649|20.5399|-0.1091|-0.53%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.8668|29.1145|-0.7523|-2.52%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|
|t5-decoder-with-lm-head-12|PASS|native_inference|

## No Progressions Found

