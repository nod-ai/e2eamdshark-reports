
# COMPILATION ERROR ANALYSIS

**Total compilation failures: 31**

| Status | Count |
|---|---|
| Timeouts | 3 |
| Errors | 28 |
| No log | 0 |

## ERRORS (grouped by error)

| Error | Count |
|---|---|
| 'OP' op operand #0 must be bool-like, but got 'OP' | 16 |
| (no error details) | 7 |
| function 'OP' uses 77824 bytes of shared memory | 2 |
| function 'OP' uses 70656 bytes of shared memory | 1 |
| function 'OP' uses 69632 bytes of shared memory | 1 |
| 'OP' op failed to distribute | 1 |

## ERROR TESTS (grouped by error)

### Error: 'OP' op operand #0 must be bool-like, but got 'OP'

**Count: 16**

| test_name | command | error |
|---|---|---|
| dpn107_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| dpn92_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn92_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn92_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnetx_002.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_002.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_002.pycls_in1k_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnetx_006.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_006.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_006.pycls_in1k_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnetx_016.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_016.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetx_016.pycls_in1k_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_002.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_002.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_002.pycls_in1k_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_004.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_004.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_004.pycls_in1k_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_016.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_016.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_016.pycls_in1k_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_032.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_032.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_032.pycls_in1k_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_032.ra_in1k_train_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_032.ra_in1k_train_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_032.ra_in1k_train_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_032.ra_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_032.ra_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_032.ra_in1k_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_064.pycls_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_064.pycls_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_064.pycls_in1k_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_064.ra3_in1k_train_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_064.ra3_in1k_train_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_064.ra3_in1k_train_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| regnety_064.ra3_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_064.ra3_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnety_064.ra3_in1k_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| resnest50d_1s4x24d_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnest50d_1s4x24d_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnest50d_1s4x24d_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |
| resnest50d_4s2x40d_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnest50d_4s2x40d_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnest50d_4s2x40d_vaiq/compiled_model.vmfb | 'arith.select' op operand #0 must be bool-like, but got 'vector<1xf32>' |

### Error: (no error details)

**Count: 7**

| test_name | command | error |
|---|---|---|
| dla60_res2next_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dla60_res2next_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dla60_res2next_vaiq/compiled_model.vmfb |  |
| dpn131_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn131_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn131_vaiq/compiled_model.vmfb |  |
| dpn98_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn98_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn98_vaiq/compiled_model.vmfb |  |
| nf_regnet_b1.ra2_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/nf_regnet_b1.ra2_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/nf_regnet_b1.ra2_in1k_vaiq/compiled_model.vmfb |  |
| regnetz_040.ra3_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetz_040.ra3_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetz_040.ra3_in1k_vaiq/compiled_model.vmfb |  |
| regnetz_040_h.ra3_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetz_040_h.ra3_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/regnetz_040_h.ra3_in1k_vaiq/compiled_model.vmfb |  |
| res2next50_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/res2next50_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/res2next50_vaiq/compiled_model.vmfb |  |

### Error: function 'OP' uses 77824 bytes of shared memory

**Count: 2**

| test_name | command | error |
|---|---|---|
| gluon_senet154_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/gluon_senet154_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/gluon_senet154_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_33_conv_512x28x28x256x3x3_i8xi8xi32' uses 77824 bytes of shared memory |
| legacy_senet154_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/legacy_senet154_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/legacy_senet154_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_33_conv_512x28x28x256x3x3_i8xi8xi32' uses 77824 bytes of shared memory |

### Error: function 'OP' uses 70656 bytes of shared memory

**Count: 1**

| test_name | command | error |
|---|---|---|
| hrnet_w40_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/hrnet_w40_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/hrnet_w40_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_290_conv_160x14x14x80x3x3_i8xi8xi32' uses 70656 bytes of shared memory |

### Error: function 'OP' uses 69632 bytes of shared memory

**Count: 1**

| test_name | command | error |
|---|---|---|
| resmlp_big_24_224.fb_distilled_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resmlp_big_24_224.fb_distilled_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resmlp_big_24_224.fb_distilled_in1k_vaiq/compiled_model.vmfb | function 'main_graph$async_dispatch_12_batch_matmul_1x768x784x784_i8xi8xi32' uses 69632 bytes of shared memory |

### Error: 'OP' op failed to distribute

**Count: 1**

| test_name | command | error |
|---|---|---|
| resnest101e_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnest101e_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resnest101e_vaiq/compiled_model.vmfb | 'func.func' op failed to distribute |

## TIMEOUT TESTS

| test_name | command |
|---|---|
| resmlp_12_224.fb_distilled_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resmlp_12_224.fb_distilled_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resmlp_12_224.fb_distilled_in1k_vaiq/compiled_model.vmfb |
| resmlp_24_224.fb_distilled_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resmlp_24_224.fb_distilled_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resmlp_24_224.fb_distilled_in1k_vaiq/compiled_model.vmfb |
| resmlp_36_224.fb_distilled_in1k_vaiq | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resmlp_36_224.fb_distilled_in1k_vaiq/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/resmlp_36_224.fb_distilled_in1k_vaiq/compiled_model.vmfb |

