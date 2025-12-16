# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1315.4152|1307.7803|-7.6349|-0.58%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1268.9819|1453.2327|184.2508|14.52%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|11026.0126|14062.5223|3036.5097|27.54%|
|migraphx_ORT__distilgpt2_1|PASS|progression|593.9835|556.969|-37.0145|-6.23%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2436.7387|2230.5019|-206.2368|-8.46%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|7697.3864|13086.7211|5389.3346|70.02%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|499.826|498.0605|-1.7654|-0.35%|
|migraphx_bert__bert-large-uncased|PASS|within tol|28906.6613|28251.6899|-654.9715|-2.27%|
|migraphx_cadene__dpn92i1|PASS|within tol|409.0078|401.8348|-7.1729|-1.75%|
|migraphx_cadene__inceptionv4i16|PASS|regression|8484.977|11891.4519|3406.475|40.15%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|803.6746|830.0773|26.4026|3.29%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|7696.7648|7256.8624|-439.9024|-5.72%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|206.4469|205.9812|-0.4657|-0.23%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|250.7792|317.6959|66.9167|26.68%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|765.6515|803.8982|38.2467|5.0%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|50.8034|53.5119|2.7085|5.33%|
|migraphx_torchvision__densenet121i32|PASS|regression|4882.8052|5679.495|796.6899|16.32%|
|migraphx_torchvision__inceptioni1|PASS|within tol|350.7603|350.7916|0.0313|0.01%|
|migraphx_torchvision__resnet50i1|PASS|regression|200.2995|227.7445|27.445|13.7%|
|migx_bench_bert-large-uncased_1_128|PASS|regression|20738.9794|29174.589|8435.6095|40.68%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|29898.6198|30902.0319|1003.4122|3.36%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|22412.2008|21657.437|-754.7638|-3.37%|

## 3 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|resnetv2_152x2_bit_teacher_384_Opset16|Numerics|compilation|
|resnetv2_152x2_bit_teacher_384_Opset17|Numerics|compilation|
|resnetv2_152x2_bit_teacher_Opset16|Numerics|compilation|

## No Progressions Found

