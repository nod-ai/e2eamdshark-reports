---
# Test Comparison Report

*Generated on: 2026-05-13*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-13/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-13/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 444 | 443 | -1 |
| IREE Compilation | 0 | 373 | +373 |
| Gold Inference | 0 | 357 | +357 |
| IREE Inference Invocation | 0 | 353 | +353 |
| Inference Comparison (PASS) | 0 | 339 | +339 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 63 | 64 | +1 |
| IREE Compilation | 444 | 70 | -374 |
| Gold Inference | 0 | 16 | +16 |
| IREE Inference Invocation | 0 | 4 | +4 |
| Inference Comparison | 0 | 14 | +14 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-12/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-13/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 444 | -49 | ⚠️ REGRESSION |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 63 | +49 | ⚠️ MORE FAILURES |
| IREE Compilation | 493 | 444 | -49 | ✅ FEWER FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -49 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-12/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-13/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 492 | 443 | -49 | ⚠️ REGRESSION |
| IREE Compilation | 422 | 373 | -49 | ⚠️ REGRESSION |
| Gold Inference | 406 | 357 | -49 | ⚠️ REGRESSION |
| IREE Inference Invocation | 402 | 353 | -49 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 388 | 339 | -49 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 64 | +49 | ⚠️ MORE FAILURES |
| IREE Compilation | 70 | 70 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 4 | 4 | 0 | ➖ NO CHANGE |
| Inference Comparison | 14 | 14 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -49 fewer tests passing
- **IREE Compilation**: -49 fewer tests passing
- **Gold Inference**: -49 fewer tests passing
- **IREE Inference Invocation**: -49 fewer tests passing
- **Inference Comparison (PASS)**: -49 fewer tests passing

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
| hf_UAE-Large-V1 | PASS | setup |
| hf_all-MiniLM-L12-v2 | PASS | setup |
| hf_all-MiniLM-L6-v2 | PASS | setup |
| hf_all-distilroberta-v1 | PASS | setup |
| hf_all-mpnet-base-v2 | PASS | setup |
| hf_all-roberta-large-v1 | PASS | setup |
| hf_bert-base-nli-mean-tokens | PASS | setup |
| hf_bert-base-turkish-cased-mean-nli-stsb-tr | PASS | setup |
| hf_bge-base-en-v1.5 | PASS | setup |
| hf_bge-large-en | PASS | setup |
| hf_bge-large-en-v1.5 | PASS | setup |
| hf_bge-large-zh-v1.5 | PASS | setup |
| hf_bge-small-en | PASS | setup |
| hf_bge-small-en-v1.5 | PASS | setup |
| hf_cross-en-de-roberta-sentence-transformer | PASS | setup |
| hf_distilbert-base-nli-mean-tokens | PASS | setup |
| hf_distilbert-base-nli-stsb-mean-tokens | PASS | setup |
| hf_distiluse-base-multilingual-cased-v1 | PASS | setup |
| hf_distiluse-base-multilingual-cased-v2 | PASS | setup |
| hf_instructor-large | PASS | setup |
| hf_jina-embeddings-v2-small-en | PASS | setup |
| hf_ko-sroberta-multitask | PASS | setup |
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
| hf_paraphrase-mpnet-base-v2 | PASS | setup |
| hf_paraphrase-multilingual-MiniLM-L12-v2 | PASS | setup |
| hf_paraphrase-multilingual-mpnet-base-v2 | PASS | setup |
| hf_paraphrase-xlm-r-multilingual-v1 | PASS | setup |
| hf_roberta-base-nli-mean-tokens | PASS | setup |
| hf_rubert-tiny2 | PASS | setup |
| hf_sbert_large_nlu_ru | PASS | setup |
| hf_snowflake-arctic-embed-m | PASS | setup |
| hf_stsb-roberta-base | PASS | setup |
| hf_stsb-xlm-r-multilingual | PASS | setup |

**Total regressed models: 49**


---

