## Passing Summary

**TOTAL TESTS = 67**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 1 | 1.5% | 1.5% |
| IREE Compilation | 1 | 1.5% | 100.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 67**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 66 | 98.5% |
| IREE Compilation | 0 | 0.0% |
| Gold Inference | 1 | 1.5% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-feature-extraction-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-feature-extraction-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_all-distilroberta-v1 | setup | None | |
| hf_all-MiniLM-L12-v2 | setup | None | |
| hf_all-MiniLM-L6-v2 | setup | None | |
| hf_all-mpnet-base-v2 | setup | None | |
| hf_all-roberta-large-v1 | setup | None | |
| hf_bart-base | setup | None | |
| hf_bert-base-nli-mean-tokens | setup | None | |
| hf_bert-base-turkish-cased-mean-nli-stsb-tr | setup | None | |
| hf_bge-base-en-v1.5 | setup | None | |
| hf_bge-large-en | setup | None | |
| hf_bge-large-en-v1.5 | setup | None | |
| hf_bge-large-zh-v1.5 | setup | None | |
| hf_bge-small-en | setup | None | |
| hf_bge-small-en-v1.5 | setup | None | |
| hf_biobert-v1.1 | setup | None | |
| hf_codebert-base | setup | None | |
| hf_conv-bert-base | setup | None | |
| hf_cross-en-de-roberta-sentence-transformer | setup | None | |
| hf_distilbert-base-nli-mean-tokens | setup | None | |
| hf_distilbert-base-nli-stsb-mean-tokens | setup | None | |
| hf_distiluse-base-multilingual-cased-v1 | setup | None | |
| hf_distiluse-base-multilingual-cased-v2 | setup | None | |
| hf_dragon-multiturn-context-encoder | setup | None | |
| hf_dragon-multiturn-query-encoder | setup | None | |
| hf_GIST-Embedding-v0 | setup | None | |
| hf_GIST-large-Embedding-v0 | setup | None | |
| hf_GIST-small-Embedding-v0 | setup | None | |
| hf_gte-small | setup | None | |
| hf_indobert-base-p1 | setup | None | |
| hf_instructor-large | setup | None | |
| hf_jina-embeddings-v2-small-en | setup | None | |
| hf_ko-sroberta-multitask | setup | None | |
| hf_kobert | setup | None | |
| hf_LaBSE | setup | None | |
| hf_LaBSE-en-ru | setup | None | |
| hf_llm-embedder | setup | None | |
| hf_msmarco-distilbert-base-tas-b | setup | None | |
| hf_msmarco-distilbert-base-v4 | setup | None | |
| hf_msmarco-distilbert-cos-v5 | setup | None | |
| hf_msmarco-distilbert-dot-v5 | setup | None | |
| hf_msmarco-MiniLM-L6-cos-v5 | setup | None | |
| hf_multi-qa-distilbert-cos-v1 | setup | None | |
| hf_multi-qa-MiniLM-L6-cos-v1 | setup | None | |
| hf_multi-qa-mpnet-base-dot-v1 | setup | None | |
| hf_mxbai-embed-large-v1 | setup | None | |
| hf_paraphrase-MiniLM-L3-v2 | setup | None | |
| hf_paraphrase-MiniLM-L6-v2 | setup | None | |
| hf_paraphrase-mpnet-base-v2 | setup | None | |
| hf_paraphrase-multilingual-MiniLM-L12-v2 | setup | None | |
| hf_paraphrase-multilingual-mpnet-base-v2 | setup | None | |
| hf_paraphrase-xlm-r-multilingual-v1 | setup | None | |
| hf_roberta-base-nli-mean-tokens | setup | None | |
| hf_rubert-base-cased | setup | None | |
| hf_rubert-tiny | setup | None | |
| hf_rubert-tiny2 | setup | None | |
| hf_ruRoPEBert-e5-base-2k | setup | None | |
| hf_SapBERT-from-PubMedBERT-fulltext | setup | None | |
| hf_SapBERT-UMLS-2020AB-all-lang-from-XLMR | setup | None | |
| hf_sbert_large_nlu_ru | setup | None | |
| hf_sentence-bert-base-ja-mean-tokens-v2 | construct_inputs | None | |
| hf_snowflake-arctic-embed-m | setup | None | |
| hf_specter2_aug2023refresh_base | setup | None | |
| hf_stsb-roberta-base | setup | None | |
| hf_stsb-xlm-r-multilingual | setup | None | |
| hf_sup-simcse-roberta-large | setup | None | |
| hf_tiny-random-mt5 | setup | None | |
| hf_UAE-Large-V1 | setup | None | |
