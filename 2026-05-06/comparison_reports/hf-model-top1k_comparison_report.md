---
# Test Comparison Report

*Generated on: 2026-05-06*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-06/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-06/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 493 | 492 | -1 |
| IREE Compilation | 429 | 422 | -7 |
| Gold Inference | 413 | 406 | -7 |
| IREE Inference Invocation | 361 | 401 | +40 |
| Inference Comparison (PASS) | 347 | 387 | +40 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 15 | +1 |
| IREE Compilation | 64 | 70 | +6 |
| Gold Inference | 16 | 16 | 0 |
| IREE Inference Invocation | 52 | 5 | -47 |
| Inference Comparison | 14 | 14 | 0 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-05/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-06/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 434 | 429 | -5 | ⚠️ REGRESSION |
| Gold Inference | 418 | 413 | -5 | ⚠️ REGRESSION |
| IREE Inference Invocation | 394 | 361 | -33 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 380 | 347 | -33 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 59 | 64 | +5 | ⚠️ MORE FAILURES |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 24 | 52 | +28 | ⚠️ MORE FAILURES |
| Inference Comparison | 14 | 14 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -5 fewer tests passing
- **Gold Inference**: -5 fewer tests passing
- **IREE Inference Invocation**: -33 fewer tests passing
- **Inference Comparison (PASS)**: -33 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_cspdarknet53.ra_in1k | PASS | compilation |
| hf_densenet121.ra_in1k | PASS | compilation |
| hf_inception_resnet_v2.tf_in1k | PASS | compilation |
| hf_BioLinkBERT-base | PASS | compiled_inference |
| hf_BioLinkBERT-large | PASS | compiled_inference |
| hf_Indobert-QA | PASS | compiled_inference |
| hf_LinkBERT-large | PASS | compiled_inference |
| hf_WSPAlign-ft-kftt | PASS | compiled_inference |
| hf_albert-base-v2-squad2 | PASS | compiled_inference |
| hf_bert-base-cased-squad-v1.1-portuguese | PASS | compiled_inference |
| hf_bert-base-cased-squad2 | PASS | compiled_inference |
| hf_bert-base-spanish-wwm-cased-finetuned-spa-squad2-es | PASS | compiled_inference |
| hf_bert-base-turkish-squad | PASS | compiled_inference |
| hf_bert-base-uncased-squad-v1 | PASS | compiled_inference |
| hf_bert-base-uncased-squad2 | PASS | compiled_inference |
| hf_bert-extractive-qa-large-project | PASS | compiled_inference |
| hf_bert-large-cased-squad-v1.1-portuguese | PASS | compiled_inference |
| hf_bert-large-cased-whole-word-masking-finetuned-squad | PASS | compiled_inference |
| hf_bert-large-finetuned-squad2 | PASS | compiled_inference |
| hf_bert-large-uncased-whole-word-masking-finetuned-squad | PASS | compiled_inference |
| hf_bert-large-uncased-whole-word-masking-squad2 | PASS | compiled_inference |
| hf_bert-tiny-finetuned-squadv2 | PASS | compiled_inference |
| hf_bertserini-bert-base-squad | PASS | compiled_inference |
| hf_biobert-base-cased-v1.1-squad | PASS | compiled_inference |
| hf_biobert-large-cased-v1.1-squad | PASS | compiled_inference |
| hf_biobert-v1.1-biomedicalQuestionAnswering | PASS | compiled_inference |
| hf_camembert-base-squadFR-fquad-piaf | PASS | compiled_inference |
| hf_distilbert-base-cased-distilled-squad | PASS | compiled_inference |
| hf_distilbert-base-uncased-distilled-squad | PASS | compiled_inference |
| hf_distilbert-extractive-qa-large-project | PASS | compiled_inference |
| hf_distilbert-extractive-qa-project | PASS | compiled_inference |
| hf_distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es | PASS | compiled_inference |
| hf_dynamic_tinybert | PASS | compiled_inference |
| hf_electra_large_discriminator_squad2_512 | PASS | compiled_inference |
| hf_gelectra-base-germanquad | PASS | compiled_inference |
| hf_gelectra-large-germanquad | PASS | compiled_inference |
| hf_indobert-lite-squad | PASS | compiled_inference |
| hf_koelectra-small-v2-distilled-korquad-384 | PASS | compiled_inference |
| hf_minilm-uncased-squad2 | PASS | compiled_inference |
| hf_question-answering-qa-may-12-tablang-LOCAL | PASS | compiled_inference |
| hf_question-answering-roberta-base-s-v2 | PASS | compiled_inference |
| hf_roberta-base-chinese-extractive-qa | PASS | compiled_inference |
| hf_roberta-base-on-cuad | PASS | compiled_inference |
| hf_roberta-base-squad2-distilled | PASS | compiled_inference |
| hf_rubert_large_squad_2 | PASS | compiled_inference |
| hf_sapbert-from-pubmedbert-squad2 | PASS | compiled_inference |
| hf_test-demo-qa | PASS | compiled_inference |
| hf_test-demo-qa-with-roberta | PASS | compiled_inference |
| hf_tiny-distilbert-base-cased-distilled-squad | PASS | compiled_inference |
| hf_tinyroberta-squad2 | PASS | compiled_inference |

*... and 2 more regressed models*

**Total regressed models: 52**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_face-parsing | compiled_inference | PASS |
| hf_segformer-b0-finetuned-ade-512-512 | compiled_inference | PASS |
| hf_segformer-b0-finetuned-cityscapes-1024-1024 | compiled_inference | PASS |
| hf_segformer-b0-finetuned-cityscapes-512-1024 | compiled_inference | PASS |
| hf_segformer-b1-finetuned-ade-512-512 | compiled_inference | PASS |
| hf_segformer-b1-finetuned-cityscapes-1024-1024 | compiled_inference | PASS |
| hf_segformer-b2-fashion | compiled_inference | PASS |
| hf_segformer-b2-finetuned-ade-512-512 | compiled_inference | PASS |
| hf_segformer-b2-finetuned-cityscapes-1024-1024 | compiled_inference | PASS |
| hf_segformer-b3-fashion | compiled_inference | PASS |
| hf_segformer-b3-finetuned-ade-512-512 | compiled_inference | PASS |
| hf_segformer-b3-finetuned-cityscapes-1024-1024 | compiled_inference | PASS |
| hf_segformer-b4-finetuned-ade-512-512 | compiled_inference | PASS |
| hf_segformer-b4-finetuned-cityscapes-1024-1024 | compiled_inference | PASS |
| hf_segformer-b5-finetuned-ade-640-640 | compiled_inference | PASS |
| hf_segformer-b5-finetuned-cityscapes-1024-1024 | compiled_inference | PASS |
| hf_segformer_b2_clothes | compiled_inference | PASS |
| hf_segformer_b3_clothes | compiled_inference | PASS |
| hf_segformer_for_optic_disc_cup_segmentation | compiled_inference | PASS |

**Total improved models: 19**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-05/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-06/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 492 | 492 | 0 | ➖ NO CHANGE |
| IREE Compilation | 436 | 422 | -14 | ⚠️ REGRESSION |
| Gold Inference | 420 | 406 | -14 | ⚠️ REGRESSION |
| IREE Inference Invocation | 414 | 401 | -13 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 396 | 387 | -9 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 15 | 0 | ➖ NO CHANGE |
| IREE Compilation | 56 | 70 | +14 | ⚠️ MORE FAILURES |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 6 | 5 | -1 | ✅ FEWER FAILURES |
| Inference Comparison | 18 | 14 | -4 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -14 fewer tests passing
- **Gold Inference**: -14 fewer tests passing
- **IREE Inference Invocation**: -13 fewer tests passing
- **Inference Comparison (PASS)**: -9 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_beit-base-patch16-224-pt22k | PASS | compilation |
| hf_beit-base-patch16-224-pt22k-ft22k | PASS | compilation |
| hf_beit_base_patch16_224.in22k_ft_in22k_in1k | PASS | compilation |
| hf_beitv2_base_patch16_224.in1k_ft_in22k | PASS | compilation |
| hf_cspdarknet53.ra_in1k | PASS | compilation |
| hf_densenet121.ra_in1k | PASS | compilation |
| hf_inception_resnet_v2.tf_in1k | PASS | compilation |
| hf_inception_v3.tf_adv_in1k | PASS | compilation |
| hf_inception_v3.tv_in1k | PASS | compilation |
| hf_pedestrian_gender_recognition | PASS | compilation |

**Total regressed models: 10**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_dragon-multiturn-context-encoder | compiled_inference | PASS |

**Total improved models: 1**


---

