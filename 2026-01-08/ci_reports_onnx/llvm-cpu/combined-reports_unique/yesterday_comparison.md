# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1245.95|1283.4886|37.5386|3.01%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1200.6125|1257.9089|57.2964|4.77%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|10788.7605|10743.2275|-45.5331|-0.42%|
|migraphx_ORT__distilgpt2_1|PASS|regression|554.2142|680.6086|126.3944|22.81%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2229.9274|2260.6606|30.7332|1.38%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|7411.8788|7583.0263|171.1475|2.31%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|469.0732|484.4023|15.3292|3.27%|
|migraphx_bert__bert-large-uncased|PASS|regression|28046.2647|30014.7346|1968.47|7.02%|
|migraphx_cadene__dpn92i1|PASS|within tol|393.0038|401.6197|8.6159|2.19%|
|migraphx_cadene__inceptionv4i16|PASS|regression|8368.7039|9472.415|1103.7111|13.19%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|803.0094|882.0449|79.0354|9.84%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|6992.1481|7385.5996|393.4515|5.63%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|31392.1122|31959.9031|567.7908|1.81%|
|migraphx_mlperf__resnet50_v1|PASS|regression|201.5539|222.1224|20.5685|10.2%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|253.848|242.771|-11.077|-4.36%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|789.6001|768.9912|-20.6088|-2.61%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|48.5687|49.7085|1.1398|2.35%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4739.9175|4901.5753|161.6578|3.41%|
|migraphx_torchvision__inceptioni1|PASS|within tol|351.8564|347.9145|-3.9419|-1.12%|
|migraphx_torchvision__resnet50i1|PASS|regression|195.2753|233.3967|38.1213|19.52%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|20646.9015|21210.3937|563.4923|2.73%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|30012.2073|30157.6733|145.466|0.48%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|20798.5755|20819.872|21.2965|0.1%|

## No Regressions Found

## 6 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_Opset18|compiled_inference|PASS|
|longt5_Opset16|compiled_inference|PASS|
|longt5_Opset17|compiled_inference|PASS|
|vit_large_patch14_clip_336.laion2b_ft_in12k_in1k|compiled_inference|PASS|
|vit_large_patch16_384.augreg_in21k_ft_in1k|compiled_inference|PASS|

