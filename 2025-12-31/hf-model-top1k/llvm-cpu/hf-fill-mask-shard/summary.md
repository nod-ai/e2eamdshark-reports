## Passing Summary

**TOTAL TESTS = 70**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 51 | 72.9% | 72.9% |
| IREE Compilation | 44 | 62.9% | 86.3% |
| Gold Inference | 44 | 62.9% | 100.0% |
| IREE Inference Invocation | 44 | 62.9% | 100.0% |
| Inference Comparison (PASS) | 44 | 62.9% | 100.0% |
## Fail Summary

**TOTAL TESTS = 70**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 19 | 27.1% |
| IREE Compilation | 7 | 10.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-fill-mask-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-fill-mask-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_albert-base-v2 | PASS | None | |
| hf_albert-japanese-v2 | PASS | None | |
| hf_ARBERTv2 | PASS | None | |
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
| hf_Bio_ClinicalBERT | PASS | None | |
| hf_biobert-base-cased-v1.2 | PASS | None | |
| hf_BiomedNLP-BiomedBERT-base-uncased-abstract | PASS | None | |
| hf_BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext | PASS | None | |
| hf_camembert-base | PASS | None | |
| hf_ChemBERTa-77M-MLM | PASS | None | |
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
| hf_IndicBERTv2-MLM-only | PASS | None | |
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
| hf_Splade_PP_en_v1 | setup | None | |
| hf_wangchanberta-base-att-spm-uncased | setup | None | |
| hf_xlm-roberta-base | setup | None | |
