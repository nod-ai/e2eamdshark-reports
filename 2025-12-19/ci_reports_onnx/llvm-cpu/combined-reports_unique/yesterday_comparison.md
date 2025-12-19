# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1856.8691|1798.7883|-58.0808|-3.13%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|1866.8547|1819.9664|-46.8884|-2.51%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|20372.4083|19965.5253|-406.883|-2.0%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|874.4496|870.3567|-4.093|-0.47%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2589.3238|2613.9824|24.6586|0.95%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|14062.4299|14011.3874|-51.0425|-0.36%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|619.8901|604.2878|-15.6022|-2.52%|
|migraphx_cadene__dpn92i1|PASS|regression|768.2872|885.287|116.9998|15.23%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|9533.8605|9788.5154|254.6548|2.67%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|1015.8396|1023.1227|7.2831|0.72%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|14303.2635|13987.2044|-316.0591|-2.21%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|354.6132|347.8519|-6.7613|-1.91%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|529.8784|540.1295|10.2511|1.93%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|2371.1359|2407.7478|36.6119|1.54%|
|migraphx_pytorch-examples__wlang_gru|PASS|progression|111.7586|93.5454|-18.2132|-16.3%|
|migraphx_torchvision__densenet121i32|PASS|within tol|5028.1441|5063.377|35.2329|0.7%|
|migraphx_torchvision__inceptioni1|PASS|within tol|373.0908|378.8298|5.739|1.54%|
|migraphx_torchvision__resnet50i1|PASS|progression|240.2369|219.3173|-20.9196|-8.71%|

## No Regressions Found

## No Progressions Found

