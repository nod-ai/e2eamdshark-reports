# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|59.482|1557.995|1498.513|2519.27%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|58.8508|1531.2507|1472.3999|2501.92%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|194.5886|12156.7693|11962.1807|6147.42%|
|migraphx_ORT__distilgpt2_1|PASS|regression|19.7531|728.1169|708.3637|3586.09%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|99.8212|2459.7803|2359.9591|2364.19%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|304.0159|10390.2524|10086.2365|3317.67%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|18.4851|645.5473|627.0622|3392.26%|
|migraphx_cadene__dpn92i1|PASS|regression|200.3038|439.0865|238.7827|119.21%|
|migraphx_cadene__inceptionv4i16|PASS|regression|4166.3814|8764.5801|4598.1988|110.36%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|153.9349|814.5588|660.6239|429.16%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|154.3832|10087.8191|9933.4358|6434.27%|
|migraphx_mlperf__resnet50_v1|PASS|regression|84.7184|163.9984|79.28|93.58%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|26.7526|298.9922|272.2396|1017.62%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|38.9904|1238.4399|1199.4495|3076.27%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|34.4351|57.7299|23.2949|67.65%|
|migraphx_pytorch-examples__wlang_lstm|PASS|regression|18.3665|32.1522|13.7857|75.06%|
|migraphx_torchvision__densenet121i32|PASS|regression|417.3434|3563.2173|3145.8739|753.79%|
|migraphx_torchvision__inceptioni1|PASS|regression|166.9604|354.9996|188.0391|112.62%|
|migraphx_torchvision__resnet50i1|PASS|regression|156.5992|201.3967|44.7975|28.61%|

## 18 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|migx_bench_bert-large-uncased_16_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_16_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_16_384|Numerics|compiled_inference|
|migx_bench_bert-large-uncased_32_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_32_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_32_384|Numerics|compiled_inference|
|migx_bench_bert-large-uncased_4_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_4_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_4_384|PASS|compiled_inference|
|migx_bench_bert-large-uncased_8_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_8_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_8_384|PASS|compiled_inference|
|resnet50-v1-12-qdq|PASS|Numerics|
|t5_Opset16|PASS|Numerics|
|t5_Opset17|PASS|Numerics|
|xlmroberta_Opset16|PASS|Numerics|

## 8 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|flaubert_Opset16|Numerics|PASS|
|regnetx_002_Opset17_timm|compiled_inference|PASS|
|regnety_002_Opset16_timm|compiled_inference|PASS|
|regnetz_d8_evos_Opset16_timm|Numerics|PASS|
|t5_Opset17_transformers|Numerics|PASS|
|xception41p_Opset16_timm|compiled_inference|PASS|
|xception65p_Opset18_timm|compiled_inference|PASS|
|xlmroberta_Opset16_transformers|Numerics|PASS|

