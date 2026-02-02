# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|1536.7092|1631.1848|94.4756|6.15%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1563.6987|1660.1295|96.4308|6.17%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|12686.5561|24699.281|12012.7249|94.69%|
|migraphx_ORT__distilgpt2_1|PASS|regression|723.8089|866.668|142.8591|19.74%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2494.0994|2513.6156|19.5162|0.78%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|10089.1428|7411.1645|-2677.9783|-26.54%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|643.16|563.3219|-79.8381|-12.41%|
|migraphx_cadene__dpn92i1|PASS|regression|439.1335|1040.0101|600.8766|136.83%|
|migraphx_cadene__inceptionv4i16|PASS|regression|8353.3471|12507.322|4153.9749|49.73%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|818.0605|1065.3922|247.3317|30.23%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|9926.9865|11767.871|1840.8845|18.54%|
|migraphx_mlperf__resnet50_v1|PASS|regression|194.9674|385.6434|190.676|97.8%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|295.3962|563.9932|268.597|90.93%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1058.9067|2418.2852|1359.3785|128.38%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|57.8116|178.5608|120.7492|208.87%|
|migraphx_pytorch-examples__wlang_lstm|PASS|regression|32.0503|45.3017|13.2513|41.35%|
|migraphx_torchvision__densenet121i32|PASS|regression|4889.6232|6895.2537|2005.6305|41.02%|
|migraphx_torchvision__inceptioni1|PASS|regression|359.9106|436.9137|77.0031|21.4%|
|migraphx_torchvision__resnet50i1|PASS|regression|200.9271|253.7962|52.8692|26.31%|

## 9 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 13 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|dm_nfnet_f0_Opset16|Numerics|PASS|
|dm_nfnet_f0_Opset17|Numerics|PASS|
|dm_nfnet_f1_Opset16|Numerics|PASS|
|dm_nfnet_f2_Opset16|Numerics|PASS|
|dm_nfnet_f2_Opset17|Numerics|PASS|
|tf_efficientnetv2_b0_Opset16|Numerics|PASS|
|tf_efficientnetv2_b0_Opset17|Numerics|PASS|
|tf_efficientnetv2_b1_Opset16|Numerics|PASS|
|tf_efficientnetv2_b1_Opset17|Numerics|PASS|
|tf_efficientnetv2_b2_Opset16|Numerics|PASS|
|tf_efficientnetv2_b2_Opset17|Numerics|PASS|
|tf_efficientnetv2_b3_Opset16|Numerics|PASS|
|tf_efficientnetv2_b3_Opset17|Numerics|PASS|

