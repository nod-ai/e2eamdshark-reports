# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.2856|101.8378|0.5521|0.55%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|283.0951|284.6461|1.5509|0.55%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.3175|57.5896|0.2721|0.47%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|75.6814|75.3336|-0.3478|-0.46%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|294.7372|295.0061|0.269|0.09%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|40.0574|40.2634|0.2061|0.51%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6208|12.6353|0.0146|0.12%|
|migraphx_cadene__dpn92i1|Numerics|within tol|10.1126|10.1416|0.0291|0.29%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.8861|21.8866|0.0005|0.0%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.1239|6.1036|-0.0203|-0.33%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.222|7.2182|-0.0038|-0.05%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.5647|19.6713|0.1066|0.54%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|14.8686|14.8335|-0.0351|-0.24%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.755|25.8704|0.1154|0.45%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.7781|112.8104|0.0324|0.03%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|14.358|14.5766|0.2186|1.52%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.6869|17.7406|0.0537|0.3%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6558|4.6755|0.0197|0.42%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.7171|3.7169|-0.0003|-0.01%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2774|20.2506|-0.0268|-0.13%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.8928|33.029|0.1362|0.41%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.7357|51.8849|0.1493|0.29%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7441|11.748|0.0039|0.03%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4321|12.4656|0.0335|0.27%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8197|12.8433|0.0237|0.18%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4647|12.4614|-0.0034|-0.03%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7291|12.7574|0.0283|0.22%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.378|14.3671|-0.0109|-0.08%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.6613|31.7479|0.0866|0.27%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.487|61.5264|0.0393|0.06%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.3621|95.4282|0.0661|0.07%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.6854|12.6743|-0.0111|-0.09%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3806|14.3316|-0.049|-0.34%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3302|20.1998|-0.1303|-0.64%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3779|14.3197|-0.0581|-0.4%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6041|20.5596|-0.0444|-0.22%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.0541|29.1078|0.0538|0.19%|

## 5 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|AlexNet_vaiq_int8|PASS|Numerics|
|sequencer2d_l_Opset17|PASS|Numerics|
|sequencer2d_s_Opset16_timm|PASS|Numerics|
|squeezenet1_1_Opset17_torch_hub|PASS|Numerics|
|tf_efficientnetv2_s_Opset17_timm|Numerics|compiled_inference|

## 10 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|ResNet18_vaiq|Numerics|PASS|
|ResNet34_vaiq|Numerics|PASS|
|mobilenet_v2_Opset17|setup|PASS|
|sequencer2d_l_Opset16|Numerics|PASS|
|sequencer2d_m_Opset17_timm|Numerics|PASS|
|sequencer2d_s_Opset16|Numerics|PASS|
|sequencer2d_s_Opset17_timm|Numerics|PASS|
|squeezenet1.0-9|Numerics|PASS|
|xcit_small_12_p8_384_dist_Opset16_timm|compiled_inference|Numerics|
|xcit_small_24_p8_384_dist_Opset16_timm|compiled_inference|Numerics|

