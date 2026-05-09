# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1427.8555|1440.4937|12.6382|0.89%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1546.1632|1520.7448|-25.4184|-1.64%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12935.1637|12945.693|10.5294|0.08%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|706.9027|718.6363|11.7336|1.66%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|1147.1037|1113.8021|-33.3016|-2.9%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|6497.7424|6405.8821|-91.8603|-1.41%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|544.8938|538.0672|-6.8266|-1.25%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|717.2534|747.0342|29.7808|4.15%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10495.0709|10607.5015|112.4305|1.07%|
|migraphx_mlperf__resnet50_v1|PASS|progression|205.7611|189.9302|-15.8308|-7.69%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|264.9434|271.4562|6.5128|2.46%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1300.8079|1351.7552|50.9473|3.92%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|96.0896|98.7592|2.6696|2.78%|
|migraphx_pytorch-examples__wlang_lstm|PASS|within tol|16.2783|16.0301|-0.2482|-1.52%|
|migraphx_torchvision__inceptioni1|PASS|regression|322.112|344.3221|22.2101|6.9%|
|migraphx_torchvision__resnet50i1|PASS|regression|146.1076|158.1097|12.0021|8.21%|

## 20 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 5 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384_Opset16_timm|compiled_inference|PASS|
|beit_large_patch16_384_Opset17_timm|compiled_inference|PASS|
|model--albert-xxl-v2-finetuned-squad--anas-awadalla|compiled_inference|PASS|
|resnet50-v1-12-qdq|Numerics|PASS|
|vit_large_patch16_384_Opset17_timm|compiled_inference|PASS|

