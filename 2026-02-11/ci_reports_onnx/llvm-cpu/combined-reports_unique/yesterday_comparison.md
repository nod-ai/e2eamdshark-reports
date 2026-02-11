# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1565.5326|1520.8242|-44.7083|-2.86%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1589.888|1553.3218|-36.5662|-2.3%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12844.4383|12408.302|-436.1362|-3.4%|
|migraphx_ORT__distilgpt2_1|PASS|progression|771.6817|723.0196|-48.6621|-6.31%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2426.1554|2456.7972|30.6419|1.26%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|regression|8349.5829|10336.432|1986.8491|23.8%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|607.9351|663.5513|55.6162|9.15%|
|migraphx_cadene__dpn92i1|PASS|within tol|462.3788|439.8399|-22.5389|-4.87%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|9161.8075|9035.1272|-126.6803|-1.38%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|841.3635|816.3918|-24.9717|-2.97%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10322.6502|10195.0849|-127.5654|-1.24%|
|migraphx_mlperf__resnet50_v1|PASS|progression|208.9116|196.581|-12.3307|-5.9%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|323.271|297.8476|-25.4233|-7.86%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|1446.9088|1383.1033|-63.8055|-4.41%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|75.0763|56.8172|-18.2591|-24.32%|
|migraphx_pytorch-examples__wlang_lstm|PASS|progression|53.6162|32.5819|-21.0343|-39.23%|
|migraphx_torchvision__densenet121i32|PASS|within tol|4877.4135|4939.5496|62.1361|1.27%|
|migraphx_torchvision__inceptioni1|PASS|within tol|373.9647|356.6177|-17.347|-4.64%|
|migraphx_torchvision__resnet50i1|PASS|progression|211.7298|197.9196|-13.8102|-6.52%|

## 9 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 6 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|beit_large_patch16_384.in22k_ft_in22k_in1k|compiled_inference|PASS|
|convnext_xlarge.fb_in22k_ft_in1k|compiled_inference|PASS|
|deit3_large_patch16_384.fb_in1k|compiled_inference|PASS|
|eva_large_patch14_336.in22k_ft_in1k|compiled_inference|PASS|
|maxvit_large_tf_512.in1k|compiled_inference|PASS|
|model--albert-xxl-v2-finetuned-squad--anas-awadalla|compiled_inference|PASS|

