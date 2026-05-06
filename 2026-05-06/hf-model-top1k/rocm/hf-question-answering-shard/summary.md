## Passing Summary

**TOTAL TESTS = 57**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 57 | 100.0% | 100.0% |
| IREE Compilation | 52 | 91.2% | 91.2% |
| Gold Inference | 50 | 87.7% | 96.2% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 57**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 5 | 8.8% |
| Gold Inference | 2 | 3.5% |
| IREE Inference Invocation | 50 | 87.7% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-question-answering-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-question-answering-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_albert-base-v2-squad2 | compiled_inference | None | |
| hf_bert-base-cased-squad-v1.1-portuguese | compiled_inference | None | |
| hf_bert-base-cased-squad2 | compiled_inference | None | |
| hf_bert-base-spanish-wwm-cased-finetuned-spa-squad2-es | compiled_inference | None | |
| hf_bert-base-turkish-squad | compiled_inference | None | |
| hf_bert-base-uncased-squad-v1 | compiled_inference | None | |
| hf_bert-base-uncased-squad2 | compiled_inference | None | |
| hf_bert-extractive-qa-large-project | compiled_inference | None | |
| hf_bert-large-cased-squad-v1.1-portuguese | compiled_inference | None | |
| hf_bert-large-cased-whole-word-masking-finetuned-squad | compiled_inference | None | |
| hf_bert-large-finetuned-squad2 | compiled_inference | None | |
| hf_bert-large-uncased-whole-word-masking-finetuned-squad | compiled_inference | None | |
| hf_bert-large-uncased-whole-word-masking-squad2 | compiled_inference | None | |
| hf_bert-tiny-finetuned-squadv2 | compiled_inference | None | |
| hf_bertserini-bert-base-squad | compiled_inference | None | |
| hf_biobert-base-cased-v1.1-squad | compiled_inference | None | |
| hf_biobert-large-cased-v1.1-squad | compiled_inference | None | |
| hf_biobert-v1.1-biomedicalQuestionAnswering | compiled_inference | None | |
| hf_BioLinkBERT-base | compiled_inference | None | |
| hf_BioLinkBERT-large | compiled_inference | None | |
| hf_camembert-base-squadFR-fquad-piaf | compiled_inference | None | |
| hf_deberta-v3-base-squad2 | compilation | None | |
| hf_deberta-v3-large-squad2 | compilation | None | |
| hf_distilbert-base-cased-distilled-squad | compiled_inference | None | |
| hf_distilbert-base-uncased-distilled-squad | compiled_inference | None | |
| hf_distilbert-extractive-qa-large-project | compiled_inference | None | |
| hf_distilbert-extractive-qa-project | compiled_inference | None | |
| hf_distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es | compiled_inference | None | |
| hf_dynamic_tinybert | compiled_inference | None | |
| hf_electra_large_discriminator_squad2_512 | compiled_inference | None | |
| hf_gelectra-base-germanquad | compiled_inference | None | |
| hf_gelectra-large-germanquad | compiled_inference | None | |
| hf_indobert-lite-squad | compiled_inference | None | |
| hf_Indobert-QA | compiled_inference | None | |
| hf_koelectra-small-v2-distilled-korquad-384 | compiled_inference | None | |
| hf_LinkBERT-large | compiled_inference | None | |
| hf_mdeberta-v3-base-squad2 | compilation | None | |
| hf_minilm-uncased-squad2 | compiled_inference | None | |
| hf_mobilebert-uncased-squad-v2 | compiled_inference | None | |
| hf_question-answering-qa-may-12-tablang-LOCAL | compiled_inference | None | |
| hf_question-answering-roberta-base-s-v2 | compiled_inference | None | |
| hf_roberta-base-chinese-extractive-qa | compiled_inference | None | |
| hf_roberta-base-on-cuad | compiled_inference | None | |
| hf_roberta-base-squad2 | construct_inputs | None | |
| hf_roberta-base-squad2-distilled | compiled_inference | None | |
| hf_roberta-large-squad2 | construct_inputs | None | |
| hf_rubert_large_squad_2 | compiled_inference | None | |
| hf_sapbert-from-pubmedbert-squad2 | compiled_inference | None | |
| hf_splinter-base | compilation | None | |
| hf_splinter-base-qass | compilation | None | |
| hf_test-demo-qa | compiled_inference | None | |
| hf_test-demo-qa-with-roberta | compiled_inference | None | |
| hf_tiny-distilbert-base-cased-distilled-squad | compiled_inference | None | |
| hf_tinyroberta-squad2 | compiled_inference | None | |
| hf_WSPAlign-ft-kftt | compiled_inference | None | |
| hf_xlm-roberta-base-squad2 | compiled_inference | None | |
| hf_xlm-roberta-base-squad2-distilled | compiled_inference | None | |
