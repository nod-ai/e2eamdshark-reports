## Passing Summary

**TOTAL TESTS = 72**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 71 | 98.6% | 98.6% |
| IREE Compilation | 60 | 83.3% | 84.5% |
| Gold Inference | 60 | 83.3% | 100.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 72**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 1.4% |
| IREE Compilation | 11 | 15.3% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 60 | 83.3% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-text-classification-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-text-classification-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_51-languages-classifier | compiled_inference | None | |
| hf_albert-xlarge-vitaminc-mnli | compiled_inference | None | |
| hf_autonlp-Gibberish-Detector-492513457 | compiled_inference | None | |
| hf_bart-large-mnli | compilation | None | |
| hf_bert-base-multilingual-uncased-sentiment | compiled_inference | None | |
| hf_bert-base-personality | compiled_inference | None | |
| hf_bert-base-uncased-emotion | compiled_inference | None | |
| hf_bert-base-uncased-hatexplain | compiled_inference | None | |
| hf_bert-base-uncased-snli | compiled_inference | None | |
| hf_bert-japanese-finetuned-sentiment | compiled_inference | None | |
| hf_bert-tiny-finetuned-sms-spam-detection | compiled_inference | None | |
| hf_bert-toxic-comment-classification | compiled_inference | None | |
| hf_bert_turkish_sentiment | compiled_inference | None | |
| hf_bertweet-base-sentiment-analysis | compiled_inference | None | |
| hf_beto-sentiment-analysis | compiled_inference | None | |
| hf_bge-reranker-base | compiled_inference | None | |
| hf_CentralBankRoBERTa-sentiment-classifier | compiled_inference | None | |
| hf_deberta-large-mnli | compilation | None | |
| hf_deberta-v3-base-absa-v1.1 | compilation | None | |
| hf_deberta-v3-base-injection | compilation | None | |
| hf_DeBERTa-v3-base-mnli-fever-anli | compilation | None | |
| hf_deberta-v3-base-zeroshot-v1.1-all-33 | compilation | None | |
| hf_deberta-v3-large_boolq | compilation | None | |
| hf_dehatebert-mono-english | compiled_inference | None | |
| hf_dehatebert-mono-portugese | compiled_inference | None | |
| hf_distilbert-base-multilingual-cased-sentiments-student | compiled_inference | None | |
| hf_distilbert-base-uncased-finetuned-sst-2-english | compiled_inference | None | |
| hf_distilroberta-finetuned-financial-news-sentiment-analysis | compiled_inference | None | |
| hf_emotion-english-distilroberta-base | compiled_inference | None | |
| hf_emotion_text_classifier | compiled_inference | None | |
| hf_english-abusive-MuRIL | compiled_inference | None | |
| hf_finbert | compiled_inference | None | |
| hf_finbert-tone | compiled_inference | None | |
| hf_Gender-Classification | compiled_inference | None | |
| hf_german-sentiment-bert | compiled_inference | None | |
| hf_indonesian-roberta-base-sentiment-classifier | compiled_inference | None | |
| hf_koelectra-small-v3-nsmc | compiled_inference | None | |
| hf_mDeBERTa-v3-base-mnli-xnli | compilation | None | |
| hf_MeaningBERT | compiled_inference | None | |
| hf_ms-marco-electra-base | compiled_inference | None | |
| hf_ms-marco-MiniLM-L-12-v2 | compiled_inference | None | |
| hf_ms-marco-MiniLM-L-2-v2 | compiled_inference | None | |
| hf_ms-marco-MiniLM-L-4-v2 | compiled_inference | None | |
| hf_ms-marco-MiniLM-L-6-v2 | compiled_inference | None | |
| hf_ms-marco-TinyBERT-L-2-v2 | compiled_inference | None | |
| hf_mxbai-rerank-base-v1 | compilation | None | |
| hf_mxbai-rerank-xsmall-v1 | compilation | None | |
| hf_my_awesome_model | setup | None | |
| hf_nli-deberta-v3-base | compilation | None | |
| hf_NSFW_text_classifier | compiled_inference | None | |
| hf_query_wellformedness_score | compiled_inference | None | |
| hf_raceBERT-ethnicity | compiled_inference | None | |
| hf_roberta-base-go_emotions | compiled_inference | None | |
| hf_roberta-base-suicide-prediction-phr | compiled_inference | None | |
| hf_roberta-hate-speech-dynabench-r4-target | compiled_inference | None | |
| hf_roberta-large-mnli | compiled_inference | None | |
| hf_robertuito-sentiment-analysis | compiled_inference | None | |
| hf_rubert-base-cased-nli-threeway | compiled_inference | None | |
| hf_rubert-tiny2-russian-sentiment | compiled_inference | None | |
| hf_Sentimental-Analysis | compiled_inference | None | |
| hf_stsb-TinyBERT-L-4 | compiled_inference | None | |
| hf_suicidality | compiled_inference | None | |
| hf_tamil-codemixed-abusive-MuRIL | compiled_inference | None | |
| hf_toxic-bert | compiled_inference | None | |
| hf_toxic-comment-model | compiled_inference | None | |
| hf_twitter-roberta-base-irony | compiled_inference | None | |
| hf_twitter-roberta-base-sentiment | compiled_inference | None | |
| hf_twitter-roberta-base-sentiment-latest | compiled_inference | None | |
| hf_twitter-xlm-roberta-base-sentiment | compiled_inference | None | |
| hf_twitter-xlm-roberta-base-sentiment-multilingual | compiled_inference | None | |
| hf_unbiased-toxic-roberta | compiled_inference | None | |
| hf_xlm-roberta-base-language-detection | compiled_inference | None | |
