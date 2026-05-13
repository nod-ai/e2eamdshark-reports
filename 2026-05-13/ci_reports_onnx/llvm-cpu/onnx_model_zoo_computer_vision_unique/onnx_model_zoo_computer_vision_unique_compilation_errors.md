
# COMPILATION ERROR ANALYSIS

**Total compilation failures: 7**

| Status | Count |
|---|---|
| Timeouts | 0 |
| Errors | 7 |
| No log | 0 |

## ERRORS (grouped by error)

| Error | Count |
|---|---|
| (no error details) | 6 |
| 'OP' op function type mismatch | 1 |

## ERROR TESTS (grouped by error)

### Error: (no error details)

**Count: 6**

| test_name | command | error |
|---|---|---|
| dpn68_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn68_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn68_Opset17_timm/compiled_model.vmfb |  |
| dpn107_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_Opset16_timm/compiled_model.vmfb |  |
| dpn98_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn98_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn98_Opset17_timm/compiled_model.vmfb |  |
| dpn131_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn131_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn131_Opset18_timm/compiled_model.vmfb |  |
| dpn68b_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn68b_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn68b_Opset16_timm/compiled_model.vmfb |  |
| dpn107_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_Opset18_timm/compiled_model.vmfb |  |

### Error: 'OP' op function type mismatch

**Count: 1**

| test_name | command | error |
|---|---|---|
| dpn92_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn92_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn92_Opset17_timm/compiled_model.vmfb | 'stream.cmd.dispatch' op function type mismatch |

