## Passing Summary

**TOTAL TESTS = 62**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 0 | 0.0% | 0.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 62**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 62 | 100.0% |
| IREE Compilation | 0 | 0.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-token-classification-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-token-classification-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_albert-tiny-chinese-ws | setup | None | |
| hf_bcms-bertic-ner | setup | None | |
| hf_bert-base-arabic-camelbert-mix-ner | setup | None | |
| hf_bert-base-chinese-ner | setup | None | |
| hf_bert-base-chinese-pos | setup | None | |
| hf_bert-base-chinese-ws | setup | None | |
| hf_bert-base-indonesian-NER | setup | None | |
| hf_bert-base-japanese-v3-ner-wikipedia-dataset | setup | None | |
| hf_bert-base-multilingual-cased-ner-hrl | setup | None | |
| hf_bert-base-NER | setup | None | |
| hf_bert-base-NER-uncased | setup | None | |
| hf_bert-base-parsbert-ner-uncased | setup | None | |
| hf_bert-base-romanian-ner | setup | None | |
| hf_bert-base-swedish-cased-ner | setup | None | |
| hf_bert-base-thai-upos | setup | None | |
| hf_bert-base-turkish-cased-ner | setup | None | |
| hf_bert-english-uncased-finetuned-pos | setup | None | |
| hf_bert-fa-base-uncased-ner-peyma | setup | None | |
| hf_bert-large-cased-finetuned-conll03-english | setup | None | |
| hf_bert-large-NER | setup | None | |
| hf_bert-large-uncased_med-ner | setup | None | |
| hf_bert-spanish-cased-finetuned-ner | setup | None | |
| hf_bert_cased_ner | setup | None | |
| hf_biomedical-ner-all | setup | None | |
| hf_bpmn-information-extraction-v2 | setup | None | |
| hf_camembert-keyword-extractor | setup | None | |
| hf_camembert-ner | setup | None | |
| hf_camembert-ner-with-dates | setup | None | |
| hf_deberta-v3-base_finetuned_ai4privacy_v2 | setup | None | |
| hf_deberta_finetuned_pii | setup | None | |
| hf_deid_roberta_i2b2 | setup | None | |
| hf_distilbert-base-cased-finetuned-conll03-english | setup | None | |
| hf_distilbert-base-multilingual-cased-ner-hrl | setup | None | |
| hf_distilbert-NER | setup | None | |
| hf_distilbert-SBD-en-judgements-laws | setup | None | |
| hf_distilcamembert-base-ner | setup | None | |
| hf_french-camembert-postag-model | setup | None | |
| hf_IndicNER | setup | None | |
| hf_indobert-model-ner | setup | None | |
| hf_indonesian-roberta-base-posp-tagger | setup | None | |
| hf_ivila-row-layoutlm-finetuned-s2vl-v2 | setup | None | |
| hf_keyphrase-extraction-distilbert-inspec | setup | None | |
| hf_keyphrase-extraction-kbir-inspec | setup | None | |
| hf_KoELECTRA-small-v3-modu-ner | setup | None | |
| hf_llmlingua-2-bert-base-multilingual-cased-meetingbank | setup | None | |
| hf_Medical-NER | setup | None | |
| hf_nbailab-base-ner-scandi | setup | None | |
| hf_ner-bert-base-cased-pt-lenerbr | setup | None | |
| hf_NER-Indian-xlm-roberta | setup | None | |
| hf_ner-vietnamese-electra-base | setup | None | |
| hf_nerkor-cars-onpp-hubert | setup | None | |
| hf_piiranha-v1-detect-personal-information | setup | None | |
| hf_punctuate-all | setup | None | |
| hf_robbert-v2-dutch-ner | setup | None | |
| hf_roberta-large-ner-english | setup | None | |
| hf_roberta-large-ontonotes5 | setup | None | |
| hf_stanford-deidentifier-base | setup | None | |
| hf_tner-xlm-roberta-base-ontonotes5 | setup | None | |
| hf_wikineural-multilingual-ner | setup | None | |
| hf_xlm-roberta-base-ner-silvanus | setup | None | |
| hf_xlm-roberta-ner-japanese | setup | None | |
| hf_ZeroShotBioNER | setup | None | |
