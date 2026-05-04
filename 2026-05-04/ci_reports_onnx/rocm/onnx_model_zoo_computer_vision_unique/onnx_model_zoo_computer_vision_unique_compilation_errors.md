
# COMPILATION ERROR ANALYSIS

**Total compilation failures: 38**

| Status | Count |
|---|---|
| Timeouts | 0 |
| Errors | 38 |
| No log | 0 |

## ERRORS (grouped by error)

| Error | Count |
|---|---|
| 'OP' op operand #0 must be bool-like, but got 'OP' | 18 |
| function 'OP' uses 81920 bytes of shared memory | 10 |
| LLVM Translation failed for operation | 6 |
| operand #0 does not dominate this use | 2 |
| (no error details) | 1 |
| 'OP' op expected type of operand #1 ('OP') to match type of corresponding result ('OP') | 1 |

## ERROR TESTS (grouped by error)

### Error: 'OP' op operand #0 must be bool-like, but got 'OP'

**Count: 18**

| test_name | command | error |
|---|---|---|
| regnet_x_1_6gf_Opset18_torch_hub | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnet_x_1_6gf_Opset18_torch_hub/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnet_x_1_6gf_Opset18_torch_hub/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnet_y_1_6gf_Opset17_torch_hub | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnet_y_1_6gf_Opset17_torch_hub/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnet_y_1_6gf_Opset17_torch_hub/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnet_y_400mf_Opset17_torch_hub | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnet_y_400mf_Opset17_torch_hub/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnet_y_400mf_Opset17_torch_hub/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnet_y_3_2gf_Opset18_torch_hub | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnet_y_3_2gf_Opset18_torch_hub/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnet_y_3_2gf_Opset18_torch_hub/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnetx_006_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_006_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_006_Opset17_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_004_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_004_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_004_Opset16_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_016_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_016_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_016_Opset16_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| dla60_res2next_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dla60_res2next_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dla60_res2next_Opset18_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| dpn107_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_Opset16_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| dpn98_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn98_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn98_Opset17_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnetx_002_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_002_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_002_Opset17_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnetx_016_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_016_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_016_Opset16_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_064_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_064_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_064_Opset17_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| dpn131_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn131_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn131_Opset18_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_032_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_032_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_032_Opset17_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| res2next50_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/res2next50_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/res2next50_Opset18_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| dpn107_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_Opset18_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_002_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_002_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_002_Opset16_timm/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |

### Error: function 'OP' uses 81920 bytes of shared memory

**Count: 10**

| test_name | command | error |
|---|---|---|
| vit_relpos_base_patch16_224_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_relpos_base_patch16_224_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_relpos_base_patch16_224_Opset16_timm/compiled_model.vmfb | function 'main_graph$async_dispatch_7_batch_matmul_12x196x196x64_f32' uses 81920 bytes of shared memory |
| tf_efficientnet_b8_ap_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/tf_efficientnet_b8_ap_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/tf_efficientnet_b8_ap_Opset17_timm/compiled_model.vmfb | function 'main_graph$async_dispatch_428_matmul_like_2816x441x704_f32' uses 81920 bytes of shared memory |
| visformer_small_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/visformer_small_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/visformer_small_Opset17_timm/compiled_model.vmfb | function 'main_graph$async_dispatch_2_conv_192x28x28x32x4x4_f32' uses 81920 bytes of shared memory |
| xception41_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xception41_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xception41_Opset17_timm/compiled_model.vmfb | function 'main_graph$async_dispatch_10_matmul_like_128x5625x128_f32' uses 81920 bytes of shared memory |
| xception71_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xception71_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xception71_Opset17_timm/compiled_model.vmfb | function 'main_graph$async_dispatch_10_matmul_like_128x5625x128_f32' uses 81920 bytes of shared memory |
| hrnet_w64_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/hrnet_w64_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/hrnet_w64_Opset16_timm/compiled_model.vmfb | function 'main_graph$async_dispatch_42_conv_64x56x56x64x3x3_f32' uses 81920 bytes of shared memory |
| resnetv2_50_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnetv2_50_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnetv2_50_Opset16_timm/compiled_model.vmfb | function 'main_graph$async_dispatch_16_matmul_like_512x28x28x256_f32' uses 81920 bytes of shared memory |
| vit_relpos_base_patch16_224_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_relpos_base_patch16_224_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_relpos_base_patch16_224_Opset17_timm/compiled_model.vmfb | function 'main_graph$async_dispatch_7_batch_matmul_12x196x196x64_f32' uses 81920 bytes of shared memory |
| xception65_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xception65_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xception65_Opset18_timm/compiled_model.vmfb | function 'main_graph$async_dispatch_10_matmul_like_128x5625x128_f32' uses 81920 bytes of shared memory |
| resnetv2_101_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnetv2_101_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnetv2_101_Opset18_timm/compiled_model.vmfb | function 'main_graph$async_dispatch_16_matmul_like_512x28x28x256_f32' uses 81920 bytes of shared memory |

### Error: LLVM Translation failed for operation

**Count: 6**

| test_name | command | error |
|---|---|---|
| jx_nest_base_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_base_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_base_Opset17_timm/compiled_model.vmfb | LLVM Translation failed for operation |
| jx_nest_small_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_small_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_small_Opset16_timm/compiled_model.vmfb | LLVM Translation failed for operation |
| jx_nest_tiny_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_tiny_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_tiny_Opset16_timm/compiled_model.vmfb | LLVM Translation failed for operation |
| jx_nest_small_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_small_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_small_Opset17_timm/compiled_model.vmfb | LLVM Translation failed for operation |
| jx_nest_tiny_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_tiny_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_tiny_Opset17_timm/compiled_model.vmfb | LLVM Translation failed for operation |
| jx_nest_base_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_base_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_base_Opset16_timm/compiled_model.vmfb | LLVM Translation failed for operation |

### Error: operand #0 does not dominate this use

**Count: 2**

| test_name | command | error |
|---|---|---|
| repvgg_b2g4_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/repvgg_b2g4_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/repvgg_b2g4_Opset16_timm/compiled_model.vmfb | operand #0 does not dominate this use |
| resnest50d_4s2x40d_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnest50d_4s2x40d_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnest50d_4s2x40d_Opset16_timm/compiled_model.vmfb | operand #0 does not dominate this use |

### Error: (no error details)

**Count: 1**

| test_name | command | error |
|---|---|---|
| dpn92_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn92_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn92_Opset17_timm/compiled_model.vmfb |  |

### Error: 'OP' op expected type of operand #1 ('OP') to match type of corresponding result ('OP')

**Count: 1**

| test_name | command | error |
|---|---|---|
| nf_regnet_b1_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/nf_regnet_b1_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/nf_regnet_b1_Opset16_timm/compiled_model.vmfb | 'linalg.copy' op expected type of operand #1 ('tensor<4x?x?x?xf32>') to match type of corresponding result ('tensor<?x?x?x?xf32>') |

