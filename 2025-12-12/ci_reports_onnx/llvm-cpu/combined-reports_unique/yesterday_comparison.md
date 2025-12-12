# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|regression|76.5731|1824.6712|1748.0982|2282.91%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|74.3915|1751.1814|1676.7899|2254.01%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|209.2272|20195.6748|19986.4476|9552.51%|
|migraphx_ORT__distilgpt2_1|PASS|regression|31.9707|837.1258|805.155|2518.42%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|regression|97.6259|2609.3986|2511.7728|2572.86%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|266.8543|14059.8558|13793.0015|5168.74%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|44.9565|642.4111|597.4546|1328.96%|
|migraphx_cadene__dpn92i1|PASS|regression|200.0304|861.5502|661.5199|330.71%|
|migraphx_cadene__inceptionv4i16|PASS|regression|8831.7309|9549.7418|718.0109|8.13%|
|migraphx_cadene__resnext101_64x4di1|PASS|regression|298.4827|1016.7835|718.3008|240.65%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|regression|1042.3007|13755.6168|12713.316|1219.74%|
|migraphx_mlperf__resnet50_v1|PASS|regression|150.4|413.3813|262.9814|174.85%|
|migraphx_models__whisper-tiny-decoder|PASS|regression|31.7376|489.6272|457.8896|1442.73%|
|migraphx_models__whisper-tiny-encoder|Numerics|regression|119.6922|2454.5918|2334.8997|1950.75%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|110.8246|99.2259|-11.5987|-10.47%|
|migraphx_torchvision__densenet121i32|PASS|regression|2681.7979|5088.2565|2406.4586|89.73%|
|migraphx_torchvision__inceptioni1|PASS|regression|291.7335|369.1837|77.4502|26.55%|
|migraphx_torchvision__resnet50i1|PASS|within tol|227.8563|216.9016|-10.9547|-4.81%|

## 26 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|RDN_pytorch_vaiq_int8|Numerics|compiled_inference|
|beit_large_patch16_384_Opset16_timm|PASS|compiled_inference|
|beit_large_patch16_384_Opset17_timm|PASS|compiled_inference|
|deit3_large_patch16_384_Opset16_timm|PASS|compiled_inference|
|efficientnet-lite4-11-qdq|Numerics|compilation|
|migraphx_pytorch-examples__wlang_lstm|PASS|compiled_inference|
|migx_bench_bert-large-uncased_16_128|PASS|compiled_inference|
|migx_bench_bert-large-uncased_16_256|PASS|compiled_inference|
|migx_bench_bert-large-uncased_16_384|Numerics|compiled_inference|
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
|vit_large_patch16_384_Opset17_timm|PASS|compiled_inference|

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

