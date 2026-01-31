# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1470.6428|1536.7092|66.0663|4.49%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1561.5465|1563.6987|2.1522|0.14%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12410.1472|12686.5561|276.409|2.23%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|714.2068|723.8089|9.6021|1.34%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2448.149|2494.0994|45.9504|1.88%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|9771.6172|10089.1428|317.5256|3.25%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|662.6366|643.16|-19.4766|-2.94%|
|migraphx_cadene__dpn92i1|PASS|within tol|433.9049|439.1335|5.2286|1.21%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8346.4987|8353.3471|6.8484|0.08%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|810.8561|818.0605|7.2044|0.89%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10322.431|9926.9865|-395.4445|-3.83%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|192.6873|194.9674|2.2801|1.18%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|292.7868|295.3962|2.6094|0.89%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1094.1743|1058.9067|-35.2676|-3.22%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|56.5281|57.8116|1.2835|2.27%|
|migraphx_pytorch-examples__wlang_lstm|PASS|within tol|32.2507|32.0503|-0.2003|-0.62%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4829.1118|4889.6232|60.5115|1.25%|
|migraphx_torchvision__inceptioni1|PASS|within tol|349.0585|359.9106|10.8521|3.11%|
|migraphx_torchvision__resnet50i1|PASS|within tol|196.1677|200.9271|4.7594|2.43%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset17|PASS|compiled_inference|
|deit3_large_patch16_384_Opset18|PASS|compiled_inference|

## No Progressions Found

