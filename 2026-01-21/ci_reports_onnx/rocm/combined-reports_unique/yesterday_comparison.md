# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.3689|101.245|-0.1238|-0.12%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|287.2826|286.5205|-0.7621|-0.27%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.6089|58.3039|0.695|1.21%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.1286|72.4619|0.3333|0.46%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.3087|286.7019|0.3932|0.14%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.7085|39.2141|0.5055|1.31%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.7287|12.7188|-0.0099|-0.08%|
|migraphx_cadene__dpn92i1|PASS|within tol|3.1569|3.0822|-0.0747|-2.37%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.1986|20.1772|-0.0215|-0.11%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.5217|2.5276|0.0059|0.23%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.3026|7.2848|-0.0177|-0.24%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|20.2949|20.9966|0.7017|3.46%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1398|15.0798|-0.0599|-0.4%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.788|26.5254|0.7373|2.86%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|113.7412|113.8752|0.134|0.12%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.6382|17.6787|0.0405|0.23%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.4379|3.4726|0.0346|1.01%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8973|1.9209|0.0235|1.24%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2533|20.299|0.0457|0.23%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|34.0359|33.8999|-0.136|-0.4%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|53.5808|53.3348|-0.246|-0.46%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8607|11.8367|-0.024|-0.2%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.482|12.5636|0.0815|0.65%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8788|12.8897|0.0109|0.08%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4495|12.5068|0.0573|0.46%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7788|12.8093|0.0305|0.24%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4552|14.4643|0.0091|0.06%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.7889|32.6421|-0.1469|-0.45%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|63.3815|63.4055|0.024|0.04%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|98.4213|98.03|-0.3913|-0.4%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7561|12.7588|0.0027|0.02%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.371|14.3864|0.0154|0.11%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.328|20.3397|0.0117|0.06%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3759|14.3935|0.0176|0.12%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6703|20.6518|-0.0185|-0.09%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.8733|29.868|-0.0052|-0.02%|

## No Regressions Found

## 244 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|crossvit_15_240|Numerics|PASS|
|crossvit_15_240_Opset16|Numerics|PASS|
|crossvit_15_240_Opset16_timm|Numerics|PASS|
|crossvit_15_240_Opset17|Numerics|PASS|
|crossvit_15_240_Opset17_timm|Numerics|PASS|
|crossvit_15_dagger_240|Numerics|PASS|
|crossvit_15_dagger_240_Opset16|Numerics|PASS|
|crossvit_15_dagger_240_Opset16_timm|Numerics|PASS|
|crossvit_15_dagger_240_Opset17|Numerics|PASS|
|crossvit_15_dagger_240_Opset17_timm|Numerics|PASS|
|crossvit_15_dagger_408|Numerics|PASS|
|crossvit_15_dagger_408_Opset16|Numerics|PASS|
|crossvit_15_dagger_408_Opset16_timm|Numerics|PASS|
|crossvit_15_dagger_408_Opset17|Numerics|PASS|
|crossvit_15_dagger_408_Opset17_timm|Numerics|PASS|
|crossvit_18_240|Numerics|PASS|
|crossvit_18_240_Opset16|Numerics|PASS|
|crossvit_18_240_Opset16_timm|Numerics|PASS|
|crossvit_18_240_Opset17|Numerics|PASS|
|crossvit_18_240_Opset17_timm|Numerics|PASS|
|crossvit_18_dagger_240|Numerics|PASS|
|crossvit_18_dagger_240_Opset16|Numerics|PASS|
|crossvit_18_dagger_240_Opset16_timm|Numerics|PASS|
|crossvit_18_dagger_240_Opset17|Numerics|PASS|
|crossvit_18_dagger_240_Opset17_timm|Numerics|PASS|
|crossvit_18_dagger_408|Numerics|PASS|
|crossvit_18_dagger_408_Opset16|Numerics|PASS|
|crossvit_18_dagger_408_Opset16_timm|Numerics|PASS|
|crossvit_18_dagger_408_Opset17|Numerics|PASS|
|crossvit_18_dagger_408_Opset17_timm|Numerics|PASS|
|crossvit_9_240|Numerics|PASS|
|crossvit_9_240_Opset16|Numerics|PASS|
|crossvit_9_240_Opset16_timm|Numerics|PASS|
|crossvit_9_240_Opset17|Numerics|PASS|
|crossvit_9_240_Opset17_timm|Numerics|PASS|
|crossvit_9_dagger_240|Numerics|PASS|
|crossvit_9_dagger_240_Opset16|Numerics|PASS|
|crossvit_9_dagger_240_Opset16_timm|Numerics|PASS|
|crossvit_9_dagger_240_Opset17|Numerics|PASS|
|crossvit_9_dagger_240_Opset17_timm|Numerics|PASS|
|crossvit_base_240|Numerics|PASS|
|crossvit_base_240_Opset16|Numerics|PASS|
|crossvit_base_240_Opset16_timm|Numerics|PASS|
|crossvit_base_240_Opset17|Numerics|PASS|
|crossvit_base_240_Opset17_timm|Numerics|PASS|
|crossvit_small_240|Numerics|PASS|
|crossvit_small_240_Opset16|Numerics|PASS|
|crossvit_small_240_Opset16_timm|Numerics|PASS|
|crossvit_small_240_Opset17|Numerics|PASS|
|crossvit_small_240_Opset17_timm|Numerics|PASS|
|crossvit_tiny_240|Numerics|PASS|
|crossvit_tiny_240_Opset16|Numerics|PASS|
|crossvit_tiny_240_Opset16_timm|Numerics|PASS|
|crossvit_tiny_240_Opset17|Numerics|PASS|
|crossvit_tiny_240_Opset17_timm|Numerics|PASS|
|cs3darknet_focus_l_Opset16|Numerics|PASS|
|cs3darknet_focus_l_Opset17|Numerics|PASS|
|cs3darknet_focus_l_Opset18|Numerics|PASS|
|cs3darknet_focus_l_Opset18_timm|Numerics|PASS|
|cs3darknet_focus_l_vaiq|Numerics|PASS|
|cs3darknet_focus_m_Opset16|Numerics|PASS|
|cs3darknet_focus_m_Opset16_timm|Numerics|PASS|
|cs3darknet_focus_m_Opset17|Numerics|PASS|
|cs3darknet_focus_m_Opset18|Numerics|PASS|
|cs3darknet_l_Opset16|Numerics|PASS|
|cs3darknet_l_Opset16_timm|Numerics|PASS|
|cs3darknet_l_Opset17|Numerics|PASS|
|cs3darknet_l_Opset18|Numerics|PASS|
|cs3darknet_m_Opset16|Numerics|PASS|
|cs3darknet_m_Opset17|Numerics|PASS|
|cs3darknet_m_Opset17_timm|Numerics|PASS|
|cs3darknet_m_Opset18|Numerics|PASS|
|cs3darknet_x_Opset16|Numerics|PASS|
|cs3darknet_x_Opset17|Numerics|PASS|
|cs3darknet_x_Opset17_timm|Numerics|PASS|
|cs3darknet_x_Opset18|Numerics|PASS|
|cs3edgenet_x_Opset16|Numerics|PASS|
|cs3edgenet_x_Opset17|Numerics|PASS|
|cs3edgenet_x_Opset18|Numerics|PASS|
|cs3edgenet_x_Opset18_timm|Numerics|PASS|
|cs3se_edgenet_x_Opset16|Numerics|PASS|
|cs3se_edgenet_x_Opset17|Numerics|PASS|
|cs3sedarknet_l_Opset16|Numerics|PASS|
|cs3sedarknet_l_Opset17|Numerics|PASS|
|cs3sedarknet_x_Opset16|Numerics|PASS|
|cs3sedarknet_x_Opset17|Numerics|PASS|
|dla60_res2net_Opset16|Numerics|PASS|
|dla60_res2net_Opset17|Numerics|PASS|
|dla60_res2net_Opset17_timm|Numerics|PASS|
|dla60_res2net_Opset18|Numerics|PASS|
|dla60_res2next_Opset16|Numerics|PASS|
|dla60_res2next_Opset17|Numerics|PASS|
|dla60_res2next_Opset18|Numerics|PASS|
|dla60_res2next_Opset18_timm|Numerics|PASS|
|dpn107_Opset16|Numerics|PASS|
|dpn107_Opset16_timm|Numerics|PASS|
|dpn107_Opset17|Numerics|PASS|
|dpn107_Opset18|Numerics|PASS|
|dpn107_Opset18_timm|Numerics|PASS|
|dpn131_Opset16|Numerics|PASS|
|dpn131_Opset17|Numerics|PASS|
|dpn131_Opset18|Numerics|PASS|
|dpn131_Opset18_timm|Numerics|PASS|
|dpn68_Opset16|Numerics|PASS|
|dpn68_Opset17|Numerics|PASS|
|dpn68_Opset17_timm|Numerics|PASS|
|dpn68_Opset18|Numerics|PASS|
|dpn92_Opset16|Numerics|PASS|
|dpn92_Opset17|Numerics|PASS|
|dpn92_Opset18|Numerics|PASS|
|dpn98_Opset16|Numerics|PASS|
|dpn98_Opset17|Numerics|PASS|
|dpn98_Opset17_timm|Numerics|PASS|
|dpn98_Opset18|Numerics|PASS|
|edgenext_base|Numerics|PASS|
|edgenext_small|Numerics|PASS|
|edgenext_small_Opset16|Numerics|PASS|
|edgenext_small_Opset16_timm|Numerics|PASS|
|edgenext_small_Opset17|Numerics|PASS|
|edgenext_small_Opset17_timm|Numerics|PASS|
|edgenext_small_Opset18|Numerics|PASS|
|edgenext_small_rw|Numerics|PASS|
|edgenext_small_rw_Opset16|Numerics|PASS|
|edgenext_small_rw_Opset16_timm|Numerics|PASS|
|edgenext_small_rw_Opset17|Numerics|PASS|
|edgenext_small_rw_Opset18|Numerics|PASS|
|edgenext_x_small|Numerics|PASS|
|edgenext_x_small_Opset16|Numerics|PASS|
|edgenext_x_small_Opset16_timm|Numerics|PASS|
|edgenext_xx_small|Numerics|PASS|
|edgenext_xx_small_Opset16|Numerics|PASS|
|edgenext_xx_small_Opset16_timm|Numerics|PASS|
|edgenext_xx_small_Opset17|Numerics|PASS|
|edgenext_xx_small_Opset18|Numerics|PASS|
|edgenext_xx_small_Opset18_timm|Numerics|PASS|
|migraphx_cadene__dpn92i1|Numerics|PASS|
|res2net101_26w_4s_Opset16|Numerics|PASS|
|res2net101_26w_4s_Opset16_timm|Numerics|PASS|
|res2net101_26w_4s_Opset17|Numerics|PASS|
|res2net101_26w_4s_Opset18|Numerics|PASS|
|res2net50_14w_8s_Opset16|Numerics|PASS|
|res2net50_14w_8s_Opset16_timm|Numerics|PASS|
|res2net50_14w_8s_Opset17|Numerics|PASS|
|res2net50_14w_8s_Opset18|Numerics|PASS|
|res2net50_26w_4s_Opset16|Numerics|PASS|
|res2net50_26w_4s_Opset16_timm|Numerics|PASS|
|res2net50_26w_4s_Opset17|Numerics|PASS|
|res2net50_26w_4s_Opset18|Numerics|PASS|
|res2net50_26w_6s_Opset16|Numerics|PASS|
|res2net50_26w_6s_Opset17|Numerics|PASS|
|res2net50_26w_6s_Opset17_timm|Numerics|PASS|
|res2net50_26w_6s_Opset18|Numerics|PASS|
|res2net50_26w_8s_Opset16|Numerics|PASS|
|res2net50_26w_8s_Opset16_timm|Numerics|PASS|
|res2net50_26w_8s_Opset17|Numerics|PASS|
|res2net50_26w_8s_Opset18|Numerics|PASS|
|res2net50_48w_2s_Opset16|Numerics|PASS|
|res2net50_48w_2s_Opset17|Numerics|PASS|
|res2net50_48w_2s_Opset18|Numerics|PASS|
|res2next50_Opset16|Numerics|PASS|
|res2next50_Opset17|Numerics|PASS|
|res2next50_Opset18|Numerics|PASS|
|res2next50_Opset18_timm|Numerics|PASS|
|rexnet_100_Opset16|Numerics|PASS|
|rexnet_100_Opset16_timm|Numerics|PASS|
|rexnet_100_Opset17|Numerics|PASS|
|rexnet_130_Opset16|Numerics|PASS|
|rexnet_130_Opset16_timm|Numerics|PASS|
|rexnet_130_Opset17|Numerics|PASS|
|rexnet_150_Opset16|Numerics|PASS|
|rexnet_150_Opset17|Numerics|PASS|
|rexnet_150_Opset17_timm|Numerics|PASS|
|rexnet_200_Opset16|Numerics|PASS|
|rexnet_200_Opset16_timm|Numerics|PASS|
|rexnet_200_Opset17|Numerics|PASS|
|rexnetr_200_Opset16|Numerics|PASS|
|rexnetr_200_Opset17|Numerics|PASS|
|rexnetr_200_Opset17_timm|Numerics|PASS|
|xcit_large_24_p16_224_Opset16|Numerics|PASS|
|xcit_large_24_p16_224_Opset16_timm|Numerics|PASS|
|xcit_large_24_p16_224_dist_Opset16|Numerics|PASS|
|xcit_large_24_p16_384_dist_Opset16|Numerics|PASS|
|xcit_large_24_p16_384_dist_Opset16_timm|Numerics|PASS|
|xcit_large_24_p8_224_Opset16|Numerics|PASS|
|xcit_large_24_p8_224_dist_Opset16|Numerics|PASS|
|xcit_large_24_p8_384_dist_Opset16|Numerics|PASS|
|xcit_large_24_p8_384_dist_Opset16_timm|Numerics|PASS|
|xcit_medium_24_p16_224_Opset16|Numerics|PASS|
|xcit_medium_24_p16_224_Opset16_timm|Numerics|PASS|
|xcit_medium_24_p16_224_dist_Opset16|Numerics|PASS|
|xcit_medium_24_p16_384_dist_Opset16|Numerics|PASS|
|xcit_medium_24_p16_384_dist_Opset16_timm|Numerics|PASS|
|xcit_medium_24_p8_224_Opset16|Numerics|PASS|
|xcit_medium_24_p8_224_Opset16_timm|Numerics|PASS|
|xcit_medium_24_p8_224_dist_Opset16|Numerics|PASS|
|xcit_medium_24_p8_384_dist_Opset16|Numerics|PASS|
|xcit_medium_24_p8_384_dist_Opset16_timm|Numerics|PASS|
|xcit_nano_12_p16_224_Opset16|Numerics|PASS|
|xcit_nano_12_p16_224_Opset16_timm|Numerics|PASS|
|xcit_nano_12_p16_224_dist_Opset16|Numerics|PASS|
|xcit_nano_12_p16_384_dist_Opset16|Numerics|PASS|
|xcit_nano_12_p16_384_dist_Opset16_timm|Numerics|PASS|
|xcit_nano_12_p8_224_Opset16|Numerics|PASS|
|xcit_nano_12_p8_224_dist_Opset16|Numerics|PASS|
|xcit_nano_12_p8_224_dist_Opset16_timm|Numerics|PASS|
|xcit_nano_12_p8_384_dist_Opset16|Numerics|PASS|
|xcit_nano_12_p8_384_dist_Opset16_timm|Numerics|PASS|
|xcit_small_12_p16_224_Opset16|Numerics|PASS|
|xcit_small_12_p16_224_dist_Opset16|Numerics|PASS|
|xcit_small_12_p16_224_dist_Opset16_timm|Numerics|PASS|
|xcit_small_12_p16_384_dist_Opset16|Numerics|PASS|
|xcit_small_12_p16_384_dist_Opset16_timm|Numerics|PASS|
|xcit_small_12_p8_224_Opset16|Numerics|PASS|
|xcit_small_12_p8_224_dist_Opset16|Numerics|PASS|
|xcit_small_12_p8_224_dist_Opset16_timm|Numerics|PASS|
|xcit_small_12_p8_384_dist_Opset16|Numerics|PASS|
|xcit_small_12_p8_384_dist_Opset16_timm|Numerics|PASS|
|xcit_small_24_p16_224_Opset16|Numerics|PASS|
|xcit_small_24_p16_224_Opset16_timm|Numerics|PASS|
|xcit_small_24_p16_224_dist_Opset16|Numerics|PASS|
|xcit_small_24_p8_224_Opset16|Numerics|PASS|
|xcit_small_24_p8_224_Opset16_timm|Numerics|PASS|
|xcit_small_24_p8_224_dist_Opset16|Numerics|PASS|
|xcit_small_24_p8_384_dist_Opset16|Numerics|PASS|
|xcit_small_24_p8_384_dist_Opset16_timm|Numerics|PASS|
|xcit_tiny_12_p16_224_Opset16|Numerics|PASS|
|xcit_tiny_12_p16_224_dist_Opset16|Numerics|PASS|
|xcit_tiny_12_p16_224_dist_Opset16_timm|Numerics|PASS|
|xcit_tiny_12_p16_384_dist_Opset16|Numerics|PASS|
|xcit_tiny_12_p16_384_dist_Opset16_timm|Numerics|PASS|
|xcit_tiny_12_p8_224_Opset16|Numerics|PASS|
|xcit_tiny_12_p8_224_Opset16_timm|Numerics|PASS|
|xcit_tiny_12_p8_224_dist_Opset16|Numerics|PASS|
|xcit_tiny_12_p8_384_dist_Opset16|Numerics|PASS|
|xcit_tiny_12_p8_384_dist_Opset16_timm|Numerics|PASS|
|xcit_tiny_24_p16_224_Opset16|Numerics|PASS|
|xcit_tiny_24_p16_224_dist_Opset16|Numerics|PASS|
|xcit_tiny_24_p16_224_dist_Opset16_timm|Numerics|PASS|
|xcit_tiny_24_p16_384_dist_Opset16|Numerics|PASS|
|xcit_tiny_24_p16_384_dist_Opset16_timm|Numerics|PASS|
|xcit_tiny_24_p8_224_Opset16|Numerics|PASS|
|xcit_tiny_24_p8_224_dist_Opset16|Numerics|PASS|
|xcit_tiny_24_p8_224_dist_Opset16_timm|Numerics|PASS|
|xcit_tiny_24_p8_384_dist_Opset16|Numerics|PASS|

