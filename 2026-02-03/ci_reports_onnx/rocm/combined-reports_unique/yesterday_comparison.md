# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|99.2995|101.2047|1.9052|1.92%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|292.0947|283.0463|-9.0484|-3.1%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.9113|57.6114|-0.2999|-0.52%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|70.407|72.2693|1.8623|2.65%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|287.2483|285.5261|-1.7223|-0.6%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|39.0529|38.7277|-0.3252|-0.83%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.7759|12.6236|-0.1523|-1.19%|
|migraphx_cadene__dpn92i1|PASS|regression|2.9627|9.8512|6.8884|232.5%|
|migraphx_cadene__inceptionv4i16|Numerics|regression|19.8084|21.818|2.0096|10.15%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|2.3892|6.085|3.6957|154.68%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2733|7.2347|-0.0386|-0.53%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|20.4954|19.5466|-0.9488|-4.63%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1523|15.0826|-0.0697|-0.46%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.3851|25.2516|-1.1335|-4.3%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|113.7618|112.4497|-1.3121|-1.15%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.4422|17.7196|0.2775|1.59%|
|migraphx_torchvision__inceptioni1|Numerics|regression|3.387|4.6305|1.2436|36.72%|
|migraphx_torchvision__resnet50i1|PASS|regression|1.8826|3.6784|1.7957|95.39%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.4248|20.2431|-0.1817|-0.89%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.3341|32.7629|-0.5712|-1.71%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.2865|51.364|-0.9225|-1.76%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8338|11.7829|-0.0509|-0.43%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5781|12.4692|-0.1089|-0.87%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.9314|12.8468|-0.0846|-0.65%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.5476|12.4793|-0.0683|-0.54%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8618|12.7655|-0.0962|-0.75%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.5307|14.3754|-0.1554|-1.07%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.021|31.5588|-0.4622|-1.44%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.2874|61.1531|-1.1343|-1.82%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|96.2034|94.6682|-1.5352|-1.6%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.8376|12.7121|-0.1255|-0.98%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.477|14.3365|-0.1405|-0.97%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.4562|20.2828|-0.1734|-0.85%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.453|14.3645|-0.0885|-0.61%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.737|20.4968|-0.2402|-1.16%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.3087|28.959|-0.3497|-1.19%|

## 627 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|t5-decoder-with-lm-head-12|PASS|native_inference|

## 135 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|RAFT_vaiq_int8|compilation|Numerics|
|bvlcalexnet-12-qdq|compilation|Numerics|
|cs3sedarknet_l_train_vaiq|compilation|PASS|
|cs3sedarknet_x_train_vaiq|compilation|PASS|
|dm_nfnet_f0.dm_in1k_train_vaiq|compilation|PASS|
|dm_nfnet_f0.dm_in1k_vaiq|compilation|PASS|
|dm_nfnet_f1.dm_in1k_train_vaiq|compilation|PASS|
|dm_nfnet_f1.dm_in1k_vaiq|compilation|PASS|
|dm_nfnet_f4.dm_in1k|compilation|PASS|
|eca_nfnet_l0.ra2_in1k_train_vaiq|compilation|PASS|
|eca_nfnet_l1.ra2_in1k_train_vaiq|compilation|PASS|
|eca_nfnet_l2.ra3_in1k_train_vaiq|compilation|PASS|
|eca_nfnet_l2.ra3_in1k_vaiq|compilation|Numerics|
|eca_resnet33ts.ra2_in1k_train_vaiq|compilation|PASS|
|eca_resnext26ts.ch_in1k_train_vaiq|compilation|PASS|
|ecaresnet26t_train_vaiq|compilation|PASS|
|ecaresnet26t_vaiq|compilation|PASS|
|ecaresnet50t_train_vaiq|compilation|PASS|
|ecaresnet50t_vaiq|compilation|PASS|
|efficientnet_b1.ft_in1k_train_vaiq|compilation|PASS|
|efficientnet_b2.ra_in1k_train_vaiq|compilation|Numerics|
|efficientnet_b3.ra2_in1k_train_vaiq|compilation|Numerics|
|efficientnet_b4.ra2_in1k_train_vaiq|compilation|PASS|
|fbnetv3_b.ra2_in1k_vaiq|compilation|Numerics|
|fbnetv3_d.ra2_in1k_vaiq|compilation|Numerics|
|flaubert_Opset17|Numerics|PASS|
|flaubert_Opset18|Numerics|PASS|
|gcresnet33ts.ra2_in1k_train_vaiq|compilation|PASS|
|gcresnet33ts_Opset16|compilation|PASS|
|gcresnet33ts_Opset16_timm|compilation|PASS|
|gcresnet33ts_Opset17|compilation|PASS|
|gcresnet33ts_Opset17_timm|compilation|PASS|
|gcresnet33ts_Opset18|compilation|PASS|
|gcresnet50t.ra2_in1k_train_vaiq|compilation|Numerics|
|gcresnet50t_Opset16|compilation|PASS|
|gcresnet50t_Opset16_timm|compilation|PASS|
|gcresnet50t_Opset17|compilation|PASS|
|gcresnet50t_Opset17_timm|compilation|PASS|
|gcresnet50t_Opset18|compilation|PASS|
|gcresnext26ts.ch_in1k_train_vaiq|compilation|Numerics|
|gcresnext26ts_Opset16|compilation|PASS|
|gcresnext26ts_Opset16_timm|compilation|PASS|
|gcresnext26ts_Opset17|compilation|PASS|
|gcresnext26ts_Opset18|compilation|PASS|
|gcresnext26ts_Opset18_timm|compilation|PASS|
|gcresnext50ts.ch_in1k_train_vaiq|compilation|Numerics|
|gcresnext50ts_Opset16|compilation|PASS|
|gcresnext50ts_Opset16_timm|compilation|PASS|
|gcresnext50ts_Opset17|compilation|PASS|
|gcresnext50ts_Opset18|compilation|PASS|
|gcresnext50ts_Opset18_timm|compilation|PASS|
|migraphx_pytorch-examples__wlang_gru|compiled_inference|PASS|
|nf_regnet_b1.ra2_in1k_train_vaiq|compilation|PASS|
|nfnet_l0.ra2_in1k_train_vaiq|compilation|PASS|
|pytorch-3dunet_vaiq_int8|compilation|Numerics|
|regnet_x_32gf_Opset16|compilation|PASS|
|regnet_x_32gf_Opset16_torch_hub|compilation|PASS|
|regnet_x_32gf_Opset17|compilation|PASS|
|regnet_x_32gf_Opset18|compilation|PASS|
|regnet_y_32gf_Opset16|compilation|PASS|
|regnet_y_32gf_Opset17|compilation|PASS|
|regnet_y_32gf_Opset18|compilation|PASS|
|regnet_y_32gf_Opset18_torch_hub|compilation|PASS|
|regnetx_040.pycls_in1k_vaiq|compilation|PASS|
|regnetx_080.pycls_in1k_vaiq|compilation|PASS|
|regnetx_160.pycls_in1k_vaiq|compilation|PASS|
|regnetx_320_Opset16|compilation|PASS|
|regnetx_320_Opset17|compilation|PASS|
|regnetx_320_Opset17_timm|compilation|PASS|
|regnetx_320_Opset18|compilation|PASS|
|regnety_040.pycls_in1k_vaiq|compilation|PASS|
|regnety_040.ra3_in1k_train_vaiq|compilation|PASS|
|regnety_040.ra3_in1k_vaiq|compilation|PASS|
|regnety_320.pycls_in1k_vaiq|compilation|PASS|
|regnety_320.seer_ft_in1k_vaiq|compilation|PASS|
|regnety_320_Opset16|compilation|PASS|
|regnety_320_Opset17|compilation|PASS|
|regnety_320_Opset17_timm|compilation|PASS|
|regnety_640.seer_ft_in1k_vaiq|compilation|PASS|
|regnetz_040.ra3_in1k_train_vaiq|compilation|PASS|
|regnetz_040.ra3_in1k_vaiq|compilation|PASS|
|regnetz_040_h.ra3_in1k_train_vaiq|compilation|PASS|
|regnetz_040_h.ra3_in1k_vaiq|compilation|PASS|
|regnetz_c16_evos.ch_in1k_train_vaiq|compilation|Numerics|
|regnetz_c16_evos.ch_in1k_vaiq|compilation|Numerics|
|regnetz_d32.ra3_in1k_train_vaiq|compilation|PASS|
|regnetz_d32.ra3_in1k_vaiq|compilation|PASS|
|regnetz_d8.ra3_in1k_train_vaiq|compilation|PASS|
|regnetz_d8.ra3_in1k_vaiq|compilation|PASS|
|regnetz_d8_evos.ch_in1k_train_vaiq|compilation|PASS|
|regnetz_d8_evos.ch_in1k_vaiq|compilation|PASS|
|regnetz_e8.ra3_in1k_train_vaiq|compilation|PASS|
|regnetz_e8.ra3_in1k_vaiq|compilation|PASS|
|repvgg_b1g4.rvgg_in1k_vaiq|compilation|PASS|
|repvgg_b2g4.rvgg_in1k_vaiq|compilation|PASS|
|resnest101e_vaiq|compilation|PASS|
|resnest14d_vaiq|compilation|PASS|
|resnest26d_vaiq|compilation|PASS|
|resnest50d_vaiq|compilation|PASS|
|resnet50_gn_test_vaiq|compilation|Numerics|
|resnet50_gn_vaiq|compilation|PASS|
|resnetrs101_train_vaiq|compilation|PASS|
|resnetrs152_train_vaiq|compilation|PASS|
|resnetrs152_vaiq|compilation|PASS|
|resnetrs200_train_vaiq|compilation|PASS|
|resnetrs200_vaiq|compilation|PASS|
|resnetv2_101x1_bit.goog_in21k_ft_in1k_vaiq|compilation|Numerics|
|resnetv2_152x2_bit.goog_in21k_ft_in1k_vaiq|compilation|Numerics|
|resnetv2_152x2_bit.goog_teacher_in21k_ft_in1k_vaiq|compilation|Numerics|
|resnetv2_50d_evos.ah_in1k_train_vaiq|compilation|PASS|
|resnetv2_50d_evos.ah_in1k_vaiq|compilation|PASS|
|resnetv2_50d_gn.ah_in1k_train_vaiq|compilation|PASS|
|resnetv2_50d_gn.ah_in1k_vaiq|compilation|Numerics|
|resnetv2_50x1_bit.goog_distilled_in1k_vaiq|compilation|PASS|
|resnetv2_50x1_bit.goog_in21k_ft_in1k_vaiq|compilation|Numerics|
|resnetv2_50x3_bit.goog_in21k_ft_in1k_vaiq|compilation|Numerics|
|sequencer2d_l_Opset16|compiled_inference|Numerics|
|sequencer2d_l_Opset16_timm|compiled_inference|Numerics|
|sequencer2d_l_Opset17|compiled_inference|Numerics|
|sequencer2d_l_Opset17_timm|compiled_inference|Numerics|
|sequencer2d_m_Opset16|compiled_inference|Numerics|
|sequencer2d_m_Opset16_timm|compiled_inference|Numerics|
|sequencer2d_m_Opset17|compiled_inference|PASS|
|sequencer2d_m_Opset17_timm|compiled_inference|PASS|
|sequencer2d_s_Opset16|compiled_inference|Numerics|
|sequencer2d_s_Opset16_timm|compiled_inference|Numerics|
|sequencer2d_s_Opset17|compiled_inference|Numerics|
|sequencer2d_s_Opset17_timm|compiled_inference|PASS|
|seresnet152d_train_vaiq|compilation|PASS|
|seresnet152d_vaiq|compilation|PASS|
|seresnet33ts.ra2_in1k_train_vaiq|compilation|PASS|
|seresnext26ts.ch_in1k_train_vaiq|compilation|PASS|
|seresnextaa101d_32x8d_test_vaiq|compilation|PASS|
|squeezebert_Opset16|compilation|PASS|
|tinynet_a.in1k_vaiq|compilation|Numerics|

