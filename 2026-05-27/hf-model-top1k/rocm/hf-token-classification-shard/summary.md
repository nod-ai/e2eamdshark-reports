## Passing Summary

**TOTAL TESTS = 62**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 60 | 96.8% | 96.8% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 62**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 2 | 3.2% |
| IREE Compilation | 60 | 96.8% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-token-classification-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-token-classification-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_albert-tiny-chinese-ws | compilation | None | |
| hf_bcms-bertic-ner | compilation | None | |
| hf_bert-base-arabic-camelbert-mix-ner | compilation | None | |
| hf_bert-base-chinese-ner | compilation | None | |
| hf_bert-base-chinese-pos | compilation | None | |
| hf_bert-base-chinese-ws | compilation | None | |
| hf_bert-base-indonesian-NER | compilation | None | |
| hf_bert-base-japanese-v3-ner-wikipedia-dataset | compilation | None | |
| hf_bert-base-multilingual-cased-ner-hrl | compilation | None | |
| hf_bert-base-NER | compilation | None | |
| hf_bert-base-NER-uncased | compilation | None | |
| hf_bert-base-parsbert-ner-uncased | compilation | None | |
| hf_bert-base-romanian-ner | compilation | None | |
| hf_bert-base-swedish-cased-ner | compilation | None | |
| hf_bert-base-thai-upos | compilation | None | |
| hf_bert-base-turkish-cased-ner | compilation | None | |
| hf_bert-english-uncased-finetuned-pos | compilation | None | |
| hf_bert-fa-base-uncased-ner-peyma | compilation | None | |
| hf_bert-large-cased-finetuned-conll03-english | compilation | None | |
| hf_bert-large-NER | compilation | None | |
| hf_bert-large-uncased_med-ner | compilation | None | |
| hf_bert-spanish-cased-finetuned-ner | compilation | None | |
| hf_bert_cased_ner | setup | None | |
| hf_biomedical-ner-all | compilation | None | |
| hf_bpmn-information-extraction-v2 | compilation | None | |
| hf_camembert-keyword-extractor | compilation | None | |
| hf_camembert-ner | compilation | None | |
| hf_camembert-ner-with-dates | compilation | None | |
| hf_deberta-v3-base_finetuned_ai4privacy_v2 | compilation | None | |
| hf_deberta_finetuned_pii | compilation | None | |
| hf_deid_roberta_i2b2 | compilation | None | |
| hf_distilbert-base-cased-finetuned-conll03-english | compilation | None | |
| hf_distilbert-base-multilingual-cased-ner-hrl | compilation | None | |
| hf_distilbert-NER | compilation | None | |
| hf_distilbert-SBD-en-judgements-laws | compilation | None | |
| hf_distilcamembert-base-ner | compilation | None | |
| hf_french-camembert-postag-model | compilation | None | |
| hf_IndicNER | setup | None | |
| hf_indobert-model-ner | compilation | None | |
| hf_indonesian-roberta-base-posp-tagger | compilation | None | |
| hf_ivila-row-layoutlm-finetuned-s2vl-v2 | compilation | None | |
| hf_keyphrase-extraction-distilbert-inspec | compilation | None | |
| hf_keyphrase-extraction-kbir-inspec | compilation | None | |
| hf_KoELECTRA-small-v3-modu-ner | compilation | None | |
| hf_llmlingua-2-bert-base-multilingual-cased-meetingbank | compilation | None | |
| hf_Medical-NER | compilation | None | |
| hf_nbailab-base-ner-scandi | compilation | None | |
| hf_ner-bert-base-cased-pt-lenerbr | compilation | None | |
| hf_NER-Indian-xlm-roberta | compilation | None | |
| hf_ner-vietnamese-electra-base | compilation | None | |
| hf_nerkor-cars-onpp-hubert | compilation | None | |
| hf_piiranha-v1-detect-personal-information | compilation | None | |
| hf_punctuate-all | compilation | None | |
| hf_robbert-v2-dutch-ner | compilation | None | |
| hf_roberta-large-ner-english | compilation | None | |
| hf_roberta-large-ontonotes5 | compilation | None | |
| hf_stanford-deidentifier-base | compilation | None | |
| hf_tner-xlm-roberta-base-ontonotes5 | compilation | None | |
| hf_wikineural-multilingual-ner | compilation | None | |
| hf_xlm-roberta-base-ner-silvanus | compilation | None | |
| hf_xlm-roberta-ner-japanese | compilation | None | |
| hf_ZeroShotBioNER | compilation | None | |
