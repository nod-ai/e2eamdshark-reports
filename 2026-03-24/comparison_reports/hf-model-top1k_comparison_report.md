---
# Test Comparison Report

*Generated on: 2026-03-24*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-03-24/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-03-24/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 494 | 493 | -1 |
| IREE Compilation | 388 | 403 | +15 |
| Gold Inference | 386 | 401 | +15 |
| IREE Inference Invocation | 383 | 397 | +14 |
| Inference Comparison (PASS) | 360 | 381 | +21 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 13 | 14 | +1 |
| IREE Compilation | 106 | 90 | -16 |
| Gold Inference | 2 | 2 | 0 |
| IREE Inference Invocation | 3 | 4 | +1 |
| Inference Comparison | 23 | 16 | -7 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-03-23/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-03-24/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 494 | 494 | 0 | ➖ NO CHANGE |
| IREE Compilation | 388 | 388 | 0 | ➖ NO CHANGE |
| Gold Inference | 386 | 386 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 288 | 383 | +95 | ✅ IMPROVED |
| Inference Comparison (PASS) | 265 | 360 | +95 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 13 | 13 | 0 | ➖ NO CHANGE |
| IREE Compilation | 106 | 106 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 98 | 3 | -95 | ✅ FEWER FAILURES |
| Inference Comparison | 23 | 23 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Inference Invocation**: +95 more tests passing
- **Inference Comparison (PASS)**: +95 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_COPA_10_shot | compiled_inference | PASS |
| hf_COPA_Bert_Base_Uncased_Finetuned | compiled_inference | PASS |
| hf_COPA_albert_base_finetuned | compiled_inference | PASS |
| hf_CRAB_bert_base_uncased_finetuned | compiled_inference | PASS |
| hf_KUCI_Bert_Base_Finetuned | compiled_inference | PASS |
| hf_KUCI_albert_base_Finetuned | compiled_inference | PASS |
| hf_LLM | compiled_inference | PASS |
| hf_Multiple_Choice_swag | compiled_inference | PASS |
| hf_Multiple_Choice_swag_lr | compiled_inference | PASS |
| hf_NLP_HW3 | compiled_inference | PASS |
| hf_bert-base-japanese-v3-jcommonsenseqa | compiled_inference | PASS |
| hf_bert-base-uncased-Figurative_Language | compiled_inference | PASS |
| hf_bert-base-uncased-Vitamin_C_Fact_Verification | compiled_inference | PASS |
| hf_bert-base-uncased-e_CARE | compiled_inference | PASS |
| hf_bert-base-uncased-finetune-kggpu | compiled_inference | PASS |
| hf_bert-base-uncased-finetuned-swag | compiled_inference | PASS |
| hf_bert_base_swag_model | compiled_inference | PASS |
| hf_bert_multiple_choice | compiled_inference | PASS |
| hf_bert_science_multiple_choice | compiled_inference | PASS |
| hf_chinese_paragraph_bert-ext | compiled_inference | PASS |
| hf_distilbert_distilbert-base-uncased-15-epoch | compiled_inference | PASS |
| hf_distilbert_multiple_choice | compiled_inference | PASS |
| hf_distilbert_science_multiple_choice | compiled_inference | PASS |
| hf_e_care_albert_base_finetuned | compiled_inference | PASS |
| hf_e_care_bert_base_uncased_finetuned | compiled_inference | PASS |
| hf_electra-base-fp16 | compiled_inference | PASS |
| hf_electra-base-multiple-choice-v2 | compiled_inference | PASS |
| hf_electra_multiple_choice | compiled_inference | PASS |
| hf_finetuned-bert-piqa | compiled_inference | PASS |
| hf_kda-albert-xxlarge-v2-race | compiled_inference | PASS |
| hf_mbert-base-parsinlu-multiple-choice | compiled_inference | PASS |
| hf_mcQA_model_bert | compiled_inference | PASS |
| hf_my_awesome_swag_model | compiled_inference | PASS |
| hf_parsbert-base-parsinlu-multiple-choice | compiled_inference | PASS |
| hf_wikibert-base-parsinlu-multiple-choice | compiled_inference | PASS |
| hf_51-languages-classifier | compiled_inference | PASS |
| hf_CentralBankRoBERTa-sentiment-classifier | compiled_inference | PASS |
| hf_Gender-Classification | compiled_inference | PASS |
| hf_MeaningBERT | compiled_inference | PASS |
| hf_NSFW_text_classifier | compiled_inference | PASS |
| hf_Sentimental-Analysis | compiled_inference | PASS |
| hf_albert-xlarge-vitaminc-mnli | compiled_inference | PASS |
| hf_autonlp-Gibberish-Detector-492513457 | compiled_inference | PASS |
| hf_bert-base-multilingual-uncased-sentiment | compiled_inference | PASS |
| hf_bert-base-personality | compiled_inference | PASS |
| hf_bert-base-uncased-emotion | compiled_inference | PASS |
| hf_bert-base-uncased-hatexplain | compiled_inference | PASS |
| hf_bert-base-uncased-snli | compiled_inference | PASS |
| hf_bert-japanese-finetuned-sentiment | compiled_inference | PASS |
| hf_bert-tiny-finetuned-sms-spam-detection | compiled_inference | PASS |

*... and 45 more improved models*

**Total improved models: 95**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-03-23/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-03-24/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 403 | 403 | 0 | ➖ NO CHANGE |
| Gold Inference | 401 | 401 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 397 | 397 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 381 | 381 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 90 | 90 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 4 | 4 | 0 | ➖ NO CHANGE |
| Inference Comparison | 16 | 16 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

