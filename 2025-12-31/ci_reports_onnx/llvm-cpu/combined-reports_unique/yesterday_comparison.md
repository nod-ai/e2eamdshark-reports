# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|1427.4152|1733.8315|306.4163|21.47%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1316.4754|1802.707|486.2315|36.93%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|11827.0413|20220.7967|8393.7554|70.97%|
|migraphx_ORT__distilgpt2_1|PASS|regression|588.538|837.5323|248.9943|42.31%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|2243.6195|2602.156|358.5365|15.98%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|7647.3687|14050.3798|6403.0111|83.73%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|515.7024|643.2586|127.5562|24.73%|
|migraphx_cadene__dpn92i1|PASS|regression|392.1716|829.3449|437.1734|111.48%|
|migraphx_cadene__inceptionv4i16|PASS|regression|9292.7906|11626.0211|2333.2306|25.11%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|810.5399|1018.1655|207.6256|25.62%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|7387.9695|14321.5804|6933.6109|93.85%|
|migraphx_mlperf__resnet50_v1|PASS|regression|251.236|390.896|139.66|55.59%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|248.1931|552.3243|304.1312|122.54%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|828.8641|2219.1718|1390.3077|167.74%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|50.8017|61.3407|10.539|20.75%|
|migraphx_torchvision__densenet121i32|PASS|within tol|5112.5852|5156.6269|44.0417|0.86%|
|migraphx_torchvision__inceptioni1|PASS|regression|348.8922|376.9046|28.0124|8.03%|
|migraphx_torchvision__resnet50i1|PASS|regression|197.427|216.9176|19.4906|9.87%|

## 5 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|migx_bench_bert-large-uncased_1_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_1_384|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_384|PASS|compiled_inference|

## No Progressions Found

