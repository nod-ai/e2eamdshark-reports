# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|100.9347|100.7402|-0.1944|-0.19%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|283.8207|283.9654|0.1446|0.05%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.2549|57.4553|0.2004|0.35%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.3356|72.0499|-0.2857|-0.39%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|285.9854|286.2588|0.2733|0.1%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.654|38.5988|-0.0552|-0.14%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.609|12.5979|-0.011|-0.09%|
|migraphx_cadene__dpn92i1|PASS|within tol|9.947|9.8526|-0.0944|-0.95%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|21.8844|21.9168|0.0324|0.15%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|6.0875|6.0545|-0.033|-0.54%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2279|7.234|0.0061|0.08%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.6747|19.0869|-0.5878|-2.99%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0569|15.0306|-0.0263|-0.17%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.6292|25.5911|-0.038|-0.15%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.9015|112.2307|-0.6708|-0.59%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|14.6254|14.0096|-0.6158|-4.21%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.7433|17.6852|-0.0582|-0.33%|
|migraphx_torchvision__inceptioni1|Numerics|within tol|4.6809|4.5799|-0.101|-2.16%|
|migraphx_torchvision__resnet50i1|PASS|within tol|3.6893|3.6806|-0.0087|-0.24%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2837|20.2626|-0.0211|-0.1%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.4245|32.8656|-0.5589|-1.67%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|52.3747|51.6018|-0.7729|-1.48%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7895|11.7917|0.0022|0.02%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4709|12.5041|0.0332|0.27%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8038|12.8333|0.0294|0.23%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.3944|12.4668|0.0724|0.58%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8134|12.7137|-0.0997|-0.78%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4069|14.3582|-0.0487|-0.34%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.1687|31.7847|-0.384|-1.19%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.4173|61.66|-0.7574|-1.21%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.9739|95.0267|-0.9472|-0.99%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.71|12.6931|-0.0169|-0.13%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.361|14.3828|0.0218|0.15%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.2571|20.2196|-0.0376|-0.19%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3833|14.3726|-0.0106|-0.07%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5716|20.5479|-0.0237|-0.12%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.3213|29.0621|-0.2593|-0.88%|

## 8 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_224_Opset16|PASS|compilation|
|coatnet_2_rw_224.sw_in12k_ft_in1k|PASS|compilation|
|coatnet_rmlp_2_rw_224.sw_in12k|PASS|compilation|
|sequencer2d_l_Opset16|PASS|Numerics|
|sequencer2d_m_Opset17|PASS|Numerics|
|sequencer2d_s_Opset17_timm|PASS|Numerics|
|swin_base_patch4_window12_384_in22k_Opset17_timm|PASS|compilation|
|xcit_nano_12_p8_384_dist_Opset16_timm|Numerics|compiled_inference|

## 6 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|sequencer2d_l_Opset17|Numerics|PASS|
|sequencer2d_m_Opset16|Numerics|PASS|
|sequencer2d_m_Opset17_timm|Numerics|PASS|
|squeezenet1.0-6|Numerics|PASS|
|xcit_small_12_p8_384_dist_Opset16_timm|compiled_inference|Numerics|
|xcit_small_24_p8_384_dist_Opset16_timm|compiled_inference|Numerics|

