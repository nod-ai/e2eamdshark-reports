
# COMPILATION ERROR ANALYSIS

**Total compilation failures: 2**

| Status | Count |
|---|---|
| Timeouts | 0 |
| Errors | 2 |
| No log | 0 |

## ERRORS (grouped by error)

| Error | Count |
|---|---|
| Cannot set layouts on a dynamically shaped iteration space | 2 |

## ERROR TESTS (grouped by error)

### Error: Cannot set layouts on a dynamically shaped iteration space

**Count: 2**

| test_name | command | error |
|---|---|---|
| model--microsoft_deberta-base_squad--Palak | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--microsoft_deberta-base_squad--Palak/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--microsoft_deberta-base_squad--Palak/compiled_model.vmfb | Cannot set layouts on a dynamically shaped iteration space |
| model--microsoft_deberta-large_squad--Palak | iree-compile /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--microsoft_deberta-large_squad--Palak/model.torch_onnx.mlir --iree-hal-target-backends=rocm --iree-hip-target=gfx942 -o /home/runner/_work/AMD-SHARK-TestSuite/AMD-SHARK-TestSuite/test-suite/alt_e2eamdshark/./test-onnx/model--microsoft_deberta-large_squad--Palak/compiled_model.vmfb | Cannot set layouts on a dynamically shaped iteration space |

