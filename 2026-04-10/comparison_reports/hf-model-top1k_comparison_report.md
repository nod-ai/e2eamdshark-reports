---
# Test Comparison Report

*Generated on: 2026-04-10*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-04-10/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-04-10/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 493 | 492 | -1 |
| IREE Compilation | 404 | 390 | -14 |
| Gold Inference | 401 | 387 | -14 |
| IREE Inference Invocation | 398 | 382 | -16 |
| Inference Comparison (PASS) | 382 | 380 | -2 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 15 | +1 |
| IREE Compilation | 89 | 102 | +13 |
| Gold Inference | 3 | 3 | 0 |
| IREE Inference Invocation | 3 | 5 | +2 |
| Inference Comparison | 16 | 2 | -14 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-04-09/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-04-10/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 494 | 493 | -1 | ⚠️ REGRESSION |
| IREE Compilation | 405 | 404 | -1 | ⚠️ REGRESSION |
| Gold Inference | 402 | 401 | -1 | ⚠️ REGRESSION |
| IREE Inference Invocation | 399 | 398 | -1 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 383 | 382 | -1 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 13 | 14 | +1 | ⚠️ MORE FAILURES |
| IREE Compilation | 89 | 89 | 0 | ➖ NO CHANGE |
| Gold Inference | 3 | 3 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3 | 3 | 0 | ➖ NO CHANGE |
| Inference Comparison | 16 | 16 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -1 fewer tests passing
- **IREE Compilation**: -1 fewer tests passing
- **Gold Inference**: -1 fewer tests passing
- **IREE Inference Invocation**: -1 fewer tests passing
- **Inference Comparison (PASS)**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_sentence-bert-base-ja-mean-tokens-v2 | PASS | setup |

**Total regressed models: 1**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-04-09/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-04-10/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 492 | -1 | ⚠️ REGRESSION |
| IREE Compilation | 407 | 390 | -17 | ⚠️ REGRESSION |
| Gold Inference | 404 | 387 | -17 | ⚠️ REGRESSION |
| IREE Inference Invocation | 399 | 382 | -17 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 381 | 380 | -1 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 15 | +1 | ⚠️ MORE FAILURES |
| IREE Compilation | 86 | 102 | +16 | ⚠️ MORE FAILURES |
| Gold Inference | 3 | 3 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 5 | 0 | ➖ NO CHANGE |
| Inference Comparison | 18 | 2 | -16 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -1 fewer tests passing
- **IREE Compilation**: -17 fewer tests passing
- **Gold Inference**: -17 fewer tests passing
- **IREE Inference Invocation**: -17 fewer tests passing
- **Inference Comparison (PASS)**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_sentence-bert-base-ja-mean-tokens-v2 | PASS | setup |

**Total regressed models: 1**


---

