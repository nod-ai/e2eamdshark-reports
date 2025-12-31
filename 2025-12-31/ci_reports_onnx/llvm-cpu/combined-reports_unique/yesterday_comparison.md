# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1733.8315|1531.9502|-201.8813|-11.64%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1802.707|1510.7496|-291.9574|-16.2%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|20220.7967|11030.7395|-9190.0572|-45.45%|
|migraphx_ORT__distilgpt2_1|PASS|progression|837.5323|620.794|-216.7383|-25.88%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2602.156|2230.0949|-372.061|-14.3%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|14050.3798|8577.7588|-5472.621|-38.95%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|643.2586|567.0965|-76.1621|-11.84%|
|migraphx_cadene__dpn92i1|PASS|progression|829.3449|402.325|-427.0199|-51.49%|
|migraphx_cadene__inceptionv4i16|PASS|progression|11626.0211|10126.4232|-1499.5979|-12.9%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|1018.1655|804.2262|-213.9393|-21.01%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|14321.5804|7004.073|-7317.5073|-51.09%|
|migraphx_mlperf__resnet50_v1|PASS|progression|390.896|205.1754|-185.7206|-47.51%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|552.3243|245.3015|-307.0229|-55.59%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|2219.1718|732.6408|-1486.531|-66.99%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|61.3407|50.0598|-11.2809|-18.39%|
|migraphx_torchvision__densenet121i32|PASS|regression|5156.6269|5479.223|322.5961|6.26%|
|migraphx_torchvision__inceptioni1|PASS|within tol|376.9046|368.0628|-8.8418|-2.35%|
|migraphx_torchvision__resnet50i1|PASS|within tol|216.9176|219.7854|2.8678|1.32%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset16_timm|PASS|compiled_inference|

## 5 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|migx_bench_bert-large-uncased_1_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_1_384|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_384|compiled_inference|PASS|

