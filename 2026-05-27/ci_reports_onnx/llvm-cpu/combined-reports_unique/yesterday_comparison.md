# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1537.0123|1472.8974|-64.1148|-4.17%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1553.9025|1452.3019|-101.6006|-6.54%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12951.2756|12754.9738|-196.3017|-1.52%|
|migraphx_ORT__distilgpt2_1|PASS|regression|698.2978|734.4021|36.1043|5.17%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|1103.4461|1103.0401|-0.406|-0.04%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|6384.0613|6522.5973|138.536|2.17%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|546.4472|543.4656|-2.9816|-0.55%|
|migraphx_cadene__dpn92i1|PASS|within tol|367.8408|380.9107|13.0698|3.55%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8538.2737|8640.7489|102.4752|1.2%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|733.4485|761.9422|28.4936|3.88%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10557.7061|10596.9396|39.2335|0.37%|
|migraphx_mlperf__resnet50_v1|PASS|regression|159.0648|215.3806|56.3158|35.4%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|261.6536|288.3378|26.6843|10.2%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1309.9423|1321.6507|11.7084|0.89%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|96.6822|98.0555|1.3732|1.42%|
|migraphx_pytorch-examples__wlang_lstm|PASS|within tol|16.1535|16.7034|0.5499|3.4%|
|migraphx_torchvision__densenet121i32|PASS|within tol|3035.2504|3076.9196|41.6691|1.37%|
|migraphx_torchvision__inceptioni1|PASS|regression|322.6493|348.8239|26.1746|8.11%|
|migraphx_torchvision__resnet50i1|PASS|regression|148.3631|162.1423|13.7792|9.29%|

## No Regressions Found

## One Progression Found:

|model name|old_status|new_status|
|---|---|---|
|RDN_pytorch_vaiq_int8|compiled_inference|Numerics|

