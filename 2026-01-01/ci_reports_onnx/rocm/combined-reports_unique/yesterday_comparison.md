# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.6707|101.504|-0.1667|-0.16%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|303.904|305.091|1.1871|0.39%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|58.1075|58.2784|0.1709|0.29%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|75.3765|75.2687|-0.1078|-0.14%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|299.005|299.4582|0.4532|0.15%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|39.2293|39.5378|0.3085|0.79%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6668|12.7084|0.0416|0.33%|
|migraphx_cadene__dpn92i1|PASS|within tol|9.9651|10.1916|0.2266|2.27%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|22.0331|21.9257|-0.1074|-0.49%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.1131|6.1406|0.0275|0.45%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2218|7.3037|0.082|1.14%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.5888|20.1176|0.5288|2.7%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|21.5346|21.5621|0.0275|0.13%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8892|26.6158|0.7266|2.81%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|148.8935|148.689|-0.2045|-0.14%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|14.079|17.1025|3.0235|21.48%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.805|17.7893|-0.0157|-0.09%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6216|4.6825|0.061|1.32%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.715|3.735|0.02|0.54%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2756|20.3077|0.0322|0.16%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.9544|32.8491|-1.1053|-3.26%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|53.1569|51.4642|-1.6927|-3.18%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8171|11.8766|0.0595|0.5%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5044|12.5527|0.0484|0.39%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8959|12.9418|0.0459|0.36%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4987|12.571|0.0723|0.58%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7825|12.8626|0.0801|0.63%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4249|14.4794|0.0545|0.38%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.6638|31.5983|-1.0656|-3.26%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|63.3743|61.3129|-2.0614|-3.25%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|97.6606|94.9961|-2.6645|-2.73%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7365|12.778|0.0415|0.33%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.37|14.4171|0.0471|0.33%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3031|20.3455|0.0424|0.21%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3822|14.4359|0.0537|0.37%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.618|20.6092|-0.0088|-0.04%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.6992|29.0737|-0.6255|-2.11%|

## 5 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|sequencer2d_m_Opset17|PASS|Numerics|
|sequencer2d_s_Opset17|PASS|Numerics|
|swin_base_patch4_window12_384_Opset17_timm|PASS|compilation|
|tf_efficientnetv2_s_Opset17_timm|Numerics|compiled_inference|
|vit_l_16_Opset16_torch_hub|PASS|compilation|

## 6 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|coatnet_3_rw_224.sw_in12k|compilation|PASS|
|sequencer2d_s_Opset17_timm|Numerics|PASS|
|squeezenet1.0-9|Numerics|PASS|
|squeezenet1.1-7|Numerics|PASS|
|swin_base_patch4_window12_384_in22k_Opset17_timm|compilation|PASS|
|xcit_nano_12_p8_384_dist_Opset16|compiled_inference|Numerics|

