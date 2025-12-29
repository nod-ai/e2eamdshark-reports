# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1522.0325|1427.4152|-94.6173|-6.22%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1330.8156|1316.4754|-14.3401|-1.08%|
|migraphx_ORT__bert_large_uncased_1|PASS|regression|10838.677|11827.0413|988.3643|9.12%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|588.1219|588.538|0.4161|0.07%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2213.2746|2243.6195|30.3449|1.37%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|7861.72|7647.3687|-214.3513|-2.73%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|regression|491.0939|515.7024|24.6084|5.01%|
|migraphx_bert__bert-large-uncased|PASS|within tol|28532.5662|28739.2126|206.6464|0.72%|
|migraphx_cadene__dpn92i1|PASS|within tol|410.5579|392.1716|-18.3863|-4.48%|
|migraphx_cadene__inceptionv4i16|PASS|regression|8439.1485|9292.7906|853.642|10.12%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|837.4799|810.5399|-26.94|-3.22%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7600.5526|7387.9695|-212.5831|-2.8%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|31260.8049|31244.1806|-16.6243|-0.05%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|243.1155|251.236|8.1205|3.34%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|245.4966|248.1931|2.6966|1.1%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|838.2573|828.8641|-9.3932|-1.12%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|50.0152|50.8017|0.7866|1.57%|
|migraphx_torchvision__densenet121i32|PASS|within tol|5188.7771|5112.5852|-76.1919|-1.47%|
|migraphx_torchvision__inceptioni1|PASS|progression|380.5215|348.8922|-31.6293|-8.31%|
|migraphx_torchvision__resnet50i1|PASS|progression|208.3504|197.427|-10.9234|-5.24%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|21131.6489|21107.309|-24.3399|-0.12%|
|migx_bench_bert-large-uncased_1_384|PASS|regression|30014.9763|33121.243|3106.2667|10.35%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|20709.9374|20794.4784|84.541|0.41%|

## No Regressions Found

## 3 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|longformer_Opset16|import_model|compilation|
|longformer_Opset17|import_model|compilation|
|longformer_Opset18|import_model|compilation|

