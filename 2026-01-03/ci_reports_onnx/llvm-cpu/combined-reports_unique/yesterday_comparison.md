# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1874.7269|1940.8782|66.1513|3.53%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1761.2893|1936.8381|175.5489|9.97%|
|migraphx_ORT__distilgpt2_1|PASS|regression|894.4114|1042.7248|148.3134|16.58%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|2615.2036|2780.1798|164.9762|6.31%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|14116.6097|12965.5012|-1151.1085|-8.15%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|650.2704|620.8643|-29.4061|-4.52%|
|migraphx_cadene__dpn92i1|PASS|progression|812.9834|592.2975|-220.6859|-27.15%|
|migraphx_cadene__inceptionv4i16|PASS|progression|15354.4168|13041.8771|-2312.5397|-15.06%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|1019.5761|1305.7537|286.1777|28.07%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|14701.1368|15931.574|1230.4372|8.37%|
|migraphx_mlperf__resnet50_v1|PASS|regression|397.0701|496.3554|99.2853|25.0%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|541.9739|376.3003|-165.6736|-30.57%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|2414.7872|1683.2835|-731.5036|-30.29%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|99.3452|98.7152|-0.63|-0.63%|
|migraphx_torchvision__densenet121i32|PASS|regression|5099.0796|6866.8787|1767.7991|34.67%|
|migraphx_torchvision__inceptioni1|PASS|regression|371.2234|469.5015|98.2782|26.47%|
|migraphx_torchvision__resnet50i1|PASS|regression|214.1649|280.4273|66.2624|30.94%|

## 10 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset16|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset16|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset17|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset18|PASS|compiled_inference|
|migraphx_bert__bert-large-uncased|PASS|compiled_inference|
|migraphx_mlperf__bert_large_mlperf|Numerics|compiled_inference|
|migx_bench_bert-large-uncased_1_128|PASS|compiled_inference|
|vit_large_patch16_384_Opset16|PASS|compiled_inference|
|vit_large_patch16_384_Opset17|PASS|compiled_inference|
|vit_large_patch16_384_Opset18|PASS|compiled_inference|

## No Progressions Found

