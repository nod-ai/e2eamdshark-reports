---
# Test Comparison Report

*Generated on: 2026-02-07*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-07/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-07/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 494 | 493 | -1 |
| IREE Compilation | 398 | 403 | +5 |
| Gold Inference | 396 | 401 | +5 |
| IREE Inference Invocation | 394 | 397 | +3 |
| Inference Comparison (PASS) | 380 | 381 | +1 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 13 | 14 | +1 |
| IREE Compilation | 96 | 90 | -6 |
| Gold Inference | 2 | 2 | 0 |
| IREE Inference Invocation | 2 | 4 | +2 |
| Inference Comparison | 14 | 16 | +2 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-06/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-07/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 1 | 494 | +493 | ✅ IMPROVED |
| IREE Compilation | 1 | 398 | +397 | ✅ IMPROVED |
| Gold Inference | 0 | 396 | +396 | ✅ IMPROVED |
| IREE Inference Invocation | 0 | 394 | +394 | ✅ IMPROVED |
| Inference Comparison (PASS) | 0 | 380 | +380 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 506 | 13 | -493 | ✅ FEWER FAILURES |
| IREE Compilation | 0 | 96 | +96 | ⚠️ MORE FAILURES |
| Gold Inference | 1 | 2 | +1 | ⚠️ MORE FAILURES |
| IREE Inference Invocation | 0 | 2 | +2 | ⚠️ MORE FAILURES |
| Inference Comparison | 0 | 14 | +14 | ⚠️ MORE FAILURES |

## Summary

### ✅ Improvements

- **Setup**: +493 more tests passing
- **IREE Compilation**: +397 more tests passing
- **Gold Inference**: +396 more tests passing
- **IREE Inference Invocation**: +394 more tests passing
- **Inference Comparison (PASS)**: +380 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_GIST-Embedding-v0 | setup | PASS |
| hf_GIST-large-Embedding-v0 | setup | PASS |
| hf_GIST-small-Embedding-v0 | setup | PASS |
| hf_LaBSE | setup | PASS |
| hf_LaBSE-en-ru | setup | PASS |
| hf_SapBERT-UMLS-2020AB-all-lang-from-XLMR | setup | PASS |
| hf_SapBERT-from-PubMedBERT-fulltext | setup | PASS |
| hf_UAE-Large-V1 | setup | PASS |
| hf_all-MiniLM-L12-v2 | setup | PASS |
| hf_all-MiniLM-L6-v2 | setup | PASS |
| hf_all-distilroberta-v1 | setup | PASS |
| hf_all-mpnet-base-v2 | setup | PASS |
| hf_all-roberta-large-v1 | setup | PASS |
| hf_bart-base | setup | PASS |
| hf_bert-base-nli-mean-tokens | setup | PASS |
| hf_bert-base-turkish-cased-mean-nli-stsb-tr | setup | PASS |
| hf_bge-base-en-v1.5 | setup | PASS |
| hf_bge-large-en | setup | PASS |
| hf_bge-large-en-v1.5 | setup | PASS |
| hf_bge-large-zh-v1.5 | setup | PASS |
| hf_bge-small-en | setup | PASS |
| hf_bge-small-en-v1.5 | setup | PASS |
| hf_biobert-v1.1 | setup | PASS |
| hf_codebert-base | setup | PASS |
| hf_conv-bert-base | setup | PASS |
| hf_cross-en-de-roberta-sentence-transformer | setup | PASS |
| hf_distilbert-base-nli-mean-tokens | setup | PASS |
| hf_distilbert-base-nli-stsb-mean-tokens | setup | PASS |
| hf_distiluse-base-multilingual-cased-v1 | setup | PASS |
| hf_distiluse-base-multilingual-cased-v2 | setup | PASS |
| hf_dragon-multiturn-context-encoder | setup | PASS |
| hf_dragon-multiturn-query-encoder | setup | PASS |
| hf_gte-small | setup | PASS |
| hf_indobert-base-p1 | setup | PASS |
| hf_instructor-large | setup | PASS |
| hf_jina-embeddings-v2-small-en | setup | PASS |
| hf_ko-sroberta-multitask | setup | PASS |
| hf_kobert | setup | PASS |
| hf_llm-embedder | setup | PASS |
| hf_msmarco-MiniLM-L6-cos-v5 | setup | PASS |
| hf_msmarco-distilbert-base-tas-b | setup | PASS |
| hf_msmarco-distilbert-base-v4 | setup | PASS |
| hf_msmarco-distilbert-cos-v5 | setup | PASS |
| hf_msmarco-distilbert-dot-v5 | setup | PASS |
| hf_multi-qa-MiniLM-L6-cos-v1 | setup | PASS |
| hf_multi-qa-distilbert-cos-v1 | setup | PASS |
| hf_multi-qa-mpnet-base-dot-v1 | setup | PASS |
| hf_mxbai-embed-large-v1 | setup | PASS |
| hf_paraphrase-MiniLM-L3-v2 | setup | PASS |
| hf_paraphrase-MiniLM-L6-v2 | setup | PASS |

*... and 330 more improved models*

**Total improved models: 380**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-06/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-07/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 397 | 397 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 381 | 381 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 90 | 90 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 4 | 4 | 0 | ➖ NO CHANGE |
| Inference Comparison | 16 | 16 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

