# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|99.0011|99.2995|0.2984|0.3%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|292.2398|292.0947|-0.1451|-0.05%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.7768|57.9113|0.1345|0.23%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|70.5466|70.407|-0.1396|-0.2%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|287.4167|287.2483|-0.1684|-0.06%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|39.1094|39.0529|-0.0565|-0.14%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.7613|12.7759|0.0147|0.11%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.9519|2.9627|0.0108|0.37%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|19.8274|19.8084|-0.019|-0.1%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.3791|2.3892|0.0101|0.43%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2899|7.2733|-0.0165|-0.23%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|20.3866|20.4954|0.1088|0.53%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1743|15.1523|-0.022|-0.14%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.535|26.3851|-0.1499|-0.56%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|113.6315|113.7618|0.1303|0.11%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.4966|17.4422|-0.0544|-0.31%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.372|3.387|0.015|0.44%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8884|1.8826|-0.0057|-0.3%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.4031|20.4248|0.0217|0.11%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.1559|33.3341|0.1781|0.54%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.9452|52.2865|0.3413|0.66%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.892|11.8338|-0.0581|-0.49%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5831|12.5781|-0.0051|-0.04%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|13.015|12.9314|-0.0836|-0.64%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4953|12.5476|0.0523|0.42%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8693|12.8618|-0.0075|-0.06%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.5786|14.5307|-0.0479|-0.33%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.9007|32.021|0.1203|0.38%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.9815|62.2874|0.3059|0.49%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.7597|96.2034|0.4437|0.46%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.8561|12.8376|-0.0185|-0.14%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.5129|14.477|-0.0359|-0.25%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.4323|20.4562|0.024|0.12%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.4991|14.453|-0.0461|-0.32%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.7004|20.737|0.0366|0.18%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.2435|29.3087|0.0652|0.22%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 2 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|cs3darknet_focus_m_vaiq|Numerics|PASS|
|t5-decoder-with-lm-head-12|native_inference|PASS|

