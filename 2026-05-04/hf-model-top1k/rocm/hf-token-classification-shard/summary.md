## Passing Summary

**TOTAL TESTS = 62**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 60 | 96.8% | 96.8% |
| IREE Compilation | 56 | 90.3% | 93.3% |
| Gold Inference | 54 | 87.1% | 96.4% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 62**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 2 | 3.2% |
| IREE Compilation | 4 | 6.5% |
| Gold Inference | 2 | 3.2% |
| IREE Inference Invocation | 54 | 87.1% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-token-classification-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-token-classification-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_albert-tiny-chinese-ws | compiled_inference | None | |
| hf_bcms-bertic-ner | compiled_inference | None | |
| hf_bert-base-arabic-camelbert-mix-ner | compiled_inference | None | |
| hf_bert-base-chinese-ner | compiled_inference | None | |
| hf_bert-base-chinese-pos | compiled_inference | None | |
| hf_bert-base-chinese-ws | compiled_inference | None | |
| hf_bert-base-indonesian-NER | compiled_inference | None | |
| hf_bert-base-japanese-v3-ner-wikipedia-dataset | compiled_inference | None | |
| hf_bert-base-multilingual-cased-ner-hrl | compiled_inference | None | |
| hf_bert-base-NER | compiled_inference | None | |
| hf_bert-base-NER-uncased | compiled_inference | None | |
| hf_bert-base-parsbert-ner-uncased | compiled_inference | None | |
| hf_bert-base-romanian-ner | compiled_inference | None | |
| hf_bert-base-swedish-cased-ner | compiled_inference | None | |
| hf_bert-base-thai-upos | compiled_inference | None | |
| hf_bert-base-turkish-cased-ner | compiled_inference | None | |
| hf_bert-english-uncased-finetuned-pos | compiled_inference | None | |
| hf_bert-fa-base-uncased-ner-peyma | compiled_inference | None | |
| hf_bert-large-cased-finetuned-conll03-english | compiled_inference | None | |
| hf_bert-large-NER | compiled_inference | None | |
| hf_bert-large-uncased_med-ner | compiled_inference | None | |
| hf_bert-spanish-cased-finetuned-ner | compiled_inference | None | |
| hf_bert_cased_ner | setup | None | |
| hf_biomedical-ner-all | compiled_inference | None | |
| hf_bpmn-information-extraction-v2 | compiled_inference | None | |
| hf_camembert-keyword-extractor | compiled_inference | None | |
| hf_camembert-ner | compiled_inference | None | |
| hf_camembert-ner-with-dates | compiled_inference | None | |
| hf_deberta-v3-base_finetuned_ai4privacy_v2 | compilation | None | |
| hf_deberta_finetuned_pii | compilation | None | |
| hf_deid_roberta_i2b2 | construct_inputs | None | |
| hf_distilbert-base-cased-finetuned-conll03-english | compiled_inference | None | |
| hf_distilbert-base-multilingual-cased-ner-hrl | compiled_inference | None | |
| hf_distilbert-NER | compiled_inference | None | |
| hf_distilbert-SBD-en-judgements-laws | compiled_inference | None | |
| hf_distilcamembert-base-ner | compiled_inference | None | |
| hf_french-camembert-postag-model | compiled_inference | None | |
| hf_IndicNER | setup | None | |
| hf_indobert-model-ner | compiled_inference | None | |
| hf_indonesian-roberta-base-posp-tagger | compiled_inference | None | |
| hf_ivila-row-layoutlm-finetuned-s2vl-v2 | compiled_inference | None | |
| hf_keyphrase-extraction-distilbert-inspec | compiled_inference | None | |
| hf_keyphrase-extraction-kbir-inspec | compiled_inference | None | |
| hf_KoELECTRA-small-v3-modu-ner | compiled_inference | None | |
| hf_llmlingua-2-bert-base-multilingual-cased-meetingbank | compiled_inference | None | |
| hf_Medical-NER | compilation | None | |
| hf_nbailab-base-ner-scandi | compiled_inference | None | |
| hf_ner-bert-base-cased-pt-lenerbr | compiled_inference | None | |
| hf_NER-Indian-xlm-roberta | compiled_inference | None | |
| hf_ner-vietnamese-electra-base | compiled_inference | None | |
| hf_nerkor-cars-onpp-hubert | compiled_inference | None | |
| hf_piiranha-v1-detect-personal-information | compilation | None | |
| hf_punctuate-all | compiled_inference | None | |
| hf_robbert-v2-dutch-ner | compiled_inference | None | |
| hf_roberta-large-ner-english | construct_inputs | None | |
| hf_roberta-large-ontonotes5 | compiled_inference | None | |
| hf_stanford-deidentifier-base | compiled_inference | None | |
| hf_tner-xlm-roberta-base-ontonotes5 | compiled_inference | None | |
| hf_wikineural-multilingual-ner | compiled_inference | None | |
| hf_xlm-roberta-base-ner-silvanus | compiled_inference | None | |
| hf_xlm-roberta-ner-japanese | compiled_inference | None | |
| hf_ZeroShotBioNER | compiled_inference | None | |
