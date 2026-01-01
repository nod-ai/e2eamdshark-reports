# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|1531.9502|2008.6073|476.6571|31.11%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1510.7496|1937.4953|426.7458|28.25%|
|migraphx_ORT__distilgpt2_1|PASS|regression|620.794|1067.4318|446.6378|71.95%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|2230.0949|2810.4839|580.389|26.03%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|8577.7588|12895.8497|4318.0909|50.34%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|567.0965|695.655|128.5585|22.67%|
|migraphx_cadene__dpn92i1|PASS|regression|402.325|889.9303|487.6052|121.2%|
|migraphx_cadene__inceptionv4i16|PASS|regression|10126.4232|12659.549|2533.1258|25.02%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|804.2262|1292.0539|487.8277|60.66%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|7004.073|15435.1616|8431.0885|120.37%|
|migraphx_mlperf__resnet50_v1|PASS|regression|205.1754|438.797|233.6215|113.86%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|245.3015|394.4254|149.1239|60.79%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|732.6408|1631.1935|898.5526|122.65%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|50.0598|132.0175|81.9576|163.72%|
|migraphx_torchvision__densenet121i32|PASS|regression|5479.223|6801.0558|1321.8329|24.12%|
|migraphx_torchvision__inceptioni1|PASS|regression|368.0628|483.3626|115.2999|31.33%|
|migraphx_torchvision__resnet50i1|PASS|regression|219.7854|280.6963|60.9109|27.71%|

## 12 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset16|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset16|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset17|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset18|PASS|compiled_inference|
|migraphx_bert__bert-large-uncased|PASS|compiled_inference|
|migraphx_mlperf__bert_large_mlperf|Numerics|compiled_inference|
|migx_bench_bert-large-uncased_1_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_1_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_1_384|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_384|PASS|compiled_inference|

## No Progressions Found

