# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1432.0303|1427.8555|-4.1748|-0.29%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1511.8883|1546.1632|34.2749|2.27%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12795.7099|12935.1637|139.4538|1.09%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|684.8227|706.9027|22.08|3.22%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|1090.2861|1147.1037|56.8176|5.21%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|6393.1289|6497.7424|104.6135|1.64%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|530.0844|544.8938|14.8094|2.79%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|732.0019|717.2534|-14.7484|-2.01%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10676.7923|10495.0709|-181.7213|-1.7%|
|migraphx_mlperf__resnet50_v1|PASS|regression|150.8389|205.7611|54.9221|36.41%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|269.4696|264.9434|-4.5262|-1.68%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1297.15|1300.8079|3.6579|0.28%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|98.5075|96.0896|-2.4179|-2.45%|
|migraphx_pytorch-examples__wlang_lstm|PASS|within tol|16.2574|16.2783|0.0209|0.13%|
|migraphx_torchvision__inceptioni1|PASS|within tol|321.435|322.112|0.677|0.21%|
|migraphx_torchvision__resnet50i1|PASS|within tol|151.1613|146.1076|-5.0537|-3.34%|

## 32 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|dpn107_Opset16|PASS|compilation|
|dpn107_Opset16_timm|PASS|compilation|
|dpn107_Opset17|PASS|compilation|
|dpn107_Opset18|PASS|compilation|
|dpn107_Opset18_timm|PASS|compilation|
|dpn131_Opset16|PASS|compilation|
|dpn131_Opset17|PASS|compilation|
|dpn131_Opset18|PASS|compilation|
|dpn131_Opset18_timm|PASS|compilation|
|dpn68_Opset16|PASS|compilation|
|dpn68_Opset17|PASS|compilation|
|dpn68_Opset17_timm|PASS|compilation|
|dpn68_Opset18|PASS|compilation|
|dpn68b_Opset16|PASS|compilation|
|dpn68b_Opset16_timm|PASS|compilation|
|dpn68b_Opset17|PASS|compilation|
|dpn68b_Opset18|PASS|compilation|
|dpn92_Opset16|PASS|compilation|
|dpn92_Opset17|PASS|compilation|
|dpn92_Opset17_timm|PASS|compilation|
|dpn92_Opset18|PASS|compilation|
|dpn98_Opset16|PASS|compilation|
|dpn98_Opset17|PASS|compilation|
|dpn98_Opset17_timm|PASS|compilation|
|dpn98_Opset18|PASS|compilation|
|migraphx_cadene__dpn92i1|PASS|compilation|
|migraphx_cadene__inceptionv4i16|PASS|compilation|
|migraphx_torchvision__densenet121i32|PASS|compilation|
|yolov4|Numerics|compilation|

## No Progressions Found

