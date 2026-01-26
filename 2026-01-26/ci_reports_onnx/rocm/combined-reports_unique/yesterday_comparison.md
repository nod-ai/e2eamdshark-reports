# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.4318|101.6694|0.2375|0.23%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|286.1131|284.0801|-2.033|-0.71%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|58.1191|57.7919|-0.3272|-0.56%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|71.954|72.332|0.378|0.53%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.0813|286.6351|0.5538|0.19%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.6848|38.7941|0.1092|0.28%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.7257|12.6963|-0.0294|-0.23%|
|migraphx_cadene__dpn92i1|PASS|within tol|3.07|2.9896|-0.0804|-2.62%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.0294|20.0296|0.0002|0.0%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.4874|2.4467|-0.0408|-1.64%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.3166|7.257|-0.0596|-0.81%|
|migraphx_mlperf__bert_large_mlperf|Numerics|progression|21.0475|19.3972|-1.6503|-7.84%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.3993|15.3861|-0.0133|-0.09%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.2664|25.8731|-0.3933|-1.5%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|113.7362|112.9615|-0.7746|-0.68%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.6248|17.5857|-0.0391|-0.22%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.4488|3.3982|-0.0506|-1.47%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.9126|1.8962|-0.0163|-0.85%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2775|20.3303|0.0527|0.26%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.1632|33.1987|0.0355|0.11%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.0716|52.1754|0.1037|0.2%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.859|11.8104|-0.0487|-0.41%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5151|12.4994|-0.0157|-0.13%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.932|12.8596|-0.0723|-0.56%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4808|12.4117|-0.0691|-0.55%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8373|12.8067|-0.0306|-0.24%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4919|14.4311|-0.0608|-0.42%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.9257|32.0879|0.1623|0.51%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.8979|62.1118|0.214|0.35%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.9129|96.3185|0.4056|0.42%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7852|12.7325|-0.0527|-0.41%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.4012|14.3852|-0.016|-0.11%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3646|20.3601|-0.0045|-0.02%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.4215|14.4129|-0.0086|-0.06%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6136|20.623|0.0094|0.05%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.2317|29.2362|0.0045|0.02%|

## 69 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|bvlcalexnet-12-qdq|Numerics|compilation|
|eca_nfnet_l0.ra2_in1k_train_vaiq|PASS|compilation|
|nfnet_l0.ra2_in1k_train_vaiq|PASS|compilation|
|regnet_x_32gf_Opset16|PASS|compilation|
|regnet_x_32gf_Opset16_torch_hub|PASS|compilation|
|regnet_x_32gf_Opset17|PASS|compilation|
|regnet_x_32gf_Opset18|PASS|compilation|
|regnet_x_3_2gf_Opset16|PASS|compilation|
|regnet_x_3_2gf_Opset16_torch_hub|PASS|compilation|
|regnet_x_3_2gf_Opset17|PASS|compilation|
|regnet_x_3_2gf_Opset18|PASS|compilation|
|regnet_x_8gf_Opset16|PASS|compilation|
|regnet_x_8gf_Opset17|PASS|compilation|
|regnet_x_8gf_Opset18|PASS|compilation|
|regnet_x_8gf_Opset18_torch_hub|PASS|compilation|
|regnet_y_16gf_Opset16|PASS|compilation|
|regnet_y_16gf_Opset17|PASS|compilation|
|regnet_y_16gf_Opset17_torch_hub|PASS|compilation|
|regnet_y_16gf_Opset18|PASS|compilation|
|regnet_y_32gf_Opset16|PASS|compilation|
|regnet_y_32gf_Opset17|PASS|compilation|
|regnet_y_32gf_Opset18|PASS|compilation|
|regnet_y_32gf_Opset18_torch_hub|PASS|compilation|
|regnetx_032_Opset16|PASS|compilation|
|regnetx_032_Opset17|PASS|compilation|
|regnetx_032_Opset18|PASS|compilation|
|regnetx_032_Opset18_timm|PASS|compilation|
|regnetx_040.pycls_in1k_vaiq|PASS|compilation|
|regnetx_080.pycls_in1k_vaiq|PASS|compilation|
|regnetx_080_Opset16|PASS|compilation|
|regnetx_080_Opset17|PASS|compilation|
|regnetx_080_Opset17_timm|PASS|compilation|
|regnetx_080_Opset18|PASS|compilation|
|regnetx_120_Opset16|PASS|compilation|
|regnetx_120_Opset16_timm|PASS|compilation|
|regnetx_120_Opset17|PASS|compilation|
|regnetx_120_Opset18|PASS|compilation|
|regnetx_160.pycls_in1k_vaiq|PASS|compilation|
|regnetx_320_Opset16|PASS|compilation|
|regnetx_320_Opset17|PASS|compilation|
|regnetx_320_Opset17_timm|PASS|compilation|
|regnetx_320_Opset18|PASS|compilation|
|regnety_040.pycls_in1k_vaiq|PASS|compilation|
|regnety_040.ra3_in1k_train_vaiq|PASS|compilation|
|regnety_040.ra3_in1k_vaiq|PASS|compilation|
|regnety_120.sw_in12k|PASS|compilation|
|regnety_120_Opset16|PASS|compilation|
|regnety_120_Opset17|PASS|compilation|
|regnety_120_Opset17_timm|PASS|compilation|
|regnety_160.deit_in1k|PASS|compilation|
|regnety_160.sw_in12k|PASS|compilation|
|regnety_160_Opset16|PASS|compilation|
|regnety_160_Opset17|PASS|compilation|
|regnety_160_Opset17_timm|PASS|compilation|
|regnety_320.pycls_in1k_vaiq|PASS|compilation|
|regnety_320_Opset16|PASS|compilation|
|regnety_320_Opset17|PASS|compilation|
|regnety_320_Opset17_timm|PASS|compilation|
|repvgg_b1g4.rvgg_in1k_vaiq|PASS|compilation|
|repvgg_b2g4.rvgg_in1k_vaiq|PASS|compilation|
|repvgg_b3g4_Opset16|PASS|compilation|
|repvgg_b3g4_Opset16_timm|PASS|compilation|
|repvgg_b3g4_Opset17|PASS|compilation|
|repvgg_b3g4_Opset18|PASS|compilation|
|resnest14d_vaiq|PASS|compilation|
|resnest26d_vaiq|PASS|compilation|
|resnest50d_1s4x24d_Opset16|PASS|compilation|
|resnest50d_1s4x24d_Opset17|PASS|compilation|
|resnest50d_vaiq|PASS|compilation|

## 30 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|RegNet_y_8gf_vaiq_int8|compilation|PASS|
|eca_nfnet_l0_Opset16|compilation|PASS|
|eca_nfnet_l0_Opset16_timm|compilation|PASS|
|eca_nfnet_l0_Opset17|compilation|PASS|
|eca_nfnet_l2_Opset16|compilation|PASS|
|eca_nfnet_l2_Opset16_timm|compilation|PASS|
|eca_nfnet_l2_Opset17|compilation|PASS|
|nfnet_l0_Opset16|compilation|PASS|
|nfnet_l0_Opset16_timm|compilation|PASS|
|nfnet_l0_Opset17|compilation|PASS|
|regnetx_064.pycls_in1k_vaiq|compilation|PASS|
|regnetx_120.pycls_in1k_vaiq|compilation|PASS|
|regnety_040_Opset16|compilation|PASS|
|regnety_040_Opset16_timm|compilation|PASS|
|regnety_040_Opset17|compilation|PASS|
|regnety_080.pycls_in1k_vaiq|compilation|PASS|
|regnety_080.ra3_in1k_train_vaiq|compilation|PASS|
|regnety_080.ra3_in1k_vaiq|compilation|PASS|
|regnety_080_tv.tv2_in1k_vaiq|compilation|PASS|
|regnety_120.pycls_in1k_vaiq|compilation|PASS|
|regnety_120.sw_in12k_ft_in1k_train_vaiq|compilation|PASS|
|regnety_160.lion_in12k_ft_in1k_train_vaiq|compilation|PASS|
|regnety_160.pycls_in1k_vaiq|compilation|PASS|
|repvgg_b2g4_Opset16|compilation|Numerics|
|repvgg_b2g4_Opset16_timm|compilation|Numerics|
|repvgg_b2g4_Opset17|compilation|Numerics|
|repvgg_b2g4_Opset18|compilation|Numerics|
|resnest50d_4s2x40d_Opset16|compilation|Numerics|
|resnest50d_4s2x40d_Opset16_timm|compilation|Numerics|
|resnest50d_4s2x40d_Opset17|compilation|Numerics|

