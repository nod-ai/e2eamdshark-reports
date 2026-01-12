# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1648.2867|1507.4566|-140.8301|-8.54%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1641.364|1549.609|-91.755|-5.59%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|25020.6048|12785.3862|-12235.2185|-48.9%|
|migraphx_ORT__distilgpt2_1|PASS|progression|882.3965|714.5773|-167.8192|-19.02%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2507.0348|2493.468|-13.5668|-0.54%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|7411.2095|9888.3916|2477.1821|33.42%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|562.6299|642.3338|79.7038|14.17%|
|migraphx_cadene__dpn92i1|PASS|progression|1029.3196|435.4421|-593.8775|-57.7%|
|migraphx_cadene__inceptionv4i16|PASS|progression|19818.4857|8908.5712|-10909.9145|-55.05%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|1045.7373|818.9331|-226.8043|-21.69%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|11729.9797|9756.1084|-1973.8713|-16.83%|
|migraphx_mlperf__resnet50_v1|PASS|progression|508.2631|203.8954|-304.3677|-59.88%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|610.2311|291.5891|-318.6419|-52.22%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|2481.1636|1146.5619|-1334.6016|-53.79%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|205.5243|56.8082|-148.7162|-72.36%|
|migraphx_torchvision__densenet121i32|PASS|progression|6309.1939|4789.2753|-1519.9186|-24.09%|
|migraphx_torchvision__inceptioni1|PASS|progression|453.0504|353.7656|-99.2848|-21.91%|
|migraphx_torchvision__resnet50i1|PASS|progression|249.1856|193.557|-55.6287|-22.32%|

## 2 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset18|PASS|compiled_inference|
|regnetz_c16_evos_Opset16_timm|PASS|Numerics|

## 29 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384_Opset16|compiled_inference|PASS|
|beit_large_patch16_384_Opset17|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset16|compiled_inference|PASS|
|convnext_xlarge_384_in22ft1k_Opset17|compiled_inference|PASS|
|migx_bench_bert-large-uncased_1_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_1_384|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_384|compiled_inference|PASS|
|vit_large_patch16_384_Opset16|compiled_inference|PASS|
|vit_large_patch16_384_Opset17|compiled_inference|PASS|
|vit_large_patch16_384_Opset18|compiled_inference|PASS|
|xception41_Opset16|compiled_inference|PASS|
|xception41_Opset17|compiled_inference|PASS|
|xception41_Opset17_timm|compiled_inference|PASS|
|xception41_Opset18|compiled_inference|PASS|
|xception41p_Opset16|compiled_inference|PASS|
|xception41p_Opset17|compiled_inference|PASS|
|xception41p_Opset18|compiled_inference|PASS|
|xception65_Opset16|compiled_inference|PASS|
|xception65_Opset17|compiled_inference|PASS|
|xception65_Opset18|compiled_inference|PASS|
|xception65p_Opset16|compiled_inference|PASS|
|xception65p_Opset17|compiled_inference|PASS|
|xception65p_Opset18|compiled_inference|PASS|
|xception71_Opset16|compiled_inference|PASS|
|xception71_Opset17|compiled_inference|PASS|
|xception71_Opset17_timm|compiled_inference|PASS|
|xception71_Opset18|compiled_inference|PASS|

