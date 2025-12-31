# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|100.961|101.6344|0.6734|0.67%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|283.746|302.8004|19.0544|6.72%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.3895|57.9599|0.5704|0.99%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|71.6316|75.2242|3.5927|5.02%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|285.6715|299.0857|13.4143|4.7%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.8035|39.1978|0.3943|1.02%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6109|12.6583|0.0474|0.38%|
|migraphx_cadene__dpn92i1|PASS|within tol|9.9692|9.9695|0.0003|0.0%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.803|21.92|0.117|0.54%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.0944|6.0866|-0.0077|-0.13%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.232|7.2367|0.0047|0.07%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.5225|19.6771|0.1546|0.79%|
|migraphx_mlperf__resnet50_v1|PASS|regression|15.0504|21.4869|6.4365|42.77%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.7877|25.8725|0.0849|0.33%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|112.6735|147.6126|34.9391|31.01%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|14.3548|14.3175|-0.0374|-0.26%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.7209|17.7367|0.0158|0.09%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6253|4.6328|0.0075|0.16%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.6742|3.7018|0.0276|0.75%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2432|20.2527|0.0095|0.05%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.0165|32.8935|-0.123|-0.37%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.6364|51.596|-0.0404|-0.08%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7771|11.8048|0.0276|0.23%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.508|12.4813|-0.0267|-0.21%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8113|12.8519|0.0407|0.32%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.403|12.4122|0.0093|0.07%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8082|12.7926|-0.0156|-0.12%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4229|14.414|-0.009|-0.06%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.7326|31.5907|-0.1419|-0.45%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.4367|61.2707|-0.1659|-0.27%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.1171|94.7865|-0.3306|-0.35%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.6849|12.7292|0.0443|0.35%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3588|14.3515|-0.0073|-0.05%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.2832|20.2801|-0.0031|-0.02%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3634|14.3528|-0.0106|-0.07%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5271|20.528|0.0009|0.0%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.0618|29.0377|-0.0241|-0.08%|

## 10 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|alexnet_Opset18_torch_hub|PASS|Numerics|
|resnet10t_Opset16|Numerics|compiled_inference|
|resnet10t_Opset17|Numerics|compiled_inference|
|resnet10t_Opset18|Numerics|compiled_inference|
|sequencer2d_m_Opset17|PASS|Numerics|
|sequencer2d_s_Opset17|PASS|Numerics|
|sequencer2d_s_vaiq|Numerics|compilation|
|squeezenet1.0-12|PASS|Numerics|
|squeezenet1.0-6|PASS|Numerics|
|vit_l_16_Opset16_torch_hub|PASS|compilation|

## 5 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_224_Opset17|compilation|PASS|
|coatnet_2_rw_224.sw_in12k|compilation|PASS|
|coatnet_rmlp_1_rw2_224.sw_in12k_ft_in1k|compilation|PASS|
|coatnet_rmlp_1_rw_224.sw_in1k|compilation|PASS|
|coatnet_rmlp_2_rw_224.sw_in12k_ft_in1k|compilation|PASS|

