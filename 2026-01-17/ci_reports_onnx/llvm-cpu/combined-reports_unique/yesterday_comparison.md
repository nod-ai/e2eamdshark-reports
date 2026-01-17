# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|54.8086|1588.9739|1534.1654|2799.13%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|56.2334|1403.5414|1347.308|2395.92%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|191.2664|12470.5519|12279.2855|6419.99%|
|migraphx_ORT__distilgpt2_1|PASS|regression|19.7176|726.4706|706.753|3584.38%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|95.1798|2524.3074|2429.1276|2552.15%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|289.5384|10424.4509|10134.9125|3500.37%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|17.7065|655.1709|637.4645|3600.18%|
|migraphx_cadene__dpn92i1|Numerics|regression|198.8713|430.8091|231.9379|116.63%|
|migraphx_cadene__inceptionv4i16|PASS|regression|4368.6556|8843.7884|4475.1328|102.44%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|135.1099|814.8585|679.7486|503.11%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|152.472|9858.1044|9705.6325|6365.52%|
|migraphx_mlperf__resnet50_v1|PASS|regression|122.9622|201.7499|78.7877|64.07%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|25.9533|289.3993|263.4461|1015.08%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|53.957|1030.8743|976.9172|1810.55%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|35.3965|58.7158|23.3192|65.88%|
|migraphx_torchvision__densenet121i32|PASS|regression|1540.9409|4750.0307|3209.0898|208.26%|
|migraphx_torchvision__inceptioni1|PASS|regression|150.7345|344.1211|193.3866|128.3%|
|migraphx_torchvision__resnet50i1|PASS|regression|126.3077|194.8629|68.5552|54.28%|

## 14 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|migx_bench_bert-large-uncased_16_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_16_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_16_384|Numerics|compiled_inference|
|migx_bench_bert-large-uncased_32_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_32_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_32_384|Numerics|compiled_inference|
|migx_bench_bert-large-uncased_4_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_4_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_4_384|PASS|compiled_inference|
|migx_bench_bert-large-uncased_8_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_8_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_8_384|PASS|compiled_inference|

## One Progression Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset16_timm|compiled_inference|PASS|

