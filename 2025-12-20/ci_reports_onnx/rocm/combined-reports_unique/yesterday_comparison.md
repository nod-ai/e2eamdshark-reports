# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.9597|102.2971|0.3374|0.33%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|284.289|286.3179|2.0288|0.71%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.4163|58.5676|1.1513|2.01%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|75.5444|75.8251|0.2807|0.37%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|294.7195|294.6921|-0.0274|-0.01%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|40.3183|40.9443|0.6261|1.55%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6355|12.6842|0.0487|0.39%|
|migraphx_cadene__dpn92i1|Numerics|within tol|9.9095|10.1818|0.2723|2.75%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.9033|21.9316|0.0283|0.13%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.0859|6.1608|0.0749|1.23%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2333|7.2977|0.0644|0.89%|
|migraphx_mlperf__bert_large_mlperf|Numerics|regression|19.503|20.7578|1.2547|6.43%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0851|15.1202|0.035|0.23%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.7492|26.6428|0.8935|3.47%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.8573|113.109|0.2517|0.22%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|14.4334|16.3935|1.9601|13.58%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.7455|17.8043|0.0589|0.33%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6376|4.6989|0.0612|1.32%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.6872|3.7137|0.0265|0.72%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2951|20.3269|0.0317|0.16%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.2121|32.8937|-0.3184|-0.96%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.0397|51.5251|-0.5146|-0.99%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7932|11.8791|0.0859|0.73%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4719|12.5788|0.107|0.86%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8658|12.9037|0.0379|0.29%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4083|12.4762|0.0679|0.55%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7663|12.8779|0.1116|0.87%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.3831|14.4744|0.0913|0.63%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.9751|31.6178|-0.3573|-1.12%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.2351|61.378|-0.8571|-1.38%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.971|95.1125|-0.8585|-0.89%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7199|12.7834|0.0634|0.5%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3932|14.4096|0.0164|0.11%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3007|20.3515|0.0509|0.25%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3908|14.4263|0.0355|0.25%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5852|20.6138|0.0286|0.14%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.1944|29.0474|-0.147|-0.5%|

## 6 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|AlexNet_vaiq_int8|PASS|Numerics|
|ResNet18_vaiq|PASS|Numerics|
|ResNet34_vaiq|PASS|Numerics|
|alexnet_Opset18|PASS|Numerics|
|sequencer2d_l_Opset16_timm|PASS|Numerics|
|squeezenet1.1-7|PASS|Numerics|

## 9 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|coatnet_rmlp_1_rw2_224.sw_in12k|compilation|PASS|
|coatnet_rmlp_1_rw2_224.sw_in12k_ft_in1k|compilation|PASS|
|coatnet_rmlp_1_rw_224.sw_in1k|compilation|PASS|
|coatnet_rmlp_2_rw_224.sw_in12k|compilation|PASS|
|coatnet_rmlp_2_rw_224.sw_in12k_ft_in1k|compilation|PASS|
|sequencer2d_m_Opset16|Numerics|PASS|
|squeezebert_Opset16|compilation|PASS|
|squeezebert_Opset16_transformers|compilation|PASS|
|squeezenet1.0-12|Numerics|PASS|

