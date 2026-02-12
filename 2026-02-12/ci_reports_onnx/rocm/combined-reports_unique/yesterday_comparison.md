# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|99.5626|99.4181|-0.1445|-0.15%|
|migraphx_ORT__bert_base_uncased_1|PASS|within tol|99.6166|99.3549|-0.2617|-0.26%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|292.7853|290.7916|-1.9936|-0.68%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.3287|57.1321|-0.1966|-0.34%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|70.6721|70.5927|-0.0794|-0.11%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|288.2355|287.3033|-0.9322|-0.32%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.6902|38.8813|0.1911|0.49%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6922|12.6843|-0.0079|-0.06%|
|migraphx_cadene__dpn92i1|PASS|within tol|2.9091|2.9082|-0.0009|-0.03%|
|migraphx_cadene__inceptionv4i16|PASS|within tol|19.6545|19.6081|-0.0464|-0.24%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.3535|2.3522|-0.0013|-0.05%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2443|7.2563|0.0119|0.16%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.589|19.6156|0.0266|0.14%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|14.901|14.8981|-0.0029|-0.02%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.8755|25.4649|-0.4107|-1.59%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.9479|112.4255|-0.5224|-0.46%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.4279|17.3609|-0.067|-0.38%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.329|3.3014|-0.0277|-0.83%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.8535|1.8599|0.0064|0.34%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.405|20.347|-0.058|-0.28%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|33.877|33.0607|-0.8163|-2.41%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|53.1341|51.8357|-1.2984|-2.44%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.792|11.7346|-0.0574|-0.49%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5361|12.4687|-0.0675|-0.54%|
|migx_bench_bert-large-uncased_1_384|PASS|progression|24.389|12.8747|-11.5143|-47.21%|
|migx_bench_bert-large-uncased_2_128|PASS|progression|29.4752|12.4024|-17.0728|-57.92%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.768|12.8251|0.0571|0.45%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.4497|14.4612|0.0115|0.08%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|32.5954|31.8031|-0.7923|-2.43%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|62.8399|61.9361|-0.9038|-1.44%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|97.1362|95.6855|-1.4507|-1.49%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7203|12.7241|0.0039|0.03%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.3783|14.3802|0.0019|0.01%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.4355|20.4113|-0.0242|-0.12%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3867|14.3849|-0.0018|-0.01%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.7521|20.7196|-0.0324|-0.16%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.6535|29.1804|-0.4731|-1.6%|

## No Regressions Found

## No Progressions Found

