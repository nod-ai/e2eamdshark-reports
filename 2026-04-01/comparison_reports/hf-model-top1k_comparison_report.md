---
# Test Comparison Report

*Generated on: 2026-04-01*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-04-01/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-04-01/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 348 | 397 | +49 |
| Inference Comparison (PASS) | 334 | 381 | +47 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 13 | 14 | +1 |
| IREE Compilation | 106 | 90 | -16 |
| Gold Inference | 2 | 2 | 0 |
| IREE Inference Invocation | 38 | 4 | -34 |
| Inference Comparison | 14 | 16 | +2 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-03-31/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-04-01/hf-model-top1k/rocm/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 383 | 348 | -35 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 369 | 334 | -35 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 13 | 13 | 0 | ➖ NO CHANGE |
| IREE Compilation | 106 | 106 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3 | 38 | +35 | ⚠️ MORE FAILURES |
| Inference Comparison | 14 | 14 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -35 fewer tests passing
- **Inference Comparison (PASS)**: -35 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_COPA_10_shot | PASS | compiled_inference |
| hf_COPA_Bert_Base_Uncased_Finetuned | PASS | compiled_inference |
| hf_COPA_albert_base_finetuned | PASS | compiled_inference |
| hf_CRAB_bert_base_uncased_finetuned | PASS | compiled_inference |
| hf_KUCI_Bert_Base_Finetuned | PASS | compiled_inference |
| hf_KUCI_albert_base_Finetuned | PASS | compiled_inference |
| hf_LLM | PASS | compiled_inference |
| hf_Multiple_Choice_swag | PASS | compiled_inference |
| hf_Multiple_Choice_swag_lr | PASS | compiled_inference |
| hf_NLP_HW3 | PASS | compiled_inference |
| hf_bert-base-japanese-v3-jcommonsenseqa | PASS | compiled_inference |
| hf_bert-base-uncased-Figurative_Language | PASS | compiled_inference |
| hf_bert-base-uncased-Vitamin_C_Fact_Verification | PASS | compiled_inference |
| hf_bert-base-uncased-e_CARE | PASS | compiled_inference |
| hf_bert-base-uncased-finetune-kggpu | PASS | compiled_inference |
| hf_bert-base-uncased-finetuned-swag | PASS | compiled_inference |
| hf_bert_base_swag_model | PASS | compiled_inference |
| hf_bert_multiple_choice | PASS | compiled_inference |
| hf_bert_science_multiple_choice | PASS | compiled_inference |
| hf_chinese_paragraph_bert-ext | PASS | compiled_inference |
| hf_distilbert_distilbert-base-uncased-15-epoch | PASS | compiled_inference |
| hf_distilbert_multiple_choice | PASS | compiled_inference |
| hf_distilbert_science_multiple_choice | PASS | compiled_inference |
| hf_e_care_albert_base_finetuned | PASS | compiled_inference |
| hf_e_care_bert_base_uncased_finetuned | PASS | compiled_inference |
| hf_electra-base-fp16 | PASS | compiled_inference |
| hf_electra-base-multiple-choice-v2 | PASS | compiled_inference |
| hf_electra_multiple_choice | PASS | compiled_inference |
| hf_finetuned-bert-piqa | PASS | compiled_inference |
| hf_kda-albert-xxlarge-v2-race | PASS | compiled_inference |
| hf_mbert-base-parsinlu-multiple-choice | PASS | compiled_inference |
| hf_mcQA_model_bert | PASS | compiled_inference |
| hf_my_awesome_swag_model | PASS | compiled_inference |
| hf_parsbert-base-parsinlu-multiple-choice | PASS | compiled_inference |
| hf_wikibert-base-parsinlu-multiple-choice | PASS | compiled_inference |

**Total regressed models: 35**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-03-31/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-04-01/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 398 | 397 | -1 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 382 | 381 | -1 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 90 | 90 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3 | 4 | +1 | ⚠️ MORE FAILURES |
| Inference Comparison | 16 | 16 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -1 fewer tests passing
- **Inference Comparison (PASS)**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_kda-albert-xxlarge-v2-race | PASS | compiled_inference |

**Total regressed models: 1**


---

