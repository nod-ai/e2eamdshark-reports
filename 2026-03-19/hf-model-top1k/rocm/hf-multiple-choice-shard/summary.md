## Passing Summary

**TOTAL TESTS = 56**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 56 | 100.0% | 100.0% |
| IREE Compilation | 37 | 66.1% | 66.1% |
| Gold Inference | 37 | 66.1% | 100.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 56**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 19 | 33.9% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 37 | 66.1% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-multiple-choice-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-multiple-choice-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_1_microsoft_deberta_V1.0 | compilation | None | |
| hf_1_microsoft_deberta_V1.1 | compilation | None | |
| hf_bert-base-japanese-v3-jcommonsenseqa | compiled_inference | None | |
| hf_bert-base-uncased-e_CARE | compiled_inference | None | |
| hf_bert-base-uncased-Figurative_Language | compiled_inference | None | |
| hf_bert-base-uncased-finetune-kggpu | compiled_inference | None | |
| hf_bert-base-uncased-finetuned-swag | compiled_inference | None | |
| hf_bert-base-uncased-Vitamin_C_Fact_Verification | compiled_inference | None | |
| hf_bert_base_swag_model | compiled_inference | None | |
| hf_bert_multiple_choice | compiled_inference | None | |
| hf_bert_science_multiple_choice | compiled_inference | None | |
| hf_checkpoints_10_1_microsoft_deberta_V1.1_384 | compilation | None | |
| hf_checkpoints_1_16 | compilation | None | |
| hf_checkpoints_26_9_microsoft_deberta_21_9 | compilation | None | |
| hf_checkpoints_28_9_microsoft_deberta_V2 | compilation | None | |
| hf_checkpoints_28_9_microsoft_deberta_V4 | compilation | None | |
| hf_checkpoints_28_9_microsoft_deberta_V5 | compilation | None | |
| hf_checkpoints_29_9_microsoft_deberta_V1 | compilation | None | |
| hf_checkpoints_30_9_microsoft_deberta_V1.0_384 | compilation | None | |
| hf_checkpoints_3_14 | compilation | None | |
| hf_chinese_paragraph_bert-ext | compiled_inference | None | |
| hf_content | compilation | None | |
| hf_COPA_10_shot | compiled_inference | None | |
| hf_COPA_albert_base_finetuned | compiled_inference | None | |
| hf_COPA_Bert_Base_Uncased_Finetuned | compiled_inference | None | |
| hf_CRAB_bert_base_uncased_finetuned | compiled_inference | None | |
| hf_deberta-v3-large_test | compilation | None | |
| hf_deberta-v3-large_test_9e-6 | compilation | None | |
| hf_Debertalarg_model_multichoice_Version2 | compilation | None | |
| hf_distilbert_distilbert-base-uncased-15-epoch | compiled_inference | None | |
| hf_distilbert_multiple_choice | compiled_inference | None | |
| hf_distilbert_science_multiple_choice | compiled_inference | None | |
| hf_e_care_albert_base_finetuned | compiled_inference | None | |
| hf_e_care_bert_base_uncased_finetuned | compiled_inference | None | |
| hf_electra-base-fp16 | compiled_inference | None | |
| hf_electra-base-multiple-choice-v2 | compiled_inference | None | |
| hf_electra_multiple_choice | compiled_inference | None | |
| hf_fine-tuned-MoritzLaurer-deberta-v3-large-zeroshot-v2.0-arceasy | compilation | None | |
| hf_finetuned-bert-piqa | compiled_inference | None | |
| hf_kda-albert-xxlarge-v2-race | compiled_inference | None | |
| hf_KUCI_albert_base_Finetuned | compiled_inference | None | |
| hf_KUCI_Bert_Base_Finetuned | compiled_inference | None | |
| hf_LLM | compiled_inference | None | |
| hf_llm-mdeberta-v3-swag | compilation | None | |
| hf_mbert-base-parsinlu-multiple-choice | compiled_inference | None | |
| hf_mcQA_model_bert | compiled_inference | None | |
| hf_mDeBERTa-v3-xnli-ft-bs-multiple-choice | compilation | None | |
| hf_Multiple_Choice_swag | compiled_inference | None | |
| hf_Multiple_Choice_swag_lr | compiled_inference | None | |
| hf_my_awesome_swag_model | compiled_inference | None | |
| hf_NLP_HW3 | compiled_inference | None | |
| hf_output | compilation | None | |
| hf_parsbert-base-parsinlu-multiple-choice | compiled_inference | None | |
| hf_phobert-base-finetuned | compiled_inference | None | |
| hf_phobert-large-finetuned | compiled_inference | None | |
| hf_wikibert-base-parsinlu-multiple-choice | compiled_inference | None | |
