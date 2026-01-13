# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1458.8858|1426.8661|-32.0198|-2.19%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1545.996|1417.5025|-128.4935|-8.31%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12238.7489|12673.8165|435.0676|3.55%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|713.6446|723.9587|10.3141|1.45%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2497.2218|2469.4943|-27.7275|-1.11%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|10295.4406|9821.1062|-474.3344|-4.61%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|632.3807|650.3727|17.992|2.85%|
|migraphx_cadene__dpn92i1|PASS|within tol|439.092|440.4548|1.3628|0.31%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8886.3263|8867.9911|-18.3352|-0.21%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|814.2217|823.8919|9.6702|1.19%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10379.8801|10052.989|-326.8911|-3.15%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|202.8334|204.3217|1.4883|0.73%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|292.565|300.5639|7.9989|2.73%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1069.2037|1193.2067|124.003|11.6%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|56.5859|57.5893|1.0035|1.77%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4771.6044|4787.8211|16.2166|0.34%|
|migraphx_torchvision__inceptioni1|PASS|within tol|365.135|356.7975|-8.3375|-2.28%|
|migraphx_torchvision__resnet50i1|PASS|within tol|195.0802|194.6869|-0.3932|-0.2%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|
|flaubert_Opset16_transformers|PASS|Numerics|

## 2 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|t5_Opset17_transformers|Numerics|PASS|
|xlmroberta_Opset16_transformers|Numerics|PASS|

