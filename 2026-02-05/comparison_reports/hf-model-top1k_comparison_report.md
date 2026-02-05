---
# Test Comparison Report

*Generated on: 2026-02-05*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-05/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-05/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 1 | 493 | +492 |
| IREE Compilation | 1 | 403 | +402 |
| Gold Inference | 0 | 401 | +401 |
| IREE Inference Invocation | 0 | 397 | +397 |
| Inference Comparison (PASS) | 0 | 366 | +366 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 506 | 14 | -492 |
| IREE Compilation | 0 | 90 | +90 |
| Gold Inference | 1 | 2 | +1 |
| IREE Inference Invocation | 0 | 4 | +4 |
| Inference Comparison | 0 | 31 | +31 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-04/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-05/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 494 | 1 | -493 | ⚠️ REGRESSION |
| IREE Compilation | 398 | 1 | -397 | ⚠️ REGRESSION |
| Gold Inference | 396 | 0 | -396 | ⚠️ REGRESSION |
| IREE Inference Invocation | 394 | 0 | -394 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 380 | 0 | -380 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 13 | 506 | +493 | ⚠️ MORE FAILURES |
| IREE Compilation | 96 | 0 | -96 | ✅ FEWER FAILURES |
| Gold Inference | 2 | 1 | -1 | ✅ FEWER FAILURES |
| IREE Inference Invocation | 2 | 0 | -2 | ✅ FEWER FAILURES |
| Inference Comparison | 14 | 0 | -14 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -493 fewer tests passing
- **IREE Compilation**: -397 fewer tests passing
- **Gold Inference**: -396 fewer tests passing
- **IREE Inference Invocation**: -394 fewer tests passing
- **Inference Comparison (PASS)**: -380 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_GIST-Embedding-v0 | PASS | setup |
| hf_GIST-large-Embedding-v0 | PASS | setup |
| hf_GIST-small-Embedding-v0 | PASS | setup |
| hf_LaBSE | PASS | setup |
| hf_LaBSE-en-ru | PASS | setup |
| hf_SapBERT-UMLS-2020AB-all-lang-from-XLMR | PASS | setup |
| hf_SapBERT-from-PubMedBERT-fulltext | PASS | setup |
| hf_UAE-Large-V1 | PASS | setup |
| hf_all-MiniLM-L12-v2 | PASS | setup |
| hf_all-MiniLM-L6-v2 | PASS | setup |
| hf_all-distilroberta-v1 | PASS | setup |
| hf_all-mpnet-base-v2 | PASS | setup |
| hf_all-roberta-large-v1 | PASS | setup |
| hf_bart-base | PASS | setup |
| hf_bert-base-nli-mean-tokens | PASS | setup |
| hf_bert-base-turkish-cased-mean-nli-stsb-tr | PASS | setup |
| hf_bge-base-en-v1.5 | PASS | setup |
| hf_bge-large-en | PASS | setup |
| hf_bge-large-en-v1.5 | PASS | setup |
| hf_bge-large-zh-v1.5 | PASS | setup |
| hf_bge-small-en | PASS | setup |
| hf_bge-small-en-v1.5 | PASS | setup |
| hf_biobert-v1.1 | PASS | setup |
| hf_codebert-base | PASS | setup |
| hf_conv-bert-base | PASS | setup |
| hf_cross-en-de-roberta-sentence-transformer | PASS | setup |
| hf_distilbert-base-nli-mean-tokens | PASS | setup |
| hf_distilbert-base-nli-stsb-mean-tokens | PASS | setup |
| hf_distiluse-base-multilingual-cased-v1 | PASS | setup |
| hf_distiluse-base-multilingual-cased-v2 | PASS | setup |
| hf_dragon-multiturn-context-encoder | PASS | setup |
| hf_dragon-multiturn-query-encoder | PASS | setup |
| hf_gte-small | PASS | setup |
| hf_indobert-base-p1 | PASS | setup |
| hf_instructor-large | PASS | setup |
| hf_jina-embeddings-v2-small-en | PASS | setup |
| hf_ko-sroberta-multitask | PASS | setup |
| hf_kobert | PASS | setup |
| hf_llm-embedder | PASS | setup |
| hf_msmarco-MiniLM-L6-cos-v5 | PASS | setup |
| hf_msmarco-distilbert-base-tas-b | PASS | setup |
| hf_msmarco-distilbert-base-v4 | PASS | setup |
| hf_msmarco-distilbert-cos-v5 | PASS | setup |
| hf_msmarco-distilbert-dot-v5 | PASS | setup |
| hf_multi-qa-MiniLM-L6-cos-v1 | PASS | setup |
| hf_multi-qa-distilbert-cos-v1 | PASS | setup |
| hf_multi-qa-mpnet-base-dot-v1 | PASS | setup |
| hf_mxbai-embed-large-v1 | PASS | setup |
| hf_paraphrase-MiniLM-L3-v2 | PASS | setup |
| hf_paraphrase-MiniLM-L6-v2 | PASS | setup |

*... and 330 more regressed models*

**Total regressed models: 380**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-04/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-05/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 403 | 403 | 0 | ➖ NO CHANGE |
| Gold Inference | 401 | 401 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 398 | 397 | -1 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 367 | 366 | -1 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 90 | 90 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3 | 4 | +1 | ⚠️ MORE FAILURES |
| Inference Comparison | 31 | 31 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -1 fewer tests passing
- **Inference Comparison (PASS)**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_kda-albert-xxlarge-v2-race | PASS | compiled_inference |

**Total regressed models: 1**


---

