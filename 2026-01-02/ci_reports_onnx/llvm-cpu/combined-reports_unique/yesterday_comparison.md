# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|2008.6073|1874.7269|-133.8804|-6.67%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1937.4953|1761.2893|-176.206|-9.09%|
|migraphx_ORT__distilgpt2_1|PASS|progression|1067.4318|894.4114|-173.0204|-16.21%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2810.4839|2615.2036|-195.2803|-6.95%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|12895.8497|14116.6097|1220.76|9.47%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|695.655|650.2704|-45.3846|-6.52%|
|migraphx_cadene__dpn92i1|PASS|progression|889.9303|812.9834|-76.9468|-8.65%|
|migraphx_cadene__inceptionv4i16|PASS|regression|12659.549|15354.4168|2694.8677|21.29%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|1292.0539|1019.5761|-272.4778|-21.09%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|15435.1616|14701.1368|-734.0248|-4.76%|
|migraphx_mlperf__resnet50_v1|PASS|progression|438.797|397.0701|-41.7269|-9.51%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|394.4254|541.9739|147.5486|37.41%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|1631.1935|2414.7872|783.5937|48.04%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|132.0175|99.3452|-32.6722|-24.75%|
|migraphx_torchvision__densenet121i32|PASS|progression|6801.0558|5099.0796|-1701.9762|-25.03%|
|migraphx_torchvision__inceptioni1|PASS|progression|483.3626|371.2234|-112.1392|-23.2%|
|migraphx_torchvision__resnet50i1|PASS|progression|280.6963|214.1649|-66.5313|-23.7%|

## No Regressions Found

## 8 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset16|compiled_inference|PASS|
|deit3_large_patch16_384_Opset16_timm|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset16|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset18|compiled_inference|PASS|
|migraphx_bert__bert-large-uncased|compiled_inference|PASS|
|migraphx_mlperf__bert_large_mlperf|compiled_inference|Numerics|
|migx_bench_bert-large-uncased_1_128|compiled_inference|PASS|

