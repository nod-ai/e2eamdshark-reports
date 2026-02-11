## Passing Summary

**TOTAL TESTS = 67**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 66 | 98.5% | 98.5% |
| IREE Compilation | 66 | 98.5% | 100.0% |
| Gold Inference | 66 | 98.5% | 100.0% |
| IREE Inference Invocation | 66 | 98.5% | 100.0% |
| Inference Comparison (PASS) | 66 | 98.5% | 100.0% |
## Fail Summary

**TOTAL TESTS = 67**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 1 | 1.5% |
| IREE Compilation | 0 | 0.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-feature-extraction-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-feature-extraction-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_all-distilroberta-v1 | PASS | None | |
| hf_all-MiniLM-L12-v2 | PASS | None | |
| hf_all-MiniLM-L6-v2 | PASS | None | |
| hf_all-mpnet-base-v2 | PASS | None | |
| hf_all-roberta-large-v1 | PASS | None | |
| hf_bart-base | PASS | None | |
| hf_bert-base-nli-mean-tokens | PASS | None | |
| hf_bert-base-turkish-cased-mean-nli-stsb-tr | PASS | None | |
| hf_bge-base-en-v1.5 | PASS | None | |
| hf_bge-large-en | PASS | None | |
| hf_bge-large-en-v1.5 | PASS | None | |
| hf_bge-large-zh-v1.5 | PASS | None | |
| hf_bge-small-en | PASS | None | |
| hf_bge-small-en-v1.5 | PASS | None | |
| hf_biobert-v1.1 | PASS | None | |
| hf_codebert-base | PASS | None | |
| hf_conv-bert-base | PASS | None | |
| hf_cross-en-de-roberta-sentence-transformer | PASS | None | |
| hf_distilbert-base-nli-mean-tokens | PASS | None | |
| hf_distilbert-base-nli-stsb-mean-tokens | PASS | None | |
| hf_distiluse-base-multilingual-cased-v1 | PASS | None | |
| hf_distiluse-base-multilingual-cased-v2 | PASS | None | |
| hf_dragon-multiturn-context-encoder | PASS | None | |
| hf_dragon-multiturn-query-encoder | PASS | None | |
| hf_GIST-Embedding-v0 | PASS | None | |
| hf_GIST-large-Embedding-v0 | PASS | None | |
| hf_GIST-small-Embedding-v0 | PASS | None | |
| hf_gte-small | PASS | None | |
| hf_indobert-base-p1 | PASS | None | |
| hf_instructor-large | PASS | None | |
| hf_jina-embeddings-v2-small-en | PASS | None | |
| hf_ko-sroberta-multitask | PASS | None | |
| hf_kobert | PASS | None | |
| hf_LaBSE | PASS | None | |
| hf_LaBSE-en-ru | PASS | None | |
| hf_llm-embedder | PASS | None | |
| hf_msmarco-distilbert-base-tas-b | PASS | None | |
| hf_msmarco-distilbert-base-v4 | PASS | None | |
| hf_msmarco-distilbert-cos-v5 | PASS | None | |
| hf_msmarco-distilbert-dot-v5 | PASS | None | |
| hf_msmarco-MiniLM-L6-cos-v5 | PASS | None | |
| hf_multi-qa-distilbert-cos-v1 | PASS | None | |
| hf_multi-qa-MiniLM-L6-cos-v1 | PASS | None | |
| hf_multi-qa-mpnet-base-dot-v1 | PASS | None | |
| hf_mxbai-embed-large-v1 | PASS | None | |
| hf_paraphrase-MiniLM-L3-v2 | PASS | None | |
| hf_paraphrase-MiniLM-L6-v2 | PASS | None | |
| hf_paraphrase-mpnet-base-v2 | PASS | None | |
| hf_paraphrase-multilingual-MiniLM-L12-v2 | PASS | None | |
| hf_paraphrase-multilingual-mpnet-base-v2 | PASS | None | |
| hf_paraphrase-xlm-r-multilingual-v1 | PASS | None | |
| hf_roberta-base-nli-mean-tokens | PASS | None | |
| hf_rubert-base-cased | PASS | None | |
| hf_rubert-tiny | PASS | None | |
| hf_rubert-tiny2 | PASS | None | |
| hf_ruRoPEBert-e5-base-2k | setup | None | |
| hf_SapBERT-from-PubMedBERT-fulltext | PASS | None | |
| hf_SapBERT-UMLS-2020AB-all-lang-from-XLMR | PASS | None | |
| hf_sbert_large_nlu_ru | PASS | None | |
| hf_sentence-bert-base-ja-mean-tokens-v2 | PASS | None | |
| hf_snowflake-arctic-embed-m | PASS | None | |
| hf_specter2_aug2023refresh_base | PASS | None | |
| hf_stsb-roberta-base | PASS | None | |
| hf_stsb-xlm-r-multilingual | PASS | None | |
| hf_sup-simcse-roberta-large | PASS | None | |
| hf_tiny-random-mt5 | PASS | None | |
| hf_UAE-Large-V1 | PASS | None | |
