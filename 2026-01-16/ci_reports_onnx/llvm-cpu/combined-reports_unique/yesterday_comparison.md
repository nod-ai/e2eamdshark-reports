# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1470.3148|54.8086|-1415.5063|-96.27%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1572.0663|56.2334|-1515.833|-96.42%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|12426.901|191.2664|-12235.6346|-98.46%|
|migraphx_ORT__distilgpt2_1|PASS|progression|742.1546|19.7176|-722.437|-97.34%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2538.5637|95.1798|-2443.3839|-96.25%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|10070.7031|289.5384|-9781.1648|-97.12%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|602.8655|17.7065|-585.159|-97.06%|
|migraphx_cadene__dpn92i1|Numerics|progression|438.4559|198.8713|-239.5846|-54.64%|
|migraphx_cadene__inceptionv4i16|PASS|progression|8896.8254|4368.6556|-4528.1698|-50.9%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|821.6452|135.1099|-686.5353|-83.56%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|10181.4235|152.472|-10028.9515|-98.5%|
|migraphx_mlperf__resnet50_v1|PASS|progression|206.6969|122.9622|-83.7347|-40.51%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|292.1236|25.9533|-266.1703|-91.12%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|1094.418|53.957|-1040.4609|-95.07%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|57.4766|35.3965|-22.08|-38.42%|
|migraphx_torchvision__densenet121i32|PASS|progression|4815.3498|1540.9409|-3274.4089|-68.0%|
|migraphx_torchvision__inceptioni1|PASS|progression|355.5206|150.7345|-204.7861|-57.6%|
|migraphx_torchvision__resnet50i1|PASS|progression|195.2303|126.3077|-68.9226|-35.3%|

## 3 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|model--albert-xxl-v2-finetuned-squad--anas-awadalla|PASS|compiled_inference|
|regnetz_d8_evos_Opset16_timm|PASS|Numerics|

## 15 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|gluon_xception65|compiled_inference|PASS|
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
|pnasnet5large|compiled_inference|Numerics|
|xception65_Opset18_timm|compiled_inference|PASS|

