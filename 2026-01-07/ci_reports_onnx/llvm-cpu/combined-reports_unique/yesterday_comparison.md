# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1260.5639|1312.72|52.1561|4.14%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1277.4421|1494.9533|217.5113|17.03%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|10938.2339|10028.2625|-909.9715|-8.32%|
|migraphx_ORT__distilgpt2_1|PASS|regression|604.9412|720.3093|115.3681|19.07%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|2231.3979|2386.3081|154.9102|6.94%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|7943.3807|8569.952|626.5713|7.89%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|463.0333|571.0695|108.0362|23.33%|
|migraphx_bert__bert-large-uncased|PASS|within tol|28725.7017|29603.186|877.4843|3.05%|
|migraphx_cadene__dpn92i1|PASS|within tol|414.4412|409.3721|-5.069|-1.22%|
|migraphx_cadene__inceptionv4i16|PASS|regression|9332.0582|11177.1082|1845.05|19.77%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|845.937|950.9347|104.9978|12.41%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|7392.1289|8889.4771|1497.3482|20.26%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|31359.8109|31660.3569|300.546|0.96%|
|migraphx_mlperf__resnet50_v1|PASS|regression|203.2775|270.4714|67.194|33.06%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|277.4327|267.657|-9.7758|-3.52%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|790.5216|763.0813|-27.4403|-3.47%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|60.7331|53.3247|-7.4084|-12.2%|
|migraphx_torchvision__densenet121i32|PASS|regression|5277.7648|6722.2393|1444.4745|27.37%|
|migraphx_torchvision__inceptioni1|PASS|within tol|385.5205|366.6102|-18.9104|-4.91%|
|migraphx_torchvision__resnet50i1|PASS|within tol|223.236|229.5874|6.3514|2.85%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|20916.8924|21037.4747|120.5823|0.58%|
|migx_bench_bert-large-uncased_2_128|PASS|regression|20754.477|23305.1777|2550.7007|12.29%|

## No Regressions Found

## 11 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset16_timm|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17_timm|compiled_inference|PASS|
|longformer_Opset16|import_model|compilation|
|longformer_Opset18|import_model|compilation|
|twins_svt_base_Opset16|compilation|compiled_inference|
|twins_svt_base_Opset17|compilation|compiled_inference|
|twins_svt_large_Opset16|compilation|compiled_inference|
|twins_svt_large_Opset17|compilation|compiled_inference|
|twins_svt_small_Opset16|compilation|compiled_inference|
|twins_svt_small_Opset17|compilation|compiled_inference|
|vit_large_patch16_384_Opset16_timm|compiled_inference|PASS|

