# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.0673|101.6899|0.6226|0.62%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|283.4453|288.6953|5.25|1.85%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.7341|58.0042|0.27|0.47%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.1329|72.5319|0.399|0.55%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.0381|286.9777|0.9396|0.33%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.8106|39.1277|0.317|0.82%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.654|12.6968|0.0429|0.34%|
|migraphx_cadene__dpn92i1|PASS|within tol|9.9918|10.4471|0.4553|4.56%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.8835|22.0749|0.1914|0.87%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.1047|6.1583|0.0536|0.88%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2538|7.2984|0.0445|0.61%|
|migraphx_mlperf__bert_large_mlperf|Numerics|regression|19.6932|20.7614|1.0682|5.42%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1167|15.1412|0.0245|0.16%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.7461|26.6451|0.8989|3.49%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.9319|114.5641|1.6323|1.45%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|14.7617|16.6266|1.8649|12.63%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.7556|17.8575|0.1019|0.57%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6546|4.6903|0.0357|0.77%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.718|3.7438|0.0259|0.7%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2981|20.3293|0.0312|0.15%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.7383|34.1687|1.4305|4.37%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.2725|53.509|2.2365|4.36%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8193|11.8852|0.0659|0.56%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5456|12.5369|-0.0087|-0.07%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8757|12.8994|0.0237|0.18%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.5366|12.4573|-0.0793|-0.63%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8389|12.8357|-0.0032|-0.02%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4595|14.5052|0.0457|0.32%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.5002|32.8688|1.3685|4.34%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|60.9445|63.572|2.6275|4.31%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|94.4052|98.1687|3.7635|3.99%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7553|12.7635|0.0082|0.06%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3975|14.4524|0.0549|0.38%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3268|20.3766|0.0499|0.25%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.4399|14.435|-0.0049|-0.03%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5974|20.7128|0.1154|0.56%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|28.9868|29.8958|0.909|3.14%|

## 4 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|gernet_m_Opset18_timm|Numerics|compiled_inference|
|resnet10t_Opset17_timm|Numerics|compiled_inference|
|sequencer2d_m_Opset17_timm|PASS|Numerics|
|squeezenet1_1_Opset17|PASS|Numerics|

## 5 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|alexnet_Opset18|Numerics|PASS|
|sequencer2d_l_Opset16|Numerics|PASS|
|squeezenet1.1-7|Numerics|PASS|
|swin_base_patch4_window12_384_in22k_Opset17_timm|compilation|PASS|
|vit_l_16_Opset16_torch_hub|compilation|PASS|

