# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.1211|100.9347|-0.1864|-0.18%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|285.1476|283.8207|-1.3268|-0.47%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|58.3375|57.2549|-1.0826|-1.86%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.0319|72.3356|0.3037|0.42%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|286.2904|285.9854|-0.3049|-0.11%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|39.1602|38.654|-0.5062|-1.29%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6512|12.609|-0.0423|-0.33%|
|migraphx_cadene__dpn92i1|PASS|within tol|10.0432|9.947|-0.0963|-0.96%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|22.0323|21.8844|-0.148|-0.67%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.1092|6.0875|-0.0217|-0.35%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2621|7.2279|-0.0343|-0.47%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|20.5421|19.6747|-0.8675|-4.22%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0927|15.0569|-0.0358|-0.24%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.7068|25.6292|-1.0777|-4.04%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|114.0201|112.9015|-1.1185|-0.98%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|16.9696|14.6254|-2.3442|-13.81%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.8237|17.7433|-0.0804|-0.45%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.7235|4.6809|-0.0426|-0.9%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.7144|3.6893|-0.025|-0.67%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2846|20.2837|-0.0009|-0.0%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.9104|33.4245|-0.4859|-1.43%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|53.1426|52.3747|-0.7679|-1.44%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8464|11.7895|-0.0569|-0.48%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5|12.4709|-0.0291|-0.23%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8538|12.8038|-0.05|-0.39%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4263|12.3944|-0.0319|-0.26%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8695|12.8134|-0.0561|-0.44%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4092|14.4069|-0.0023|-0.02%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.5845|32.1687|-0.4158|-1.28%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|63.2465|62.4173|-0.8291|-1.31%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|97.3495|95.9739|-1.3755|-1.41%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7432|12.71|-0.0332|-0.26%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3783|14.361|-0.0173|-0.12%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3044|20.2571|-0.0473|-0.23%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3888|14.3833|-0.0055|-0.04%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6498|20.5716|-0.0783|-0.38%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.6885|29.3213|-0.3672|-1.24%|

## 4 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|sequencer2d_l_Opset17|PASS|Numerics|
|squeezenet1.0-6|PASS|Numerics|
|xcit_small_12_p8_384_dist_Opset16_timm|Numerics|compiled_inference|
|xcit_small_24_p8_384_dist_Opset16_timm|Numerics|compiled_inference|

## 4 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|coatnet_rmlp_2_rw_224.sw_in12k|compilation|PASS|
|inception_v3.tf_in1k_vaiq|Numerics|PASS|
|sequencer2d_l_Opset16|Numerics|PASS|
|sequencer2d_s_Opset16|Numerics|PASS|

