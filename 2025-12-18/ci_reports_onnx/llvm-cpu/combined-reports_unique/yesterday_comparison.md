# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|76.5731|1947.771|1871.198|2443.68%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|74.3915|1931.3085|1856.9169|2496.14%|
|migraphx_ORT__distilgpt2_1|PASS|regression|31.9707|1033.8233|1001.8526|3133.66%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|97.6259|2777.6296|2680.0037|2745.18%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|266.8543|12855.1191|12588.2648|4717.28%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|44.9565|641.7387|596.7822|1327.47%|
|migraphx_cadene__dpn92i1|PASS|regression|200.0304|595.6336|395.6032|197.77%|
|migraphx_cadene__inceptionv4i16|PASS|regression|8831.7309|12909.3248|4077.5939|46.17%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|298.4827|1293.9598|995.4771|333.51%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|1042.3007|15344.2407|14301.94|1372.15%|
|migraphx_mlperf__resnet50_v1|PASS|regression|150.4|548.3999|398.0|264.63%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|31.7376|372.6379|340.9003|1074.12%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|119.6922|1653.988|1534.2958|1281.87%|
|migraphx_pytorch-examples__wlang_gru|PASS|regression|110.8246|133.3203|22.4957|20.3%|
|migraphx_torchvision__densenet121i32|PASS|regression|2681.7979|6604.1958|3922.398|146.26%|
|migraphx_torchvision__inceptioni1|PASS|regression|291.7335|492.4882|200.7547|68.81%|
|migraphx_torchvision__resnet50i1|PASS|regression|227.8563|276.5113|48.6551|21.35%|

## 25 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|RDN_pytorch_vaiq_int8|Numerics|compiled_inference|
|efficientnet-lite4-11-qdq|Numerics|compilation|
|migraphx_bert__bert-large-uncased|PASS|compiled_inference|
|migraphx_mlperf__bert_large_mlperf|Numerics|compiled_inference|
|migraphx_pytorch-examples__wlang_lstm|PASS|compiled_inference|
|migx_bench_bert-large-uncased_16_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_16_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_16_384|Numerics|compiled_inference|
|migx_bench_bert-large-uncased_1_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_1_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_1_384|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_2_384|PASS|compiled_inference|
|migx_bench_bert-large-uncased_32_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_32_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_32_384|Numerics|compiled_inference|
|migx_bench_bert-large-uncased_4_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_4_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_4_384|PASS|compiled_inference|
|migx_bench_bert-large-uncased_8_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_8_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_8_384|PASS|compiled_inference|
|model--albert-xxl-v2-finetuned-squad--anas-awadalla|PASS|compiled_inference|
|t5-decoder-with-lm-head-12|PASS|native_inference|

## 28 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|convit_base_Opset16_timm|Numerics|PASS|
|convit_base_Opset17_timm|Numerics|PASS|
|model--MTL-distilbert-base-uncased-squad--jgammack|compilation|PASS|
|model--bert-engonly-sentiment-test--SiddharthaM|compilation|PASS|
|model--distilBERT-infoExtract--tony4194|compilation|PASS|
|model--distilbert-base-NER--51la5|compilation|PASS|
|model--distilbert-base-cased-distilled-squad--distilbert|compilation|PASS|
|model--distilbert-base-german-cased-finetuned-ner--FabianWillner|compilation|PASS|
|model--distilbert-base-multilingual-cased-finetuned-squad--monakth|compilation|PASS|
|model--distilbert-base-uncased-finetuned-ner--dbsamu|compilation|PASS|
|model--distilbert-srb-ner--Aleksandar|compilation|PASS|
|model--finetuning-sentiment-imdb--Timothy1337|compilation|PASS|
|model--finetuning-sentiment-model-3000-samples--DuboiJ|compilation|PASS|
|model--microsoft_deberta-base_squad--Palak|compilation|PASS|
|model--microsoft_deberta-large_squad--Palak|compilation|PASS|
|mvitv2_base|Numerics|PASS|
|mvitv2_small|Numerics|PASS|
|mvitv2_tiny|Numerics|PASS|
|regnetz_c16_evos.ch_in1k_train_vaiq|Numerics|PASS|
|regnetz_c16_evos.ch_in1k_vaiq|Numerics|PASS|
|regnetz_d8_evos.ch_in1k_train_vaiq|Numerics|PASS|
|regnetz_d8_evos.ch_in1k_vaiq|Numerics|PASS|
|sequencer2d_l_Opset16_timm|Numerics|PASS|
|sequencer2d_l_Opset17_timm|Numerics|PASS|
|sequencer2d_m_Opset16_timm|Numerics|PASS|
|sequencer2d_m_Opset17_timm|Numerics|PASS|
|sequencer2d_s_Opset16_timm|Numerics|PASS|
|sequencer2d_s_Opset17_timm|Numerics|PASS|

