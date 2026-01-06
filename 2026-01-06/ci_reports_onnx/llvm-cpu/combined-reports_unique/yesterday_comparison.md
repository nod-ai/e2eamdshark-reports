# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1940.8782|1260.5639|-680.3143|-35.05%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1936.8381|1277.4421|-659.3961|-34.04%|
|migraphx_ORT__distilgpt2_1|PASS|progression|1042.7248|604.9412|-437.7836|-41.98%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2780.1798|2231.3979|-548.7819|-19.74%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|12965.5012|7943.3807|-5022.1205|-38.73%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|620.8643|463.0333|-157.831|-25.42%|
|migraphx_cadene__dpn92i1|PASS|progression|592.2975|414.4412|-177.8563|-30.03%|
|migraphx_cadene__inceptionv4i16|PASS|progression|13041.8771|9332.0582|-3709.8189|-28.45%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|1305.7537|845.937|-459.8168|-35.21%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|15931.574|7392.1289|-8539.4451|-53.6%|
|migraphx_mlperf__resnet50_v1|PASS|progression|496.3554|203.2775|-293.0779|-59.05%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|376.3003|277.4327|-98.8676|-26.27%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|1683.2835|790.5216|-892.7619|-53.04%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|98.7152|60.7331|-37.9822|-38.48%|
|migraphx_torchvision__densenet121i32|PASS|progression|6866.8787|5277.7648|-1589.1139|-23.14%|
|migraphx_torchvision__inceptioni1|PASS|progression|469.5015|385.5205|-83.981|-17.89%|
|migraphx_torchvision__resnet50i1|PASS|progression|280.4273|223.236|-57.1913|-20.39%|

## 5 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|convnext_xlarge_384_in22ft1k_Opset16_timm|PASS|compiled_inference|
|deit3_large_patch16_384_in21ft1k_Opset17_timm|PASS|compiled_inference|
|longformer_Opset16|compilation|import_model|
|longformer_Opset18|compilation|import_model|
|vit_large_patch16_384_Opset16_timm|PASS|compiled_inference|

## 15 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|deit3_large_patch16_384_Opset16|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset16|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset17|compiled_inference|PASS|
|deit3_large_patch16_384_in21ft1k_Opset18|compiled_inference|PASS|
|migraphx_bert__bert-large-uncased|compiled_inference|PASS|
|migraphx_mlperf__bert_large_mlperf|compiled_inference|Numerics|
|migx_bench_bert-large-uncased_1_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_1_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_1_384|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_384|compiled_inference|PASS|
|vit_large_patch16_384_Opset16|compiled_inference|PASS|
|vit_large_patch16_384_Opset17|compiled_inference|PASS|
|vit_large_patch16_384_Opset18|compiled_inference|PASS|

