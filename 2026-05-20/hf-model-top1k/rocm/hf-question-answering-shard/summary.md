## Passing Summary

**TOTAL TESTS = 57**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 57 | 100.0% | 100.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 57**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 57 | 100.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-question-answering-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-question-answering-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_albert-base-v2-squad2 | compilation | None | |
| hf_bert-base-cased-squad-v1.1-portuguese | compilation | None | |
| hf_bert-base-cased-squad2 | compilation | None | |
| hf_bert-base-spanish-wwm-cased-finetuned-spa-squad2-es | compilation | None | |
| hf_bert-base-turkish-squad | compilation | None | |
| hf_bert-base-uncased-squad-v1 | compilation | None | |
| hf_bert-base-uncased-squad2 | compilation | None | |
| hf_bert-extractive-qa-large-project | compilation | None | |
| hf_bert-large-cased-squad-v1.1-portuguese | compilation | None | |
| hf_bert-large-cased-whole-word-masking-finetuned-squad | compilation | None | |
| hf_bert-large-finetuned-squad2 | compilation | None | |
| hf_bert-large-uncased-whole-word-masking-finetuned-squad | compilation | None | |
| hf_bert-large-uncased-whole-word-masking-squad2 | compilation | None | |
| hf_bert-tiny-finetuned-squadv2 | compilation | None | |
| hf_bertserini-bert-base-squad | compilation | None | |
| hf_biobert-base-cased-v1.1-squad | compilation | None | |
| hf_biobert-large-cased-v1.1-squad | compilation | None | |
| hf_biobert-v1.1-biomedicalQuestionAnswering | compilation | None | |
| hf_BioLinkBERT-base | compilation | None | |
| hf_BioLinkBERT-large | compilation | None | |
| hf_camembert-base-squadFR-fquad-piaf | compilation | None | |
| hf_deberta-v3-base-squad2 | compilation | None | |
| hf_deberta-v3-large-squad2 | compilation | None | |
| hf_distilbert-base-cased-distilled-squad | compilation | None | |
| hf_distilbert-base-uncased-distilled-squad | compilation | None | |
| hf_distilbert-extractive-qa-large-project | compilation | None | |
| hf_distilbert-extractive-qa-project | compilation | None | |
| hf_distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es | compilation | None | |
| hf_dynamic_tinybert | compilation | None | |
| hf_electra_large_discriminator_squad2_512 | compilation | None | |
| hf_gelectra-base-germanquad | compilation | None | |
| hf_gelectra-large-germanquad | compilation | None | |
| hf_indobert-lite-squad | compilation | None | |
| hf_Indobert-QA | compilation | None | |
| hf_koelectra-small-v2-distilled-korquad-384 | compilation | None | |
| hf_LinkBERT-large | compilation | None | |
| hf_mdeberta-v3-base-squad2 | compilation | None | |
| hf_minilm-uncased-squad2 | compilation | None | |
| hf_mobilebert-uncased-squad-v2 | compilation | None | |
| hf_question-answering-qa-may-12-tablang-LOCAL | compilation | None | |
| hf_question-answering-roberta-base-s-v2 | compilation | None | |
| hf_roberta-base-chinese-extractive-qa | compilation | None | |
| hf_roberta-base-on-cuad | compilation | None | |
| hf_roberta-base-squad2 | compilation | None | |
| hf_roberta-base-squad2-distilled | compilation | None | |
| hf_roberta-large-squad2 | compilation | None | |
| hf_rubert_large_squad_2 | compilation | None | |
| hf_sapbert-from-pubmedbert-squad2 | compilation | None | |
| hf_splinter-base | compilation | None | |
| hf_splinter-base-qass | compilation | None | |
| hf_test-demo-qa | compilation | None | |
| hf_test-demo-qa-with-roberta | compilation | None | |
| hf_tiny-distilbert-base-cased-distilled-squad | compilation | None | |
| hf_tinyroberta-squad2 | compilation | None | |
| hf_WSPAlign-ft-kftt | compilation | None | |
| hf_xlm-roberta-base-squad2 | compilation | None | |
| hf_xlm-roberta-base-squad2-distilled | compilation | None | |
