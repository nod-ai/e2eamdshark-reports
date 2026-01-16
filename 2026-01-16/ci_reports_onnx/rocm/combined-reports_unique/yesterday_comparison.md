# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|100.6267|100.6989|0.0723|0.07%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|283.0087|282.3085|-0.7002|-0.25%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.5936|57.6294|0.0357|0.06%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.0095|71.8174|-0.1921|-0.27%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|285.7729|285.7505|-0.0224|-0.01%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.4564|38.8225|0.3661|0.95%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6338|12.686|0.0522|0.41%|
|migraphx_cadene__dpn92i1|Numerics|within tol|3.1013|3.1085|0.0071|0.23%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.0825|20.1345|0.052|0.26%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.4543|2.4753|0.021|0.86%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.223|7.2463|0.0233|0.32%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.328|19.7742|0.4461|2.31%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0678|15.1044|0.0366|0.24%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.1235|25.8874|0.764|3.04%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.4932|113.0416|0.5484|0.49%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.5142|17.6229|0.1087|0.62%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.4286|3.4377|0.0091|0.27%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.899|1.9043|0.0053|0.28%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2083|20.2806|0.0723|0.36%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.8096|33.1145|0.3049|0.93%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.5148|52.0303|0.5155|1.0%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7809|11.7943|0.0134|0.11%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5092|12.5332|0.024|0.19%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.81|12.8927|0.0827|0.65%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.3991|12.4165|0.0174|0.14%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7955|12.7881|-0.0075|-0.06%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.3526|14.4521|0.0995|0.69%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.6711|31.8574|0.1863|0.59%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.3308|61.8907|0.5599|0.91%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.0362|95.9698|0.9336|0.98%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.6976|12.738|0.0403|0.32%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3671|14.3929|0.0258|0.18%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3019|20.3245|0.0226|0.11%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.386|14.3947|0.0087|0.06%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5504|20.5748|0.0244|0.12%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.0199|29.127|0.1071|0.37%|

## 221 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|DeepLabV3_resnet50_vaiq_int8|PASS|compilation|
|EfficientNet_b0_vaiq|Numerics|compilation|
|EfficientNet_b2_vaiq|Numerics|compilation|
|EfficientNet_b3_vaiq|Numerics|compilation|
|EfficientNet_b4_vaiq|Numerics|compilation|
|FCN_vaiq_int8|PASS|compilation|
|RAFT_vaiq_int8|Numerics|compilation|
|ResNet101_vaiq|PASS|compilation|
|ResNet152_vaiq|PASS|compilation|
|ResNet152_vaiq_int8|PASS|compilation|
|ResNet18_vaiq|PASS|compilation|
|ResNet34_vaiq|PASS|compilation|
|ResNet50_vaiq|PASS|compilation|
|VideoResNet_vaiq_int8|PASS|compilation|
|WideResNet_101_2_vaiq|PASS|compilation|
|WideResNet_50_2_vaiq|PASS|compilation|
|WideResNet_50_2_vaiq_int8|PASS|compilation|
|cs3se_edgenet_x_train_vaiq|PASS|compilation|
|cs3se_edgenet_x_vaiq|PASS|compilation|
|cs3sedarknet_l_train_vaiq|PASS|compilation|
|cs3sedarknet_x_train_vaiq|PASS|compilation|
|dm_nfnet_f4.dm_in1k|PASS|compilation|
|dpn107_vaiq|PASS|compilation|
|dpn98_vaiq|Numerics|compilation|
|eca_nfnet_l1.ra2_in1k_train_vaiq|PASS|compilation|
|eca_nfnet_l2.ra3_in1k_train_vaiq|PASS|compilation|
|eca_nfnet_l2.ra3_in1k_vaiq|Numerics|compilation|
|eca_resnet33ts.ra2_in1k_train_vaiq|PASS|compilation|
|eca_resnet33ts.ra2_in1k_vaiq|PASS|compilation|
|eca_resnext26ts.ch_in1k_train_vaiq|PASS|compilation|
|eca_resnext26ts.ch_in1k_vaiq|PASS|compilation|
|ecaresnet26t_train_vaiq|PASS|compilation|
|ecaresnet26t_vaiq|PASS|compilation|
|ecaresnet50t_train_vaiq|PASS|compilation|
|ecaresnet50t_vaiq|PASS|compilation|
|efficientnet_b0.ra_in1k_vaiq|Numerics|compilation|
|efficientnet_b1.ft_in1k_train_vaiq|PASS|compilation|
|efficientnet_b1.ft_in1k_vaiq|PASS|compilation|
|efficientnet_b2.ra_in1k_train_vaiq|Numerics|compilation|
|efficientnet_b2.ra_in1k_vaiq|Numerics|compilation|
|efficientnet_b3.ra2_in1k_train_vaiq|Numerics|compilation|
|efficientnet_b3.ra2_in1k_vaiq|Numerics|compilation|
|efficientnet_b4.ra2_in1k_train_vaiq|PASS|compilation|
|efficientnet_b4.ra2_in1k_vaiq|Numerics|compilation|
|efficientnet_b5.sw_in12k_vaiq|Numerics|compilation|
|fbnetv3_b.ra2_in1k_vaiq|Numerics|compilation|
|fbnetv3_d.ra2_in1k_vaiq|Numerics|compilation|
|flaubert_Opset17|PASS|Numerics|
|flaubert_Opset17_transformers|PASS|Numerics|
|flaubert_Opset18|PASS|Numerics|
|gcresnet33ts.ra2_in1k_train_vaiq|PASS|compilation|
|gcresnet33ts_Opset16|PASS|compilation|
|gcresnet33ts_Opset16_timm|PASS|compilation|
|gcresnet33ts_Opset17|PASS|compilation|
|gcresnet33ts_Opset17_timm|PASS|compilation|
|gcresnet33ts_Opset18|PASS|compilation|
|gcresnet50t.ra2_in1k_train_vaiq|Numerics|compilation|
|gcresnet50t_Opset16|PASS|compilation|
|gcresnet50t_Opset16_timm|PASS|compilation|
|gcresnet50t_Opset17|PASS|compilation|
|gcresnet50t_Opset17_timm|PASS|compilation|
|gcresnet50t_Opset18|PASS|compilation|
|gcresnext26ts.ch_in1k_train_vaiq|Numerics|compilation|
|gcresnext26ts_Opset16|PASS|compilation|
|gcresnext26ts_Opset16_timm|PASS|compilation|
|gcresnext26ts_Opset17|PASS|compilation|
|gcresnext26ts_Opset18|PASS|compilation|
|gcresnext26ts_Opset18_timm|PASS|compilation|
|gcresnext50ts.ch_in1k_train_vaiq|Numerics|compilation|
|gcresnext50ts_Opset16|PASS|compilation|
|gcresnext50ts_Opset16_timm|PASS|compilation|
|gcresnext50ts_Opset17|PASS|compilation|
|gcresnext50ts_Opset18|PASS|compilation|
|gcresnext50ts_Opset18_timm|PASS|compilation|
|gernet_l.idstcv_in1k_vaiq|PASS|compilation|
|gernet_m.idstcv_in1k_vaiq|PASS|compilation|
|gluon_resnet101_v1c_vaiq|PASS|compilation|
|gluon_resnet101_v1s_vaiq|PASS|compilation|
|gluon_resnet152_v1c_vaiq|PASS|compilation|
|gluon_resnet152_v1s_vaiq|PASS|compilation|
|gluon_resnet18_v1b_vaiq|PASS|compilation|
|gluon_resnet50_v1c_vaiq|PASS|compilation|
|gluon_resnet50_v1s_vaiq|PASS|compilation|
|gluon_resnext101_32x4d_vaiq|PASS|compilation|
|gluon_resnext101_64x4d_vaiq|PASS|compilation|
|gluon_seresnext101_32x4d_vaiq|PASS|compilation|
|gluon_seresnext101_64x4d_vaiq|PASS|compilation|
|gluon_seresnext50_32x4d_vaiq|PASS|compilation|
|ig_resnext101_32x16d_vaiq|PASS|compilation|
|legacy_seresnet101_vaiq|PASS|compilation|
|legacy_seresnet152_vaiq|PASS|compilation|
|legacy_seresnet18_vaiq|PASS|compilation|
|legacy_seresnet34_vaiq|PASS|compilation|
|legacy_seresnet50_vaiq|PASS|compilation|
|legacy_seresnext101_32x4d_vaiq|PASS|compilation|
|legacy_seresnext26_32x4d_vaiq|PASS|compilation|
|legacy_seresnext50_32x4d_vaiq|PASS|compilation|
|nf_regnet_b1.ra2_in1k_train_vaiq|PASS|compilation|
|nf_regnet_b1_Opset16|Numerics|compilation|
|nf_regnet_b1_Opset16_timm|Numerics|compilation|
|nf_regnet_b1_Opset17|Numerics|compilation|
|pytorch-3dunet_vaiq_int8|Numerics|compilation|
|regnetv_040.ra3_in1k_train_vaiq|PASS|compilation|
|regnetv_040.ra3_in1k_vaiq|PASS|compilation|
|regnetx_008.pycls_in1k_vaiq|PASS|compilation|
|regnetx_160.pycls_in1k_vaiq|PASS|compilation|
|regnety_008.pycls_in1k_vaiq|PASS|compilation|
|regnety_040.pycls_in1k_vaiq|PASS|compilation|
|regnety_040.ra3_in1k_train_vaiq|PASS|compilation|
|regnety_040.ra3_in1k_vaiq|PASS|compilation|
|regnety_320.seer_ft_in1k_vaiq|PASS|compilation|
|regnety_640.seer_ft_in1k_vaiq|PASS|compilation|
|regnetz_040.ra3_in1k_train_vaiq|PASS|compilation|
|regnetz_040.ra3_in1k_vaiq|PASS|compilation|
|regnetz_040_h.ra3_in1k_train_vaiq|PASS|compilation|
|regnetz_040_h.ra3_in1k_vaiq|PASS|compilation|
|regnetz_c16.ra3_in1k_vaiq|PASS|compilation|
|regnetz_c16_evos.ch_in1k_train_vaiq|PASS|compilation|
|regnetz_c16_evos.ch_in1k_vaiq|PASS|compilation|
|regnetz_d32.ra3_in1k_train_vaiq|PASS|compilation|
|regnetz_d32.ra3_in1k_vaiq|PASS|compilation|
|regnetz_d8.ra3_in1k_train_vaiq|PASS|compilation|
|regnetz_d8.ra3_in1k_vaiq|PASS|compilation|
|regnetz_d8_evos.ch_in1k_train_vaiq|PASS|compilation|
|regnetz_d8_evos.ch_in1k_vaiq|PASS|compilation|
|regnetz_e8.ra3_in1k_train_vaiq|PASS|compilation|
|regnetz_e8.ra3_in1k_vaiq|PASS|compilation|
|repvgg_b0.rvgg_in1k_vaiq|PASS|compilation|
|repvgg_b1.rvgg_in1k_vaiq|PASS|compilation|
|repvgg_b1g4.rvgg_in1k_vaiq|PASS|compilation|
|repvgg_b3.rvgg_in1k_vaiq|PASS|compilation|
|repvgg_b3g4.rvgg_in1k_vaiq|PASS|compilation|
|repvgg_b3g4_Opset16|PASS|compilation|
|repvgg_b3g4_Opset16_timm|PASS|compilation|
|repvgg_b3g4_Opset17|PASS|compilation|
|repvgg_b3g4_Opset18|PASS|compilation|
|res2net101_26w_4s_vaiq|Numerics|compilation|
|res2net50_14w_8s_vaiq|Numerics|compilation|
|res2net50_26w_4s_vaiq|Numerics|compilation|
|res2net50_26w_6s_vaiq|Numerics|compilation|
|res2net50_26w_8s_vaiq|Numerics|compilation|
|res2net50_48w_2s_vaiq|PASS|compilation|
|res2next50_vaiq|PASS|compilation|
|resnest101e_vaiq|PASS|compilation|
|resnet101_test_vaiq|PASS|compilation|
|resnet152_test_vaiq|PASS|compilation|
|resnet18_test_vaiq|PASS|compilation|
|resnet26_test_vaiq|PASS|compilation|
|resnet26_vaiq|PASS|compilation|
|resnet32ts.ra2_in1k_train_vaiq|PASS|compilation|
|resnet32ts.ra2_in1k_vaiq|PASS|compilation|
|resnet33ts.ra2_in1k_train_vaiq|PASS|compilation|
|resnet33ts.ra2_in1k_vaiq|PASS|compilation|
|resnet34_test_vaiq|PASS|compilation|
|resnet50.a1_in1k_vaiq|PASS|compilation|
|resnet50_gn_test_vaiq|Numerics|compilation|
|resnet50_gn_vaiq|PASS|compilation|
|resnet50_test_vaiq|PASS|compilation|
|resnet51q.ra2_in1k_train_vaiq|PASS|compilation|
|resnet51q.ra2_in1k_vaiq|PASS|compilation|
|resnet61q.ra2_in1k_train_vaiq|PASS|compilation|
|resnet61q.ra2_in1k_vaiq|PASS|compilation|
|resnetaa50_train_vaiq|PASS|compilation|
|resnetaa50_vaiq|PASS|compilation|
|resnetblur50_test_vaiq|PASS|compilation|
|resnetblur50_vaiq|PASS|compilation|
|resnetrs101_train_vaiq|PASS|compilation|
|resnetrs152_train_vaiq|PASS|compilation|
|resnetrs152_vaiq|PASS|compilation|
|resnetrs200_train_vaiq|PASS|compilation|
|resnetrs200_vaiq|PASS|compilation|
|resnetv2_101.a1h_in1k_train_vaiq|PASS|compilation|
|resnetv2_101.a1h_in1k_vaiq|PASS|compilation|
|resnetv2_101x1_bit.goog_in21k_ft_in1k_vaiq|Numerics|compilation|
|resnetv2_152x2_bit.goog_in21k_ft_in1k_vaiq|Numerics|compilation|
|resnetv2_152x2_bit.goog_teacher_in21k_ft_in1k_vaiq|Numerics|compilation|
|resnetv2_50.a1h_in1k_train_vaiq|PASS|compilation|
|resnetv2_50.a1h_in1k_vaiq|PASS|compilation|
|resnetv2_50d_evos.ah_in1k_train_vaiq|PASS|compilation|
|resnetv2_50d_evos.ah_in1k_vaiq|PASS|compilation|
|resnetv2_50d_gn.ah_in1k_train_vaiq|PASS|compilation|
|resnetv2_50d_gn.ah_in1k_vaiq|Numerics|compilation|
|resnetv2_50x1_bit.goog_distilled_in1k_vaiq|PASS|compilation|
|resnetv2_50x1_bit.goog_in21k_ft_in1k_vaiq|Numerics|compilation|
|resnetv2_50x3_bit.goog_in21k_ft_in1k_vaiq|Numerics|compilation|
|resnext101_64x4d_train_vaiq|PASS|compilation|
|resnext101_64x4d_vaiq|PASS|compilation|
|resnext26ts.ra2_in1k_train_vaiq|PASS|compilation|
|resnext26ts.ra2_in1k_vaiq|PASS|compilation|
|resnext50_32x4d_test_vaiq|PASS|compilation|
|sequencer2d_m_vaiq|compiled_inference|compilation|
|sequencer2d_s_vaiq|compiled_inference|compilation|
|seresnet152d_train_vaiq|PASS|compilation|
|seresnet152d_vaiq|PASS|compilation|
|seresnet33ts.ra2_in1k_train_vaiq|PASS|compilation|
|seresnet33ts.ra2_in1k_vaiq|PASS|compilation|
|seresnet50_test_vaiq|PASS|compilation|
|seresnet50_vaiq|PASS|compilation|
|seresnext101_32x8d_train_vaiq|PASS|compilation|
|seresnext101_32x8d_vaiq|PASS|compilation|
|seresnext26ts.ch_in1k_train_vaiq|PASS|compilation|
|seresnext26ts.ch_in1k_vaiq|PASS|compilation|
|seresnext50_32x4d_test_vaiq|PASS|compilation|
|seresnextaa101d_32x8d_test_vaiq|PASS|compilation|
|skresnet18_vaiq|PASS|compilation|
|skresnet34_vaiq|PASS|compilation|
|skresnext50_32x4d_vaiq|PASS|compilation|
|ssl_resnext101_32x16d_vaiq|PASS|compilation|
|tinynet_a.in1k_vaiq|Numerics|compilation|
|tv_resnet101_vaiq|PASS|compilation|
|tv_resnet152_vaiq|PASS|compilation|
|tv_resnet34_vaiq|PASS|compilation|
|tv_resnet50_vaiq|PASS|compilation|
|tv_resnext50_32x4d_vaiq|PASS|compilation|
|wide_resnet101_2_vaiq|PASS|compilation|
|wide_resnet50_2_test_vaiq|PASS|compilation|
|wide_resnet50_2_vaiq|PASS|compilation|
|xception41_vaiq|PASS|compilation|
|xception41p_vaiq|PASS|compilation|
|xception65_vaiq|PASS|compilation|
|xception65p_vaiq|PASS|compilation|

## One Progression Found:

|model name|old_status|new_status|
|---|---|---|
|migx_bench_bert-large-uncased_16_384|Numerics|PASS|

