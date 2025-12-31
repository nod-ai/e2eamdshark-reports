# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.6344|101.6707|0.0363|0.04%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|302.8004|303.904|1.1036|0.36%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.9599|58.1075|0.1475|0.25%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|75.2242|75.3765|0.1523|0.2%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|299.0857|299.005|-0.0807|-0.03%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|39.1978|39.2293|0.0316|0.08%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6583|12.6668|0.0085|0.07%|
|migraphx_cadene__dpn92i1|PASS|within tol|9.9695|9.9651|-0.0044|-0.04%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.92|22.0331|0.113|0.52%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.0866|6.1131|0.0264|0.43%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2367|7.2218|-0.0149|-0.21%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.6771|19.5888|-0.0883|-0.45%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|21.4869|21.5346|0.0477|0.22%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8725|25.8892|0.0167|0.06%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|147.6126|148.8935|1.2809|0.87%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|14.3175|14.079|-0.2385|-1.67%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.7367|17.805|0.0683|0.39%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6328|4.6216|-0.0113|-0.24%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.7018|3.715|0.0132|0.36%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2527|20.2756|0.0228|0.11%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.8935|33.9544|1.0609|3.23%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.596|53.1569|1.5609|3.03%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8048|11.8171|0.0123|0.1%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4813|12.5044|0.0231|0.19%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8519|12.8959|0.044|0.34%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4122|12.4987|0.0865|0.7%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7926|12.7825|-0.0101|-0.08%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.414|14.4249|0.0109|0.08%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.5907|32.6638|1.0731|3.4%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.2707|63.3743|2.1036|3.43%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|94.7865|97.6606|2.8741|3.03%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7292|12.7365|0.0073|0.06%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3515|14.37|0.0185|0.13%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.2801|20.3031|0.023|0.11%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3528|14.3822|0.0294|0.2%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.528|20.618|0.09|0.44%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.0377|29.6992|0.6615|2.28%|

## 3 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|swin_base_patch4_window12_384_in22k_Opset17_timm|PASS|compilation|
|t5-decoder-with-lm-head-12|PASS|native_inference|
|xcit_nano_12_p8_384_dist_Opset16|Numerics|compiled_inference|

## 7 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|coatnet_rmlp_1_rw2_224.sw_in12k|compilation|PASS|
|coatnet_rmlp_2_rw_224.sw_in12k|compilation|PASS|
|inception_v3.tf_in1k_vaiq|Numerics|PASS|
|sequencer2d_m_Opset17|Numerics|PASS|
|sequencer2d_m_Opset17_timm|Numerics|PASS|
|sequencer2d_s_Opset17|Numerics|PASS|
|vit_l_16_Opset16_torch_hub|compilation|PASS|

