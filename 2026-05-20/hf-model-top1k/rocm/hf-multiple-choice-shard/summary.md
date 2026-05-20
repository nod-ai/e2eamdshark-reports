## Passing Summary

**TOTAL TESTS = 56**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 56 | 100.0% | 100.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 56**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 56 | 100.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-multiple-choice-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-multiple-choice-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_1_microsoft_deberta_V1.0 | compilation | None | |
| hf_1_microsoft_deberta_V1.1 | compilation | None | |
| hf_bert-base-japanese-v3-jcommonsenseqa | compilation | None | |
| hf_bert-base-uncased-e_CARE | compilation | None | |
| hf_bert-base-uncased-Figurative_Language | compilation | None | |
| hf_bert-base-uncased-finetune-kggpu | compilation | None | |
| hf_bert-base-uncased-finetuned-swag | compilation | None | |
| hf_bert-base-uncased-Vitamin_C_Fact_Verification | compilation | None | |
| hf_bert_base_swag_model | compilation | None | |
| hf_bert_multiple_choice | compilation | None | |
| hf_bert_science_multiple_choice | compilation | None | |
| hf_checkpoints_10_1_microsoft_deberta_V1.1_384 | compilation | None | |
| hf_checkpoints_1_16 | compilation | None | |
| hf_checkpoints_26_9_microsoft_deberta_21_9 | compilation | None | |
| hf_checkpoints_28_9_microsoft_deberta_V2 | compilation | None | |
| hf_checkpoints_28_9_microsoft_deberta_V4 | compilation | None | |
| hf_checkpoints_28_9_microsoft_deberta_V5 | compilation | None | |
| hf_checkpoints_29_9_microsoft_deberta_V1 | compilation | None | |
| hf_checkpoints_30_9_microsoft_deberta_V1.0_384 | compilation | None | |
| hf_checkpoints_3_14 | compilation | None | |
| hf_chinese_paragraph_bert-ext | compilation | None | |
| hf_content | compilation | None | |
| hf_COPA_10_shot | compilation | None | |
| hf_COPA_albert_base_finetuned | compilation | None | |
| hf_COPA_Bert_Base_Uncased_Finetuned | compilation | None | |
| hf_CRAB_bert_base_uncased_finetuned | compilation | None | |
| hf_deberta-v3-large_test | compilation | None | |
| hf_deberta-v3-large_test_9e-6 | compilation | None | |
| hf_Debertalarg_model_multichoice_Version2 | compilation | None | |
| hf_distilbert_distilbert-base-uncased-15-epoch | compilation | None | |
| hf_distilbert_multiple_choice | compilation | None | |
| hf_distilbert_science_multiple_choice | compilation | None | |
| hf_e_care_albert_base_finetuned | compilation | None | |
| hf_e_care_bert_base_uncased_finetuned | compilation | None | |
| hf_electra-base-fp16 | compilation | None | |
| hf_electra-base-multiple-choice-v2 | compilation | None | |
| hf_electra_multiple_choice | compilation | None | |
| hf_fine-tuned-MoritzLaurer-deberta-v3-large-zeroshot-v2.0-arceasy | compilation | None | |
| hf_finetuned-bert-piqa | compilation | None | |
| hf_kda-albert-xxlarge-v2-race | compilation | None | |
| hf_KUCI_albert_base_Finetuned | compilation | None | |
| hf_KUCI_Bert_Base_Finetuned | compilation | None | |
| hf_LLM | compilation | None | |
| hf_llm-mdeberta-v3-swag | compilation | None | |
| hf_mbert-base-parsinlu-multiple-choice | compilation | None | |
| hf_mcQA_model_bert | compilation | None | |
| hf_mDeBERTa-v3-xnli-ft-bs-multiple-choice | compilation | None | |
| hf_Multiple_Choice_swag | compilation | None | |
| hf_Multiple_Choice_swag_lr | compilation | None | |
| hf_my_awesome_swag_model | compilation | None | |
| hf_NLP_HW3 | compilation | None | |
| hf_output | compilation | None | |
| hf_parsbert-base-parsinlu-multiple-choice | compilation | None | |
| hf_phobert-base-finetuned | compilation | None | |
| hf_phobert-large-finetuned | compilation | None | |
| hf_wikibert-base-parsinlu-multiple-choice | compilation | None | |
