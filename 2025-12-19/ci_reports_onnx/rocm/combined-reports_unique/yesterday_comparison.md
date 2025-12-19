# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.8137|101.115|-0.6987|-0.69%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|283.2935|285.1791|1.8857|0.67%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.5088|57.7591|0.2503|0.44%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|75.6058|75.5473|-0.0585|-0.08%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|294.0081|295.239|1.2309|0.42%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|40.3238|40.1991|-0.1247|-0.31%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6243|12.6086|-0.0157|-0.12%|
|migraphx_cadene__dpn92i1|Numerics|within tol|10.1521|10.0989|-0.0531|-0.52%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.797|21.9672|0.1702|0.78%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.0933|6.0458|-0.0475|-0.78%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2106|7.2165|0.0059|0.08%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.6416|19.6668|0.0252|0.13%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|14.8511|15.0856|0.2344|1.58%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8792|26.0822|0.2029|0.78%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.6345|112.9078|0.2733|0.24%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|14.5736|14.5949|0.0212|0.15%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.7102|17.7373|0.0271|0.15%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6551|4.6584|0.0033|0.07%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.7007|3.6949|-0.0059|-0.16%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2376|20.2847|0.047|0.23%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.6846|33.3187|0.6341|1.94%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.3434|52.2661|0.9227|1.8%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7515|11.795|0.0434|0.37%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4134|12.49|0.0766|0.62%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8227|12.8445|0.0218|0.17%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.2942|12.3902|0.096|0.78%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7208|12.8253|0.1045|0.82%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.3501|14.4289|0.0788|0.55%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.4355|32.0723|0.6368|2.03%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.1425|62.1197|0.9772|1.6%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|94.9297|96.1747|1.245|1.31%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.6635|12.7101|0.0466|0.37%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3472|14.4056|0.0584|0.41%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.2472|20.3113|0.0641|0.32%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3057|14.3746|0.0689|0.48%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5505|20.5733|0.0229|0.11%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|28.8694|29.2104|0.341|1.18%|

## 7 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|ResNet18_vaiq|PASS|Numerics|
|ResNet34_vaiq|PASS|Numerics|
|sequencer2d_s_Opset16_timm|PASS|Numerics|
|squeezenet1.0-12|PASS|Numerics|
|squeezenet1_1_Opset16|PASS|Numerics|
|squeezenet1_1_Opset17_torch_hub|PASS|Numerics|
|swin_base_patch4_window12_384_in22k_Opset17_timm|PASS|compilation|

## 17 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|coatnet_0_rw_224.sw_in1k|compilation|PASS|
|coatnet_1_rw_224.sw_in1k|compilation|PASS|
|coatnet_2_rw_224.sw_in12k_ft_in1k|compilation|PASS|
|coatnet_nano_rw_224.sw_in1k|compilation|PASS|
|coatnet_rmlp_nano_rw_224.sw_in1k|compilation|PASS|
|coatnext_nano_rw_224.sw_in1k|compilation|PASS|
|cs3darknet_focus_l_train_vaiq|Numerics|PASS|
|cs3darknet_l_train_vaiq|Numerics|PASS|
|cs3sedarknet_l_train_vaiq|Numerics|PASS|
|cspdarknet53_vaiq|Numerics|PASS|
|pit_xs_224|compilation|PASS|
|pit_xs_distilled_224|compilation|PASS|
|pit_xs_distilled_224_Opset16_timm|compilation|PASS|
|sequencer2d_m_Opset17_timm|Numerics|PASS|
|sequencer2d_s_Opset16|Numerics|PASS|
|tf_efficientnetv2_s_Opset17_timm|compiled_inference|Numerics|
|vit_l_16_Opset16_torch_hub|compilation|PASS|

