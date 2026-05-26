# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|47.4443|1537.0123|1489.5679|3139.61%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|48.7142|1553.9025|1505.1884|3089.84%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|172.5802|12951.2756|12778.6954|7404.5%|
|migraphx_ORT__distilgpt2_1|PASS|regression|23.5193|698.2978|674.7786|2869.05%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|51.2145|1103.4461|1052.2316|2054.56%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|165.2878|6384.0613|6218.7735|3762.39%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|18.6168|546.4472|527.8304|2835.24%|
|migraphx_cadene__dpn92i1|PASS|regression|221.0015|367.8408|146.8394|66.44%|
|migraphx_cadene__inceptionv4i16|PASS|regression|4993.5482|8538.2737|3544.7255|70.99%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|169.856|733.4485|563.5925|331.81%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|205.2874|10557.7061|10352.4187|5042.89%|
|migraphx_mlperf__resnet50_v1|PASS|regression|84.1955|159.0648|74.8693|88.92%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|27.0782|261.6536|234.5753|866.29%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|242.4911|1309.9423|1067.4512|440.2%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|71.0377|96.6822|25.6445|36.1%|
|migraphx_pytorch-examples__wlang_lstm|PASS|regression|7.8572|16.1535|8.2962|105.59%|
|migraphx_torchvision__densenet121i32|PASS|regression|491.9471|3035.2504|2543.3033|516.99%|
|migraphx_torchvision__inceptioni1|PASS|regression|156.3653|322.6493|166.284|106.34%|
|migraphx_torchvision__resnet50i1|PASS|regression|86.7561|148.3631|61.6071|71.01%|

## 13 Regressions Found:

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
|model--roberta_shared_bbc_xsum--patrickvonplaten|PASS|Numerics|

## No Progressions Found

