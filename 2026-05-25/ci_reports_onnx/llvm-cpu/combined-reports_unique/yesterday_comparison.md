# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1519.204|47.4443|-1471.7597|-96.88%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1495.078|48.7142|-1446.3639|-96.74%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|12870.1732|172.5802|-12697.593|-98.66%|
|migraphx_ORT__distilgpt2_1|PASS|progression|722.7454|23.5193|-699.2261|-96.75%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|1099.3006|51.2145|-1048.086|-95.34%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|6416.2656|165.2878|-6250.9778|-97.42%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|541.1192|18.6168|-522.5024|-96.56%|
|migraphx_cadene__dpn92i1|PASS|progression|366.9694|221.0015|-145.968|-39.78%|
|migraphx_cadene__inceptionv4i16|PASS|progression|8505.8604|4993.5482|-3512.3122|-41.29%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|726.9799|169.856|-557.1239|-76.64%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|10472.9991|205.2874|-10267.7117|-98.04%|
|migraphx_mlperf__resnet50_v1|PASS|progression|158.5127|84.1955|-74.3172|-46.88%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|261.6371|27.0782|-234.5589|-89.65%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|1332.6117|242.4911|-1090.1206|-81.8%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|93.7122|71.0377|-22.6745|-24.2%|
|migraphx_pytorch-examples__wlang_lstm|PASS|progression|16.0244|7.8572|-8.1671|-50.97%|
|migraphx_torchvision__densenet121i32|PASS|progression|3037.9506|491.9471|-2546.0035|-83.81%|
|migraphx_torchvision__inceptioni1|PASS|progression|314.7079|156.3653|-158.3426|-50.31%|
|migraphx_torchvision__resnet50i1|PASS|progression|148.8413|86.7561|-62.0852|-41.71%|

## No Regressions Found

## 13 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|migx_bench_bert-large-uncased_16_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_16_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_16_384|compiled_inference|Numerics|
|migx_bench_bert-large-uncased_32_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_32_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_32_384|compiled_inference|Numerics|
|migx_bench_bert-large-uncased_4_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_4_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_4_384|compiled_inference|PASS|
|migx_bench_bert-large-uncased_8_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_8_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_8_384|compiled_inference|PASS|
|model--roberta_shared_bbc_xsum--patrickvonplaten|Numerics|PASS|

