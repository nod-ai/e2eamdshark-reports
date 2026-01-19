# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.1638|100.9462|-0.2176|-0.22%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|286.4025|286.8793|0.4768|0.17%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|58.1939|57.5762|-0.6178|-1.06%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.2721|72.2903|0.0182|0.03%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.2244|286.4163|0.1919|0.07%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.9633|38.8522|-0.1111|-0.29%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.7018|12.734|0.0322|0.25%|
|migraphx_cadene__dpn92i1|Numerics|within tol|3.1447|3.1397|-0.005|-0.16%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.2085|20.197|-0.0116|-0.06%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.5082|2.4805|-0.0276|-1.1%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2924|7.2945|0.0021|0.03%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|20.534|20.6656|0.1315|0.64%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1531|15.1027|-0.0504|-0.33%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.5793|26.527|-0.0522|-0.2%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|114.2438|114.1607|-0.083|-0.07%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.6514|17.6838|0.0324|0.18%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.4744|3.4956|0.0211|0.61%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.9194|1.9125|-0.0069|-0.36%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2888|20.3274|0.0386|0.19%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|34.0365|34.078|0.0416|0.12%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|53.5103|53.5601|0.0498|0.09%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8445|11.803|-0.0414|-0.35%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5061|12.5757|0.0696|0.56%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.9046|12.94|0.0354|0.27%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4498|12.4754|0.0256|0.21%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8422|12.8379|-0.0043|-0.03%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4866|14.4525|-0.0342|-0.24%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.8016|32.792|-0.0096|-0.03%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|63.3542|63.461|0.1068|0.17%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|98.2976|98.0755|-0.222|-0.23%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7621|12.7561|-0.006|-0.05%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3852|14.4343|0.0491|0.34%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3322|20.3984|0.0662|0.33%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.374|14.4038|0.0298|0.21%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5862|20.649|0.0628|0.31%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.8492|29.8668|0.0176|0.06%|

## No Regressions Found

## No Progressions Found

