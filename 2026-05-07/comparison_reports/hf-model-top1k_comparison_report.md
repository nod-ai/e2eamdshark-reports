---
# Test Comparison Report

*Generated on: 2026-05-07*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-07/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-07/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 410 | 401 | -9 |
| Inference Comparison (PASS) | 396 | 387 | -9 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 15 | +1 |
| IREE Compilation | 64 | 70 | +6 |
| Gold Inference | 16 | 16 | 0 |
| IREE Inference Invocation | 3 | 5 | +2 |
| Inference Comparison | 14 | 14 | 0 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-06/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-07/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 429 | 429 | 0 | ➖ NO CHANGE |
| Gold Inference | 413 | 413 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 361 | 410 | +49 | ✅ IMPROVED |
| Inference Comparison (PASS) | 347 | 396 | +49 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 64 | 64 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 52 | 3 | -49 | ✅ FEWER FAILURES |
| Inference Comparison | 14 | 14 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Inference Invocation**: +49 more tests passing
- **Inference Comparison (PASS)**: +49 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_BioLinkBERT-base | compiled_inference | PASS |
| hf_BioLinkBERT-large | compiled_inference | PASS |
| hf_Indobert-QA | compiled_inference | PASS |
| hf_LinkBERT-large | compiled_inference | PASS |
| hf_WSPAlign-ft-kftt | compiled_inference | PASS |
| hf_albert-base-v2-squad2 | compiled_inference | PASS |
| hf_bert-base-cased-squad-v1.1-portuguese | compiled_inference | PASS |
| hf_bert-base-cased-squad2 | compiled_inference | PASS |
| hf_bert-base-spanish-wwm-cased-finetuned-spa-squad2-es | compiled_inference | PASS |
| hf_bert-base-turkish-squad | compiled_inference | PASS |
| hf_bert-base-uncased-squad-v1 | compiled_inference | PASS |
| hf_bert-base-uncased-squad2 | compiled_inference | PASS |
| hf_bert-extractive-qa-large-project | compiled_inference | PASS |
| hf_bert-large-cased-squad-v1.1-portuguese | compiled_inference | PASS |
| hf_bert-large-cased-whole-word-masking-finetuned-squad | compiled_inference | PASS |
| hf_bert-large-finetuned-squad2 | compiled_inference | PASS |
| hf_bert-large-uncased-whole-word-masking-finetuned-squad | compiled_inference | PASS |
| hf_bert-large-uncased-whole-word-masking-squad2 | compiled_inference | PASS |
| hf_bert-tiny-finetuned-squadv2 | compiled_inference | PASS |
| hf_bertserini-bert-base-squad | compiled_inference | PASS |
| hf_biobert-base-cased-v1.1-squad | compiled_inference | PASS |
| hf_biobert-large-cased-v1.1-squad | compiled_inference | PASS |
| hf_biobert-v1.1-biomedicalQuestionAnswering | compiled_inference | PASS |
| hf_camembert-base-squadFR-fquad-piaf | compiled_inference | PASS |
| hf_distilbert-base-cased-distilled-squad | compiled_inference | PASS |
| hf_distilbert-base-uncased-distilled-squad | compiled_inference | PASS |
| hf_distilbert-extractive-qa-large-project | compiled_inference | PASS |
| hf_distilbert-extractive-qa-project | compiled_inference | PASS |
| hf_distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es | compiled_inference | PASS |
| hf_dynamic_tinybert | compiled_inference | PASS |
| hf_electra_large_discriminator_squad2_512 | compiled_inference | PASS |
| hf_gelectra-base-germanquad | compiled_inference | PASS |
| hf_gelectra-large-germanquad | compiled_inference | PASS |
| hf_indobert-lite-squad | compiled_inference | PASS |
| hf_koelectra-small-v2-distilled-korquad-384 | compiled_inference | PASS |
| hf_minilm-uncased-squad2 | compiled_inference | PASS |
| hf_question-answering-qa-may-12-tablang-LOCAL | compiled_inference | PASS |
| hf_question-answering-roberta-base-s-v2 | compiled_inference | PASS |
| hf_roberta-base-chinese-extractive-qa | compiled_inference | PASS |
| hf_roberta-base-on-cuad | compiled_inference | PASS |
| hf_roberta-base-squad2-distilled | compiled_inference | PASS |
| hf_rubert_large_squad_2 | compiled_inference | PASS |
| hf_sapbert-from-pubmedbert-squad2 | compiled_inference | PASS |
| hf_test-demo-qa | compiled_inference | PASS |
| hf_test-demo-qa-with-roberta | compiled_inference | PASS |
| hf_tiny-distilbert-base-cased-distilled-squad | compiled_inference | PASS |
| hf_tinyroberta-squad2 | compiled_inference | PASS |
| hf_xlm-roberta-base-squad2 | compiled_inference | PASS |
| hf_xlm-roberta-base-squad2-distilled | compiled_inference | PASS |

**Total improved models: 49**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-06/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-07/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 492 | 492 | 0 | ➖ NO CHANGE |
| IREE Compilation | 422 | 422 | 0 | ➖ NO CHANGE |
| Gold Inference | 406 | 406 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 401 | 401 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 387 | 387 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 15 | 0 | ➖ NO CHANGE |
| IREE Compilation | 70 | 70 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 5 | 0 | ➖ NO CHANGE |
| Inference Comparison | 14 | 14 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

