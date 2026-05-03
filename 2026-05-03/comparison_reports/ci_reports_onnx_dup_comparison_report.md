---
# Test Comparison Report

*Generated on: 2026-05-03*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-03/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-05-03/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2361 | 1987 | -374 |
| IREE Compilation | 2237 | 1941 | -296 |
| Gold Inference | 2237 | 1941 | -296 |
| IREE Inference Invocation | 2190 | 1940 | -250 |
| Inference Comparison (PASS) | 2166 | 1915 | -251 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 0 | 374 | +374 |
| IREE Compilation | 124 | 46 | -78 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 47 | 1 | -46 |
| Inference Comparison | 24 | 25 | +1 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-04-26/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-05-03/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2355 | 2361 | +6 | ✅ IMPROVED |
| IREE Compilation | 2236 | 2237 | +1 | ✅ IMPROVED |
| Gold Inference | 2236 | 2237 | +1 | ✅ IMPROVED |
| IREE Inference Invocation | 1984 | 2190 | +206 | ✅ IMPROVED |
| Inference Comparison (PASS) | 1956 | 2166 | +210 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 6 | 0 | -6 | ✅ FEWER FAILURES |
| IREE Compilation | 119 | 124 | +5 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 252 | 47 | -205 | ✅ FEWER FAILURES |
| Inference Comparison | 28 | 24 | -4 | ✅ FEWER FAILURES |

## Summary

### ✅ Improvements

- **Setup**: +6 more tests passing
- **IREE Compilation**: +1 more tests passing
- **Gold Inference**: +1 more tests passing
- **IREE Inference Invocation**: +206 more tests passing
- **Inference Comparison (PASS)**: +210 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| bat_resnext26ts.ch_in1k | PASS | compiled_inference |
| beitv2_base_patch16_224.in1k_ft_in22k_in1k | PASS | compiled_inference |
| beitv2_large_patch16_224.in1k_ft_in22k_in1k | PASS | compiled_inference |
| coatnet_rmlp_2_rw_224.sw_in1k | PASS | compiled_inference |
| convnext_base.clip_laion2b_augreg | PASS | compiled_inference |
| convnext_base.clip_laiona | PASS | compiled_inference |
| convnext_base.clip_laiona_320 | PASS | compiled_inference |
| convnext_base.clip_laiona_augreg_320 | PASS | compiled_inference |
| convnext_base.clip_laiona_augreg_ft_in1k_384 | PASS | compiled_inference |
| convnext_base.fb_in1k | PASS | compiled_inference |
| convnext_base.fb_in22k_ft_in1k | PASS | compiled_inference |
| convnext_base.fb_in22k_ft_in1k_384 | PASS | compiled_inference |
| convnext_large.fb_in22k_ft_in1k | PASS | compiled_inference |
| convnext_large.fb_in22k_ft_in1k_384 | PASS | compiled_inference |
| convnext_large_mlp.clip_laion2b_augreg_ft_in1k_384 | PASS | compiled_inference |
| convnext_large_mlp.clip_laion2b_ft_320 | PASS | compiled_inference |
| convnext_large_mlp.clip_laion2b_ft_soup_320 | PASS | compiled_inference |
| convnext_nano.in12k_ft_in1k | PASS | compiled_inference |
| convnext_small.fb_in22k_ft_in1k | PASS | compiled_inference |
| convnext_small.fb_in22k_ft_in1k_384 | PASS | compiled_inference |
| convnext_small.in12k_ft_in1k | PASS | compiled_inference |
| convnext_small.in12k_ft_in1k_384 | PASS | compiled_inference |
| convnext_tiny.fb_in22k_ft_in1k | PASS | compiled_inference |
| convnext_tiny.fb_in22k_ft_in1k_384 | PASS | compiled_inference |
| convnext_tiny.in12k_ft_in1k | PASS | compiled_inference |
| convnext_tiny.in12k_ft_in1k_384 | PASS | compiled_inference |
| convnext_xlarge.fb_in22k_ft_in1k_384 | PASS | compiled_inference |
| convnextv2_base.fcmae_ft_in22k_in1k | PASS | compiled_inference |
| convnextv2_base.fcmae_ft_in22k_in1k_384 | PASS | compiled_inference |
| convnextv2_large.fcmae_ft_in22k_in1k | PASS | compiled_inference |
| convnextv2_large.fcmae_ft_in22k_in1k_384 | PASS | compiled_inference |
| convnextv2_nano.fcmae_ft_in22k_in1k | PASS | compiled_inference |
| convnextv2_nano.fcmae_ft_in22k_in1k_384 | PASS | compiled_inference |
| convnextv2_tiny.fcmae_ft_in22k_in1k | PASS | compiled_inference |
| convnextv2_tiny.fcmae_ft_in22k_in1k_384 | PASS | compiled_inference |
| deit3_base_patch16_224.fb_in22k_ft_in1k | PASS | compiled_inference |
| deit3_base_patch16_384.fb_in22k_ft_in1k | PASS | compiled_inference |
| deit3_large_patch16_224.fb_in22k_ft_in1k | PASS | compiled_inference |
| deit3_large_patch16_384.fb_in22k_ft_in1k | PASS | compiled_inference |
| deit3_medium_patch16_224.fb_in22k_ft_in1k | PASS | compiled_inference |
| deit3_small_patch16_224.fb_in22k_ft_in1k | PASS | compiled_inference |
| deit3_small_patch16_384.fb_in22k_ft_in1k | PASS | compiled_inference |
| deit_tiny_patch16_224.fb_in1k | PASS | compiled_inference |
| migraphx_cadene__resnext101_64x4di16 | PASS | compiled_inference |
| migraphx_torchvision__inceptioni32 | PASS | compiled_inference |
| migraphx_torchvision__resnet50i64 | PASS | compiled_inference |

**Total regressed models: 46**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| adv_inception_v3_Opset17_timm | compiled_inference | PASS |
| bat_resnext26ts_Opset18_timm | compiled_inference | PASS |
| botnet26t_256_Opset17_timm | compiled_inference | PASS |
| botnet26t_256_Opset18_timm | compiled_inference | PASS |
| coat_lite_small_Opset18_timm | compiled_inference | PASS |
| coat_lite_tiny_Opset18_timm | compiled_inference | PASS |
| coat_mini_Opset17_timm | compiled_inference | PASS |
| convnext_base_in22ft1k_Opset16_timm | compiled_inference | PASS |
| convnext_base_in22k_Opset18_timm | compiled_inference | PASS |
| convnext_large_Opset17_timm | compiled_inference | PASS |
| convnext_large_in22ft1k_Opset18_timm | compiled_inference | PASS |
| convnext_tiny_Opset17_timm | compiled_inference | PASS |
| convnext_tiny_Opset18_timm | compiled_inference | PASS |
| convnext_xlarge_384_in22ft1k_Opset18_timm | compiled_inference | PASS |
| convnext_xlarge_in22k_Opset18_timm | compiled_inference | PASS |
| cs3darknet_focus_l_Opset16_timm | compiled_inference | PASS |
| cs3darknet_m_Opset16_timm | compiled_inference | PASS |
| cs3darknet_m_Opset18_timm | compiled_inference | PASS |
| cs3se_edgenet_x_Opset17_timm | compiled_inference | PASS |
| cs3sedarknet_x_Opset16_timm | compiled_inference | PASS |
| cspdarknet53_Opset16_timm | compiled_inference | PASS |
| cspdarknet53_Opset17_timm | compiled_inference | PASS |
| darknet53_Opset16_timm | compiled_inference | PASS |
| deit3_base_patch16_224_Opset17_timm | compiled_inference | PASS |
| deit3_base_patch16_224_in21ft1k_Opset16_timm | compiled_inference | PASS |
| deit3_base_patch16_384_Opset16_timm | compiled_inference | PASS |
| deit3_base_patch16_384_Opset18_timm | compiled_inference | PASS |
| deit3_large_patch16_224_in21ft1k_Opset16_timm | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset16_timm | compiled_inference | PASS |
| deit3_small_patch16_224_in21ft1k_Opset16_timm | compiled_inference | PASS |
| deit_small_distilled_patch16_224_Opset17_timm | compiled_inference | PASS |
| deit_tiny_patch16_224_Opset18_timm | compiled_inference | PASS |
| densenet121_Opset18_timm | compiled_inference | PASS |
| densenet121_Opset18_torch_hub | compiled_inference | PASS |
| densenet161_Opset16_timm | compiled_inference | PASS |
| densenet161_Opset16_torch_hub | compiled_inference | PASS |
| densenet161_Opset17_timm | compiled_inference | PASS |
| densenet169_Opset18_timm | compiled_inference | PASS |
| densenetblur121d_Opset16_timm | compiled_inference | PASS |
| densenetblur121d_Opset18_timm | compiled_inference | PASS |
| dla102_Opset16_timm | compiled_inference | PASS |
| dla102_Opset17_timm | compiled_inference | PASS |
| dla102x_Opset17_timm | compiled_inference | PASS |
| dla46_c_Opset16_timm | compiled_inference | PASS |
| dla60_Opset17_timm | compiled_inference | PASS |
| dla60_res2net_Opset16_timm | compiled_inference | PASS |
| dla60_res2net_Opset18_timm | compiled_inference | PASS |
| dm_nfnet_f1_Opset17_timm | setup | PASS |
| eca_nfnet_l2_Opset17_timm | compiled_inference | PASS |
| ecaresnet269d_Opset17_timm | compiled_inference | PASS |

*... and 206 more improved models*

**Total improved models: 256**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-04-26/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-05-03/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 1987 | 1987 | 0 | ➖ NO CHANGE |
| IREE Compilation | 1945 | 1941 | -4 | ⚠️ REGRESSION |
| Gold Inference | 1945 | 1941 | -4 | ⚠️ REGRESSION |
| IREE Inference Invocation | 1944 | 1940 | -4 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 1913 | 1915 | +2 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 42 | 46 | +4 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1 | 1 | 0 | ➖ NO CHANGE |
| Inference Comparison | 31 | 25 | -6 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -4 fewer tests passing
- **Gold Inference**: -4 fewer tests passing
- **IREE Inference Invocation**: -4 fewer tests passing

### ✅ Improvements

- **Inference Comparison (PASS)**: +2 more tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| flaubert_Opset18_transformers | Numerics | PASS |
| umt5_Opset17_transformers | Numerics | PASS |

**Total improved models: 2**


---

