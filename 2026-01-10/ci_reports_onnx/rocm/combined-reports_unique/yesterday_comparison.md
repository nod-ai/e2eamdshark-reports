# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.6488|101.1589|-0.4899|-0.48%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|284.3112|283.0061|-1.3051|-0.46%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.8246|57.5795|-0.2451|-0.42%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|71.7477|72.4973|0.7497|1.04%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.4533|286.2312|-0.222|-0.08%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.6817|38.7595|0.0778|0.2%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6226|12.6248|0.0022|0.02%|
|migraphx_cadene__dpn92i1|PASS|within tol|9.862|9.8069|-0.0551|-0.56%|
|migraphx_cadene__inceptionv4i16|Numerics|progression|21.8569|20.1136|-1.7433|-7.98%|
|migraphx_cadene__resnext101_64x4di1|Numerics|progression|6.0703|3.293|-2.7773|-45.75%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2452|7.238|-0.0072|-0.1%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.6529|19.6161|-0.0368|-0.19%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1166|15.1223|0.0057|0.04%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.6848|25.8387|0.1539|0.6%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|113.1393|112.7854|-0.3538|-0.31%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|15.1968|14.6157|-0.5811|-3.82%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.7469|17.5781|-0.1688|-0.95%|
|migraphx_torchvision__inceptioni1|PASS|progression|4.6287|3.431|-1.1977|-25.87%|
|migraphx_torchvision__resnet50i1|PASS|progression|3.7058|1.9012|-1.8045|-48.7%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2852|20.2773|-0.0079|-0.04%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.5247|32.8712|-0.6536|-1.95%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.4649|51.5472|-0.9177|-1.75%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8097|11.7695|-0.0402|-0.34%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5408|12.5243|-0.0165|-0.13%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8786|12.8694|-0.0092|-0.07%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4322|12.5096|0.0774|0.62%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7647|12.7582|-0.0065|-0.05%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.451|14.4433|-0.0077|-0.05%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.2691|31.6143|-0.6548|-2.03%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.5705|61.3128|-1.2578|-2.01%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|97.0581|95.0067|-2.0514|-2.11%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7297|12.7142|-0.0155|-0.12%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3663|14.3707|0.0044|0.03%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.2982|20.2946|-0.0036|-0.02%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.399|14.3882|-0.0108|-0.07%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6032|20.5955|-0.0078|-0.04%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.3753|29.0103|-0.3649|-1.24%|

## 4 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|AlexNet_vaiq_int8|PASS|Numerics|
|migraphx_cadene__resnext101_64x4di1|PASS|Numerics|
|sequencer2d_m_Opset17_timm|PASS|Numerics|
|squeezenet1.1-7|PASS|Numerics|

## 50 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|coatnet_rmlp_nano_rw_224.sw_in1k|compilation|PASS|
|convit_tiny_Opset16|compilation|PASS|
|cs3darknet_focus_l_train_vaiq|Numerics|PASS|
|efficientnet_v2_l_Opset18|Numerics|PASS|
|gernet_m_Opset16|compiled_inference|PASS|
|gernet_m_Opset17|compiled_inference|PASS|
|gernet_m_Opset18|compiled_inference|PASS|
|gluon_resnet18_v1b_Opset16|compiled_inference|PASS|
|gluon_resnet18_v1b_Opset17|compiled_inference|PASS|
|gluon_resnet18_v1b_Opset18|compiled_inference|PASS|
|gluon_resnet34_v1b_Opset16|compiled_inference|PASS|
|gluon_resnet34_v1b_Opset17|compiled_inference|PASS|
|gluon_resnet34_v1b_Opset18|compiled_inference|PASS|
|migraphx_torchvision__inceptioni1|Numerics|PASS|
|resnet34_test_vaiq|Numerics|PASS|
|resnet34d_test_vaiq|Numerics|PASS|
|resnet34d_vaiq|Numerics|PASS|
|selecsls42b_vaiq|compilation|PASS|
|sequencer2d_m_vaiq|compilation|Numerics|
|sequencer2d_s_vaiq|compilation|Numerics|
|skresnet18_Opset16|compiled_inference|PASS|
|skresnet18_Opset17|compiled_inference|PASS|
|skresnet34_Opset16|compiled_inference|PASS|
|skresnet34_Opset17|compiled_inference|PASS|
|t5-decoder-with-lm-head-12|native_inference|PASS|
|tf_efficientnet_el.in1k_vaiq|compilation|PASS|
|tf_efficientnet_em.in1k_vaiq|compilation|PASS|
|tf_efficientnetv2_b0.in1k_vaiq|compilation|PASS|
|tf_efficientnetv2_b1.in1k_vaiq|compilation|Numerics|
|tf_efficientnetv2_b2.in1k_train_vaiq|Numerics|PASS|
|tf_efficientnetv2_b3.in1k_train_vaiq|compilation|PASS|
|tf_efficientnetv2_b3.in1k_vaiq|compilation|PASS|
|tf_efficientnetv2_s_Opset17_timm|compiled_inference|Numerics|
|tinynet_e_Opset16|Numerics|PASS|
|tinynet_e_Opset17|Numerics|PASS|
|tv_resnet34_vaiq|Numerics|PASS|
|xception41p_vaiq|compilation|PASS|
|xception65p_vaiq|compilation|PASS|
|xcit_large_24_p16_224_dist_Opset16|Numerics|PASS|
|xcit_medium_24_p16_384_dist_Opset16|Numerics|PASS|
|xcit_medium_24_p8_384_dist_Opset16|compiled_inference|PASS|
|xcit_nano_12_p16_384_dist_Opset16|Numerics|PASS|
|xcit_nano_12_p8_224_Opset16|Numerics|PASS|
|xcit_nano_12_p8_224_dist_Opset16|Numerics|PASS|
|xcit_nano_12_p8_384_dist_Opset16|Numerics|PASS|
|xcit_small_12_p16_384_dist_Opset16|Numerics|PASS|
|xcit_small_12_p8_384_dist_Opset16|Numerics|PASS|
|xcit_small_24_p8_384_dist_Opset16|Numerics|PASS|
|xcit_tiny_24_p8_224_Opset16|compiled_inference|PASS|
|xcit_tiny_24_p8_224_dist_Opset16|compiled_inference|PASS|

