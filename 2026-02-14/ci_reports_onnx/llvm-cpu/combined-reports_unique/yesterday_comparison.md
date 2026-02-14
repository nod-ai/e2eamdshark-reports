# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1564.1408|1531.0751|-33.0657|-2.11%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1542.745|1498.4515|-44.2935|-2.87%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12481.4681|12318.1616|-163.3065|-1.31%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|745.6582|737.96|-7.6983|-1.03%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2475.8384|2471.561|-4.2774|-0.17%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|9930.1176|10109.9765|179.8589|1.81%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|626.1884|647.6955|21.5071|3.43%|
|migraphx_cadene__dpn92i1|PASS|within tol|440.645|440.5356|-0.1094|-0.02%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8808.6188|8768.4416|-40.1771|-0.46%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|810.5485|808.6799|-1.8686|-0.23%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10503.8937|10300.3301|-203.5636|-1.94%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|165.1387|164.9651|-0.1736|-0.11%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|299.992|296.1233|-3.8688|-1.29%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1416.3181|1549.4456|133.1274|9.4%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|58.2469|57.5234|-0.7234|-1.24%|
|migraphx_pytorch-examples__wlang_lstm|PASS|within tol|33.2865|32.1151|-1.1713|-3.52%|
|migraphx_torchvision__densenet121i32|PASS|within tol|3560.1576|3583.5535|23.3959|0.66%|
|migraphx_torchvision__inceptioni1|PASS|regression|358.075|395.4558|37.3808|10.44%|
|migraphx_torchvision__resnet50i1|PASS|within tol|197.458|195.729|-1.729|-0.88%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 6 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|RRDB_ESRGAN_vaiq_int8|compilation|Numerics|
|eva_large_patch14_336.in22k_ft_in1k|compiled_inference|PASS|
|maxvit_large_tf_512.in1k|compiled_inference|PASS|
|vit_large_patch16_384_Opset16|compiled_inference|PASS|
|vit_large_patch16_384_Opset17|compiled_inference|PASS|
|vit_large_patch16_384_Opset18|compiled_inference|PASS|

