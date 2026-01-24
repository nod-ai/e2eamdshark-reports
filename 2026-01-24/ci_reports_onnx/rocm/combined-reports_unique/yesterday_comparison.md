# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|101.0957|101.4318|0.3361|0.33%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|285.6545|286.1131|0.4586|0.16%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|58.6226|58.1191|-0.5036|-0.86%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.3813|71.954|-0.4273|-0.59%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|285.9121|286.0813|0.1692|0.06%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.9666|38.6848|-0.2818|-0.72%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6878|12.7257|0.0379|0.3%|
|migraphx_cadene__dpn92i1|PASS|within tol|3.07|3.07|-0.0|-0.0%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.1164|20.0294|-0.087|-0.43%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.5152|2.4874|-0.0278|-1.11%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2946|7.3166|0.022|0.3%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|20.2873|21.0475|0.7603|3.75%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0831|15.3993|0.3162|2.1%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|26.6531|26.2664|-0.3867|-1.45%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|113.4454|113.7362|0.2908|0.26%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.5874|17.6248|0.0374|0.21%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.435|3.4488|0.0138|0.4%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.9274|1.9126|-0.0149|-0.77%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.2429|20.2775|0.0346|0.17%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.6944|33.1632|0.4687|1.43%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.4013|52.0716|0.6703|1.3%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.8359|11.859|0.0231|0.2%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.555|12.5151|-0.0399|-0.32%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.9252|12.932|0.0068|0.05%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.504|12.4808|-0.0232|-0.19%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8156|12.8373|0.0216|0.17%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4552|14.4919|0.0368|0.25%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.7322|31.9257|0.1935|0.61%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.4866|61.8979|0.4113|0.67%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.4069|95.9129|0.5061|0.53%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7624|12.7852|0.0228|0.18%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3615|14.4012|0.0396|0.28%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3672|20.3646|-0.0026|-0.01%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3924|14.4215|0.0292|0.2%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5388|20.6136|0.0748|0.36%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.1239|29.2317|0.1078|0.37%|

## No Regressions Found

## One Progression Found:

|model name|old_status|new_status|
|---|---|---|
|t5-decoder-with-lm-head-12|native_inference|PASS|

