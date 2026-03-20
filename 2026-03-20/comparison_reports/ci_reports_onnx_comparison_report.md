---
# Test Comparison Report

*Generated on: 2026-03-20*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-03-20/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-03-20/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4103 | 4103 | 0 |
| IREE Compilation | 3552 | 3969 | +417 |
| Gold Inference | 3551 | 3968 | +417 |
| IREE Inference Invocation | 3020 | 3944 | +924 |
| Inference Comparison (PASS) | 2910 | 3658 | +748 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4 | 4 | 0 |
| IREE Compilation | 551 | 134 | -417 |
| Gold Inference | 1 | 1 | 0 |
| IREE Inference Invocation | 531 | 24 | -507 |
| Inference Comparison | 110 | 286 | +176 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-23/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-03-20/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3441 | 3552 | +111 | ✅ IMPROVED |
| Gold Inference | 3440 | 3551 | +111 | ✅ IMPROVED |
| IREE Inference Invocation | 3326 | 3020 | -306 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3193 | 2910 | -283 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 662 | 551 | -111 | ✅ FEWER FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 114 | 531 | +417 | ⚠️ MORE FAILURES |
| Inference Comparison | 133 | 110 | -23 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -306 fewer tests passing
- **Inference Comparison (PASS)**: -283 fewer tests passing

### ✅ Improvements

- **IREE Compilation**: +111 more tests passing
- **Gold Inference**: +111 more tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| eca_resnet33ts.ra2_in1k_vaiq | PASS | compilation |
| eca_resnext26ts.ch_in1k_vaiq | PASS | compilation |
| gernet_l.idstcv_in1k_vaiq | PASS | compilation |
| gernet_m.idstcv_in1k_vaiq | PASS | compilation |
| gernet_s.idstcv_in1k_vaiq | PASS | compilation |
| gluon_resnet101_v1c_vaiq | PASS | compilation |
| gluon_resnet101_v1s_vaiq | PASS | compilation |
| gluon_resnet152_v1c_vaiq | PASS | compilation |
| gluon_resnet152_v1s_vaiq | PASS | compilation |
| gluon_resnet18_v1b_vaiq | PASS | compilation |
| gluon_resnet50_v1c_vaiq | PASS | compilation |
| gluon_resnet50_v1s_vaiq | PASS | compilation |
| gluon_resnext101_32x4d_vaiq | PASS | compilation |
| gluon_resnext101_64x4d_vaiq | PASS | compilation |
| gluon_seresnext101_32x4d_vaiq | PASS | compilation |
| gluon_seresnext101_64x4d_vaiq | PASS | compilation |
| gluon_seresnext50_32x4d_vaiq | PASS | compilation |
| ig_resnext101_32x16d_vaiq | PASS | compilation |
| legacy_senet154_vaiq | PASS | compiled_inference |
| legacy_seresnet101_vaiq | PASS | compilation |
| legacy_seresnet152_vaiq | PASS | compilation |
| legacy_seresnet18_vaiq | PASS | compilation |
| legacy_seresnet34_vaiq | PASS | compilation |
| legacy_seresnet50_vaiq | PASS | compilation |
| legacy_seresnext101_32x4d_vaiq | PASS | compilation |
| legacy_seresnext26_32x4d_vaiq | PASS | compilation |
| legacy_seresnext50_32x4d_vaiq | PASS | compilation |
| mixnet_l.ft_in1k_vaiq | PASS | compiled_inference |
| mixnet_m.ft_in1k_vaiq | PASS | compiled_inference |
| mixnet_s.ft_in1k_vaiq | PASS | compiled_inference |
| mixnet_xl.ra_in1k_vaiq | PASS | compiled_inference |
| mobilenetv3_rw.rmsp_in1k_vaiq | PASS | compiled_inference |
| nf_regnet_b1.ra2_in1k_vaiq | PASS | compiled_inference |
| nfnet_l0.ra2_in1k_vaiq | PASS | compiled_inference |
| regnetv_040.ra3_in1k_train_vaiq | PASS | compilation |
| regnetv_040.ra3_in1k_vaiq | PASS | compilation |
| regnetv_064.ra3_in1k_train_vaiq | PASS | compiled_inference |
| regnetv_064.ra3_in1k_vaiq | PASS | compiled_inference |
| regnetx_002.pycls_in1k_vaiq | PASS | compiled_inference |
| regnetx_004.pycls_in1k_vaiq | PASS | compiled_inference |
| regnetx_004_tv.tv2_in1k_vaiq | PASS | compiled_inference |
| regnetx_006.pycls_in1k_vaiq | PASS | compiled_inference |
| regnetx_008.pycls_in1k_vaiq | PASS | compiled_inference |
| regnetx_016.pycls_in1k_vaiq | PASS | compiled_inference |
| regnetx_032.pycls_in1k_vaiq | PASS | compilation |
| regnetx_064.pycls_in1k_vaiq | PASS | compiled_inference |
| regnetx_120.pycls_in1k_vaiq | PASS | compilation |
| regnety_002.pycls_in1k_vaiq | PASS | compiled_inference |
| regnety_004.pycls_in1k_vaiq | PASS | compiled_inference |
| regnety_006.pycls_in1k_vaiq | PASS | compilation |

*... and 433 more regressed models*

**Total regressed models: 483**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| cait_m36_384 | compilation | PASS |
| cait_s24_384 | compilation | PASS |
| cait_s36_384 | compilation | PASS |
| cait_xxs24_384 | compilation | PASS |
| cait_xxs36_384 | compilation | PASS |
| davit_base.msft_in1k | compilation | PASS |
| davit_small.msft_in1k | compilation | PASS |
| davit_tiny.msft_in1k | compilation | PASS |
| gcvit_base | compilation | PASS |
| gcvit_small | compilation | PASS |
| gcvit_tiny | compilation | PASS |
| gcvit_xtiny | compilation | PASS |
| gcvit_xxtiny | compilation | PASS |
| maxvit_base_tf_224.in1k | compilation | PASS |
| maxvit_large_tf_224.in1k | compilation | PASS |
| maxvit_small_tf_224.in1k | compilation | PASS |
| maxvit_tiny_tf_224.in1k | compilation | PASS |
| maxvit_tiny_tf_384.in1k | compilation | PASS |
| maxvit_tiny_tf_512.in1k | compilation | PASS |
| maxxvitv2_rmlp_base_rw_224.sw_in12k | compilation | PASS |
| maxxvitv2_rmlp_base_rw_224.sw_in12k_ft_in1k | compilation | PASS |
| maxxvitv2_rmlp_base_rw_384.sw_in12k_ft_in1k | compilation | PASS |
| mobilevit_s | compilation | PASS |
| mobilevit_xxs | compilation | PASS |
| swinv2_base_window12to16_192to256.ms_in22k_ft_in1k | compilation | PASS |
| swinv2_base_window12to24_192to384.ms_in22k_ft_in1k | compilation | PASS |
| swinv2_base_window8_256.ms_in1k | compilation | PASS |
| twins_svt_base | compilation | PASS |
| twins_svt_large | compilation | PASS |
| twins_svt_small | compilation | PASS |
| xcit_large_24_p16_224 | compilation | PASS |
| xcit_large_24_p16_384_dist | compilation | PASS |
| xcit_large_24_p8_224 | compilation | PASS |
| xcit_medium_24_p16_224 | compilation | PASS |
| xcit_nano_12_p16_224 | compilation | PASS |
| xcit_nano_12_p16_384_dist | compilation | PASS |
| xcit_nano_12_p8_224 | compilation | PASS |
| xcit_nano_12_p8_384_dist | compilation | PASS |
| xcit_small_12_p16_224 | compilation | PASS |
| xcit_small_12_p16_384_dist | compilation | PASS |
| xcit_small_12_p8_224 | compilation | PASS |
| xcit_small_24_p16_224 | compilation | PASS |
| xcit_small_24_p16_384_dist | compilation | PASS |
| xcit_small_24_p8_224 | compilation | PASS |
| xcit_tiny_12_p16_224 | compilation | PASS |
| xcit_tiny_12_p16_384_dist | compilation | PASS |
| xcit_tiny_12_p8_224 | compilation | PASS |
| xcit_tiny_24_p16_224 | compilation | PASS |
| xcit_tiny_24_p16_384_dist | compilation | PASS |
| xcit_tiny_24_p8_224 | compilation | PASS |

*... and 150 more improved models*

**Total improved models: 200**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-23/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-03-20/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3965 | 3969 | +4 | ✅ IMPROVED |
| Gold Inference | 3964 | 3968 | +4 | ✅ IMPROVED |
| IREE Inference Invocation | 3935 | 3944 | +9 | ✅ IMPROVED |
| Inference Comparison (PASS) | 3640 | 3658 | +18 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 138 | 134 | -4 | ✅ FEWER FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 29 | 24 | -5 | ✅ FEWER FAILURES |
| Inference Comparison | 295 | 286 | -9 | ✅ FEWER FAILURES |

## Summary

### ✅ Improvements

- **IREE Compilation**: +4 more tests passing
- **Gold Inference**: +4 more tests passing
- **IREE Inference Invocation**: +9 more tests passing
- **Inference Comparison (PASS)**: +18 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| beit_large_patch16_384.in22k_ft_in22k_in1k | compiled_inference | PASS |
| convnext_xlarge.fb_in22k_ft_in1k | compiled_inference | PASS |
| deit3_large_patch16_384.fb_in1k | compiled_inference | PASS |
| dm_nfnet_f4.dm_in1k | compiled_inference | PASS |
| model--s2t-medium-librispeech-asr--facebook | Numerics | PASS |
| beit_large_patch16_384_Opset16 | compiled_inference | PASS |
| beit_large_patch16_384_Opset17 | compiled_inference | PASS |
| convnext_xlarge_384_in22ft1k_Opset16 | compiled_inference | PASS |
| convnext_xlarge_384_in22ft1k_Opset17 | compiled_inference | PASS |
| dm_nfnet_f0_Opset16 | Numerics | PASS |
| dm_nfnet_f0_Opset17 | Numerics | PASS |
| dm_nfnet_f1_Opset16 | Numerics | PASS |
| dm_nfnet_f2_Opset16 | Numerics | PASS |
| dm_nfnet_f2_Opset17 | Numerics | PASS |
| fcn-resnet101-11 | Numerics | PASS |
| fcn-resnet50-11 | Numerics | PASS |
| fcn-resnet50-12 | Numerics | PASS |
| rain-princess-8 | Numerics | PASS |

**Total improved models: 18**


---

