
# COMPILATION ERROR ANALYSIS

**Total compilation failures: 9**

| Status | Count |
|---|---|
| Timeouts | 0 |
| Errors | 9 |
| No log | 0 |

## ERRORS (grouped by error)

| Error | Count |
|---|---|
| 'OP' op write affecting operations on global resources are restricted to workgroup distributed contexts. | 9 |

## ERROR TESTS (grouped by error)

### Error: 'OP' op write affecting operations on global resources are restricted to workgroup distributed contexts.

**Count: 9**

| test_name | command | error |
|---|---|---|
| efficientformerv2_l.snap_dist_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/efficientformerv2_l.snap_dist_in1k/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/efficientformerv2_l.snap_dist_in1k/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| efficientformerv2_s0.snap_dist_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/efficientformerv2_s0.snap_dist_in1k/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/efficientformerv2_s0.snap_dist_in1k/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| efficientformerv2_s1.snap_dist_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/efficientformerv2_s1.snap_dist_in1k/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/efficientformerv2_s1.snap_dist_in1k/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| efficientformerv2_s2.snap_dist_in1k | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/efficientformerv2_s2.snap_dist_in1k/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/efficientformerv2_s2.snap_dist_in1k/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| pit_b_224 | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_b_224/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_b_224/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| pit_b_distilled_224 | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_b_distilled_224/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_b_distilled_224/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| pit_s_distilled_224 | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_s_distilled_224/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_s_distilled_224/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| pit_ti_distilled_224 | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_ti_distilled_224/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_ti_distilled_224/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| pit_xs_distilled_224 | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_xs_distilled_224/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_xs_distilled_224/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |

