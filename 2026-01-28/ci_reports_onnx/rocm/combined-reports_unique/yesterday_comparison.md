# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|100.6265|100.9819|0.3553|0.35%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|282.167|282.329|0.1619|0.06%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.3743|57.6046|0.2303|0.4%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.1081|71.8512|-0.2569|-0.36%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|285.9409|286.046|0.1051|0.04%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.8128|38.8294|0.0166|0.04%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.634|12.707|0.0729|0.58%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.989|3.0367|0.0477|1.6%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|19.9561|20.0271|0.071|0.36%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.4573|2.4521|-0.0052|-0.21%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2371|7.2633|0.0261|0.36%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.7029|19.7456|0.0426|0.22%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.2963|15.3767|0.0804|0.53%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.22|25.5946|0.3746|1.49%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.3907|112.8623|0.4717|0.42%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.5462|17.5772|0.031|0.18%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.3948|3.3997|0.0049|0.14%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8958|1.9052|0.0093|0.49%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.1829|20.2998|0.117|0.58%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.9879|32.7904|-0.1975|-0.6%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.8757|51.5342|-0.3416|-0.66%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7804|11.8096|0.0292|0.25%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.4774|12.5107|0.0333|0.27%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.8384|12.9016|0.0632|0.49%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.4009|12.5162|0.1153|0.93%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.7719|12.812|0.0402|0.31%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4166|14.4432|0.0266|0.18%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.7334|31.4204|-0.3131|-0.99%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.564|60.9276|-0.6364|-1.03%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.604|94.5665|-1.0375|-1.09%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.6942|12.7479|0.0537|0.42%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3671|14.3863|0.0192|0.13%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.2906|20.3697|0.0791|0.39%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3516|14.3849|0.0333|0.23%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.5739|20.5845|0.0106|0.05%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.1105|29.0521|-0.0583|-0.2%|

## No Regressions Found

## One Progression Found:

|model name|old_status|new_status|
|---|---|---|
|t5-decoder-with-lm-head-12|native_inference|PASS|

