# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.6899|101.6383|-0.0516|-0.05%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|288.6953|283.2922|-5.4031|-1.87%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|58.0042|57.6406|-0.3636|-0.63%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.5319|71.9528|-0.5791|-0.8%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.9777|286.2523|-0.7254|-0.25%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|39.1277|38.6871|-0.4406|-1.13%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6968|12.6311|-0.0657|-0.52%|
|migraphx_cadene__dpn92i1|PASS|within tol|10.4471|10.0607|-0.3863|-3.7%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|22.0749|21.942|-0.1329|-0.6%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.1583|6.0775|-0.0808|-1.31%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2984|7.2462|-0.0522|-0.71%|
|migraphx_mlperf__bert_large_mlperf|Numerics|progression|20.7614|19.6045|-1.1569|-5.57%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.1412|15.0829|-0.0583|-0.38%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.6451|25.7309|-0.9142|-3.43%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|114.5641|112.7455|-1.8186|-1.59%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|16.6266|14.1761|-2.4505|-14.74%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.8575|17.7475|-0.11|-0.62%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6903|4.6821|-0.0083|-0.18%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.7438|3.6971|-0.0468|-1.25%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.3293|20.2843|-0.045|-0.22%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|34.1687|32.9312|-1.2376|-3.62%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|53.509|51.583|-1.926|-3.6%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8852|11.8025|-0.0827|-0.7%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5369|12.5339|-0.003|-0.02%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8994|12.8243|-0.0751|-0.58%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4573|12.417|-0.0404|-0.32%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8357|12.7905|-0.0452|-0.35%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.5052|14.439|-0.0662|-0.46%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.8688|31.6724|-1.1964|-3.64%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|63.572|61.4799|-2.0921|-3.29%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|98.1687|95.1935|-2.9752|-3.03%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7635|12.7214|-0.0421|-0.33%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.4524|14.4003|-0.052|-0.36%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3766|20.2903|-0.0864|-0.42%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.435|14.4145|-0.0205|-0.14%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.7128|20.5365|-0.1762|-0.85%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.8958|29.0437|-0.8522|-2.85%|

## 6 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|alexnet_Opset18|PASS|Numerics|
|beit_large_patch16_224_Opset17|PASS|compilation|
|sequencer2d_l_Opset16|PASS|Numerics|
|sequencer2d_m_Opset16|PASS|Numerics|
|sequencer2d_s_Opset17_timm|PASS|Numerics|
|squeezenet1.1-7|PASS|Numerics|

## 5 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|AlexNet_vaiq_int8|Numerics|PASS|
|alexnet_Opset17|Numerics|PASS|
|inception_v3.tf_in1k_vaiq|Numerics|PASS|
|sequencer2d_m_Opset17|Numerics|PASS|
|swin_base_patch4_window12_384_Opset17_timm|compilation|PASS|

