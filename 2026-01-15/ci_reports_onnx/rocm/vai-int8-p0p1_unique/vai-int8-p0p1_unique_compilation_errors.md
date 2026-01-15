
# COMPILATION ERROR ANALYSIS

**Total compilation failures: 22**

| Status | Count |
|---|---|
| Timeouts | 5 |
| Errors | 17 |
| No log | 0 |

## ERRORS (grouped by error)

| Error | Count |
|---|---|
| function 'OP' uses 106496 bytes of shared memory | 5 |
| function 'OP' uses 74240 bytes of shared memory | 4 |
| function 'OP' uses 77824 bytes of shared memory | 3 |
| function 'OP' uses 120832 bytes of shared memory | 2 |
| function 'OP' uses 81920 bytes of shared memory | 1 |
| function 'OP' uses 73728 bytes of shared memory | 1 |
| function 'OP' uses 86016 bytes of shared memory | 1 |

## ERROR TESTS (grouped by error)

### Error: function 'OP' uses 106496 bytes of shared memory

**Count: 5**

| test_name | command | error |
|---|---|---|
| regnetx_120.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_120.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_120.pycls_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_2x112x56x56x112x3x3_i8xi8xi32' uses 106496 bytes of shared memory |
| regnety_120.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_120.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_120.pycls_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_2x112x56x56x112x3x3_i8xi8xi32' uses 106496 bytes of shared memory |
| regnety_120.sw_in12k_ft_in1k_train_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_120.sw_in12k_ft_in1k_train_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_120.sw_in12k_ft_in1k_train_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_2x112x56x56x112x3x3_i8xi8xi32' uses 106496 bytes of shared memory |
| regnety_160.lion_in12k_ft_in1k_train_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_160.lion_in12k_ft_in1k_train_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_160.lion_in12k_ft_in1k_train_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_2x112x56x56x112x3x3_i8xi8xi32' uses 106496 bytes of shared memory |
| regnety_160.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_160.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_160.pycls_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_2x112x56x56x112x3x3_i8xi8xi32' uses 106496 bytes of shared memory |

### Error: function 'OP' uses 74240 bytes of shared memory

**Count: 4**

| test_name | command | error |
|---|---|---|
| regnetx_064.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_064.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_064.pycls_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_3x56x56x56x56x3x3_i8xi8xi32' uses 74240 bytes of shared memory |
| regnety_080.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_080.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_080.pycls_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_3x56x56x56x56x3x3_i8xi8xi32' uses 74240 bytes of shared memory |
| regnety_080.ra3_in1k_train_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_080.ra3_in1k_train_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_080.ra3_in1k_train_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_3x56x56x56x56x3x3_i8xi8xi32' uses 74240 bytes of shared memory |
| regnety_080_tv.tv2_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_080_tv.tv2_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_080_tv.tv2_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_4x56x56x56x56x3x3_i8xi8xi32' uses 74240 bytes of shared memory |

### Error: function 'OP' uses 77824 bytes of shared memory

**Count: 3**

| test_name | command | error |
|---|---|---|
| dm_nfnet_f1.dm_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f1.dm_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f1.dm_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_29_conv_2x128x40x40x128x3x3_i8xi8xi32' uses 77824 bytes of shared memory |
| regnetx_320.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_320.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_320.pycls_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_2x168x56x56x168x3x3_i8xi8xi32' uses 77824 bytes of shared memory |
| regnety_080.ra3_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_080.ra3_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_080.ra3_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_3x56x72x72x56x3x3_i8xi8xi32' uses 77824 bytes of shared memory |

### Error: function 'OP' uses 120832 bytes of shared memory

**Count: 2**

| test_name | command | error |
|---|---|---|
| regnety_120.sw_in12k_ft_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_120.sw_in12k_ft_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_120.sw_in12k_ft_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_2x112x72x72x112x3x3_i8xi8xi32' uses 120832 bytes of shared memory |
| regnety_160.lion_in12k_ft_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_160.lion_in12k_ft_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_160.lion_in12k_ft_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_3_conv_2x112x72x72x112x3x3_i8xi8xi32' uses 120832 bytes of shared memory |

### Error: function 'OP' uses 81920 bytes of shared memory

**Count: 1**

| test_name | command | error |
|---|---|---|
| dm_nfnet_f0.dm_in1k_train_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f0.dm_in1k_train_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f0.dm_in1k_train_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_18_conv_2x128x24x24x128x3x3_i8xi8xi32' uses 81920 bytes of shared memory |

### Error: function 'OP' uses 73728 bytes of shared memory

**Count: 1**

| test_name | command | error |
|---|---|---|
| dm_nfnet_f0.dm_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f0.dm_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f0.dm_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_112_conv_6x128x8x8x128x3x3_i8xi8xi32' uses 73728 bytes of shared memory |

### Error: function 'OP' uses 86016 bytes of shared memory

**Count: 1**

| test_name | command | error |
|---|---|---|
| dm_nfnet_f1.dm_in1k_train_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f1.dm_in1k_train_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dm_nfnet_f1.dm_in1k_train_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_29_conv_2x128x28x28x128x3x3_i8xi8xi32' uses 86016 bytes of shared memory |

## TIMEOUT TESTS

| test_name | command |
|---|---|
| gcresnet33ts.ra2_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/gcresnet33ts.ra2_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/gcresnet33ts.ra2_in1k_vaiq/compiled_model.vmfb |
| gcresnet50t.ra2_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/gcresnet50t.ra2_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/gcresnet50t.ra2_in1k_vaiq/compiled_model.vmfb |
| gcresnext26ts.ch_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/gcresnext26ts.ch_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/gcresnext26ts.ch_in1k_vaiq/compiled_model.vmfb |
| gcresnext50ts.ch_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/gcresnext50ts.ch_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/gcresnext50ts.ch_in1k_vaiq/compiled_model.vmfb |
| regnetz_c16.ra3_in1k_train_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetz_c16.ra3_in1k_train_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetz_c16.ra3_in1k_train_vaiq/compiled_model.vmfb |

