# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1312.72|1245.95|-66.77|-5.09%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1494.9533|1200.6125|-294.3408|-19.69%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|10028.2625|10788.7605|760.4981|7.58%|
|migraphx_ORT__distilgpt2_1|PASS|progression|720.3093|554.2142|-166.0952|-23.06%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2386.3081|2229.9274|-156.3807|-6.55%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|8569.952|7411.8788|-1158.0731|-13.51%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|571.0695|469.0732|-101.9963|-17.86%|
|migraphx_bert__bert-large-uncased|PASS|progression|29603.186|28046.2647|-1556.9213|-5.26%|
|migraphx_cadene__dpn92i1|PASS|within tol|409.3721|393.0038|-16.3683|-4.0%|
|migraphx_cadene__inceptionv4i16|PASS|progression|11177.1082|8368.7039|-2808.4043|-25.13%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|950.9347|803.0094|-147.9253|-15.56%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|8889.4771|6992.1481|-1897.3291|-21.34%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|31660.3569|31392.1122|-268.2447|-0.85%|
|migraphx_mlperf__resnet50_v1|PASS|progression|270.4714|201.5539|-68.9175|-25.48%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|267.657|253.848|-13.809|-5.16%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|763.0813|789.6001|26.5188|3.48%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|53.3247|48.5687|-4.756|-8.92%|
|migraphx_torchvision__densenet121i32|PASS|progression|6722.2393|4739.9175|-1982.3218|-29.49%|
|migraphx_torchvision__inceptioni1|PASS|within tol|366.6102|351.8564|-14.7538|-4.02%|
|migraphx_torchvision__resnet50i1|PASS|progression|229.5874|195.2753|-34.3121|-14.95%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|21037.4747|20646.9015|-390.5733|-1.86%|
|migx_bench_bert-large-uncased_2_128|PASS|progression|23305.1777|20798.5755|-2506.6021|-10.76%|

## 6 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset17|PASS|compiled_inference|
|deit3_large_patch16_384_Opset18|PASS|compiled_inference|
|longt5_Opset16|PASS|compiled_inference|
|longt5_Opset17|PASS|compiled_inference|
|vit_large_patch14_clip_336.laion2b_ft_in12k_in1k|PASS|compiled_inference|
|vit_large_patch16_384.augreg_in21k_ft_in1k|PASS|compiled_inference|

## No Progressions Found

