# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1947.771|1856.8691|-90.902|-4.67%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1931.3085|1866.8547|-64.4537|-3.34%|
|migraphx_ORT__distilgpt2_1|PASS|progression|1033.8233|874.4496|-159.3737|-15.42%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2777.6296|2589.3238|-188.3057|-6.78%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|12855.1191|14062.4299|1207.3108|9.39%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|641.7387|619.8901|-21.8487|-3.4%|
|migraphx_cadene__dpn92i1|PASS|regression|595.6336|768.2872|172.6536|28.99%|
|migraphx_cadene__inceptionv4i16|PASS|progression|12909.3248|9533.8605|-3375.4643|-26.15%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|1293.9598|1015.8396|-278.1202|-21.49%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|15344.2407|14303.2635|-1040.9772|-6.78%|
|migraphx_mlperf__resnet50_v1|PASS|progression|548.3999|354.6132|-193.7867|-35.34%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|372.6379|529.8784|157.2404|42.2%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1653.988|2371.1359|717.1479|43.36%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|133.3203|111.7586|-21.5617|-16.17%|
|migraphx_torchvision__densenet121i32|PASS|progression|6604.1958|5028.1441|-1576.0517|-23.86%|
|migraphx_torchvision__inceptioni1|PASS|progression|492.4882|373.0908|-119.3975|-24.24%|
|migraphx_torchvision__resnet50i1|PASS|progression|276.5113|240.2369|-36.2744|-13.12%|

## No Regressions Found

## 5 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_Opset18|compiled_inference|PASS|
|migraphx_bert__bert-large-uncased|compiled_inference|PASS|
|migraphx_mlperf__bert_large_mlperf|compiled_inference|Numerics|
|migx_bench_bert-large-uncased_1_128|compiled_inference|PASS|

