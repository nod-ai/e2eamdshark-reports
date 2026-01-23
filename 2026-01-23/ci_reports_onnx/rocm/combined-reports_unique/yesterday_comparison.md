# Test Run Comparison Report

## Performance Comparison

regression tolerance: 5.0%

progression tolerance: 5.0%

|model name|exit_status|analysis|old_time_ms|new_time_ms|change_ms|percent_change|
|---|---|---|---|---|---|---|
|migraphx_ORT__bert_base_cased_1|PASS|within tol|100.9309|101.0957|0.1648|0.16%|
|migraphx_ORT__bert_large_uncased_1|PASS|within tol|282.7619|285.6545|2.8926|1.02%|
|migraphx_ORT__distilgpt2_1|PASS|within tol|57.7268|58.6226|0.8958|1.55%|
|migraphx_ORT__onnx_models__bert_base_cased_1_fp16_gpu|Numerics|within tol|72.127|72.3813|0.2542|0.35%|
|migraphx_ORT__onnx_models__bert_large_uncased_1_fp16_gpu|Numerics|within tol|285.8373|285.9121|0.0748|0.03%|
|migraphx_ORT__onnx_models__distilgpt2_1_fp16_gpu|Numerics|within tol|38.7618|38.9666|0.2048|0.53%|
|migraphx_bert__bert-large-uncased|PASS|within tol|12.6572|12.6878|0.0306|0.24%|
|migraphx_cadene__dpn92i1|PASS|within tol|3.0345|3.07|0.0356|1.17%|
|migraphx_cadene__inceptionv4i16|Numerics|within tol|20.1194|20.1164|-0.003|-0.01%|
|migraphx_cadene__resnext101_64x4di1|PASS|within tol|2.4576|2.5152|0.0576|2.34%|
|migraphx_huggingface-transformers__bert_mrpc8|PASS|within tol|7.2426|7.2946|0.052|0.72%|
|migraphx_mlperf__bert_large_mlperf|Numerics|within tol|19.5801|20.2873|0.7072|3.61%|
|migraphx_mlperf__resnet50_v1|PASS|within tol|15.0788|15.0831|0.0043|0.03%|
|migraphx_models__whisper-tiny-decoder|PASS|within tol|25.5218|26.6531|1.1313|4.43%|
|migraphx_models__whisper-tiny-encoder|Numerics|within tol|112.2709|113.4454|1.1745|1.05%|
|migraphx_torchvision__densenet121i32|PASS|within tol|17.5789|17.5874|0.0085|0.05%|
|migraphx_torchvision__inceptioni1|PASS|within tol|3.4318|3.435|0.0032|0.09%|
|migraphx_torchvision__resnet50i1|PASS|within tol|1.9029|1.9274|0.0246|1.29%|
|migx_bench_bert-large-uncased_16_128|PASS|within tol|20.256|20.2429|-0.0131|-0.06%|
|migx_bench_bert-large-uncased_16_256|PASS|within tol|32.9062|32.6944|-0.2117|-0.64%|
|migx_bench_bert-large-uncased_16_384|PASS|within tol|51.7769|51.4013|-0.3756|-0.73%|
|migx_bench_bert-large-uncased_1_128|PASS|within tol|11.7647|11.8359|0.0712|0.61%|
|migx_bench_bert-large-uncased_1_256|PASS|within tol|12.5125|12.555|0.0425|0.34%|
|migx_bench_bert-large-uncased_1_384|PASS|within tol|12.867|12.9252|0.0582|0.45%|
|migx_bench_bert-large-uncased_2_128|PASS|within tol|12.3979|12.504|0.106|0.86%|
|migx_bench_bert-large-uncased_2_256|PASS|within tol|12.8363|12.8156|-0.0207|-0.16%|
|migx_bench_bert-large-uncased_2_384|PASS|within tol|14.442|14.4552|0.0132|0.09%|
|migx_bench_bert-large-uncased_32_128|PASS|within tol|31.6764|31.7322|0.0558|0.18%|
|migx_bench_bert-large-uncased_32_256|PASS|within tol|61.4793|61.4866|0.0072|0.01%|
|migx_bench_bert-large-uncased_32_384|Numerics|within tol|95.5162|95.4069|-0.1094|-0.11%|
|migx_bench_bert-large-uncased_4_128|PASS|within tol|12.7101|12.7624|0.0523|0.41%|
|migx_bench_bert-large-uncased_4_256|PASS|within tol|14.324|14.3615|0.0376|0.26%|
|migx_bench_bert-large-uncased_4_384|PASS|within tol|20.3017|20.3672|0.0655|0.32%|
|migx_bench_bert-large-uncased_8_128|PASS|within tol|14.3842|14.3924|0.0082|0.06%|
|migx_bench_bert-large-uncased_8_256|PASS|within tol|20.6208|20.5388|-0.082|-0.4%|
|migx_bench_bert-large-uncased_8_384|PASS|within tol|29.0603|29.1239|0.0636|0.22%|

## 15 Regressions Found:

|model name|old_status|new_status|
|---|---|---|
|model--YuisekinAI-mistral-0.7B--yuiseki|PASS|import_model|
|model--finetuned_gpt2-large_sst2_negation0.0_pretrainedFalse--yuhuizhang|PASS|import_model|
|model--long-t5-tglobal-large-pubmed-3k-booksum-16384-WIP--pszemraj|PASS|import_model|
|model--m2m100_418M-finetuned-kde4-en-to-pt_BR--danhsf|PASS|import_model|
|model--m2m100_418M-fr--Jour|PASS|import_model|
|model--mT5-base-HunSum-1--SZTAKI-HLT|compiled_inference|import_model|
|model--manifestoberta-xlm-roberta-56policy-topics-sentence-2023-1-1--manifesto-project|PASS|import_model|
|model--my_xlm-roberta-large-finetuned-conll03--BahAdoR0101|PASS|import_model|
|model--pegasus-cnn_dailymail--google|PASS|import_model|
|model--pegasus-large-book-summary--pszemraj|PASS|import_model|
|model--pegasus-large-booksum--cnicu|PASS|import_model|
|model--roberta-ner-multilingual--julian-schelb|PASS|import_model|
|model--t5-large-finetuned-xsum-cnn--sysresearch101|PASS|import_model|
|model--xlm-roberta-large-squad2--deepset|PASS|import_model|
|t5-decoder-with-lm-head-12|PASS|native_inference|

## No Progressions Found

