# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|100.7402|101.0673|0.3271|0.32%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|283.9654|283.4453|-0.5201|-0.18%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.4553|57.7341|0.2788|0.49%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.0499|72.1329|0.0829|0.12%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.2588|286.0381|-0.2207|-0.08%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.5988|38.8106|0.2118|0.55%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.5979|12.654|0.056|0.44%|
|migraphx_cadene__dpn92i1|PASS|within tol|9.8526|9.9918|0.1392|1.41%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.9168|21.8835|-0.0332|-0.15%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.0545|6.1047|0.0502|0.83%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.234|7.2538|0.0199|0.27%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.0869|19.6932|0.6062|3.18%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0306|15.1167|0.0861|0.57%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.5911|25.7461|0.155|0.61%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.2307|112.9319|0.7011|0.62%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|14.0096|14.7617|0.7521|5.37%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.6852|17.7556|0.0704|0.4%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.5799|4.6546|0.0747|1.63%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.6806|3.718|0.0373|1.01%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2626|20.2981|0.0354|0.17%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.8656|32.7383|-0.1273|-0.39%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.6018|51.2725|-0.3293|-0.64%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7917|11.8193|0.0275|0.23%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5041|12.5456|0.0415|0.33%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8333|12.8757|0.0425|0.33%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4668|12.5366|0.0698|0.56%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7137|12.8389|0.1251|0.98%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.3582|14.4595|0.1013|0.71%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.7847|31.5002|-0.2845|-0.89%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.66|60.9445|-0.7154|-1.16%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.0267|94.4052|-0.6215|-0.65%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.6931|12.7553|0.0622|0.49%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3828|14.3975|0.0147|0.1%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.2196|20.3268|0.1072|0.53%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3726|14.4399|0.0672|0.47%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5479|20.5974|0.0495|0.24%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.0621|28.9868|-0.0752|-0.26%|

## 6 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|inception_v3.tf_in1k_vaiq|PASS|Numerics|
|sequencer2d_l_Opset17|PASS|Numerics|
|sequencer2d_s_Opset16|PASS|Numerics|
|squeezenet1.0-6|PASS|Numerics|
|swin_base_patch4_window12_384_Opset17_timm|PASS|compilation|
|vit_l_16_Opset16_torch_hub|PASS|compilation|

## 14 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_224_Opset16|compilation|PASS|
|coatnet_2_rw_224.sw_in12k_ft_in1k|compilation|PASS|
|coatnet_rmlp_2_rw_224.sw_in12k|compilation|PASS|
|gernet_m_Opset18_timm|compiled_inference|Numerics|
|resnet10t_Opset17_timm|compiled_inference|Numerics|
|sequencer2d_s_Opset17_timm|Numerics|PASS|
|squeezenet1_1_Opset17|Numerics|PASS|
|twins_svt_base_Opset16|compilation|compiled_inference|
|twins_svt_base_Opset17|compilation|compiled_inference|
|twins_svt_large_Opset16|compilation|compiled_inference|
|twins_svt_large_Opset17|compilation|compiled_inference|
|twins_svt_small_Opset16|compilation|compiled_inference|
|twins_svt_small_Opset17|compilation|compiled_inference|
|xcit_nano_12_p8_384_dist_Opset16_timm|compiled_inference|Numerics|

