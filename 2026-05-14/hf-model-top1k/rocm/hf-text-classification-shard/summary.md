## Passing Summary

**TOTAL TESTS = 72**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 71 | 98.6% | 98.6% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 72**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 1.4% |
| IREE Compilation | 71 | 98.6% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-text-classification-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-text-classification-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_51-languages-classifier | compilation | None | |
| hf_albert-xlarge-vitaminc-mnli | compilation | None | |
| hf_autonlp-Gibberish-Detector-492513457 | compilation | None | |
| hf_bart-large-mnli | compilation | None | |
| hf_bert-base-multilingual-uncased-sentiment | compilation | None | |
| hf_bert-base-personality | compilation | None | |
| hf_bert-base-uncased-emotion | compilation | None | |
| hf_bert-base-uncased-hatexplain | compilation | None | |
| hf_bert-base-uncased-snli | compilation | None | |
| hf_bert-japanese-finetuned-sentiment | compilation | None | |
| hf_bert-tiny-finetuned-sms-spam-detection | compilation | None | |
| hf_bert-toxic-comment-classification | compilation | None | |
| hf_bert_turkish_sentiment | compilation | None | |
| hf_bertweet-base-sentiment-analysis | compilation | None | |
| hf_beto-sentiment-analysis | compilation | None | |
| hf_bge-reranker-base | compilation | None | |
| hf_CentralBankRoBERTa-sentiment-classifier | compilation | None | |
| hf_deberta-large-mnli | compilation | None | |
| hf_deberta-v3-base-absa-v1.1 | compilation | None | |
| hf_deberta-v3-base-injection | compilation | None | |
| hf_DeBERTa-v3-base-mnli-fever-anli | compilation | None | |
| hf_deberta-v3-base-zeroshot-v1.1-all-33 | compilation | None | |
| hf_deberta-v3-large_boolq | compilation | None | |
| hf_dehatebert-mono-english | compilation | None | |
| hf_dehatebert-mono-portugese | compilation | None | |
| hf_distilbert-base-multilingual-cased-sentiments-student | compilation | None | |
| hf_distilbert-base-uncased-finetuned-sst-2-english | compilation | None | |
| hf_distilroberta-finetuned-financial-news-sentiment-analysis | compilation | None | |
| hf_emotion-english-distilroberta-base | compilation | None | |
| hf_emotion_text_classifier | compilation | None | |
| hf_english-abusive-MuRIL | compilation | None | |
| hf_finbert | compilation | None | |
| hf_finbert-tone | compilation | None | |
| hf_Gender-Classification | compilation | None | |
| hf_german-sentiment-bert | compilation | None | |
| hf_indonesian-roberta-base-sentiment-classifier | compilation | None | |
| hf_koelectra-small-v3-nsmc | compilation | None | |
| hf_mDeBERTa-v3-base-mnli-xnli | compilation | None | |
| hf_MeaningBERT | compilation | None | |
| hf_ms-marco-electra-base | compilation | None | |
| hf_ms-marco-MiniLM-L-12-v2 | compilation | None | |
| hf_ms-marco-MiniLM-L-2-v2 | compilation | None | |
| hf_ms-marco-MiniLM-L-4-v2 | compilation | None | |
| hf_ms-marco-MiniLM-L-6-v2 | compilation | None | |
| hf_ms-marco-TinyBERT-L-2-v2 | compilation | None | |
| hf_mxbai-rerank-base-v1 | compilation | None | |
| hf_mxbai-rerank-xsmall-v1 | compilation | None | |
| hf_my_awesome_model | setup | None | |
| hf_nli-deberta-v3-base | compilation | None | |
| hf_NSFW_text_classifier | compilation | None | |
| hf_query_wellformedness_score | compilation | None | |
| hf_raceBERT-ethnicity | compilation | None | |
| hf_roberta-base-go_emotions | compilation | None | |
| hf_roberta-base-suicide-prediction-phr | compilation | None | |
| hf_roberta-hate-speech-dynabench-r4-target | compilation | None | |
| hf_roberta-large-mnli | compilation | None | |
| hf_robertuito-sentiment-analysis | compilation | None | |
| hf_rubert-base-cased-nli-threeway | compilation | None | |
| hf_rubert-tiny2-russian-sentiment | compilation | None | |
| hf_Sentimental-Analysis | compilation | None | |
| hf_stsb-TinyBERT-L-4 | compilation | None | |
| hf_suicidality | compilation | None | |
| hf_tamil-codemixed-abusive-MuRIL | compilation | None | |
| hf_toxic-bert | compilation | None | |
| hf_toxic-comment-model | compilation | None | |
| hf_twitter-roberta-base-irony | compilation | None | |
| hf_twitter-roberta-base-sentiment | compilation | None | |
| hf_twitter-roberta-base-sentiment-latest | compilation | None | |
| hf_twitter-xlm-roberta-base-sentiment | compilation | None | |
| hf_twitter-xlm-roberta-base-sentiment-multilingual | compilation | None | |
| hf_unbiased-toxic-roberta | compilation | None | |
| hf_xlm-roberta-base-language-detection | compilation | None | |
