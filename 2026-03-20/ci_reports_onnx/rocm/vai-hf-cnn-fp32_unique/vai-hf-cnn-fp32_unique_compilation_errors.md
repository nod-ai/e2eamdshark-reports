
# COMPILATION ERROR ANALYSIS

**Total compilation failures: 29**

| Status | Count |
|---|---|
| Timeouts | 0 |
| Errors | 29 |
| No log | 0 |

## ERRORS (grouped by error)

| Error | Count |
|---|---|
| 'OP' op failed to distribute | 22 |
| function 'OP' uses 77824 bytes of shared memory | 3 |
| function 'OP' uses 82432 bytes of shared memory | 1 |
| function 'OP' uses 85504 bytes of shared memory | 1 |
| function 'OP' uses 90112 bytes of shared memory | 1 |
| function 'OP' uses 83968 bytes of shared memory | 1 |

## ERROR TESTS (grouped by error)

### Error: 'OP' op failed to distribute

**Count: 22**

| test_name | command | error |
|---|---|---|
| cait_xs24_384 | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/cait_xs24_384/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/cait_xs24_384/compiled_model.vmfb | 'func.func' op failed to distribute |
| dm_nfnet_f4.dm_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f4.dm_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f4.dm_in1k/compiled_model.vmfb | 'func.func' op failed to distribute |
| jx_nest_base | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_base/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_base/compiled_model.vmfb | 'func.func' op failed to distribute |
| jx_nest_small | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_small/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_small/compiled_model.vmfb | 'func.func' op failed to distribute |
| jx_nest_tiny | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_tiny/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/jx_nest_tiny/compiled_model.vmfb | 'func.func' op failed to distribute |
| maxvit_base_tf_384.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_base_tf_384.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_base_tf_384.in1k/compiled_model.vmfb | 'func.func' op failed to distribute |
| maxvit_base_tf_512.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_base_tf_512.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_base_tf_512.in1k/compiled_model.vmfb | 'func.func' op failed to distribute |
| maxvit_large_tf_384.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_large_tf_384.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_large_tf_384.in1k/compiled_model.vmfb | 'func.func' op failed to distribute |
| maxvit_large_tf_512.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_large_tf_512.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_large_tf_512.in1k/compiled_model.vmfb | 'func.func' op failed to distribute |
| maxvit_small_tf_384.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_small_tf_384.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_small_tf_384.in1k/compiled_model.vmfb | 'func.func' op failed to distribute |
| maxvit_small_tf_512.in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_small_tf_512.in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_small_tf_512.in1k/compiled_model.vmfb | 'func.func' op failed to distribute |
| maxvit_xlarge_tf_384.in21k_ft_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_xlarge_tf_384.in21k_ft_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/maxvit_xlarge_tf_384.in21k_ft_in1k/compiled_model.vmfb | 'func.func' op failed to distribute |
| swinv2_large_window12to16_192to256.ms_in22k_ft_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/swinv2_large_window12to16_192to256.ms_in22k_ft_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/swinv2_large_window12to16_192to256.ms_in22k_ft_in1k/compiled_model.vmfb | 'func.func' op failed to distribute |
| swinv2_large_window12to24_192to384.ms_in22k_ft_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/swinv2_large_window12to24_192to384.ms_in22k_ft_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/swinv2_large_window12to24_192to384.ms_in22k_ft_in1k/compiled_model.vmfb | 'func.func' op failed to distribute |
| xcit_large_24_p8_384_dist | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_large_24_p8_384_dist/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_large_24_p8_384_dist/compiled_model.vmfb | 'func.func' op failed to distribute |
| xcit_medium_24_p16_384_dist | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_medium_24_p16_384_dist/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_medium_24_p16_384_dist/compiled_model.vmfb | 'func.func' op failed to distribute |
| xcit_medium_24_p8_224 | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_medium_24_p8_224/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_medium_24_p8_224/compiled_model.vmfb | 'func.func' op failed to distribute |
| xcit_medium_24_p8_384_dist | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_medium_24_p8_384_dist/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_medium_24_p8_384_dist/compiled_model.vmfb | 'func.func' op failed to distribute |
| xcit_small_12_p8_384_dist | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_small_12_p8_384_dist/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_small_12_p8_384_dist/compiled_model.vmfb | 'func.func' op failed to distribute |
| xcit_small_24_p8_384_dist | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_small_24_p8_384_dist/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_small_24_p8_384_dist/compiled_model.vmfb | 'func.func' op failed to distribute |
| xcit_tiny_12_p8_384_dist | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_tiny_12_p8_384_dist/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_tiny_12_p8_384_dist/compiled_model.vmfb | 'func.func' op failed to distribute |
| xcit_tiny_24_p8_384_dist | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_tiny_24_p8_384_dist/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/xcit_tiny_24_p8_384_dist/compiled_model.vmfb | 'func.func' op failed to distribute |

### Error: function 'OP' uses 77824 bytes of shared memory

**Count: 3**

| test_name | command | error |
|---|---|---|
| regnety_120.sw_in12k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_120.sw_in12k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_120.sw_in12k/compiled_model.vmfb | function 'torch_jit$async_dispatch_3_conv_2x112x72x72x112x3x3_f32' uses 77824 bytes of shared memory |
| regnety_160.deit_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_160.deit_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_160.deit_in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_3_conv_2x112x72x72x112x3x3_f32' uses 77824 bytes of shared memory |
| regnety_160.sw_in12k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_160.sw_in12k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_160.sw_in12k/compiled_model.vmfb | function 'torch_jit$async_dispatch_3_conv_2x112x72x72x112x3x3_f32' uses 77824 bytes of shared memory |

### Error: function 'OP' uses 82432 bytes of shared memory

**Count: 1**

| test_name | command | error |
|---|---|---|
| dm_nfnet_f2.dm_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f2.dm_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f2.dm_in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_86_conv_6x128x22x22x128x3x3_f32' uses 82432 bytes of shared memory |

### Error: function 'OP' uses 85504 bytes of shared memory

**Count: 1**

| test_name | command | error |
|---|---|---|
| dm_nfnet_f3.dm_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f3.dm_in1k/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f3.dm_in1k/compiled_model.vmfb | function 'torch_jit$async_dispatch_112_conv_6x128x26x26x128x3x3_f32' uses 85504 bytes of shared memory |

### Error: function 'OP' uses 90112 bytes of shared memory

**Count: 1**

| test_name | command | error |
|---|---|---|
| resnest200e | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnest200e/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnest200e/compiled_model.vmfb | function 'torch_jit$async_dispatch_6_conv_2x64x80x80x32x3x3_f32' uses 90112 bytes of shared memory |

### Error: function 'OP' uses 83968 bytes of shared memory

**Count: 1**

| test_name | command | error |
|---|---|---|
| resnest269e | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnest269e/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnest269e/compiled_model.vmfb | function 'torch_jit$async_dispatch_6_conv_2x64x104x104x32x3x3_f32' uses 83968 bytes of shared memory |

