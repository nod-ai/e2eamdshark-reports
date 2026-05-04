# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1580.8284|1432.0303|-148.7981|-9.41%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1554.7037|1511.8883|-42.8154|-2.75%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12244.1396|12795.7099|551.5703|4.5%|
|migraphx_ORT__distilgpt2_1|PASS|progression|728.7059|684.8227|-43.8831|-6.02%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|1249.8873|1090.2861|-159.6013|-12.77%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|6994.2266|6393.1289|-601.0977|-8.59%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|623.1345|530.0844|-93.05|-14.93%|
|migraphx_cadene__dpn92i1|PASS|progression|437.5316|369.128|-68.4036|-15.63%|
|migraphx_cadene__inceptionv4i16|PASS|progression|9331.1994|8537.4611|-793.7383|-8.51%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|815.4423|732.0019|-83.4404|-10.23%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|9731.4014|10676.7923|945.3909|9.71%|
|migraphx_mlperf__resnet50_v1|PASS|progression|164.277|150.8389|-13.4381|-8.18%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|302.5713|269.4696|-33.1016|-10.94%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|1436.8228|1297.15|-139.6728|-9.72%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|55.5935|98.5075|42.914|77.19%|
|migraphx_pytorch-examples__wlang_lstm|PASS|progression|32.0338|16.2574|-15.7765|-49.25%|
|migraphx_torchvision__densenet121i32|PASS|progression|3574.453|3055.3172|-519.1358|-14.52%|
|migraphx_torchvision__inceptioni1|PASS|progression|368.2478|321.435|-46.8129|-12.71%|
|migraphx_torchvision__resnet50i1|PASS|progression|196.3842|151.1613|-45.2229|-23.03%|

## 10 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|efficientformerv2_l.snap_dist_in1k|PASS|compilation|
|efficientformerv2_s0.snap_dist_in1k|PASS|compilation|
|efficientformerv2_s1.snap_dist_in1k|PASS|compilation|
|efficientformerv2_s2.snap_dist_in1k|PASS|compilation|
|model--roberta_shared_bbc_xsum--patrickvonplaten|PASS|Numerics|
|squeezebert_Opset16|PASS|compilation|
|squeezebert_Opset16_transformers|PASS|compilation|
|squeezebert_Opset17|PASS|compilation|
|squeezebert_Opset18|PASS|compilation|
|squeezebert_Opset18_transformers|PASS|compilation|

## 19 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|flaubert_Opset16|Numerics|PASS|
|flaubert_Opset16_transformers|Numerics|PASS|
|flaubert_Opset17|Numerics|PASS|
|flaubert_Opset17_transformers|Numerics|PASS|
|flaubert_Opset18|Numerics|PASS|
|regnetz_c16_evos_Opset16|Numerics|PASS|
|regnetz_c16_evos_Opset16_timm|Numerics|PASS|
|regnetz_c16_evos_Opset17|Numerics|PASS|
|regnetz_d8_evos_Opset16|Numerics|PASS|
|regnetz_d8_evos_Opset16_timm|Numerics|PASS|
|regnetz_d8_evos_Opset17|Numerics|PASS|
|resnetv2_50d_evos_Opset16|Numerics|PASS|
|resnetv2_50d_evos_Opset17|Numerics|PASS|
|resnetv2_50d_evos_Opset17_timm|Numerics|PASS|
|umt5_Opset16|Numerics|PASS|
|umt5_Opset16_transformers|Numerics|PASS|
|umt5_Opset17|Numerics|PASS|
|xlmroberta_Opset16|Numerics|PASS|
|xlmroberta_Opset16_transformers|Numerics|PASS|

