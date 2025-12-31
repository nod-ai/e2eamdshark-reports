## Passing Summary

**TOTAL TESTS = 137**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 111 | 81.0% | 81.0% |
| IREE Compilation | 104 | 75.9% | 93.7% |
| Gold Inference | 80 | 58.4% | 76.9% |
| IREE Inference Invocation | 80 | 58.4% | 100.0% |
| Inference Comparison (PASS) | 80 | 58.4% | 100.0% |
## Fail Summary

**TOTAL TESTS = 137**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 26 | 19.0% |
| IREE Compilation | 7 | 5.1% |
| Gold Inference | 24 | 17.5% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(sources=['./e2eamdshark-reports/ci_reports_llvm-cpu_hf-feature-extraction-shard_onnx_json/hf-feature-extraction-shard.json', './e2eamdshark-reports/ci_reports_llvm-cpu_hf-fill-mask-shard_onnx_json/hf-fill-mask-shard.json'], output='./e2eamdshark-reports/combined_reports_unique.json', report=True, report_file='./e2eamdshark-reports/combined_reports_unique.md')

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_GIST-Embedding-v0 | PASS | None | |
| hf_GIST-large-Embedding-v0 | PASS | None | |
| hf_GIST-small-Embedding-v0 | PASS | None | |
| hf_LaBSE | PASS | None | |
| hf_LaBSE-en-ru | PASS | None | |
| hf_SapBERT-UMLS-2020AB-all-lang-from-XLMR | PASS | None | |
| hf_SapBERT-from-PubMedBERT-fulltext | PASS | None | |
| hf_UAE-Large-V1 | PASS | None | |
| hf_all-MiniLM-L12-v2 | PASS | None | |
| hf_all-MiniLM-L6-v2 | PASS | None | |
| hf_all-distilroberta-v1 | PASS | None | |
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
| hf_gte-small | PASS | None | |
| hf_indobert-base-p1 | PASS | None | |
| hf_instructor-large | PASS | None | |
| hf_jina-embeddings-v2-small-en | PASS | None | |
| hf_ko-sroberta-multitask | construct_inputs | None | |
| hf_kobert | setup | None | |
| hf_llm-embedder | construct_inputs | None | |
| hf_msmarco-MiniLM-L6-cos-v5 | construct_inputs | None | |
| hf_msmarco-distilbert-base-tas-b | construct_inputs | None | |
| hf_msmarco-distilbert-base-v4 | construct_inputs | None | |
| hf_msmarco-distilbert-cos-v5 | construct_inputs | None | |
| hf_msmarco-distilbert-dot-v5 | construct_inputs | None | |
| hf_multi-qa-MiniLM-L6-cos-v1 | construct_inputs | None | |
| hf_multi-qa-distilbert-cos-v1 | construct_inputs | None | |
| hf_multi-qa-mpnet-base-dot-v1 | construct_inputs | None | |
| hf_mxbai-embed-large-v1 | construct_inputs | None | |
| hf_paraphrase-MiniLM-L3-v2 | construct_inputs | None | |
| hf_paraphrase-MiniLM-L6-v2 | construct_inputs | None | |
| hf_paraphrase-mpnet-base-v2 | construct_inputs | None | |
| hf_paraphrase-multilingual-MiniLM-L12-v2 | construct_inputs | None | |
| hf_paraphrase-multilingual-mpnet-base-v2 | construct_inputs | None | |
| hf_paraphrase-xlm-r-multilingual-v1 | construct_inputs | None | |
| hf_roberta-base-nli-mean-tokens | construct_inputs | None | |
| hf_ruRoPEBert-e5-base-2k | setup | None | |
| hf_rubert-base-cased | setup | None | |
| hf_rubert-tiny | setup | None | |
| hf_rubert-tiny2 | construct_inputs | None | |
| hf_sbert_large_nlu_ru | construct_inputs | None | |
| hf_sentence-bert-base-ja-mean-tokens-v2 | construct_inputs | None | |
| hf_snowflake-arctic-embed-m | construct_inputs | None | |
| hf_specter2_aug2023refresh_base | setup | None | |
| hf_stsb-roberta-base | construct_inputs | None | |
| hf_stsb-xlm-r-multilingual | construct_inputs | None | |
| hf_sup-simcse-roberta-large | setup | None | |
| hf_tiny-random-mt5 | setup | None | |
| hf_ARBERTv2 | PASS | None | |
| hf_Bio_ClinicalBERT | PASS | None | |
| hf_BiomedNLP-BiomedBERT-base-uncased-abstract | PASS | None | |
| hf_BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext | PASS | None | |
| hf_ChemBERTa-77M-MLM | PASS | None | |
| hf_IndicBERTv2-MLM-only | PASS | None | |
| hf_Splade_PP_en_v1 | setup | None | |
| hf_albert-base-v2 | PASS | None | |
| hf_albert-japanese-v2 | PASS | None | |
| hf_astroBERT | PASS | None | |
| hf_bert-base-5lang-cased | PASS | None | |
| hf_bert-base-arabertv02 | PASS | None | |
| hf_bert-base-cased | PASS | None | |
| hf_bert-base-chinese | PASS | None | |
| hf_bert-base-german-cased | PASS | None | |
| hf_bert-base-indonesian-1.5G | PASS | None | |
| hf_bert-base-italian-xxl-cased | PASS | None | |
| hf_bert-base-italian-xxl-uncased | PASS | None | |
| hf_bert-base-japanese | PASS | None | |
| hf_bert-base-japanese-char | PASS | None | |
| hf_bert-base-japanese-char-v2 | PASS | None | |
| hf_bert-base-japanese-whole-word-masking | PASS | None | |
| hf_bert-base-multilingual-cased | PASS | None | |
| hf_bert-base-multilingual-uncased | PASS | None | |
| hf_bert-base-portuguese-cased | PASS | None | |
| hf_bert-base-spanish-wwm-uncased | PASS | None | |
| hf_bert-base-uncased | PASS | None | |
| hf_bert-kor-base | PASS | None | |
| hf_bert-large-cased | PASS | None | |
| hf_bert-large-portuguese-cased | PASS | None | |
| hf_bert-large-uncased | PASS | None | |
| hf_bertweet-base | PASS | None | |
| hf_biobert-base-cased-v1.2 | PASS | None | |
| hf_camembert-base | PASS | None | |
| hf_chinese-roberta-wwm-ext | PASS | None | |
| hf_codebert-base-mlm | PASS | None | |
| hf_codebert-java | PASS | None | |
| hf_codebert-python | PASS | None | |
| hf_deberta-base | compilation | None | |
| hf_deberta-v2-base-japanese | compilation | None | |
| hf_deberta-v2-base-japanese-char-wwm | compilation | None | |
| hf_deberta-v3-base | compilation | None | |
| hf_deberta-v3-large | compilation | None | |
| hf_deberta-v3-small | compilation | None | |
| hf_deberta-v3-xsmall | compilation | None | |
| hf_distilbert-base-cased | PASS | None | |
| hf_distilbert-base-multilingual-cased | PASS | None | |
| hf_distilbert-base-uncased | PASS | None | |
| hf_distilroberta-base | PASS | None | |
| hf_efficient-splade-VI-BT-large-doc | setup | None | |
| hf_efficient-splade-VI-BT-large-query | setup | None | |
| hf_esm2_t12_35M_UR50D | PASS | None | |
| hf_esm2_t30_150M_UR50D | PASS | None | |
| hf_esm2_t36_3B_UR50D | setup | None | |
| hf_esm2_t6_8M_UR50D | PASS | None | |
| hf_legal-bert-base-uncased | setup | None | |
| hf_legal-bert-small-uncased | setup | None | |
| hf_mdeberta-v3-base | setup | None | |
| hf_opensearch-neural-sparse-encoding-doc-v2-distill | setup | None | |
| hf_phobert-base | setup | None | |
| hf_phobert-base-v2 | setup | None | |
| hf_prot_bert | setup | None | |
| hf_robbert-v2-dutch-base | setup | None | |
| hf_robeczech-base | setup | None | |
| hf_roberta-base | setup | None | |
| hf_roberta-large | setup | None | |
| hf_splade-cocondenser-ensembledistil | setup | None | |
| hf_splade-cocondenser-selfdistil | setup | None | |
| hf_wangchanberta-base-att-spm-uncased | setup | None | |
| hf_xlm-roberta-base | setup | None | |
