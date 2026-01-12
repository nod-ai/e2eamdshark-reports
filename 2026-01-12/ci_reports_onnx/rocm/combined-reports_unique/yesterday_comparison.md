# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.1589|101.8368|0.6778|0.67%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|283.0061|286.3802|3.3741|1.19%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.5795|58.191|0.6114|1.06%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.4973|72.6645|0.1672|0.23%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.2312|287.0673|0.836|0.29%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.7595|39.1586|0.3991|1.03%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6248|12.7097|0.0849|0.67%|
|migraphx_cadene__dpn92i1|PASS|within tol|9.8069|9.9573|0.1504|1.53%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.1136|20.1881|0.0745|0.37%|
|migraphx_cadene__resnext101_64x4di1|Numerics|within tol|3.293|3.3252|0.0322|0.98%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.238|7.3006|0.0626|0.86%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.6161|20.3876|0.7716|3.93%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1223|15.1597|0.0374|0.25%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8387|26.607|0.7684|2.97%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.7854|113.8026|1.0172|0.9%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|14.6157|17.1469|2.5312|17.32%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.5781|17.6563|0.0782|0.45%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.431|3.4804|0.0494|1.44%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.9012|1.9272|0.026|1.37%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2773|20.3904|0.1131|0.56%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.8712|33.1997|0.3285|1.0%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.5472|52.0362|0.4891|0.95%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7695|11.8512|0.0817|0.69%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5243|12.5543|0.03|0.24%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8694|12.8947|0.0253|0.2%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.5096|12.5374|0.0278|0.22%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7582|12.8635|0.1053|0.83%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4433|14.4372|-0.0061|-0.04%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.6143|31.9266|0.3123|0.99%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.3128|62.0208|0.7081|1.15%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.0067|96.0858|1.0791|1.14%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7142|12.762|0.0478|0.38%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3707|14.4499|0.0792|0.55%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.2946|20.4145|0.1199|0.59%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3882|14.4791|0.0909|0.63%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5955|20.6936|0.0981|0.48%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.0103|29.1522|0.1419|0.49%|

## 8 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|dm_nfnet_f0.dm_in1k_train_vaiq|PASS|compilation|
|dm_nfnet_f0.dm_in1k_vaiq|PASS|compilation|
|dm_nfnet_f1.dm_in1k_train_vaiq|PASS|compilation|
|dm_nfnet_f1.dm_in1k_vaiq|PASS|compilation|
|efficientformerv2_s0.snap_dist_in1k|Numerics|compiled_inference|
|squeezebert_Opset16|PASS|compilation|
|squeezebert_Opset16_transformers|PASS|compilation|
|swinv2_base_window12_192_22k_Opset17|PASS|compiled_inference|

## 380 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|AlexNet_vaiq_int8|Numerics|PASS|
|CSP-DarkNet_vaiq_int8|Numerics|PASS|
|EfficientNet_v2_s_vaiq_int8|compilation|PASS|
|Inception_v3_vaiq|Numerics|PASS|
|RRDB_ESRGAN_pro_vaiq|compilation|Numerics|
|RRDB_ESRGAN_vaiq|compilation|Numerics|
|RRDB_ESRGAN_vaiq_int8|compilation|Numerics|
|ResNet18_vaiq|Numerics|PASS|
|ResNet34_vaiq|Numerics|PASS|
|VideoResNet_vaiq_int8|Numerics|PASS|
|YoloNetV3_vaiq|Numerics|PASS|
|YoloNetV3_vaiq_int8|Numerics|PASS|
|alexnet_Opset16|Numerics|PASS|
|alexnet_Opset17|Numerics|PASS|
|alexnet_Opset18|Numerics|PASS|
|alexnet_Opset18_torch_hub|Numerics|PASS|
|arcfaceresnet100-8|compilation|PASS|
|coat_lite_mini|compilation|PASS|
|coat_lite_mini_Opset16|compilation|PASS|
|coat_lite_mini_Opset16_timm|compilation|PASS|
|coat_lite_mini_Opset17|compilation|PASS|
|coat_lite_mini_Opset18|compilation|PASS|
|coat_lite_mini_Opset18_timm|compilation|PASS|
|coat_lite_small|compilation|PASS|
|coat_lite_small_Opset16|compilation|PASS|
|coat_lite_small_Opset16_timm|compilation|PASS|
|coat_lite_small_Opset17|compilation|PASS|
|coat_lite_small_Opset17_timm|compilation|PASS|
|coat_lite_small_Opset18|compilation|PASS|
|coat_lite_tiny|compilation|PASS|
|coat_lite_tiny_Opset16|compilation|PASS|
|coat_lite_tiny_Opset16_timm|compilation|PASS|
|coat_lite_tiny_Opset17|compilation|PASS|
|coat_lite_tiny_Opset17_timm|compilation|PASS|
|coat_lite_tiny_Opset18|compilation|PASS|
|coat_mini|compilation|PASS|
|coat_mini_Opset16|compilation|PASS|
|coat_mini_Opset16_timm|compilation|PASS|
|coat_mini_Opset17|compilation|PASS|
|coat_mini_Opset18|compilation|PASS|
|coat_mini_Opset18_timm|compilation|PASS|
|coat_tiny|compilation|PASS|
|coat_tiny_Opset16|compilation|PASS|
|coat_tiny_Opset16_timm|compilation|PASS|
|coat_tiny_Opset17|compilation|PASS|
|coat_tiny_Opset18|compilation|PASS|
|coat_tiny_Opset18_timm|compilation|PASS|
|coatnet_0_rw_224.sw_in1k|compilation|PASS|
|coatnet_1_rw_224.sw_in1k|compilation|PASS|
|coatnet_2_rw_224.sw_in12k|compilation|PASS|
|coatnet_2_rw_224.sw_in12k_ft_in1k|compilation|PASS|
|coatnet_3_rw_224.sw_in12k|compilation|PASS|
|coatnet_rmlp_1_rw2_224.sw_in12k|compilation|PASS|
|coatnet_rmlp_1_rw2_224.sw_in12k_ft_in1k|compilation|PASS|
|coatnet_rmlp_1_rw_224.sw_in1k|compilation|PASS|
|coatnet_rmlp_2_rw_224.sw_in12k|compilation|PASS|
|coatnet_rmlp_2_rw_224.sw_in12k_ft_in1k|compilation|PASS|
|convit_base|compilation|PASS|
|convit_base_Opset16|compilation|PASS|
|convit_base_Opset16_timm|compilation|PASS|
|convit_base_Opset17|compilation|PASS|
|convit_base_Opset17_timm|compilation|PASS|
|convit_base_Opset18|compilation|PASS|
|convit_small|compilation|PASS|
|convit_small_Opset16|compilation|PASS|
|convit_small_Opset16_timm|compilation|PASS|
|convit_small_Opset17|compilation|PASS|
|convit_small_Opset17_timm|compilation|PASS|
|convit_small_Opset18|compilation|PASS|
|convit_tiny|compilation|PASS|
|convit_tiny_Opset16_timm|compilation|PASS|
|convit_tiny_Opset17|compilation|PASS|
|convit_tiny_Opset17_timm|compilation|PASS|
|convit_tiny_Opset18|compilation|PASS|
|crossvit_15_240|compilation|PASS|
|crossvit_15_240_Opset16|compilation|PASS|
|crossvit_15_240_Opset16_timm|compilation|PASS|
|crossvit_15_240_Opset17|compilation|PASS|
|crossvit_15_240_Opset17_timm|compilation|PASS|
|crossvit_15_dagger_240|compilation|PASS|
|crossvit_15_dagger_240_Opset16|compilation|PASS|
|crossvit_15_dagger_240_Opset16_timm|compilation|PASS|
|crossvit_15_dagger_240_Opset17|compilation|PASS|
|crossvit_15_dagger_240_Opset17_timm|compilation|PASS|
|crossvit_15_dagger_408|compilation|PASS|
|crossvit_15_dagger_408_Opset16|compilation|PASS|
|crossvit_15_dagger_408_Opset16_timm|compilation|PASS|
|crossvit_15_dagger_408_Opset17|compilation|PASS|
|crossvit_15_dagger_408_Opset17_timm|compilation|PASS|
|crossvit_18_240|compilation|PASS|
|crossvit_18_240_Opset16|compilation|PASS|
|crossvit_18_240_Opset16_timm|compilation|PASS|
|crossvit_18_240_Opset17|compilation|PASS|
|crossvit_18_240_Opset17_timm|compilation|PASS|
|crossvit_18_dagger_240|compilation|PASS|
|crossvit_18_dagger_240_Opset16|compilation|PASS|
|crossvit_18_dagger_240_Opset16_timm|compilation|PASS|
|crossvit_18_dagger_240_Opset17|compilation|PASS|
|crossvit_18_dagger_240_Opset17_timm|compilation|PASS|
|crossvit_18_dagger_408|compilation|PASS|
|crossvit_18_dagger_408_Opset16|compilation|PASS|
|crossvit_18_dagger_408_Opset16_timm|compilation|PASS|
|crossvit_18_dagger_408_Opset17|compilation|PASS|
|crossvit_18_dagger_408_Opset17_timm|compilation|PASS|
|crossvit_9_240|compilation|PASS|
|crossvit_9_240_Opset16|compilation|PASS|
|crossvit_9_240_Opset16_timm|compilation|PASS|
|crossvit_9_240_Opset17|compilation|PASS|
|crossvit_9_240_Opset17_timm|compilation|PASS|
|crossvit_9_dagger_240|compilation|PASS|
|crossvit_9_dagger_240_Opset16|compilation|PASS|
|crossvit_9_dagger_240_Opset16_timm|compilation|PASS|
|crossvit_9_dagger_240_Opset17|compilation|PASS|
|crossvit_9_dagger_240_Opset17_timm|compilation|PASS|
|crossvit_base_240|compilation|PASS|
|crossvit_base_240_Opset16|compilation|PASS|
|crossvit_base_240_Opset16_timm|compilation|PASS|
|crossvit_base_240_Opset17|compilation|PASS|
|crossvit_base_240_Opset17_timm|compilation|PASS|
|crossvit_small_240|compilation|PASS|
|crossvit_small_240_Opset16|compilation|PASS|
|crossvit_small_240_Opset16_timm|compilation|PASS|
|crossvit_small_240_Opset17|compilation|PASS|
|crossvit_small_240_Opset17_timm|compilation|PASS|
|cs3darknet_focus_l_vaiq|Numerics|PASS|
|cs3darknet_l_vaiq|Numerics|PASS|
|cs3darknet_x_vaiq|compilation|PASS|
|cs3edgenet_x_train_vaiq|compilation|PASS|
|cs3edgenet_x_vaiq|compilation|PASS|
|cs3se_edgenet_x_train_vaiq|compilation|PASS|
|cs3se_edgenet_x_vaiq|compilation|PASS|
|cs3sedarknet_l_vaiq|Numerics|PASS|
|cs3sedarknet_x_vaiq|compilation|PASS|
|darknetaa53|compiled_inference|PASS|
|dla102x_vaiq|Numerics|PASS|
|dla34_Opset16|compiled_inference|PASS|
|dla34_Opset17|compiled_inference|PASS|
|dla34_Opset17_timm|compiled_inference|PASS|
|dla34_Opset18|compiled_inference|PASS|
|dla60_vaiq|Numerics|PASS|
|dla60x_vaiq|Numerics|PASS|
|edgenext_x_small|compilation|PASS|
|efficientformer_l3.snap_dist_in1k|compilation|PASS|
|efficientnet_el_pruned.in1k_vaiq|compilation|PASS|
|efficientnet_em.ra2_in1k_vaiq|compilation|PASS|
|efficientnet_v2_l_Opset16|Numerics|PASS|
|efficientnet_v2_l_Opset17|Numerics|PASS|
|efficientnet_v2_l_Opset17_torch_hub|Numerics|PASS|
|efficientnetv2_rw_t.ra2_in1k_train_vaiq|compilation|PASS|
|focalnet_base_lrf.ms_in1k|compilation|PASS|
|focalnet_base_srf.ms_in1k|compilation|PASS|
|gc_efficientnetv2_rw_t.agc_in1k_train_vaiq|compilation|Numerics|
|gernet_m_Opset18_timm|compiled_inference|PASS|
|gluon_resnet18_v1b_vaiq|Numerics|PASS|
|gluon_senet154_Opset16|Numerics|PASS|
|gluon_senet154_Opset17|Numerics|PASS|
|gluon_senet154_vaiq|compilation|Numerics|
|hrnet_w18_small_Opset16|compilation|PASS|
|hrnet_w18_small_Opset17|compilation|PASS|
|hrnet_w18_small_Opset18|compilation|PASS|
|hrnet_w18_small_Opset18_timm|compilation|PASS|
|hrnet_w18_small_vaiq|compilation|Numerics|
|hrnet_w32_Opset16|compilation|PASS|
|hrnet_w32_Opset17|compilation|PASS|
|hrnet_w32_Opset17_timm|compilation|PASS|
|hrnet_w32_Opset18|compilation|PASS|
|hrnet_w32_vaiq|compilation|Numerics|
|hrnet_w40_Opset16|compilation|Numerics|
|hrnet_w40_Opset16_timm|compilation|Numerics|
|hrnet_w40_Opset17|compilation|Numerics|
|hrnet_w40_Opset18|compilation|Numerics|
|hrnet_w40_vaiq|compilation|Numerics|
|hrnet_w44_vaiq|compilation|Numerics|
|hrnet_w64_Opset16|compilation|PASS|
|hrnet_w64_Opset16_timm|compilation|PASS|
|hrnet_w64_Opset17|compilation|PASS|
|hrnet_w64_Opset18|compilation|PASS|
|hrnet_w64_vaiq|compilation|Numerics|
|inception-v2-9|Numerics|PASS|
|inception_v3.tf_in1k_vaiq|Numerics|PASS|
|legacy_senet154_Opset16_timm|Numerics|PASS|
|legacy_senet154_vaiq|compilation|Numerics|
|levit_128.fb_dist_in1k|compilation|PASS|
|levit_128_Opset16|compilation|PASS|
|levit_128_Opset16_timm|compilation|PASS|
|levit_128_Opset17|compilation|PASS|
|levit_128s.fb_dist_in1k|compilation|PASS|
|levit_128s_Opset16|compilation|PASS|
|levit_128s_Opset16_timm|compilation|PASS|
|levit_128s_Opset17|compilation|PASS|
|levit_192.fb_dist_in1k|compilation|Numerics|
|levit_192_Opset16|compilation|Numerics|
|levit_192_Opset16_timm|compilation|Numerics|
|levit_192_Opset17|compilation|Numerics|
|levit_256.fb_dist_in1k|compilation|PASS|
|levit_256_Opset16|compilation|PASS|
|levit_256_Opset16_timm|compilation|PASS|
|levit_256_Opset17|compilation|PASS|
|levit_384.fb_dist_in1k|compilation|PASS|
|levit_384_Opset16|compilation|PASS|
|levit_384_Opset16_timm|compilation|PASS|
|levit_384_Opset17|compilation|PASS|
|maxvit_tiny_rw_224.sw_in1k|compilation|PASS|
|mvitv2_base|compilation|PASS|
|mvitv2_large|compilation|PASS|
|mvitv2_small|compilation|PASS|
|mvitv2_tiny|compilation|PASS|
|pit_b_224|compilation|PASS|
|pit_b_224_Opset16|compilation|PASS|
|pit_b_224_Opset16_timm|compilation|PASS|
|pit_b_224_Opset17|compilation|PASS|
|pit_b_224_Opset17_timm|compilation|PASS|
|pit_b_224_Opset18|compilation|PASS|
|pit_b_distilled_224|compilation|PASS|
|pit_b_distilled_224_Opset16|compilation|PASS|
|pit_b_distilled_224_Opset16_timm|compilation|PASS|
|pit_b_distilled_224_Opset17|compilation|PASS|
|pit_b_distilled_224_Opset18|compilation|PASS|
|pit_b_distilled_224_Opset18_timm|compilation|PASS|
|pit_s_224|compilation|PASS|
|pit_s_224_Opset16|compilation|PASS|
|pit_s_224_Opset16_timm|compilation|PASS|
|pit_s_224_Opset17|compilation|PASS|
|pit_s_224_Opset18|compilation|PASS|
|pit_s_224_Opset18_timm|compilation|PASS|
|pit_s_distilled_224|compilation|PASS|
|pit_s_distilled_224_Opset16|compilation|PASS|
|pit_s_distilled_224_Opset16_timm|compilation|PASS|
|pit_s_distilled_224_Opset17|compilation|PASS|
|pit_s_distilled_224_Opset17_timm|compilation|PASS|
|pit_s_distilled_224_Opset18|compilation|PASS|
|pit_ti_224|compilation|PASS|
|pit_ti_224_Opset16|compilation|PASS|
|pit_ti_224_Opset16_timm|compilation|PASS|
|pit_ti_224_Opset17|compilation|PASS|
|pit_ti_224_Opset17_timm|compilation|PASS|
|pit_ti_224_Opset18|compilation|PASS|
|pit_ti_distilled_224|compilation|PASS|
|pit_ti_distilled_224_Opset16|compilation|PASS|
|pit_ti_distilled_224_Opset16_timm|compilation|PASS|
|pit_ti_distilled_224_Opset17|compilation|PASS|
|pit_ti_distilled_224_Opset17_timm|compilation|PASS|
|pit_ti_distilled_224_Opset18|compilation|PASS|
|resmlp_12_224.fb_distilled_in1k_vaiq|compilation|PASS|
|resmlp_24_224.fb_distilled_in1k_vaiq|compilation|PASS|
|resmlp_36_224.fb_distilled_in1k_vaiq|compilation|PASS|
|resmlp_big_24_224.fb_distilled_in1k_vaiq|compilation|PASS|
|resnet10t_Opset16|compiled_inference|PASS|
|resnet10t_Opset17|compiled_inference|PASS|
|resnet10t_Opset17_timm|compiled_inference|PASS|
|resnet10t_Opset18|compiled_inference|PASS|
|resnet10t_vaiq|Numerics|PASS|
|resnet18_Opset18_torch_hub|compiled_inference|PASS|
|resnet18_test_vaiq|Numerics|PASS|
|resnet18d_Opset16|compiled_inference|PASS|
|resnet18d_Opset17|compiled_inference|PASS|
|resnet18d_Opset17_timm|compiled_inference|PASS|
|resnet18d_Opset18|compiled_inference|PASS|
|resnet18d_test_vaiq|Numerics|PASS|
|resnet18d_vaiq|Numerics|PASS|
|resnet34_Opset17_torch_hub|compiled_inference|PASS|
|resnet34_Opset18_timm|compiled_inference|PASS|
|resnet34d_Opset16|compiled_inference|PASS|
|resnet34d_Opset17|compiled_inference|PASS|
|resnet34d_Opset17_timm|compiled_inference|PASS|
|resnet34d_Opset18|compiled_inference|PASS|
|resnet34d_Opset18_timm|compiled_inference|PASS|
|resnetv2_101_Opset16|compilation|PASS|
|resnetv2_101_Opset17|compilation|PASS|
|resnetv2_101_Opset18|compilation|PASS|
|resnetv2_101_Opset18_timm|compilation|PASS|
|resnetv2_50_Opset16|compilation|PASS|
|resnetv2_50_Opset16_timm|compilation|PASS|
|resnetv2_50_Opset17|compilation|PASS|
|resnetv2_50_Opset18|compilation|PASS|
|senet154_Opset16|Numerics|PASS|
|senet154_Opset16_timm|Numerics|PASS|
|senet154_Opset17|Numerics|PASS|
|sequencer2d_l_Opset16|Numerics|PASS|
|sequencer2d_l_Opset16_timm|Numerics|PASS|
|sequencer2d_l_Opset17|Numerics|PASS|
|sequencer2d_l_Opset17_timm|Numerics|PASS|
|sequencer2d_m_Opset16|Numerics|PASS|
|sequencer2d_m_Opset16_timm|Numerics|PASS|
|sequencer2d_m_Opset17_timm|Numerics|PASS|
|sequencer2d_s_Opset16|Numerics|PASS|
|sequencer2d_s_Opset16_timm|Numerics|PASS|
|sequencer2d_s_Opset17|Numerics|PASS|
|sequencer2d_s_Opset17_timm|Numerics|PASS|
|skresnet18_Opset16_timm|compiled_inference|PASS|
|skresnet34_Opset16_timm|compiled_inference|PASS|
|squeezenet1.0-12|Numerics|PASS|
|squeezenet1.0-6|Numerics|PASS|
|squeezenet1.0-9|Numerics|PASS|
|squeezenet1.1-7|Numerics|PASS|
|squeezenet1_1_Opset16|Numerics|PASS|
|squeezenet1_1_Opset17|Numerics|PASS|
|squeezenet1_1_Opset17_torch_hub|Numerics|PASS|
|squeezenet1_1_Opset18|Numerics|PASS|
|ssl_resnet18_Opset16|compiled_inference|PASS|
|ssl_resnet18_Opset16_timm|compiled_inference|PASS|
|ssl_resnet18_Opset17|compiled_inference|PASS|
|ssl_resnet18_Opset18|compiled_inference|PASS|
|swin_b_Opset18_torch_hub|compilation|PASS|
|swin_base_patch4_window7_224_Opset17_timm|compilation|PASS|
|swin_base_patch4_window7_224_in22k_Opset17_timm|compilation|PASS|
|swin_large_patch4_window12_384_Opset17_timm|compilation|PASS|
|swin_large_patch4_window12_384_in22k_Opset17_timm|compilation|PASS|
|swin_large_patch4_window7_224_Opset17_timm|compilation|PASS|
|swin_large_patch4_window7_224_in22k_Opset17_timm|compilation|PASS|
|swin_s3_base_224_Opset16_timm|compilation|PASS|
|swin_s3_base_224_Opset17_timm|compilation|PASS|
|swin_s3_small_224_Opset16_timm|compilation|PASS|
|swin_s3_small_224_Opset17_timm|compilation|PASS|
|swin_s3_tiny_224_Opset16_timm|compilation|PASS|
|swin_s3_tiny_224_Opset17_timm|compilation|PASS|
|swin_s_Opset16_torch_hub|compilation|PASS|
|swin_s_Opset18_torch_hub|compilation|PASS|
|swin_small_patch4_window7_224_Opset16_timm|compilation|PASS|
|swin_small_patch4_window7_224_Opset17_timm|compilation|PASS|
|swin_t_Opset16_torch_hub|compilation|PASS|
|swin_t_Opset18_torch_hub|compilation|PASS|
|swin_tiny_patch4_window7_224_Opset16_timm|compilation|PASS|
|swin_tiny_patch4_window7_224_Opset17_timm|compilation|PASS|
|swsl_resnet18_Opset16|compiled_inference|PASS|
|swsl_resnet18_Opset17|compiled_inference|PASS|
|swsl_resnet18_Opset18|compiled_inference|PASS|
|tf_efficientnet_b8.ap_in1k|compilation|PASS|
|tf_efficientnet_b8_ap_Opset17_timm|compilation|PASS|
|tf_efficientnetv2_b1.in1k_vaiq|Numerics|PASS|
|tf_efficientnetv2_b2_Opset17_timm|Numerics|PASS|
|tf_efficientnetv2_b3_Opset17_timm|Numerics|PASS|
|tf_efficientnetv2_l.in1k|Numerics|PASS|
|tf_efficientnetv2_l_in21ft1k_Opset17_timm|Numerics|PASS|
|tf_efficientnetv2_l_in21k_Opset16_timm|Numerics|PASS|
|tf_efficientnetv2_xl_in21ft1k_Opset17_timm|Numerics|PASS|
|tf_efficientnetv2_xl_in21k_Opset17_timm|Numerics|PASS|
|tinynet_b.in1k|compilation|PASS|
|tinynet_b_Opset16|compilation|PASS|
|tinynet_b_Opset16_timm|compilation|PASS|
|tinynet_b_Opset17|compilation|PASS|
|tinynet_e.in1k|Numerics|PASS|
|tinynet_e_Opset17_timm|Numerics|PASS|
|tv_resnet34_Opset16|compiled_inference|PASS|
|tv_resnet34_Opset17|compiled_inference|PASS|
|tv_resnet34_Opset18|compiled_inference|PASS|
|twins_svt_base_Opset17_timm|compilation|PASS|
|twins_svt_large_Opset17_timm|compilation|PASS|
|twins_svt_small_Opset17_timm|compilation|PASS|
|vit_relpos_base_patch16_224.sw_in1k|compilation|PASS|
|vit_relpos_base_patch16_224_Opset16|compilation|PASS|
|vit_relpos_base_patch16_224_Opset16_timm|compilation|PASS|
|vit_relpos_base_patch16_224_Opset17|compilation|PASS|
|vit_relpos_base_patch16_224_Opset17_timm|compilation|PASS|
|xception41_Opset16|compilation|PASS|
|xception41_Opset17|compilation|PASS|
|xception41_Opset17_timm|compilation|PASS|
|xception41_Opset18|compilation|PASS|
|xception65_Opset16|compilation|PASS|
|xception65_Opset17|compilation|PASS|
|xception65_Opset18|compilation|PASS|
|xception65_Opset18_timm|compilation|PASS|
|xception71_Opset16|compilation|PASS|
|xception71_Opset17|compilation|PASS|
|xception71_Opset17_timm|compilation|PASS|
|xception71_Opset18|compilation|PASS|
|xcit_large_24_p16_224_Opset16|Numerics|PASS|
|xcit_large_24_p16_224_Opset16_timm|Numerics|PASS|
|xcit_medium_24_p16_384_dist_Opset16_timm|Numerics|PASS|
|xcit_medium_24_p8_384_dist_Opset16_timm|compiled_inference|PASS|
|xcit_nano_12_p16_384_dist_Opset16_timm|Numerics|PASS|
|xcit_nano_12_p8_224_dist_Opset16_timm|Numerics|PASS|
|xcit_nano_12_p8_384_dist_Opset16_timm|Numerics|PASS|
|xcit_small_12_p16_384_dist_Opset16_timm|Numerics|PASS|
|xcit_small_12_p8_384_dist_Opset16_timm|Numerics|PASS|
|xcit_small_24_p8_384_dist_Opset16_timm|Numerics|PASS|
|xcit_tiny_12_p8_224_Opset16|compiled_inference|PASS|
|xcit_tiny_12_p8_224_Opset16_timm|compiled_inference|PASS|
|xcit_tiny_12_p8_224_dist_Opset16|compiled_inference|PASS|
|xcit_tiny_24_p8_224_dist_Opset16_timm|compiled_inference|PASS|

