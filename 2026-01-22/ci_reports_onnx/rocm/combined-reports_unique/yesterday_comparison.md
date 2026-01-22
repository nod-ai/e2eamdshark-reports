# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.245|100.9309|-0.3141|-0.31%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|286.5205|282.7619|-3.7587|-1.31%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|58.3039|57.7268|-0.5771|-0.99%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.4619|72.127|-0.3349|-0.46%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.7019|285.8373|-0.8646|-0.3%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|39.2141|38.7618|-0.4523|-1.15%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.7188|12.6572|-0.0615|-0.48%|
|migraphx_cadene__dpn92i1|PASS|within tol|3.0822|3.0345|-0.0477|-1.55%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.1772|20.1194|-0.0578|-0.29%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.5276|2.4576|-0.07|-2.77%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2848|7.2426|-0.0422|-0.58%|
|migraphx_mlperf__bert_large_mlperf|Numerics|progression|20.9966|19.5801|-1.4165|-6.75%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0798|15.0788|-0.001|-0.01%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.5254|25.5218|-1.0036|-3.78%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|113.8752|112.2709|-1.6043|-1.41%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.6787|17.5789|-0.0998|-0.56%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.4726|3.4318|-0.0407|-1.17%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.9209|1.9029|-0.018|-0.94%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.299|20.256|-0.0429|-0.21%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.8999|32.9062|-0.9937|-2.93%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|53.3348|51.7769|-1.5579|-2.92%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8367|11.7647|-0.072|-0.61%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5636|12.5125|-0.0511|-0.41%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8897|12.867|-0.0228|-0.18%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.5068|12.3979|-0.1088|-0.87%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8093|12.8363|0.027|0.21%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4643|14.442|-0.0223|-0.15%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.6421|31.6764|-0.9656|-2.96%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|63.4055|61.4793|-1.9261|-3.04%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|98.03|95.5162|-2.5138|-2.56%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7588|12.7101|-0.0487|-0.38%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3864|14.324|-0.0624|-0.43%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3397|20.3017|-0.038|-0.19%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3935|14.3842|-0.0094|-0.06%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6518|20.6208|-0.031|-0.15%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.868|29.0603|-0.8077|-2.7%|

## No Regressions Found

## 11 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|cs3se_edgenet_x_Opset16_timm|Numerics|PASS|
|cs3sedarknet_l_Opset16_timm|Numerics|PASS|
|cs3sedarknet_x_Opset17_timm|Numerics|PASS|
|dpn92_Opset17_timm|Numerics|PASS|
|edgenext_small_rw_Opset18_timm|Numerics|PASS|
|res2net50_48w_2s_Opset18_timm|Numerics|PASS|
|rexnetr_200.sw_in12k|Numerics|PASS|
|rexnetr_300.sw_in12k|Numerics|PASS|
|t5-decoder-with-lm-head-12|native_inference|PASS|
|xcit_large_24_p8_224_Opset16_timm|Numerics|PASS|
|xcit_tiny_24_p8_384_dist_Opset16_timm|Numerics|PASS|

