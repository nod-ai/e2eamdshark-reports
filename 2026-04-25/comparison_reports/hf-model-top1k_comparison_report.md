---
# Test Comparison Report

*Generated on: 2026-04-25*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-04-25/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-04-25/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 493 | 492 | -1 |
| IREE Compilation | 434 | 420 | -14 |
| Gold Inference | 418 | 404 | -14 |
| IREE Inference Invocation | 400 | 399 | -1 |
| Inference Comparison (PASS) | 398 | 397 | -1 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 15 | +1 |
| IREE Compilation | 59 | 72 | +13 |
| Gold Inference | 16 | 16 | 0 |
| IREE Inference Invocation | 18 | 5 | -13 |
| Inference Comparison | 2 | 2 | 0 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-04-24/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-04-25/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 434 | 434 | 0 | ➖ NO CHANGE |
| Gold Inference | 431 | 418 | -13 | ⚠️ REGRESSION |
| IREE Inference Invocation | 428 | 400 | -28 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 412 | 398 | -14 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 59 | 59 | 0 | ➖ NO CHANGE |
| Gold Inference | 3 | 16 | +13 | ⚠️ MORE FAILURES |
| IREE Inference Invocation | 3 | 18 | +15 | ⚠️ MORE FAILURES |
| Inference Comparison | 16 | 2 | -14 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **Gold Inference**: -13 fewer tests passing
- **IREE Inference Invocation**: -28 fewer tests passing
- **Inference Comparison (PASS)**: -14 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_codebert-base | PASS | construct_inputs |
| hf_sup-simcse-roberta-large | PASS | construct_inputs |
| hf_codebert-base-mlm | PASS | construct_inputs |
| hf_yolos-tiny | PASS | compiled_inference |
| hf_roberta-base-squad2 | PASS | construct_inputs |
| hf_roberta-large-squad2 | PASS | construct_inputs |
| hf_query_wellformedness_score | PASS | construct_inputs |
| hf_roberta-hate-speech-dynabench-r4-target | PASS | construct_inputs |
| hf_twitter-roberta-base-irony | PASS | construct_inputs |
| hf_twitter-roberta-base-sentiment | PASS | construct_inputs |
| hf_twitter-roberta-base-sentiment-latest | PASS | construct_inputs |
| hf_unbiased-toxic-roberta | PASS | construct_inputs |
| hf_deid_roberta_i2b2 | PASS | construct_inputs |
| hf_roberta-large-ner-english | PASS | construct_inputs |

**Total regressed models: 14**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-04-24/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-04-25/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 492 | 492 | 0 | ➖ NO CHANGE |
| IREE Compilation | 420 | 420 | 0 | ➖ NO CHANGE |
| Gold Inference | 417 | 404 | -13 | ⚠️ REGRESSION |
| IREE Inference Invocation | 412 | 399 | -13 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 410 | 397 | -13 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 15 | 0 | ➖ NO CHANGE |
| IREE Compilation | 72 | 72 | 0 | ➖ NO CHANGE |
| Gold Inference | 3 | 16 | +13 | ⚠️ MORE FAILURES |
| IREE Inference Invocation | 5 | 5 | 0 | ➖ NO CHANGE |
| Inference Comparison | 2 | 2 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **Gold Inference**: -13 fewer tests passing
- **IREE Inference Invocation**: -13 fewer tests passing
- **Inference Comparison (PASS)**: -13 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_codebert-base | PASS | construct_inputs |
| hf_sup-simcse-roberta-large | PASS | construct_inputs |
| hf_codebert-base-mlm | PASS | construct_inputs |
| hf_roberta-base-squad2 | PASS | construct_inputs |
| hf_roberta-large-squad2 | PASS | construct_inputs |
| hf_query_wellformedness_score | PASS | construct_inputs |
| hf_roberta-hate-speech-dynabench-r4-target | PASS | construct_inputs |
| hf_twitter-roberta-base-irony | PASS | construct_inputs |
| hf_twitter-roberta-base-sentiment | PASS | construct_inputs |
| hf_twitter-roberta-base-sentiment-latest | PASS | construct_inputs |
| hf_unbiased-toxic-roberta | PASS | construct_inputs |
| hf_deid_roberta_i2b2 | PASS | construct_inputs |
| hf_roberta-large-ner-english | PASS | construct_inputs |

**Total regressed models: 13**


---

