# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|57.6861|1524.7377|1467.0516|2543.16%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|55.7779|1565.8597|1510.0818|2707.31%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|196.059|12486.6549|12290.596|6268.83%|
|migraphx_ORT__distilgpt2_1|PASS|regression|20.1132|744.9039|724.7907|3603.56%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|96.8481|2521.2953|2424.4471|2503.35%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|293.1291|10263.3798|9970.2507|3401.32%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|18.0354|627.6207|609.5854|3379.94%|
|migraphx_cadene__dpn92i1|PASS|regression|200.3524|438.8148|238.4624|119.02%|
|migraphx_cadene__inceptionv4i16|PASS|regression|4389.8409|8875.1283|4485.2873|102.17%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|135.5174|823.7375|688.2201|507.85%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|153.2448|10301.765|10148.5203|6622.43%|
|migraphx_mlperf__resnet50_v1|PASS|regression|121.7012|204.1768|82.4755|67.77%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|26.8932|293.0406|266.1475|989.65%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|53.0555|1071.0626|1018.0071|1918.76%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|35.629|56.4949|20.8659|58.56%|
|migraphx_torchvision__densenet121i32|PASS|regression|1525.2894|4796.69|3271.4006|214.48%|
|migraphx_torchvision__inceptioni1|PASS|regression|150.4832|358.5608|208.0776|138.27%|
|migraphx_torchvision__resnet50i1|PASS|regression|125.7994|192.9886|67.1892|53.41%|

## 34 Regressions Found:

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
|model--YuisekinAI-mistral-0.7B--yuiseki|PASS|import_model|
|model--finetuned_gpt2-large_sst2_negation0.0_pretrainedFalse--yuhuizhang|PASS|import_model|
|model--flan-t5-large-samsum--oguuzhansahin|PASS|import_model|
|model--long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP--pszemraj|PASS|import_model|
|model--m2m100_418M-finetuned-kde4-en-to-pt_BR--danhsf|PASS|import_model|
|model--m2m100_418M-fr--Jour|PASS|import_model|
|model--mT5-base-HunSum-1--SZTAKI-HLT|PASS|import_model|
|model--manifestoberta-xlm-roberta-56policy-topics-sentence-2023-1-1--manifesto-project|PASS|import_model|
|model--my_xlm-roberta-large-finetuned-conll03--BahAdoR0101|PASS|import_model|
|model--pegasus-cnn_dailymail--google|PASS|import_model|
|model--pegasus-large-book-summary--pszemraj|PASS|import_model|
|model--pegasus-large-booksum--cnicu|PASS|import_model|
|model--roberta-ner-multilingual--julian-schelb|PASS|import_model|
|model--t5-large-finetuned-xsum-cnn--sysresearch101|PASS|import_model|
|model--xlm-roberta-large-squad2--deepset|PASS|import_model|
|t5_Opset16|PASS|Numerics|
|t5_Opset17|PASS|Numerics|
|xlmroberta_Opset16|PASS|Numerics|

## One Progression Found:

|model name|old_status|new_status|
|---|---|---|
|flaubert_Opset16|Numerics|PASS|

