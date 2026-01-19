# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1588.9739|1610.9442|21.9703|1.38%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1403.5414|1447.3939|43.8525|3.12%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12470.5519|12446.5602|-23.9917|-0.19%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|726.4706|729.3772|2.9065|0.4%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2524.3074|2508.789|-15.5184|-0.61%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|10424.4509|10018.537|-405.9139|-3.89%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|655.1709|653.1028|-2.0681|-0.32%|
|migraphx_cadene__dpn92i1|Numerics|within tol|430.8091|436.59|5.7808|1.34%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8843.7884|8880.6809|36.8925|0.42%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|814.8585|825.7871|10.9286|1.34%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|9858.1044|10164.6293|306.5249|3.11%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|201.7499|208.8736|7.1238|3.53%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|289.3993|299.0157|9.6164|3.32%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1030.8743|1078.0304|47.1561|4.57%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|58.7158|56.1748|-2.5409|-4.33%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4750.0307|4855.4627|105.432|2.22%|
|migraphx_torchvision__inceptioni1|PASS|within tol|344.1211|356.3414|12.2203|3.55%|
|migraphx_torchvision__resnet50i1|PASS|within tol|194.8629|199.0866|4.2236|2.17%|

## No Regressions Found

## 3 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|model--albert-xxl-v2-finetuned-squad--anas-awadalla|compiled_inference|PASS|
|resnet50_gn_vaiq|Numerics|PASS|
|resnetv2_50d_gn.ah_in1k_vaiq|Numerics|PASS|

