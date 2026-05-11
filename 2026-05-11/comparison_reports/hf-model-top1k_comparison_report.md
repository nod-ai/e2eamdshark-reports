---
# Test Comparison Report

*Generated on: 2026-05-11*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-11/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-11/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 493 | 492 | -1 |
| IREE Compilation | 0 | 422 | +422 |
| Gold Inference | 0 | 406 | +406 |
| IREE Inference Invocation | 0 | 401 | +401 |
| Inference Comparison (PASS) | 0 | 387 | +387 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 15 | +1 |
| IREE Compilation | 493 | 70 | -423 |
| Gold Inference | 0 | 16 | +16 |
| IREE Inference Invocation | 0 | 5 | +5 |
| Inference Comparison | 0 | 14 | +14 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-07/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-11/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 429 | 0 | -429 | ⚠️ REGRESSION |
| Gold Inference | 413 | 0 | -413 | ⚠️ REGRESSION |
| IREE Inference Invocation | 410 | 0 | -410 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 396 | 0 | -396 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 64 | 493 | +429 | ⚠️ MORE FAILURES |
| Gold Inference | 16 | 0 | -16 | ✅ FEWER FAILURES |
| IREE Inference Invocation | 3 | 0 | -3 | ✅ FEWER FAILURES |
| Inference Comparison | 14 | 0 | -14 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -429 fewer tests passing
- **Gold Inference**: -413 fewer tests passing
- **IREE Inference Invocation**: -410 fewer tests passing
- **Inference Comparison (PASS)**: -396 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_GIST-Embedding-v0 | PASS | compilation |
| hf_GIST-large-Embedding-v0 | PASS | compilation |
| hf_GIST-small-Embedding-v0 | PASS | compilation |
| hf_LaBSE | PASS | compilation |
| hf_LaBSE-en-ru | PASS | compilation |
| hf_SapBERT-UMLS-2020AB-all-lang-from-XLMR | PASS | compilation |
| hf_SapBERT-from-PubMedBERT-fulltext | PASS | compilation |
| hf_UAE-Large-V1 | PASS | compilation |
| hf_all-MiniLM-L12-v2 | PASS | compilation |
| hf_all-MiniLM-L6-v2 | PASS | compilation |
| hf_all-distilroberta-v1 | PASS | compilation |
| hf_all-mpnet-base-v2 | PASS | compilation |
| hf_all-roberta-large-v1 | PASS | compilation |
| hf_bart-base | PASS | compilation |
| hf_bert-base-nli-mean-tokens | PASS | compilation |
| hf_bert-base-turkish-cased-mean-nli-stsb-tr | PASS | compilation |
| hf_bge-base-en-v1.5 | PASS | compilation |
| hf_bge-large-en | PASS | compilation |
| hf_bge-large-en-v1.5 | PASS | compilation |
| hf_bge-large-zh-v1.5 | PASS | compilation |
| hf_bge-small-en | PASS | compilation |
| hf_bge-small-en-v1.5 | PASS | compilation |
| hf_biobert-v1.1 | PASS | compilation |
| hf_conv-bert-base | PASS | compilation |
| hf_cross-en-de-roberta-sentence-transformer | PASS | compilation |
| hf_distilbert-base-nli-mean-tokens | PASS | compilation |
| hf_distilbert-base-nli-stsb-mean-tokens | PASS | compilation |
| hf_distiluse-base-multilingual-cased-v1 | PASS | compilation |
| hf_distiluse-base-multilingual-cased-v2 | PASS | compilation |
| hf_dragon-multiturn-context-encoder | PASS | compilation |
| hf_dragon-multiturn-query-encoder | PASS | compilation |
| hf_gte-small | PASS | compilation |
| hf_indobert-base-p1 | PASS | compilation |
| hf_instructor-large | PASS | compilation |
| hf_jina-embeddings-v2-small-en | PASS | compilation |
| hf_ko-sroberta-multitask | PASS | compilation |
| hf_kobert | PASS | compilation |
| hf_llm-embedder | PASS | compilation |
| hf_msmarco-MiniLM-L6-cos-v5 | PASS | compilation |
| hf_msmarco-distilbert-base-tas-b | PASS | compilation |
| hf_msmarco-distilbert-base-v4 | PASS | compilation |
| hf_msmarco-distilbert-cos-v5 | PASS | compilation |
| hf_msmarco-distilbert-dot-v5 | PASS | compilation |
| hf_multi-qa-MiniLM-L6-cos-v1 | PASS | compilation |
| hf_multi-qa-distilbert-cos-v1 | PASS | compilation |
| hf_multi-qa-mpnet-base-dot-v1 | PASS | compilation |
| hf_mxbai-embed-large-v1 | PASS | compilation |
| hf_paraphrase-MiniLM-L3-v2 | PASS | compilation |
| hf_paraphrase-MiniLM-L6-v2 | PASS | compilation |
| hf_paraphrase-mpnet-base-v2 | PASS | compilation |

*... and 346 more regressed models*

**Total regressed models: 396**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-07/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-11/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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

