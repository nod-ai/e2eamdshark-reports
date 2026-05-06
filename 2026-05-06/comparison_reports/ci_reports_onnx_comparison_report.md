---
# Test Comparison Report

*Generated on: 2026-05-06*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-06/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-06/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4102 | 4103 | +1 |
| IREE Compilation | 3772 | 3931 | +159 |
| Gold Inference | 3771 | 3930 | +159 |
| IREE Inference Invocation | 3391 | 3903 | +512 |
| Inference Comparison (PASS) | 3193 | 3636 | +443 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 5 | 4 | -1 |
| IREE Compilation | 330 | 172 | -158 |
| Gold Inference | 1 | 1 | 0 |
| IREE Inference Invocation | 380 | 27 | -353 |
| Inference Comparison | 198 | 267 | +69 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-04/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-06/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4096 | 4102 | +6 | ✅ IMPROVED |
| IREE Compilation | 3777 | 3772 | -5 | ⚠️ REGRESSION |
| Gold Inference | 3777 | 3771 | -6 | ⚠️ REGRESSION |
| IREE Inference Invocation | 2773 | 3391 | +618 | ✅ IMPROVED |
| Inference Comparison (PASS) | 2635 | 3193 | +558 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 11 | 5 | -6 | ✅ FEWER FAILURES |
| IREE Compilation | 319 | 330 | +11 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 1 | +1 | ⚠️ MORE FAILURES |
| IREE Inference Invocation | 1004 | 380 | -624 | ✅ FEWER FAILURES |
| Inference Comparison | 138 | 198 | +60 | ⚠️ MORE FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -5 fewer tests passing
- **Gold Inference**: -6 fewer tests passing

### ✅ Improvements

- **Setup**: +6 more tests passing
- **IREE Inference Invocation**: +618 more tests passing
- **Inference Comparison (PASS)**: +558 more tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| dpn68_Opset17_timm | PASS | compilation |
| dpn68b_Opset16_timm | PASS | compilation |
| dpn68_Opset16 | PASS | compilation |
| dpn68_Opset17 | PASS | compilation |
| dpn68_Opset18 | PASS | compilation |
| dpn68b_Opset16 | PASS | compilation |
| dpn68b_Opset17 | PASS | compilation |
| dpn68b_Opset18 | PASS | compilation |
| xcit_large_24_p8_224_Opset17 | PASS | setup |
| migraphx_cadene__dpn92i1 | PASS | compilation |
| migraphx_torchvision__densenet121i32 | PASS | compilation |
| t5-decoder-with-lm-head-12 | PASS | native_inference |

**Total regressed models: 12**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| efficientnet_b1.ft_in1k_vaiq | compiled_inference | PASS |
| efficientnet_el_pruned.in1k_vaiq | compiled_inference | PASS |
| efficientnet_em.ra2_in1k_vaiq | compiled_inference | PASS |
| efficientnet_es_pruned.in1k_vaiq | compiled_inference | PASS |
| efficientnet_lite0.ra_in1k_vaiq | compiled_inference | PASS |
| efficientnetv2_rw_s.ra2_in1k_vaiq | compiled_inference | PASS |
| efficientnetv2_rw_t.ra2_in1k_vaiq | compiled_inference | PASS |
| fbnetc_100.rmsp_in1k_vaiq | compiled_inference | PASS |
| legacy_seresnet101_vaiq | compiled_inference | PASS |
| legacy_seresnet152_vaiq | compiled_inference | PASS |
| legacy_seresnet18_vaiq | compiled_inference | PASS |
| legacy_seresnet34_vaiq | compiled_inference | PASS |
| legacy_seresnet50_vaiq | compiled_inference | PASS |
| legacy_seresnext101_32x4d_vaiq | compiled_inference | PASS |
| legacy_seresnext26_32x4d_vaiq | compiled_inference | PASS |
| legacy_seresnext50_32x4d_vaiq | compiled_inference | PASS |
| mixnet_l.ft_in1k_vaiq | compiled_inference | PASS |
| mixnet_m.ft_in1k_vaiq | compiled_inference | PASS |
| mixnet_s.ft_in1k_vaiq | compiled_inference | PASS |
| mixnet_xl.ra_in1k_vaiq | compiled_inference | PASS |
| mnasnet_100.rmsp_in1k_vaiq | compiled_inference | PASS |
| mnasnet_small.lamb_in1k_vaiq | compiled_inference | PASS |
| mobilenetv2_050.lamb_in1k_vaiq | compiled_inference | PASS |
| mobilenetv2_100.ra_in1k_vaiq | compiled_inference | PASS |
| mobilenetv2_110d.ra_in1k_vaiq | compiled_inference | PASS |
| mobilenetv2_120d.ra_in1k_vaiq | compiled_inference | PASS |
| mobilenetv2_140.ra_in1k_vaiq | compiled_inference | PASS |
| mobilenetv3_large_100.ra_in1k_vaiq | compiled_inference | PASS |
| mobilenetv3_rw.rmsp_in1k_vaiq | compiled_inference | PASS |
| nf_regnet_b1.ra2_in1k_train_vaiq | compiled_inference | PASS |
| nfnet_l0.ra2_in1k_train_vaiq | compiled_inference | PASS |
| nfnet_l0.ra2_in1k_vaiq | compiled_inference | PASS |
| regnetv_040.ra3_in1k_train_vaiq | compiled_inference | PASS |
| regnetv_040.ra3_in1k_vaiq | compiled_inference | PASS |
| regnetv_064.ra3_in1k_train_vaiq | compiled_inference | PASS |
| regnetv_064.ra3_in1k_vaiq | compiled_inference | PASS |
| regnetx_004.pycls_in1k_vaiq | compiled_inference | PASS |
| regnetx_004_tv.tv2_in1k_vaiq | compiled_inference | PASS |
| regnetx_008.pycls_in1k_vaiq | compiled_inference | PASS |
| regnetx_032.pycls_in1k_vaiq | compiled_inference | PASS |
| regnetx_040.pycls_in1k_vaiq | compiled_inference | PASS |
| regnetx_064.pycls_in1k_vaiq | compiled_inference | PASS |
| regnetx_080.pycls_in1k_vaiq | compiled_inference | PASS |
| regnetx_320.pycls_in1k_vaiq | compiled_inference | PASS |
| regnety_006.pycls_in1k_vaiq | compiled_inference | PASS |
| regnety_008.pycls_in1k_vaiq | compiled_inference | PASS |
| regnety_008_tv.tv2_in1k_vaiq | compiled_inference | PASS |
| regnety_040.pycls_in1k_vaiq | compiled_inference | PASS |
| regnety_040.ra3_in1k_train_vaiq | compiled_inference | PASS |
| regnety_040.ra3_in1k_vaiq | compiled_inference | PASS |

*... and 520 more improved models*

**Total improved models: 570**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-04/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-06/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3960 | 3931 | -29 | ⚠️ REGRESSION |
| Gold Inference | 3959 | 3930 | -29 | ⚠️ REGRESSION |
| IREE Inference Invocation | 3935 | 3903 | -32 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3667 | 3636 | -31 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 143 | 172 | +29 | ⚠️ MORE FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 24 | 27 | +3 | ⚠️ MORE FAILURES |
| Inference Comparison | 268 | 267 | -1 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -29 fewer tests passing
- **Gold Inference**: -29 fewer tests passing
- **IREE Inference Invocation**: -32 fewer tests passing
- **Inference Comparison (PASS)**: -31 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| beit_large_patch16_384_Opset16_timm | PASS | compiled_inference |
| beit_large_patch16_384_Opset17_timm | PASS | compiled_inference |
| dpn107_Opset16_timm | PASS | compilation |
| dpn107_Opset18_timm | PASS | compilation |
| dpn131_Opset18_timm | PASS | compilation |
| dpn68_Opset17_timm | PASS | compilation |
| dpn68b_Opset16_timm | PASS | compilation |
| dpn92_Opset17_timm | PASS | compilation |
| dpn98_Opset17_timm | PASS | compilation |
| vit_large_patch16_384_Opset17_timm | PASS | compiled_inference |
| dpn107_Opset16 | PASS | compilation |
| dpn107_Opset17 | PASS | compilation |
| dpn107_Opset18 | PASS | compilation |
| dpn131_Opset16 | PASS | compilation |
| dpn131_Opset17 | PASS | compilation |
| dpn131_Opset18 | PASS | compilation |
| dpn68_Opset16 | PASS | compilation |
| dpn68_Opset17 | PASS | compilation |
| dpn68_Opset18 | PASS | compilation |
| dpn68b_Opset16 | PASS | compilation |
| dpn68b_Opset17 | PASS | compilation |
| dpn68b_Opset18 | PASS | compilation |
| dpn92_Opset16 | PASS | compilation |
| dpn92_Opset17 | PASS | compilation |
| dpn92_Opset18 | PASS | compilation |
| dpn98_Opset16 | PASS | compilation |
| dpn98_Opset17 | PASS | compilation |
| dpn98_Opset18 | PASS | compilation |
| migraphx_cadene__dpn92i1 | PASS | compilation |
| migraphx_cadene__inceptionv4i16 | PASS | compilation |
| migraphx_torchvision__densenet121i32 | PASS | compilation |

**Total regressed models: 31**


---

