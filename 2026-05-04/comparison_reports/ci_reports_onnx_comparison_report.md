---
# Test Comparison Report

*Generated on: 2026-05-04*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-04/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-04/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4096 | 4103 | +7 |
| IREE Compilation | 3777 | 3960 | +183 |
| Gold Inference | 3777 | 3959 | +182 |
| IREE Inference Invocation | 2773 | 3935 | +1162 |
| Inference Comparison (PASS) | 2635 | 3667 | +1032 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 11 | 4 | -7 |
| IREE Compilation | 319 | 143 | -176 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 1004 | 24 | -980 |
| Inference Comparison | 138 | 268 | +130 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-03-20/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-04/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4096 | -7 | ⚠️ REGRESSION |
| IREE Compilation | 3552 | 3777 | +225 | ✅ IMPROVED |
| Gold Inference | 3551 | 3777 | +226 | ✅ IMPROVED |
| IREE Inference Invocation | 3020 | 2773 | -247 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 2910 | 2635 | -275 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 11 | +7 | ⚠️ MORE FAILURES |
| IREE Compilation | 551 | 319 | -232 | ✅ FEWER FAILURES |
| Gold Inference | 1 | 0 | -1 | ✅ FEWER FAILURES |
| IREE Inference Invocation | 531 | 1004 | +473 | ⚠️ MORE FAILURES |
| Inference Comparison | 110 | 138 | +28 | ⚠️ MORE FAILURES |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -7 fewer tests passing
- **IREE Inference Invocation**: -247 fewer tests passing
- **Inference Comparison (PASS)**: -275 fewer tests passing

### ✅ Improvements

- **IREE Compilation**: +225 more tests passing
- **Gold Inference**: +226 more tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| dla60_res2next_vaiq | PASS | compilation |
| dpn107_vaiq | PASS | compilation |
| dpn131_vaiq | PASS | compilation |
| dpn92_vaiq | PASS | compilation |
| efficientnet_el_pruned.in1k_vaiq | PASS | compiled_inference |
| efficientnet_em.ra2_in1k_vaiq | PASS | compiled_inference |
| efficientnet_es_pruned.in1k_vaiq | PASS | compiled_inference |
| efficientnet_lite0.ra_in1k_vaiq | PASS | compiled_inference |
| efficientnetv2_rw_s.ra2_in1k_vaiq | PASS | compiled_inference |
| efficientnetv2_rw_t.ra2_in1k_vaiq | PASS | compiled_inference |
| fbnetc_100.rmsp_in1k_vaiq | PASS | compiled_inference |
| gluon_senet154_vaiq | PASS | compilation |
| hrnet_w40_vaiq | PASS | compilation |
| mnasnet_100.rmsp_in1k_vaiq | PASS | compiled_inference |
| mnasnet_small.lamb_in1k_vaiq | PASS | compiled_inference |
| mobilenetv2_050.lamb_in1k_vaiq | PASS | compiled_inference |
| mobilenetv2_100.ra_in1k_vaiq | PASS | compiled_inference |
| mobilenetv2_110d.ra_in1k_vaiq | PASS | compiled_inference |
| mobilenetv2_120d.ra_in1k_vaiq | PASS | compiled_inference |
| mobilenetv2_140.ra_in1k_vaiq | PASS | compiled_inference |
| mobilenetv3_large_100.ra_in1k_vaiq | PASS | compiled_inference |
| maxvit_base_tf_224.in1k | PASS | compilation |
| maxvit_large_tf_224.in1k | PASS | compilation |
| maxvit_small_tf_224.in1k | PASS | compilation |
| maxvit_tiny_tf_224.in1k | PASS | compilation |
| maxvit_tiny_tf_384.in1k | PASS | compilation |
| maxxvit_rmlp_nano_rw_256.sw_in1k | PASS | compilation |
| maxxvit_rmlp_small_rw_256.sw_in1k | PASS | compilation |
| maxxvitv2_nano_rw_256.sw_in1k | PASS | compilation |
| maxxvitv2_rmlp_base_rw_224.sw_in12k | PASS | compilation |
| maxxvitv2_rmlp_base_rw_224.sw_in12k_ft_in1k | PASS | compilation |
| tf_efficientnet_b0.aa_in1k | PASS | compiled_inference |
| tf_efficientnet_b1.aa_in1k | PASS | compiled_inference |
| tf_efficientnet_b2.aa_in1k | PASS | compiled_inference |
| tf_efficientnet_b3.aa_in1k | PASS | compiled_inference |
| tf_efficientnet_b4.aa_in1k | PASS | compiled_inference |
| tf_efficientnet_b5.ap_in1k | PASS | compiled_inference |
| tf_efficientnet_b6.aa_in1k | PASS | compiled_inference |
| tf_efficientnet_b7.ap_in1k | PASS | compiled_inference |
| tf_efficientnet_b8.ap_in1k | PASS | compilation |
| tf_efficientnet_l2.ns_jft_in1k | PASS | compiled_inference |
| tf_efficientnetv2_l.in1k | PASS | compiled_inference |
| tf_efficientnetv2_m.in1k | PASS | compiled_inference |
| tf_efficientnetv2_s.in1k | PASS | compiled_inference |
| tf_efficientnetv2_xl.in21k_ft_in1k | PASS | compiled_inference |
| tf_mixnet_l.in1k | PASS | compiled_inference |
| tf_mixnet_m.in1k | PASS | compiled_inference |
| tf_mixnet_s.in1k | PASS | compiled_inference |
| tf_mobilenetv3_large_075.in1k | PASS | compiled_inference |
| tf_mobilenetv3_large_100.in1k | PASS | compiled_inference |

*... and 518 more regressed models*

**Total regressed models: 568**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| cs3se_edgenet_x_train_vaiq | compilation | PASS |
| cs3se_edgenet_x_vaiq | compilation | PASS |
| cs3sedarknet_l_train_vaiq | compilation | PASS |
| cs3sedarknet_x_train_vaiq | compilation | PASS |
| dm_nfnet_f0.dm_in1k_train_vaiq | compilation | PASS |
| dm_nfnet_f0.dm_in1k_vaiq | compilation | PASS |
| dm_nfnet_f1.dm_in1k_train_vaiq | compilation | PASS |
| dm_nfnet_f1.dm_in1k_vaiq | compilation | PASS |
| dpn68b_test_vaiq | Numerics | PASS |
| dpn68b_vaiq | Numerics | PASS |
| eca_nfnet_l0.ra2_in1k_train_vaiq | compilation | PASS |
| eca_nfnet_l1.ra2_in1k_train_vaiq | compilation | PASS |
| eca_nfnet_l2.ra3_in1k_train_vaiq | compilation | PASS |
| eca_resnext26ts.ch_in1k_train_vaiq | compilation | PASS |
| eca_resnext26ts.ch_in1k_vaiq | compilation | PASS |
| ecaresnet26t_train_vaiq | compilation | PASS |
| ecaresnet26t_vaiq | compilation | PASS |
| ecaresnet50t_train_vaiq | compilation | PASS |
| ecaresnet50t_vaiq | compilation | PASS |
| efficientnet_b1.ft_in1k_train_vaiq | compilation | PASS |
| efficientnet_b4.ra2_in1k_train_vaiq | compilation | PASS |
| gluon_resnet101_v1c_vaiq | compilation | PASS |
| gluon_resnet101_v1s_vaiq | compilation | PASS |
| gluon_resnet152_v1c_vaiq | compilation | PASS |
| gluon_resnet152_v1s_vaiq | compilation | PASS |
| gluon_resnet18_v1b_vaiq | compilation | PASS |
| gluon_resnet50_v1c_vaiq | compilation | PASS |
| gluon_resnet50_v1s_vaiq | compilation | PASS |
| gluon_resnext101_32x4d_vaiq | compilation | PASS |
| gluon_resnext101_64x4d_vaiq | compilation | PASS |
| gluon_seresnext101_32x4d_vaiq | compilation | PASS |
| gluon_seresnext101_64x4d_vaiq | compilation | PASS |
| gluon_seresnext50_32x4d_vaiq | compilation | PASS |
| ig_resnext101_32x16d_vaiq | compilation | PASS |
| resnet26_test_vaiq | compilation | PASS |
| resnet26_vaiq | compilation | PASS |
| resnet34_test_vaiq | compilation | PASS |
| resnet50_test_vaiq | compilation | PASS |
| resnetaa50_train_vaiq | compilation | PASS |
| resnetaa50_vaiq | compilation | PASS |
| resnetblur50_test_vaiq | compilation | PASS |
| resnetblur50_vaiq | compilation | PASS |
| resnetrs101_train_vaiq | compilation | PASS |
| resnetrs152_train_vaiq | compilation | PASS |
| resnetrs152_vaiq | compilation | PASS |
| resnetrs200_train_vaiq | compilation | PASS |
| resnetrs200_vaiq | compilation | PASS |
| resnetv2_50d_evos.ah_in1k_train_vaiq | compilation | PASS |
| resnetv2_50d_evos.ah_in1k_vaiq | compilation | PASS |
| resnetv2_50d_gn.ah_in1k_train_vaiq | compilation | PASS |

*... and 243 more improved models*

**Total improved models: 293**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-03-20/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-04/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3969 | 3960 | -9 | ⚠️ REGRESSION |
| Gold Inference | 3968 | 3959 | -9 | ⚠️ REGRESSION |
| IREE Inference Invocation | 3944 | 3935 | -9 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3658 | 3667 | +9 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 134 | 143 | +9 | ⚠️ MORE FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 24 | 24 | 0 | ➖ NO CHANGE |
| Inference Comparison | 286 | 268 | -18 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -9 fewer tests passing
- **Gold Inference**: -9 fewer tests passing
- **IREE Inference Invocation**: -9 fewer tests passing

### ✅ Improvements

- **Inference Comparison (PASS)**: +9 more tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| efficientformerv2_l.snap_dist_in1k | PASS | compilation |
| efficientformerv2_s0.snap_dist_in1k | PASS | compilation |
| efficientformerv2_s1.snap_dist_in1k | PASS | compilation |
| efficientformerv2_s2.snap_dist_in1k | PASS | compilation |
| model--roberta_shared_bbc_xsum--patrickvonplaten | PASS | Numerics |
| squeezebert_Opset16 | PASS | compilation |
| squeezebert_Opset17 | PASS | compilation |
| squeezebert_Opset18 | PASS | compilation |
| squeezebert_Opset16_transformers | PASS | compilation |
| squeezebert_Opset18_transformers | PASS | compilation |

**Total regressed models: 10**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| regnetz_c16_evos_Opset16_timm | Numerics | PASS |
| regnetz_d8_evos_Opset16_timm | Numerics | PASS |
| resnetv2_50d_evos_Opset17_timm | Numerics | PASS |
| flaubert_Opset16 | Numerics | PASS |
| flaubert_Opset17 | Numerics | PASS |
| flaubert_Opset18 | Numerics | PASS |
| regnetz_c16_evos_Opset16 | Numerics | PASS |
| regnetz_c16_evos_Opset17 | Numerics | PASS |
| regnetz_d8_evos_Opset16 | Numerics | PASS |
| regnetz_d8_evos_Opset17 | Numerics | PASS |
| resnetv2_50d_evos_Opset16 | Numerics | PASS |
| resnetv2_50d_evos_Opset17 | Numerics | PASS |
| umt5_Opset16 | Numerics | PASS |
| umt5_Opset17 | Numerics | PASS |
| xlmroberta_Opset16 | Numerics | PASS |
| flaubert_Opset16_transformers | Numerics | PASS |
| flaubert_Opset17_transformers | Numerics | PASS |
| umt5_Opset16_transformers | Numerics | PASS |
| xlmroberta_Opset16_transformers | Numerics | PASS |

**Total improved models: 19**


---

