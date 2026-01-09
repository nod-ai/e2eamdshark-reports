# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.6383|101.6488|0.0105|0.01%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|283.2922|284.3112|1.019|0.36%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.6406|57.8246|0.184|0.32%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|71.9528|71.7477|-0.2051|-0.29%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.2523|286.4533|0.201|0.07%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.6871|38.6817|-0.0054|-0.01%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6311|12.6226|-0.0085|-0.07%|
|migraphx_cadene__dpn92i1|PASS|within tol|10.0607|9.862|-0.1987|-1.98%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.942|21.8569|-0.0851|-0.39%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.0775|6.0703|-0.0072|-0.12%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2462|7.2452|-0.001|-0.01%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.6045|19.6529|0.0484|0.25%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0829|15.1166|0.0337|0.22%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.7309|25.6848|-0.0461|-0.18%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.7455|113.1393|0.3937|0.35%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|14.1761|15.1968|1.0207|7.2%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.7475|17.7469|-0.0006|-0.0%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6821|4.6287|-0.0534|-1.14%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.6971|3.7058|0.0087|0.24%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2843|20.2852|0.0009|0.0%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.9312|33.5247|0.5936|1.8%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.583|52.4649|0.8819|1.71%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8025|11.8097|0.0073|0.06%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5339|12.5408|0.0069|0.06%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8243|12.8786|0.0543|0.42%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.417|12.4322|0.0152|0.12%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7905|12.7647|-0.0258|-0.2%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.439|14.451|0.012|0.08%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.6724|32.2691|0.5967|1.88%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.4799|62.5705|1.0906|1.77%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.1935|97.0581|1.8646|1.96%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7214|12.7297|0.0084|0.07%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.4003|14.3663|-0.0341|-0.24%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.2903|20.2982|0.0079|0.04%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.4145|14.399|-0.0155|-0.11%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5365|20.6032|0.0667|0.32%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.0437|29.3753|0.3316|1.14%|

## 16 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|ResNet18_vaiq|PASS|Numerics|
|ResNet34_vaiq|PASS|Numerics|
|alexnet_Opset17|PASS|Numerics|
|coatnet_0_rw_224.sw_in1k|PASS|compilation|
|coatnet_1_rw_224.sw_in1k|PASS|compilation|
|coatnet_2_rw_224.sw_in12k|PASS|compilation|
|coatnet_2_rw_224.sw_in12k_ft_in1k|PASS|compilation|
|coatnet_rmlp_1_rw2_224.sw_in12k|PASS|compilation|
|coatnet_rmlp_1_rw2_224.sw_in12k_ft_in1k|PASS|compilation|
|coatnet_rmlp_1_rw_224.sw_in1k|PASS|compilation|
|coatnet_rmlp_2_rw_224.sw_in12k|PASS|compilation|
|coatnet_rmlp_2_rw_224.sw_in12k_ft_in1k|PASS|compilation|
|coatnet_rmlp_nano_rw_224.sw_in1k|PASS|compilation|
|cs3darknet_focus_l_train_vaiq|PASS|Numerics|
|inception_v3.tf_in1k_vaiq|PASS|Numerics|
|tf_efficientnetv2_s_Opset17_timm|Numerics|compiled_inference|

## 4 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_224_Opset17|compilation|PASS|
|sequencer2d_m_Opset17_timm|Numerics|PASS|
|squeezenet1.1-7|Numerics|PASS|
|tf_inception_v3_vaiq|Numerics|PASS|

