
# COMPILATION ERROR ANALYSIS

**Total compilation failures: 25**

| Status | Count |
|---|---|
| Timeouts | 0 |
| Errors | 25 |
| No log | 0 |

## ERRORS (grouped by error)

| Error | Count |
|---|---|
| function 'OP' uses 81920 bytes of shared memory | 16 |
| 'OP' op expected type of operand #1 ('OP') to match type of corresponding result ('OP') | 5 |
| LLVM Translation failed for operation | 3 |
| 'OP' op failed to distribute | 1 |

## ERROR TESTS (grouped by error)

### Error: function 'OP' uses 81920 bytes of shared memory

**Count: 16**

| test_name | command | error |
|---|---|---|
| dm_nfnet_f2.dm_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f2.dm_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f2.dm_in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_259_matmul_like_1536x121x1536_f32' uses 81920 bytes of shared memory |
| maxvit_base_tf_224.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_base_tf_224.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_base_tf_224.in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_2_conv_64x112x112x64x3x3_f32' uses 81920 bytes of shared memory |
| maxvit_base_tf_384.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_base_tf_384.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_base_tf_384.in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_2_conv_64x192x192x64x3x3_f32' uses 81920 bytes of shared memory |
| maxvit_base_tf_512.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_base_tf_512.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_base_tf_512.in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_136_matmul_4096x192x768_f32' uses 81920 bytes of shared memory |
| maxvit_large_tf_224.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_large_tf_224.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_large_tf_224.in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_2_conv_128x112x112x128x3x3_f32' uses 81920 bytes of shared memory |
| maxvit_large_tf_384.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_large_tf_384.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_large_tf_384.in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_2_conv_128x192x192x128x3x3_f32' uses 81920 bytes of shared memory |
| maxvit_small_tf_224.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_small_tf_224.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_small_tf_224.in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_2_conv_64x112x112x64x3x3_f32' uses 81920 bytes of shared memory |
| maxvit_small_tf_384.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_small_tf_384.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_small_tf_384.in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_2_conv_64x192x192x64x3x3_f32' uses 81920 bytes of shared memory |
| maxvit_small_tf_512.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_small_tf_512.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_small_tf_512.in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_136_matmul_4096x192x768_f32' uses 81920 bytes of shared memory |
| maxvit_tiny_tf_224.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_tiny_tf_224.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_tiny_tf_224.in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_2_conv_64x112x112x64x3x3_f32' uses 81920 bytes of shared memory |
| maxvit_tiny_tf_384.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_tiny_tf_384.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_tiny_tf_384.in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_2_conv_64x192x192x64x3x3_f32' uses 81920 bytes of shared memory |
| maxvit_xlarge_tf_384.in21k_ft_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_xlarge_tf_384.in21k_ft_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_xlarge_tf_384.in21k_ft_in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_2_conv_192x192x192x192x3x3_f32' uses 81920 bytes of shared memory |
| nasnetalarge | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/nasnetalarge/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/nasnetalarge/compiled_model.vmfb | function 'torch_jit$async_dispatch_519_matmul_like_672x121x2688_f32' uses 81920 bytes of shared memory |
| tf_efficientnet_b8.ap_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/tf_efficientnet_b8.ap_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/tf_efficientnet_b8.ap_in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_428_matmul_like_2816x441x704_f32' uses 81920 bytes of shared memory |
| visformer_small | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/visformer_small/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/visformer_small/compiled_model.vmfb | function 'torch_jit$async_dispatch_2_conv_192x28x28x32x4x4_f32' uses 81920 bytes of shared memory |
| vit_relpos_base_patch16_224.sw_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_relpos_base_patch16_224.sw_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_relpos_base_patch16_224.sw_in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_6_batch_matmul_12x196x196x64_f32' uses 81920 bytes of shared memory |

### Error: 'OP' op expected type of operand #1 ('OP') to match type of corresponding result ('OP')

**Count: 5**

| test_name | command | error |
|---|---|---|
| maxxvit_rmlp_nano_rw_256.sw_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxxvit_rmlp_nano_rw_256.sw_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxxvit_rmlp_nano_rw_256.sw_in1k/compiled_model.vmfb | 'linalg.copy' op expected type of operand #1 ('tensor<?x2x?x?xf32>') to match type of corresponding result ('tensor<?x?x?x?xf32>') |
| maxxvit_rmlp_small_rw_256.sw_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxxvit_rmlp_small_rw_256.sw_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxxvit_rmlp_small_rw_256.sw_in1k/compiled_model.vmfb | 'linalg.copy' op expected type of operand #1 ('tensor<?x2x?x?xf32>') to match type of corresponding result ('tensor<?x?x?x?xf32>') |
| maxxvitv2_nano_rw_256.sw_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxxvitv2_nano_rw_256.sw_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxxvitv2_nano_rw_256.sw_in1k/compiled_model.vmfb | 'linalg.copy' op expected type of operand #1 ('tensor<?x2x?x?xf32>') to match type of corresponding result ('tensor<?x?x?x?xf32>') |
| maxxvitv2_rmlp_base_rw_224.sw_in12k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxxvitv2_rmlp_base_rw_224.sw_in12k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxxvitv2_rmlp_base_rw_224.sw_in12k/compiled_model.vmfb | 'linalg.copy' op expected type of operand #1 ('tensor<?x2x1x?xf32>') to match type of corresponding result ('tensor<?x?x1x?xf32>') |
| maxxvitv2_rmlp_base_rw_224.sw_in12k_ft_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxxvitv2_rmlp_base_rw_224.sw_in12k_ft_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxxvitv2_rmlp_base_rw_224.sw_in12k_ft_in1k/compiled_model.vmfb | 'linalg.copy' op expected type of operand #1 ('tensor<?x2x1x?xf32>') to match type of corresponding result ('tensor<?x?x1x?xf32>') |

### Error: LLVM Translation failed for operation

**Count: 3**

| test_name | command | error |
|---|---|---|
| jx_nest_base | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_base/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_base/compiled_model.vmfb | LLVM Translation failed for operation |
| jx_nest_small | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_small/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_small/compiled_model.vmfb | LLVM Translation failed for operation |
| jx_nest_tiny | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_tiny/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_tiny/compiled_model.vmfb | LLVM Translation failed for operation |

### Error: 'OP' op failed to distribute

**Count: 1**

| test_name | command | error |
|---|---|---|
| dm_nfnet_f4.dm_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f4.dm_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f4.dm_in1k/compiled_model.vmfb | 'func.func' op failed to distribute |

