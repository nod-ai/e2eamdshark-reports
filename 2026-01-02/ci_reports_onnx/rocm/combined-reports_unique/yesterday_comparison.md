# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.504|101.1211|-0.3829|-0.38%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|305.091|285.1476|-19.9435|-6.54%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|58.2784|58.3375|0.0591|0.1%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|75.2687|72.0319|-3.2367|-4.3%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|299.4582|286.2904|-13.1678|-4.4%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|39.5378|39.1602|-0.3776|-0.96%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.7084|12.6512|-0.0572|-0.45%|
|migraphx_cadene__dpn92i1|PASS|within tol|10.1916|10.0432|-0.1484|-1.46%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.9257|22.0323|0.1067|0.49%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.1406|6.1092|-0.0314|-0.51%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.3037|7.2621|-0.0416|-0.57%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|20.1176|20.5421|0.4246|2.11%|
|migraphx_mlperf__resnet50_v1|PASS|progression|21.5621|15.0927|-6.4694|-30.0%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.6158|26.7068|0.091|0.34%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|148.689|114.0201|-34.669|-23.32%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|17.1025|16.9696|-0.1329|-0.78%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.7893|17.8237|0.0344|0.19%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6825|4.7235|0.0409|0.87%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.735|3.7144|-0.0206|-0.55%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.3077|20.2846|-0.0231|-0.11%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.8491|33.9104|1.0613|3.23%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.4642|53.1426|1.6784|3.26%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8766|11.8464|-0.0302|-0.25%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5527|12.5|-0.0527|-0.42%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.9418|12.8538|-0.088|-0.68%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.571|12.4263|-0.1447|-1.15%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8626|12.8695|0.0069|0.05%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4794|14.4092|-0.0702|-0.48%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.5983|32.5845|0.9863|3.12%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.3129|63.2465|1.9336|3.15%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|94.9961|97.3495|2.3534|2.48%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.778|12.7432|-0.0348|-0.27%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.4171|14.3783|-0.0388|-0.27%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3455|20.3044|-0.0411|-0.2%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.4359|14.3888|-0.0472|-0.33%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6092|20.6498|0.0406|0.2%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.0737|29.6885|0.6148|2.11%|

## 6 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|coatnet_3_rw_224.sw_in12k|PASS|compilation|
|coatnet_rmlp_2_rw_224.sw_in12k|PASS|compilation|
|inception_v3.tf_in1k_vaiq|PASS|Numerics|
|sequencer2d_m_Opset17_timm|PASS|Numerics|
|squeezenet1.0-9|PASS|Numerics|
|squeezenet1.1-7|PASS|Numerics|

## 8 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|ResNet18_vaiq|Numerics|PASS|
|ResNet34_vaiq|Numerics|PASS|
|sequencer2d_l_Opset17|Numerics|PASS|
|sequencer2d_m_Opset17|Numerics|PASS|
|squeezenet1.0-6|Numerics|PASS|
|swin_base_patch4_window12_384_Opset17_timm|compilation|PASS|
|tf_efficientnetv2_s_Opset17_timm|compiled_inference|Numerics|
|vit_l_16_Opset16_torch_hub|compilation|PASS|

