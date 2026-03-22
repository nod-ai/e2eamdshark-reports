## Passing Summary

**TOTAL TESTS = 70**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 63 | 90.0% | 90.0% |
| IREE Compilation | 55 | 78.6% | 87.3% |
| Gold Inference | 55 | 78.6% | 100.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 70**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 7 | 10.0% |
| IREE Compilation | 8 | 11.4% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 55 | 78.6% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-fill-mask-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-fill-mask-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_albert-base-v2 | compiled_inference | None | |
| hf_albert-japanese-v2 | compiled_inference | None | |
| hf_ARBERTv2 | compiled_inference | None | |
| hf_astroBERT | compiled_inference | None | |
| hf_bert-base-5lang-cased | compiled_inference | None | |
| hf_bert-base-arabertv02 | compiled_inference | None | |
| hf_bert-base-cased | compiled_inference | None | |
| hf_bert-base-chinese | compiled_inference | None | |
| hf_bert-base-german-cased | compiled_inference | None | |
| hf_bert-base-indonesian-1.5G | compiled_inference | None | |
| hf_bert-base-italian-xxl-cased | compiled_inference | None | |
| hf_bert-base-italian-xxl-uncased | compiled_inference | None | |
| hf_bert-base-japanese | compiled_inference | None | |
| hf_bert-base-japanese-char | compiled_inference | None | |
| hf_bert-base-japanese-char-v2 | compiled_inference | None | |
| hf_bert-base-japanese-whole-word-masking | compiled_inference | None | |
| hf_bert-base-multilingual-cased | compiled_inference | None | |
| hf_bert-base-multilingual-uncased | compiled_inference | None | |
| hf_bert-base-portuguese-cased | compiled_inference | None | |
| hf_bert-base-spanish-wwm-uncased | compiled_inference | None | |
| hf_bert-base-uncased | compiled_inference | None | |
| hf_bert-kor-base | compiled_inference | None | |
| hf_bert-large-cased | compiled_inference | None | |
| hf_bert-large-portuguese-cased | compiled_inference | None | |
| hf_bert-large-uncased | compiled_inference | None | |
| hf_bertweet-base | compiled_inference | None | |
| hf_Bio_ClinicalBERT | compiled_inference | None | |
| hf_biobert-base-cased-v1.2 | compiled_inference | None | |
| hf_BiomedNLP-BiomedBERT-base-uncased-abstract | compiled_inference | None | |
| hf_BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext | compiled_inference | None | |
| hf_camembert-base | compiled_inference | None | |
| hf_ChemBERTa-77M-MLM | compiled_inference | None | |
| hf_chinese-roberta-wwm-ext | compiled_inference | None | |
| hf_codebert-base-mlm | compiled_inference | None | |
| hf_codebert-java | compiled_inference | None | |
| hf_codebert-python | compiled_inference | None | |
| hf_deberta-base | compilation | None | |
| hf_deberta-v2-base-japanese | compilation | None | |
| hf_deberta-v2-base-japanese-char-wwm | compilation | None | |
| hf_deberta-v3-base | compilation | None | |
| hf_deberta-v3-large | compilation | None | |
| hf_deberta-v3-small | compilation | None | |
| hf_deberta-v3-xsmall | compilation | None | |
| hf_distilbert-base-cased | compiled_inference | None | |
| hf_distilbert-base-multilingual-cased | compiled_inference | None | |
| hf_distilbert-base-uncased | compiled_inference | None | |
| hf_distilroberta-base | compiled_inference | None | |
| hf_efficient-splade-VI-BT-large-doc | setup | None | |
| hf_efficient-splade-VI-BT-large-query | setup | None | |
| hf_esm2_t12_35M_UR50D | compiled_inference | None | |
| hf_esm2_t30_150M_UR50D | compiled_inference | None | |
| hf_esm2_t36_3B_UR50D | setup | None | |
| hf_esm2_t6_8M_UR50D | compiled_inference | None | |
| hf_IndicBERTv2-MLM-only | compiled_inference | None | |
| hf_legal-bert-base-uncased | compiled_inference | None | |
| hf_legal-bert-small-uncased | compiled_inference | None | |
| hf_mdeberta-v3-base | compilation | None | |
| hf_opensearch-neural-sparse-encoding-doc-v2-distill | setup | None | |
| hf_phobert-base | compiled_inference | None | |
| hf_phobert-base-v2 | compiled_inference | None | |
| hf_prot_bert | compiled_inference | None | |
| hf_robbert-v2-dutch-base | compiled_inference | None | |
| hf_robeczech-base | compiled_inference | None | |
| hf_roberta-base | compiled_inference | None | |
| hf_roberta-large | compiled_inference | None | |
| hf_splade-cocondenser-ensembledistil | setup | None | |
| hf_splade-cocondenser-selfdistil | setup | None | |
| hf_Splade_PP_en_v1 | setup | None | |
| hf_wangchanberta-base-att-spm-uncased | compiled_inference | None | |
| hf_xlm-roberta-base | compiled_inference | None | |
