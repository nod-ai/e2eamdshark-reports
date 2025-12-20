# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|progression|1798.7883|1522.0325|-276.7558|-15.39%|
|migraphx_ORT__bert_base_uncased_1|PASS|progression|1819.9664|1330.8156|-489.1508|-26.88%|
|migraphx_ORT__bert_large_uncased_1|PASS|progression|19965.5253|10838.677|-9126.8483|-45.71%|
|migraphx_ORT__distilgpt2_1|PASS|progression|870.3567|588.1219|-282.2348|-32.43%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|progression|2613.9824|2213.2746|-400.7078|-15.33%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|progression|14011.3874|7861.72|-6149.6675|-43.89%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|progression|604.2878|491.0939|-113.1939|-18.73%|
|migraphx_cadene__dpn92i1|PASS|progression|885.287|410.5579|-474.7291|-53.62%|
|migraphx_cadene__inceptionv4i16|PASS|progression|9788.5154|8439.1485|-1349.3668|-13.79%|
|migraphx_cadene__resnext101_64x4di1|PASS|progression|1023.1227|837.4799|-185.6428|-18.14%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|progression|13987.2044|7600.5526|-6386.6518|-45.66%|
|migraphx_mlperf__resnet50_v1|PASS|progression|347.8519|243.1155|-104.7364|-30.11%|
|migraphx_models__whisper-tiny-decoder|PASS|progression|540.1295|245.4966|-294.6329|-54.55%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|2407.7478|838.2573|-1569.4905|-65.19%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|93.5454|50.0152|-43.5302|-46.53%|
|migraphx_torchvision__densenet121i32|PASS|within tol|5063.377|5188.7771|125.4001|2.48%|
|migraphx_torchvision__inceptioni1|PASS|within tol|378.8298|380.5215|1.6917|0.45%|
|migraphx_torchvision__resnet50i1|PASS|progression|219.3173|208.3504|-10.9669|-5.0%|

## 3 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|longformer_Opset16|compilation|import_model|
|longformer_Opset17|compilation|import_model|
|longformer_Opset18|compilation|import_model|

## 5 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|migx_bench_bert-large-uncased_1_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_1_384|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_128|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_256|compiled_inference|PASS|
|migx_bench_bert-large-uncased_2_384|compiled_inference|PASS|

