# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.2177|101.3689|0.1512|0.15%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|282.8731|287.2826|4.4095|1.56%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.8061|57.6089|-0.1972|-0.34%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|71.8873|72.1286|0.2413|0.34%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|285.8049|286.3087|0.5038|0.18%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.8023|38.7085|-0.0938|-0.24%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.67|12.7287|0.0587|0.46%|
|migraphx_cadene__dpn92i1|Numerics|within tol|3.1091|3.1569|0.0478|1.54%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.076|20.1986|0.1227|0.61%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.4803|2.5217|0.0414|1.67%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2402|7.3026|0.0624|0.86%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.779|20.2949|0.5159|2.61%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0855|15.1398|0.0542|0.36%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.9129|25.788|-0.1248|-0.48%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.6652|113.7412|1.076|0.96%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.5916|17.6382|0.0466|0.26%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.4332|3.4379|0.0047|0.14%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.9044|1.8973|-0.0071|-0.37%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2205|20.2533|0.0328|0.16%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.9886|34.0359|1.0473|3.17%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.8741|53.5808|1.7067|3.29%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8034|11.8607|0.0573|0.49%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4597|12.482|0.0224|0.18%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8131|12.8788|0.0657|0.51%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.5021|12.4495|-0.0526|-0.42%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8048|12.7788|-0.026|-0.2%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4132|14.4552|0.042|0.29%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.7576|32.7889|1.0313|3.25%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.5332|63.3815|1.8483|3.0%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.2969|98.4213|3.1244|3.28%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.6959|12.7561|0.0602|0.47%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3389|14.371|0.0321|0.22%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3203|20.328|0.0076|0.04%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3886|14.3759|-0.0127|-0.09%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5399|20.6703|0.1304|0.63%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.1145|29.8733|0.7588|2.61%|

## One Regression Found:

|model name|old_status|new_status|
|---|---|---|

## 111 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|DeepLabV3_resnet50_vaiq_int8|compilation|PASS|
|FCN_vaiq_int8|compilation|PASS|
|ResNet101_vaiq|compilation|PASS|
|ResNet152_vaiq|compilation|PASS|
|ResNet152_vaiq_int8|compilation|PASS|
|ResNet18_vaiq|compilation|PASS|
|ResNet34_vaiq|compilation|PASS|
|ResNet50_vaiq|compilation|PASS|
|VideoResNet_vaiq_int8|compilation|PASS|
|WideResNet_101_2_vaiq|compilation|PASS|
|WideResNet_50_2_vaiq|compilation|PASS|
|WideResNet_50_2_vaiq_int8|compilation|PASS|
|dpn107_vaiq|compilation|PASS|
|dpn98_vaiq|compilation|Numerics|
|eca_resnet33ts.ra2_in1k_vaiq|compilation|PASS|
|eca_resnext26ts.ch_in1k_vaiq|compilation|PASS|
|gernet_l.idstcv_in1k_vaiq|compilation|PASS|
|gernet_m.idstcv_in1k_vaiq|compilation|PASS|
|gluon_resnet101_v1c_vaiq|compilation|PASS|
|gluon_resnet101_v1s_vaiq|compilation|PASS|
|gluon_resnet152_v1c_vaiq|compilation|PASS|
|gluon_resnet152_v1s_vaiq|compilation|PASS|
|gluon_resnet18_v1b_vaiq|compilation|PASS|
|gluon_resnet50_v1c_vaiq|compilation|PASS|
|gluon_resnet50_v1s_vaiq|compilation|PASS|
|gluon_resnext101_32x4d_vaiq|compilation|PASS|
|gluon_resnext101_64x4d_vaiq|compilation|PASS|
|gluon_seresnext101_32x4d_vaiq|compilation|PASS|
|gluon_seresnext101_64x4d_vaiq|compilation|PASS|
|gluon_seresnext50_32x4d_vaiq|compilation|PASS|
|ig_resnext101_32x16d_vaiq|compilation|PASS|
|legacy_seresnet101_vaiq|compilation|PASS|
|legacy_seresnet152_vaiq|compilation|PASS|
|legacy_seresnet18_vaiq|compilation|PASS|
|legacy_seresnet34_vaiq|compilation|PASS|
|legacy_seresnet50_vaiq|compilation|PASS|
|legacy_seresnext101_32x4d_vaiq|compilation|PASS|
|legacy_seresnext26_32x4d_vaiq|compilation|PASS|
|legacy_seresnext50_32x4d_vaiq|compilation|PASS|
|regnetv_040.ra3_in1k_train_vaiq|compilation|PASS|
|regnetv_040.ra3_in1k_vaiq|compilation|PASS|
|regnetx_008.pycls_in1k_vaiq|compilation|PASS|
|regnetx_160.pycls_in1k_vaiq|compilation|PASS|
|regnety_008.pycls_in1k_vaiq|compilation|PASS|
|regnety_040.pycls_in1k_vaiq|compilation|PASS|
|regnety_040.ra3_in1k_train_vaiq|compilation|PASS|
|regnety_040.ra3_in1k_vaiq|compilation|PASS|
|repvgg_b0.rvgg_in1k_vaiq|compilation|PASS|
|repvgg_b1.rvgg_in1k_vaiq|compilation|PASS|
|repvgg_b1g4.rvgg_in1k_vaiq|compilation|PASS|
|repvgg_b3.rvgg_in1k_vaiq|compilation|PASS|
|repvgg_b3g4.rvgg_in1k_vaiq|compilation|PASS|
|res2net101_26w_4s_vaiq|compilation|Numerics|
|res2net50_14w_8s_vaiq|compilation|Numerics|
|res2net50_26w_4s_vaiq|compilation|Numerics|
|res2net50_26w_6s_vaiq|compilation|Numerics|
|res2net50_26w_8s_vaiq|compilation|Numerics|
|res2net50_48w_2s_vaiq|compilation|PASS|
|res2next50_vaiq|compilation|PASS|
|resnet101_test_vaiq|compilation|PASS|
|resnet152_test_vaiq|compilation|PASS|
|resnet18_test_vaiq|compilation|PASS|
|resnet26_test_vaiq|compilation|PASS|
|resnet26_vaiq|compilation|PASS|
|resnet32ts.ra2_in1k_train_vaiq|compilation|PASS|
|resnet32ts.ra2_in1k_vaiq|compilation|PASS|
|resnet33ts.ra2_in1k_train_vaiq|compilation|PASS|
|resnet33ts.ra2_in1k_vaiq|compilation|PASS|
|resnet34_test_vaiq|compilation|PASS|
|resnet50.a1_in1k_vaiq|compilation|PASS|
|resnet50_test_vaiq|compilation|PASS|
|resnet51q.ra2_in1k_train_vaiq|compilation|PASS|
|resnet51q.ra2_in1k_vaiq|compilation|PASS|
|resnet61q.ra2_in1k_train_vaiq|compilation|PASS|
|resnet61q.ra2_in1k_vaiq|compilation|PASS|
|resnetaa50_train_vaiq|compilation|PASS|
|resnetaa50_vaiq|compilation|PASS|
|resnetblur50_test_vaiq|compilation|PASS|
|resnetblur50_vaiq|compilation|PASS|
|resnetv2_101.a1h_in1k_train_vaiq|compilation|PASS|
|resnetv2_101.a1h_in1k_vaiq|compilation|PASS|
|resnetv2_50.a1h_in1k_train_vaiq|compilation|PASS|
|resnetv2_50.a1h_in1k_vaiq|compilation|PASS|
|resnext101_64x4d_train_vaiq|compilation|PASS|
|resnext101_64x4d_vaiq|compilation|PASS|
|resnext26ts.ra2_in1k_train_vaiq|compilation|PASS|
|resnext26ts.ra2_in1k_vaiq|compilation|PASS|
|resnext50_32x4d_test_vaiq|compilation|PASS|
|seresnet33ts.ra2_in1k_vaiq|compilation|PASS|
|seresnet50_test_vaiq|compilation|PASS|
|seresnet50_vaiq|compilation|PASS|
|seresnext101_32x8d_train_vaiq|compilation|PASS|
|seresnext101_32x8d_vaiq|compilation|PASS|
|seresnext26ts.ch_in1k_vaiq|compilation|PASS|
|seresnext50_32x4d_test_vaiq|compilation|PASS|
|skresnet18_vaiq|compilation|PASS|
|skresnet34_vaiq|compilation|PASS|
|skresnext50_32x4d_vaiq|compilation|PASS|
|ssl_resnext101_32x16d_vaiq|compilation|PASS|
|tv_resnet101_vaiq|compilation|PASS|
|tv_resnet152_vaiq|compilation|PASS|
|tv_resnet34_vaiq|compilation|PASS|
|tv_resnet50_vaiq|compilation|PASS|
|tv_resnext50_32x4d_vaiq|compilation|PASS|
|wide_resnet101_2_vaiq|compilation|PASS|
|wide_resnet50_2_test_vaiq|compilation|PASS|
|wide_resnet50_2_vaiq|compilation|PASS|
|xception41_vaiq|compilation|PASS|
|xception41p_vaiq|compilation|PASS|
|xception65_vaiq|compilation|PASS|
|xception65p_vaiq|compilation|PASS|

