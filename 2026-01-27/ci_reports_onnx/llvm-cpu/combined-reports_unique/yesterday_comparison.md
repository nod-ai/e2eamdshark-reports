# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|1396.2521|1553.1071|156.855|11.23%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1552.1987|1574.9518|22.7531|1.47%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12353.6958|12562.6251|208.9293|1.69%|
|migraphx_ORT__distilgpt2_1|PASS|regression|739.1835|789.6654|50.4819|6.83%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2467.9484|2431.7581|-36.1903|-1.47%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|10012.3254|8379.0526|-1633.2728|-16.31%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|678.3723|589.8358|-88.5365|-13.05%|
|migraphx_cadene__dpn92i1|PASS|regression|438.4495|463.1181|24.6686|5.63%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8851.5166|8978.7204|127.2038|1.44%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|822.0821|845.5736|23.4914|2.86%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10488.4946|10005.7121|-482.7825|-4.6%|
|migraphx_mlperf__resnet50_v1|PASS|regression|202.0378|217.6015|15.5637|7.7%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|293.4156|325.5798|32.1642|10.96%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|1292.7896|1165.8648|-126.9247|-9.82%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|55.9257|75.987|20.0613|35.87%|
|migraphx_pytorch-examples__wlang_lstm|PASS|regression|32.2031|54.5817|22.3785|69.49%|
|migraphx_torchvision__densenet121i32|PASS|regression|4809.499|5065.9845|256.4855|5.33%|
|migraphx_torchvision__inceptioni1|PASS|regression|350.5243|375.3602|24.8359|7.09%|
|migraphx_torchvision__resnet50i1|PASS|regression|194.108|207.343|13.235|6.82%|

## 7 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 4 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset16|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset16|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset18|compiled_inference|PASS|

