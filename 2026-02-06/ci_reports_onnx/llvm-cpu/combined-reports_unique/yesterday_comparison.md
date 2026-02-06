# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|1557.995|1652.0766|94.0815|6.04%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1531.2507|1614.7642|83.5135|5.45%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|12156.7693|24664.8197|12508.0504|102.89%|
|migraphx_ORT__distilgpt2_1|PASS|regression|728.1169|856.4805|128.3636|17.63%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2459.7803|2539.1315|79.3512|3.23%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|10390.2524|7368.2327|-3022.0197|-29.09%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|645.5473|561.7193|-83.828|-12.99%|
|migraphx_cadene__dpn92i1|PASS|regression|439.0865|1043.0583|603.9718|137.55%|
|migraphx_cadene__inceptionv4i16|PASS|regression|8764.5801|16394.06|7629.4798|87.05%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|814.5588|1045.4949|230.9361|28.35%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|10087.8191|11638.3671|1550.5481|15.37%|
|migraphx_mlperf__resnet50_v1|PASS|regression|163.9984|451.5819|287.5835|175.36%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|298.9922|604.0575|305.0654|102.03%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1238.4399|2337.259|1098.8191|88.73%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|57.7299|185.4896|127.7597|221.31%|
|migraphx_pytorch-examples__wlang_lstm|PASS|regression|32.1522|44.7311|12.5789|39.12%|
|migraphx_torchvision__densenet121i32|PASS|regression|3563.2173|6722.048|3158.8307|88.65%|
|migraphx_torchvision__inceptioni1|PASS|regression|354.9996|436.7604|81.7608|23.03%|
|migraphx_torchvision__resnet50i1|PASS|regression|201.3967|251.36|49.9633|24.81%|

## 12 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|regnetz_d8_evos_Opset16_timm|PASS|Numerics|
|t5_Opset17_transformers|PASS|Numerics|
|xlmroberta_Opset16_transformers|PASS|Numerics|

## 10 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|dm_nfnet_f0_Opset16|Numerics|PASS|
|dm_nfnet_f0_Opset17|Numerics|PASS|
|dm_nfnet_f1_Opset16|Numerics|PASS|
|dm_nfnet_f2_Opset16|Numerics|PASS|
|dm_nfnet_f2_Opset17|Numerics|PASS|
|fcn-resnet101-11|Numerics|PASS|
|fcn-resnet50-11|Numerics|PASS|
|fcn-resnet50-12|Numerics|PASS|
|flaubert_Opset16_transformers|Numerics|PASS|
|xception65_Opset18_timm|compiled_inference|PASS|

