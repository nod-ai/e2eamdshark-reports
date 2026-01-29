## Passing Summary

**TOTAL TESTS = 62**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 60 | 96.8% | 96.8% |
| IREE Compilation | 56 | 90.3% | 93.3% |
| Gold Inference | 56 | 90.3% | 100.0% |
| IREE Inference Invocation | 56 | 90.3% | 100.0% |
| Inference Comparison (PASS) | 56 | 90.3% | 100.0% |
## Fail Summary

**TOTAL TESTS = 62**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 2 | 3.2% |
| IREE Compilation | 4 | 6.5% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-token-classification-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-token-classification-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_albert-tiny-chinese-ws | PASS | None | |
| hf_bcms-bertic-ner | PASS | None | |
| hf_bert-base-arabic-camelbert-mix-ner | PASS | None | |
| hf_bert-base-chinese-ner | PASS | None | |
| hf_bert-base-chinese-pos | PASS | None | |
| hf_bert-base-chinese-ws | PASS | None | |
| hf_bert-base-indonesian-NER | PASS | None | |
| hf_bert-base-japanese-v3-ner-wikipedia-dataset | PASS | None | |
| hf_bert-base-multilingual-cased-ner-hrl | PASS | None | |
| hf_bert-base-NER | PASS | None | |
| hf_bert-base-NER-uncased | PASS | None | |
| hf_bert-base-parsbert-ner-uncased | PASS | None | |
| hf_bert-base-romanian-ner | PASS | None | |
| hf_bert-base-swedish-cased-ner | PASS | None | |
| hf_bert-base-thai-upos | PASS | None | |
| hf_bert-base-turkish-cased-ner | PASS | None | |
| hf_bert-english-uncased-finetuned-pos | PASS | None | |
| hf_bert-fa-base-uncased-ner-peyma | PASS | None | |
| hf_bert-large-cased-finetuned-conll03-english | PASS | None | |
| hf_bert-large-NER | PASS | None | |
| hf_bert-large-uncased_med-ner | PASS | None | |
| hf_bert-spanish-cased-finetuned-ner | PASS | None | |
| hf_bert_cased_ner | setup | None | |
| hf_biomedical-ner-all | PASS | None | |
| hf_bpmn-information-extraction-v2 | PASS | None | |
| hf_camembert-keyword-extractor | PASS | None | |
| hf_camembert-ner | PASS | None | |
| hf_camembert-ner-with-dates | PASS | None | |
| hf_deberta-v3-base_finetuned_ai4privacy_v2 | compilation | None | |
| hf_deberta_finetuned_pii | compilation | None | |
| hf_deid_roberta_i2b2 | PASS | None | |
| hf_distilbert-base-cased-finetuned-conll03-english | PASS | None | |
| hf_distilbert-base-multilingual-cased-ner-hrl | PASS | None | |
| hf_distilbert-NER | PASS | None | |
| hf_distilbert-SBD-en-judgements-laws | PASS | None | |
| hf_distilcamembert-base-ner | PASS | None | |
| hf_french-camembert-postag-model | PASS | None | |
| hf_IndicNER | setup | None | |
| hf_indobert-model-ner | PASS | None | |
| hf_indonesian-roberta-base-posp-tagger | PASS | None | |
| hf_ivila-row-layoutlm-finetuned-s2vl-v2 | PASS | None | |
| hf_keyphrase-extraction-distilbert-inspec | PASS | None | |
| hf_keyphrase-extraction-kbir-inspec | PASS | None | |
| hf_KoELECTRA-small-v3-modu-ner | PASS | None | |
| hf_llmlingua-2-bert-base-multilingual-cased-meetingbank | PASS | None | |
| hf_Medical-NER | compilation | None | |
| hf_nbailab-base-ner-scandi | PASS | None | |
| hf_ner-bert-base-cased-pt-lenerbr | PASS | None | |
| hf_NER-Indian-xlm-roberta | PASS | None | |
| hf_ner-vietnamese-electra-base | PASS | None | |
| hf_nerkor-cars-onpp-hubert | PASS | None | |
| hf_piiranha-v1-detect-personal-information | compilation | None | |
| hf_punctuate-all | PASS | None | |
| hf_robbert-v2-dutch-ner | PASS | None | |
| hf_roberta-large-ner-english | PASS | None | |
| hf_roberta-large-ontonotes5 | PASS | None | |
| hf_stanford-deidentifier-base | PASS | None | |
| hf_tner-xlm-roberta-base-ontonotes5 | PASS | None | |
| hf_wikineural-multilingual-ner | PASS | None | |
| hf_xlm-roberta-base-ner-silvanus | PASS | None | |
| hf_xlm-roberta-ner-japanese | PASS | None | |
| hf_ZeroShotBioNER | PASS | None | |
