# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|102.2971|100.961|-1.3361|-1.31%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|286.3179|283.746|-2.5718|-0.9%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|58.5676|57.3895|-1.1781|-2.01%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|75.8251|71.6316|-4.1935|-5.53%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|294.6921|285.6715|-9.0207|-3.06%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|40.9443|38.8035|-2.1408|-5.23%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6842|12.6109|-0.0733|-0.58%|
|migraphx_cadene__dpn92i1|PASS|within tol|10.1818|9.9692|-0.2126|-2.09%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.9316|21.803|-0.1286|-0.59%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.1608|6.0944|-0.0664|-1.08%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2977|7.232|-0.0658|-0.9%|
|migraphx_mlperf__bert_large_mlperf|Numerics|progression|20.7578|19.5225|-1.2352|-5.95%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1202|15.0504|-0.0698|-0.46%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.6428|25.7877|-0.8551|-3.21%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|113.109|112.6735|-0.4355|-0.39%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|16.3935|14.3548|-2.0387|-12.44%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.8043|17.7209|-0.0834|-0.47%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6989|4.6253|-0.0735|-1.57%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.7137|3.6742|-0.0395|-1.06%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.3269|20.2432|-0.0836|-0.41%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.8937|33.0165|0.1229|0.37%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.5251|51.6364|0.1113|0.22%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8791|11.7771|-0.102|-0.86%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5788|12.508|-0.0708|-0.56%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.9037|12.8113|-0.0925|-0.72%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4762|12.403|-0.0732|-0.59%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8779|12.8082|-0.0697|-0.54%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4744|14.4229|-0.0514|-0.36%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.6178|31.7326|0.1148|0.36%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.378|61.4367|0.0587|0.1%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.1125|95.1171|0.0047|0.0%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7834|12.6849|-0.0985|-0.77%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.4096|14.3588|-0.0508|-0.35%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3515|20.2832|-0.0683|-0.34%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.4263|14.3634|-0.0629|-0.44%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6138|20.5271|-0.0867|-0.42%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.0474|29.0618|0.0144|0.05%|

## 9 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_224_Opset17|PASS|compilation|
|coatnet_2_rw_224.sw_in12k|PASS|compilation|
|coatnet_rmlp_1_rw2_224.sw_in12k|PASS|compilation|
|coatnet_rmlp_1_rw2_224.sw_in12k_ft_in1k|PASS|compilation|
|coatnet_rmlp_1_rw_224.sw_in1k|PASS|compilation|
|coatnet_rmlp_2_rw_224.sw_in12k|PASS|compilation|
|coatnet_rmlp_2_rw_224.sw_in12k_ft_in1k|PASS|compilation|
|sequencer2d_m_Opset16|PASS|Numerics|
|sequencer2d_m_Opset17_timm|PASS|Numerics|

## 76 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|alexnet_Opset18_torch_hub|Numerics|PASS|
|dm_nfnet_f1.dm_in1k_train_vaiq|Numerics|PASS|
|dpn107_vaiq|Numerics|PASS|
|dpn131_vaiq|Numerics|PASS|
|dpn68_vaiq|Numerics|PASS|
|eca_nfnet_l0.ra2_in1k_train_vaiq|Numerics|PASS|
|eca_resnext26ts.ch_in1k_vaiq|Numerics|PASS|
|efficientnet_b2_pruned.in1k|Numerics|PASS|
|efficientnet_b3_pruned.in1k|Numerics|PASS|
|gluon_resnext101_32x4d_vaiq|Numerics|PASS|
|gluon_resnext101_64x4d_vaiq|Numerics|PASS|
|gluon_seresnext101_32x4d_vaiq|Numerics|PASS|
|gluon_seresnext101_64x4d_vaiq|Numerics|PASS|
|gluon_seresnext50_32x4d_vaiq|Numerics|PASS|
|ig_resnext101_32x16d_vaiq|Numerics|PASS|
|legacy_seresnext101_32x4d_vaiq|Numerics|PASS|
|legacy_seresnext26_32x4d_vaiq|Numerics|PASS|
|legacy_seresnext50_32x4d_vaiq|Numerics|PASS|
|migraphx_cadene__dpn92i1|Numerics|PASS|
|mixnet_m_Opset16|Numerics|PASS|
|mixnet_m_Opset16_timm|Numerics|PASS|
|mixnet_m_Opset17|Numerics|PASS|
|mixnet_s_Opset16|Numerics|PASS|
|mixnet_s_Opset16_timm|Numerics|PASS|
|mixnet_s_Opset17|Numerics|PASS|
|nfnet_l0.ra2_in1k_train_vaiq|Numerics|PASS|
|regnetz_d32.ra3_in1k_vaiq|Numerics|PASS|
|repvgg_a2.rvgg_in1k_vaiq|Numerics|PASS|
|res2next50_vaiq|Numerics|PASS|
|resnet10t_Opset16|compiled_inference|Numerics|
|resnet10t_Opset17|compiled_inference|Numerics|
|resnet10t_Opset18|compiled_inference|Numerics|
|resnet51q.ra2_in1k_vaiq|Numerics|PASS|
|resnet61q.ra2_in1k_vaiq|Numerics|PASS|
|resnext101_64x4d_train_vaiq|Numerics|PASS|
|resnext101_64x4d_vaiq|Numerics|PASS|
|resnext26ts.ra2_in1k_vaiq|Numerics|PASS|
|resnext50_32x4d_test_vaiq|Numerics|PASS|
|resnext50d_32x4d_test_vaiq|Numerics|PASS|
|resnext50d_32x4d_vaiq|Numerics|PASS|
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
|sequencer2d_m_Opset17|Numerics|PASS|
|sequencer2d_s_Opset17|Numerics|PASS|
|sequencer2d_s_vaiq|compilation|Numerics|
|seresnext101_32x8d_train_vaiq|Numerics|PASS|
|seresnext101_32x8d_vaiq|Numerics|PASS|
|seresnext101d_32x8d_train_vaiq|Numerics|PASS|
|seresnext101d_32x8d_vaiq|Numerics|PASS|
|seresnext26d_32x4d_test_vaiq|Numerics|PASS|
|seresnext26d_32x4d_vaiq|Numerics|PASS|
|seresnext26t_32x4d_test_vaiq|Numerics|PASS|
|seresnext26t_32x4d_vaiq|Numerics|PASS|
|seresnext26ts.ch_in1k_vaiq|Numerics|PASS|
|seresnext50_32x4d_test_vaiq|Numerics|PASS|
|seresnextaa101d_32x8d_test_vaiq|Numerics|PASS|
|seresnextaa101d_32x8d_vaiq|Numerics|PASS|
|shufflenet-7|Numerics|PASS|
|skresnext50_32x4d_vaiq|Numerics|PASS|
|squeezenet1.0-6|Numerics|PASS|
|t5-decoder-with-lm-head-12|native_inference|PASS|
|tf_mixnet_m.in1k|Numerics|PASS|
|tf_mixnet_m_Opset16_timm|Numerics|PASS|
|tf_mixnet_s.in1k|Numerics|PASS|
|tf_mixnet_s_Opset16_timm|Numerics|PASS|
|tv_resnext50_32x4d_vaiq|Numerics|PASS|

