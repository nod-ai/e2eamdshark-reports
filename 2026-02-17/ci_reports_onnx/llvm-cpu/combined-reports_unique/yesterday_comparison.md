# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|1531.0751|1597.9898|66.9147|4.37%|
|migraphx_ORT__bert_base_uncased_1|PASS|regression|1498.4515|1589.3946|90.9431|6.07%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|12318.1616|12896.7411|578.5794|4.7%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|737.96|738.1373|0.1774|0.02%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|2471.561|2507.9459|36.3849|1.47%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|10109.9765|10140.8748|30.8983|0.31%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|647.6955|615.5751|-32.1204|-4.96%|
|migraphx_cadene__dpn92i1|PASS|within tol|440.5356|437.0882|-3.4474|-0.78%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|8768.4416|8760.5088|-7.9329|-0.09%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|808.6799|807.1926|-1.4873|-0.18%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|10300.3301|10474.3753|174.0452|1.69%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|164.9651|163.1392|-1.826|-1.11%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|296.1233|294.4752|-1.6481|-0.56%|
|migraphx_models__whisper-tiny-encoder|Numerics|progression|1549.4456|1432.1454|-117.3002|-7.57%|
|migraphx_pytorch-examples__wlang_gru|PASS|within tol|57.5234|55.4166|-2.1069|-3.66%|
|migraphx_pytorch-examples__wlang_lstm|PASS|regression|32.1151|35.5753|3.4601|10.77%|
|migraphx_torchvision__densenet121i32|PASS|within tol|3583.5535|3541.0458|-42.5078|-1.19%|
|migraphx_torchvision__inceptioni1|PASS|progression|395.4558|357.2608|-38.195|-9.66%|
|migraphx_torchvision__resnet50i1|PASS|within tol|195.729|200.3825|4.6535|2.38%|

## 10 Regressions Found:

|model name|old_status|new_status|
|---|---|---|

## 6 Progressions Found:

|model name|old_status|new_status|
|---|---|---|
|gluon_xception65|compiled_inference|PASS|
|pnasnet5large|compiled_inference|Numerics|
|regnetz_c16_evos_Opset16|Numerics|PASS|
|regnetz_c16_evos_Opset17|Numerics|PASS|
|regnetz_d8_evos_Opset16|Numerics|PASS|
|regnetz_d8_evos_Opset17|Numerics|PASS|

