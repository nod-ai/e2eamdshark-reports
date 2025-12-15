# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1777.795|1315.4152|-462.3799|-26.01%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1794.1761|1268.9819|-525.1942|-29.27%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|19503.2769|11026.0126|-8477.2643|-43.47%|
|migraphx_ORT__distilgpt2_1|PASS|progression|841.9634|593.9835|-247.9799|-29.45%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2583.0912|2436.7387|-146.3525|-5.67%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|14066.9943|7697.3864|-6369.6078|-45.28%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|617.2811|499.826|-117.4552|-19.03%|
|migraphx_cadene__dpn92i1|PASS|progression|825.6118|409.0078|-416.604|-50.46%|
|migraphx_cadene__inceptionv4i16|PASS|progression|9545.7038|8484.977|-1060.7268|-11.11%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|1017.1637|803.6746|-213.4891|-20.99%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|14168.4835|7696.7648|-6471.7188|-45.68%|
|migraphx_mlperf__resnet50_v1|PASS|progression|358.8715|206.4469|-152.4245|-42.47%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|557.3747|250.7792|-306.5955|-55.01%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|2349.4241|765.6515|-1583.7726|-67.41%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|103.5409|50.8034|-52.7375|-50.93%|
|migraphx_torchvision__densenet121i32|PASS|within tol|5053.6158|4882.8052|-170.8107|-3.38%|
|migraphx_torchvision__inceptioni1|PASS|progression|370.9709|350.7603|-20.2106|-5.45%|
|migraphx_torchvision__resnet50i1|PASS|progression|213.9783|200.2995|-13.6787|-6.39%|

## No Regressions Found

## 5 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|migx_bench_bert-large-uncased_1_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_1_384|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_384|compiled_inference|PASS|

