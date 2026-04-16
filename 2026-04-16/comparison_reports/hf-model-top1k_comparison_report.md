---
# Test Comparison Report

*Generated on: 2026-04-16*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-04-16/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-04-16/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| Gold Inference | 431 | 417 | -14 |
| IREE Inference Invocation | 428 | 412 | -16 |
| Inference Comparison (PASS) | 412 | 410 | -2 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 15 | +1 |
| IREE Compilation | 59 | 72 | +13 |
| Gold Inference | 3 | 3 | 0 |
| IREE Inference Invocation | 3 | 5 | +2 |
| Inference Comparison | 16 | 2 | -14 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-04-15/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-04-16/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 404 | 434 | +30 | ✅ IMPROVED |
| Gold Inference | 401 | 431 | +30 | ✅ IMPROVED |
| IREE Inference Invocation | 398 | 428 | +30 | ✅ IMPROVED |
| Inference Comparison (PASS) | 382 | 412 | +30 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 89 | 59 | -30 | ✅ FEWER FAILURES |
| Gold Inference | 3 | 3 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3 | 3 | 0 | ➖ NO CHANGE |
| Inference Comparison | 16 | 16 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Compilation**: +30 more tests passing
- **Gold Inference**: +30 more tests passing
- **IREE Inference Invocation**: +30 more tests passing
- **Inference Comparison (PASS)**: +30 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_mit-b0 | compilation | PASS |
| hf_mit-b5 | compilation | PASS |
| hf_nfnet_l0.ra2_in1k | compilation | PASS |
| hf_face-parsing | compilation | PASS |
| hf_segformer-b0-finetuned-ade-512-512 | compilation | PASS |
| hf_segformer-b0-finetuned-cityscapes-1024-1024 | compilation | PASS |
| hf_segformer-b0-finetuned-cityscapes-512-1024 | compilation | PASS |
| hf_segformer-b1-finetuned-ade-512-512 | compilation | PASS |
| hf_segformer-b1-finetuned-cityscapes-1024-1024 | compilation | PASS |
| hf_segformer-b2-fashion | compilation | PASS |
| hf_segformer-b2-finetuned-ade-512-512 | compilation | PASS |
| hf_segformer-b2-finetuned-cityscapes-1024-1024 | compilation | PASS |
| hf_segformer-b3-fashion | compilation | PASS |
| hf_segformer-b3-finetuned-ade-512-512 | compilation | PASS |
| hf_segformer-b3-finetuned-cityscapes-1024-1024 | compilation | PASS |
| hf_segformer-b4-finetuned-ade-512-512 | compilation | PASS |
| hf_segformer-b4-finetuned-cityscapes-1024-1024 | compilation | PASS |
| hf_segformer-b5-finetuned-ade-640-640 | compilation | PASS |
| hf_segformer-b5-finetuned-cityscapes-1024-1024 | compilation | PASS |
| hf_segformer_b2_clothes | compilation | PASS |
| hf_segformer_b3_clothes | compilation | PASS |
| hf_segformer_for_optic_disc_cup_segmentation | compilation | PASS |
| hf_yolos-tiny | compilation | PASS |
| hf_segformer-b0-finetuned-segments-sidewalk-2 | compilation | PASS |
| hf_segformer-b4-finetuned-segments-sidewalk | compilation | PASS |
| hf_tcd-segformer-mit-b0 | compilation | PASS |
| hf_tcd-segformer-mit-b1 | compilation | PASS |
| hf_tcd-segformer-mit-b2 | compilation | PASS |
| hf_tcd-segformer-mit-b3 | compilation | PASS |
| hf_tcd-segformer-mit-b4 | compilation | PASS |

**Total improved models: 30**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-04-15/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-04-16/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 492 | 492 | 0 | ➖ NO CHANGE |
| IREE Compilation | 390 | 420 | +30 | ✅ IMPROVED |
| Gold Inference | 387 | 417 | +30 | ✅ IMPROVED |
| IREE Inference Invocation | 382 | 412 | +30 | ✅ IMPROVED |
| Inference Comparison (PASS) | 380 | 410 | +30 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 15 | 0 | ➖ NO CHANGE |
| IREE Compilation | 102 | 72 | -30 | ✅ FEWER FAILURES |
| Gold Inference | 3 | 3 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 5 | 0 | ➖ NO CHANGE |
| Inference Comparison | 2 | 2 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Compilation**: +30 more tests passing
- **Gold Inference**: +30 more tests passing
- **IREE Inference Invocation**: +30 more tests passing
- **Inference Comparison (PASS)**: +30 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_mit-b0 | compilation | PASS |
| hf_mit-b5 | compilation | PASS |
| hf_nfnet_l0.ra2_in1k | compilation | PASS |
| hf_face-parsing | compilation | PASS |
| hf_segformer-b0-finetuned-ade-512-512 | compilation | PASS |
| hf_segformer-b0-finetuned-cityscapes-1024-1024 | compilation | PASS |
| hf_segformer-b0-finetuned-cityscapes-512-1024 | compilation | PASS |
| hf_segformer-b1-finetuned-ade-512-512 | compilation | PASS |
| hf_segformer-b1-finetuned-cityscapes-1024-1024 | compilation | PASS |
| hf_segformer-b2-fashion | compilation | PASS |
| hf_segformer-b2-finetuned-ade-512-512 | compilation | PASS |
| hf_segformer-b2-finetuned-cityscapes-1024-1024 | compilation | PASS |
| hf_segformer-b3-fashion | compilation | PASS |
| hf_segformer-b3-finetuned-ade-512-512 | compilation | PASS |
| hf_segformer-b3-finetuned-cityscapes-1024-1024 | compilation | PASS |
| hf_segformer-b4-finetuned-ade-512-512 | compilation | PASS |
| hf_segformer-b4-finetuned-cityscapes-1024-1024 | compilation | PASS |
| hf_segformer-b5-finetuned-ade-640-640 | compilation | PASS |
| hf_segformer-b5-finetuned-cityscapes-1024-1024 | compilation | PASS |
| hf_segformer_b2_clothes | compilation | PASS |
| hf_segformer_b3_clothes | compilation | PASS |
| hf_segformer_for_optic_disc_cup_segmentation | compilation | PASS |
| hf_yolos-tiny | compilation | PASS |
| hf_segformer-b0-finetuned-segments-sidewalk-2 | compilation | PASS |
| hf_segformer-b4-finetuned-segments-sidewalk | compilation | PASS |
| hf_tcd-segformer-mit-b0 | compilation | PASS |
| hf_tcd-segformer-mit-b1 | compilation | PASS |
| hf_tcd-segformer-mit-b2 | compilation | PASS |
| hf_tcd-segformer-mit-b3 | compilation | PASS |
| hf_tcd-segformer-mit-b4 | compilation | PASS |

**Total improved models: 30**


---

