## Passing Summary

**TOTAL TESTS = 67**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 65 | 97.0% | 97.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 67**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 2 | 3.0% |
| IREE Compilation | 65 | 97.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-feature-extraction-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-feature-extraction-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_all-distilroberta-v1 | compilation | None | |
| hf_all-MiniLM-L12-v2 | compilation | None | |
| hf_all-MiniLM-L6-v2 | compilation | None | |
| hf_all-mpnet-base-v2 | compilation | None | |
| hf_all-roberta-large-v1 | compilation | None | |
| hf_bart-base | compilation | None | |
| hf_bert-base-nli-mean-tokens | compilation | None | |
| hf_bert-base-turkish-cased-mean-nli-stsb-tr | compilation | None | |
| hf_bge-base-en-v1.5 | compilation | None | |
| hf_bge-large-en | compilation | None | |
| hf_bge-large-en-v1.5 | compilation | None | |
| hf_bge-large-zh-v1.5 | compilation | None | |
| hf_bge-small-en | compilation | None | |
| hf_bge-small-en-v1.5 | compilation | None | |
| hf_biobert-v1.1 | compilation | None | |
| hf_codebert-base | compilation | None | |
| hf_conv-bert-base | compilation | None | |
| hf_cross-en-de-roberta-sentence-transformer | compilation | None | |
| hf_distilbert-base-nli-mean-tokens | compilation | None | |
| hf_distilbert-base-nli-stsb-mean-tokens | compilation | None | |
| hf_distiluse-base-multilingual-cased-v1 | compilation | None | |
| hf_distiluse-base-multilingual-cased-v2 | compilation | None | |
| hf_dragon-multiturn-context-encoder | compilation | None | |
| hf_dragon-multiturn-query-encoder | compilation | None | |
| hf_GIST-Embedding-v0 | compilation | None | |
| hf_GIST-large-Embedding-v0 | compilation | None | |
| hf_GIST-small-Embedding-v0 | compilation | None | |
| hf_gte-small | compilation | None | |
| hf_indobert-base-p1 | compilation | None | |
| hf_instructor-large | compilation | None | |
| hf_jina-embeddings-v2-small-en | compilation | None | |
| hf_ko-sroberta-multitask | compilation | None | |
| hf_kobert | compilation | None | |
| hf_LaBSE | compilation | None | |
| hf_LaBSE-en-ru | compilation | None | |
| hf_llm-embedder | compilation | None | |
| hf_msmarco-distilbert-base-tas-b | compilation | None | |
| hf_msmarco-distilbert-base-v4 | compilation | None | |
| hf_msmarco-distilbert-cos-v5 | compilation | None | |
| hf_msmarco-distilbert-dot-v5 | compilation | None | |
| hf_msmarco-MiniLM-L6-cos-v5 | compilation | None | |
| hf_multi-qa-distilbert-cos-v1 | compilation | None | |
| hf_multi-qa-MiniLM-L6-cos-v1 | compilation | None | |
| hf_multi-qa-mpnet-base-dot-v1 | compilation | None | |
| hf_mxbai-embed-large-v1 | compilation | None | |
| hf_paraphrase-MiniLM-L3-v2 | compilation | None | |
| hf_paraphrase-MiniLM-L6-v2 | compilation | None | |
| hf_paraphrase-mpnet-base-v2 | compilation | None | |
| hf_paraphrase-multilingual-MiniLM-L12-v2 | compilation | None | |
| hf_paraphrase-multilingual-mpnet-base-v2 | compilation | None | |
| hf_paraphrase-xlm-r-multilingual-v1 | compilation | None | |
| hf_roberta-base-nli-mean-tokens | compilation | None | |
| hf_rubert-base-cased | compilation | None | |
| hf_rubert-tiny | compilation | None | |
| hf_rubert-tiny2 | compilation | None | |
| hf_ruRoPEBert-e5-base-2k | setup | None | |
| hf_SapBERT-from-PubMedBERT-fulltext | compilation | None | |
| hf_SapBERT-UMLS-2020AB-all-lang-from-XLMR | compilation | None | |
| hf_sbert_large_nlu_ru | compilation | None | |
| hf_sentence-bert-base-ja-mean-tokens-v2 | setup | None | |
| hf_snowflake-arctic-embed-m | compilation | None | |
| hf_specter2_aug2023refresh_base | compilation | None | |
| hf_stsb-roberta-base | compilation | None | |
| hf_stsb-xlm-r-multilingual | compilation | None | |
| hf_sup-simcse-roberta-large | compilation | None | |
| hf_tiny-random-mt5 | compilation | None | |
| hf_UAE-Large-V1 | compilation | None | |
