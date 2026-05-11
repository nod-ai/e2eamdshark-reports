
# COMPILATION ERROR ANALYSIS

**Total compilation failures: 19**

| Status | Count |
|---|---|
| Timeouts | 0 |
| Errors | 19 |
| No log | 0 |

## ERRORS (grouped by error)

| Error | Count |
|---|---|
| 'OP' op write affecting operations on global resources are restricted to workgroup distributed contexts. | 12 |
| (no error details) | 5 |
| 'OP' op function type mismatch | 2 |

## ERROR TESTS (grouped by error)

### Error: 'OP' op write affecting operations on global resources are restricted to workgroup distributed contexts.

**Count: 12**

| test_name | command | error |
|---|---|---|
| coat_lite_mini_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/coat_lite_mini_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/coat_lite_mini_Opset18_timm/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| coat_tiny_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/coat_tiny_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/coat_tiny_Opset16_timm/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| crossvit_18_240_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/crossvit_18_240_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/crossvit_18_240_Opset16_timm/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| crossvit_18_240_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/crossvit_18_240_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/crossvit_18_240_Opset17_timm/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| pit_b_distilled_224_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_b_distilled_224_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_b_distilled_224_Opset16_timm/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| pit_b_distilled_224_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_b_distilled_224_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/pit_b_distilled_224_Opset18_timm/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| vit_base_patch8_224_dino_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_base_patch8_224_dino_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_base_patch8_224_dino_Opset16_timm/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| vit_base_patch8_224_dino_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_base_patch8_224_dino_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_base_patch8_224_dino_Opset18_timm/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| vit_base_patch8_224_in21k_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_base_patch8_224_in21k_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_base_patch8_224_in21k_Opset16_timm/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| vit_base_patch8_224_in21k_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_base_patch8_224_in21k_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_base_patch8_224_in21k_Opset17_timm/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| vit_small_patch8_224_dino_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_small_patch8_224_dino_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_small_patch8_224_dino_Opset16_timm/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |
| vit_small_patch8_224_dino_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_small_patch8_224_dino_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/vit_small_patch8_224_dino_Opset18_timm/compiled_model.vmfb | 'linalg.generic' op write affecting operations on global resources are restricted to workgroup distributed contexts. |

### Error: (no error details)

**Count: 5**

| test_name | command | error |
|---|---|---|
| dpn68_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn68_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn68_Opset17_timm/compiled_model.vmfb |  |
| dpn92_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn92_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn92_Opset17_timm/compiled_model.vmfb |  |
| dpn107_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_Opset16_timm/compiled_model.vmfb |  |
| dpn98_Opset17_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn98_Opset17_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn98_Opset17_timm/compiled_model.vmfb |  |
| dpn68b_Opset16_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn68b_Opset16_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn68b_Opset16_timm/compiled_model.vmfb |  |

### Error: 'OP' op function type mismatch

**Count: 2**

| test_name | command | error |
|---|---|---|
| dpn131_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn131_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn131_Opset18_timm/compiled_model.vmfb | 'stream.cmd.dispatch' op function type mismatch |
| dpn107_Opset18_timm | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_Opset18_timm/model.torch_onnx.mlir --iree-hal-target-backends=llvm-cpu --iree-llvmcpu-target-cpu=host -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/dpn107_Opset18_timm/compiled_model.vmfb | 'stream.cmd.dispatch' op function type mismatch |

