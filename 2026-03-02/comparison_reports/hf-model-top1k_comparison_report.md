---
# Test Comparison Report

*Generated on: 2026-03-02*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-03-02/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-03-02/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 383 | 398 | +15 |
| Inference Comparison (PASS) | 364 | 367 | +3 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 13 | 14 | +1 |
| IREE Compilation | 106 | 90 | -16 |
| Gold Inference | 2 | 2 | 0 |
| IREE Inference Invocation | 3 | 3 | 0 |
| Inference Comparison | 19 | 31 | +12 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-27/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-03-02/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 494 | 494 | 0 | ➖ NO CHANGE |
| IREE Compilation | 398 | 388 | -10 | ⚠️ REGRESSION |
| Gold Inference | 396 | 386 | -10 | ⚠️ REGRESSION |
| IREE Inference Invocation | 394 | 383 | -11 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 380 | 364 | -16 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 13 | 13 | 0 | ➖ NO CHANGE |
| IREE Compilation | 96 | 106 | +10 | ⚠️ MORE FAILURES |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 2 | 3 | +1 | ⚠️ MORE FAILURES |
| Inference Comparison | 14 | 19 | +5 | ⚠️ MORE FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -10 fewer tests passing
- **Gold Inference**: -10 fewer tests passing
- **IREE Inference Invocation**: -11 fewer tests passing
- **Inference Comparison (PASS)**: -16 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_GIST-Embedding-v0 | PASS | compilation |
| hf_GIST-large-Embedding-v0 | PASS | compilation |
| hf_GIST-small-Embedding-v0 | PASS | compilation |
| hf_bge-base-en-v1.5 | PASS | compilation |
| hf_bge-large-en | PASS | compilation |
| hf_bge-large-en-v1.5 | PASS | compilation |
| hf_bge-large-zh-v1.5 | PASS | compilation |
| hf_bge-small-en | PASS | compilation |
| hf_bge-small-en-v1.5 | PASS | compilation |
| hf_llm-embedder | PASS | compilation |
| hf_snowflake-arctic-embed-m | PASS | compilation |
| hf_resnet-50 | PASS | Numerics |
| hf_resnet101.a1h_in1k | PASS | Numerics |
| hf_resnet50.a1_in1k | PASS | Numerics |
| hf_resnext50_32x4d.fb_swsl_ig1b_ft_in1k | PASS | Numerics |
| hf_wide_resnet50_2.racm_in1k | PASS | Numerics |

**Total regressed models: 16**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-27/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-03-02/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 397 | 398 | +1 | ✅ IMPROVED |
| Inference Comparison (PASS) | 366 | 367 | +1 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 90 | 90 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 4 | 3 | -1 | ✅ FEWER FAILURES |
| Inference Comparison | 31 | 31 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Inference Invocation**: +1 more tests passing
- **Inference Comparison (PASS)**: +1 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_kda-albert-xxlarge-v2-race | compiled_inference | PASS |

**Total improved models: 1**


---

