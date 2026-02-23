
# COMPILATION ERROR ANALYSIS

**Total compilation failures: 5**

| Status | Count |
|---|---|
| Timeouts | 0 |
| Errors | 5 |
| No log | 0 |

## ERRORS (grouped by error)

| Error | Count |
|---|---|
| 'OP' op operand #3 must be vector of integer or index values, but got 'OP' | 3 |
| Cannot set layouts on a dynamically shaped iteration space | 2 |

## ERROR TESTS (grouped by error)

### Error: 'OP' op operand #3 must be vector of integer or index values, but got 'OP'

**Count: 3**

| test_name | command | error |
|---|---|---|
| model--mobilebert-squadv2--aware-ai | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--mobilebert-squadv2--aware-ai/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--mobilebert-squadv2--aware-ai/compiled_model.vmfb | 'vector.gather' op operand #3 must be vector of integer or index values, but got 'index' |
| model--mobilebert_cola--Alireza1044 | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--mobilebert_cola--Alireza1044/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--mobilebert_cola--Alireza1044/compiled_model.vmfb | 'vector.gather' op operand #3 must be vector of integer or index values, but got 'index' |
| model--mobilebert_mnli--Alireza1044 | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--mobilebert_mnli--Alireza1044/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--mobilebert_mnli--Alireza1044/compiled_model.vmfb | 'vector.gather' op operand #3 must be vector of integer or index values, but got 'index' |

### Error: Cannot set layouts on a dynamically shaped iteration space

**Count: 2**

| test_name | command | error |
|---|---|---|
| model--microsoft_deberta-base_squad--Palak | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--microsoft_deberta-base_squad--Palak/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--microsoft_deberta-base_squad--Palak/compiled_model.vmfb | Cannot set layouts on a dynamically shaped iteration space |
| model--microsoft_deberta-large_squad--Palak | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--microsoft_deberta-large_squad--Palak/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--microsoft_deberta-large_squad--Palak/compiled_model.vmfb | Cannot set layouts on a dynamically shaped iteration space |

