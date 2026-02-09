# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1652.0766|1526.5667|-125.5099|-7.6%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1614.7642|1520.2143|-94.5499|-5.86%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|24664.8197|12450.6361|-12214.1835|-49.52%|
|migraphx_ORT__distilgpt2_1|PASS|progression|856.4805|752.8726|-103.6079|-12.1%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2539.1315|2523.982|-15.1495|-0.6%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|7368.2327|10243.3061|2875.0734|39.02%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|561.7193|671.5233|109.804|19.55%|
|migraphx_cadene__dpn92i1|PASS|progression|1043.0583|438.7368|-604.3215|-57.94%|
|migraphx_cadene__inceptionv4i16|PASS|progression|16394.06|9021.5812|-7372.4787|-44.97%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|1045.4949|815.5667|-229.9282|-21.99%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|11638.3671|10152.965|-1485.4021|-12.76%|
|migraphx_mlperf__resnet50_v1|PASS|progression|451.5819|196.4572|-255.1247|-56.5%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|604.0575|296.6689|-307.3887|-50.89%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|2337.259|1423.1732|-914.0858|-39.11%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|185.4896|57.0445|-128.4451|-69.25%|
|migraphx_pytorch-examples__wlang_lstm|PASS|progression|44.7311|32.2439|-12.4872|-27.92%|
|migraphx_torchvision__densenet121i32|PASS|progression|6722.048|4948.394|-1773.6541|-26.39%|
|migraphx_torchvision__inceptioni1|PASS|progression|436.7604|355.3275|-81.4328|-18.64%|
|migraphx_torchvision__resnet50i1|PASS|progression|251.36|198.3432|-53.0169|-21.09%|

## 20 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|flaubert_Opset16|PASS|Numerics|
|flaubert_Opset16_transformers|PASS|Numerics|
|mobilevitv2_150_384_in22ft1k_Opset16|PASS|Numerics|
|mobilevitv2_150_384_in22ft1k_Opset16_timm|PASS|Numerics|
|mobilevitv2_150_384_in22ft1k_Opset17|PASS|Numerics|
|mobilevitv2_150_384_in22ft1k_Opset18|PASS|Numerics|
|mobilevitv2_175_384_in22ft1k_Opset16|PASS|Numerics|
|mobilevitv2_175_384_in22ft1k_Opset17|PASS|Numerics|
|mobilevitv2_175_384_in22ft1k_Opset17_timm|PASS|Numerics|
|mobilevitv2_175_384_in22ft1k_Opset18|PASS|Numerics|
|mobilevitv2_200_384_in22ft1k_Opset16|PASS|Numerics|
|mobilevitv2_200_384_in22ft1k_Opset17|PASS|Numerics|
|mobilevitv2_200_384_in22ft1k_Opset18|PASS|Numerics|
|mobilevitv2_200_384_in22ft1k_Opset18_timm|PASS|Numerics|
|pytorch-3dunet_vaiq_int8|PASS|Numerics|
|resnet50_gn_test_vaiq|PASS|Numerics|
|resnet50_gn_vaiq|PASS|Numerics|
|resnetv2_50d_gn.ah_in1k_train_vaiq|PASS|Numerics|
|resnetv2_50d_gn.ah_in1k_vaiq|PASS|Numerics|
|resnetv2_50x1_bit.goog_distilled_in1k_vaiq|PASS|Numerics|

## 6 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_in22ft1k_Opset17_timm|import_model|PASS|
|migx_bench_bert-large-uncased_1_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_1_384|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_384|compiled_inference|PASS|

