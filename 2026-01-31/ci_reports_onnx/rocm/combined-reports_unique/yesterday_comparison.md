# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.5102|99.0011|-2.5091|-2.47%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|282.5672|292.2398|9.6726|3.42%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.7004|57.7768|0.0764|0.13%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.2049|70.5466|-1.6583|-2.3%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.1538|287.4167|1.263|0.44%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.8707|39.1094|0.2388|0.61%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6693|12.7613|0.092|0.73%|
|migraphx_cadene__dpn92i1|PASS|within tol|3.0625|2.9519|-0.1106|-3.61%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|19.9984|19.8274|-0.1709|-0.85%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.4631|2.3791|-0.084|-3.41%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2447|7.2899|0.0451|0.62%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.7585|20.3866|0.6281|3.18%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1281|15.1743|0.0462|0.31%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8102|26.535|0.7248|2.81%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.6447|113.6315|0.9868|0.88%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.5883|17.4966|-0.0917|-0.52%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.4071|3.372|-0.0352|-1.03%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8964|1.8884|-0.008|-0.42%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2737|20.4031|0.1294|0.64%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.989|33.1559|0.1669|0.51%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.7793|51.9452|0.1659|0.32%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7782|11.892|0.1137|0.97%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.511|12.5831|0.0721|0.58%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8956|13.015|0.1194|0.93%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.3791|12.4953|0.1162|0.94%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8217|12.8693|0.0475|0.37%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4098|14.5786|0.1688|1.17%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.7443|31.9007|0.1564|0.49%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.606|61.9815|0.3756|0.61%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.4121|95.7597|0.3476|0.36%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7263|12.8561|0.1297|1.02%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3758|14.5129|0.1372|0.95%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3195|20.4323|0.1128|0.55%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3866|14.4991|0.1125|0.78%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6094|20.7004|0.091|0.44%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.1041|29.2435|0.1393|0.48%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## One Progression Found:

|model name|old_status|new_status|
|---|---|---|
|dla60_res2net_vaiq|Numerics|PASS|

