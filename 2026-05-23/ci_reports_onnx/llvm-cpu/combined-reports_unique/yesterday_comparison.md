# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1559.8958|1519.204|-40.6918|-2.61%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1533.6338|1495.078|-38.5557|-2.51%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|13166.1211|12870.1732|-295.9479|-2.25%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|710.9848|722.7454|11.7606|1.65%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|1115.3593|1099.3006|-16.0588|-1.44%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|6518.3284|6416.2656|-102.0628|-1.57%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|526.0833|541.1192|15.0359|2.86%|
|migraphx_cadene__dpn92i1|PASS|within tol|367.8794|366.9694|-0.91|-0.25%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8516.9397|8505.8604|-11.0793|-0.13%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|731.073|726.9799|-4.0931|-0.56%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10505.4507|10472.9991|-32.4516|-0.31%|
|migraphx_mlperf__resnet50_v1|PASS|progression|230.707|158.5127|-72.1943|-31.29%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|257.7966|261.6371|3.8406|1.49%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1377.5259|1332.6117|-44.9142|-3.26%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|97.0172|93.7122|-3.305|-3.41%|
|migraphx_pytorch-examples__wlang_lstm|PASS|within tol|16.1351|16.0244|-0.1107|-0.69%|
|migraphx_torchvision__densenet121i32|PASS|within tol|3075.1068|3037.9506|-37.1562|-1.21%|
|migraphx_torchvision__inceptioni1|PASS|within tol|325.5299|314.7079|-10.822|-3.32%|
|migraphx_torchvision__resnet50i1|PASS|within tol|149.1808|148.8413|-0.3394|-0.23%|

## No Regressions Found

## No Progressions Found

