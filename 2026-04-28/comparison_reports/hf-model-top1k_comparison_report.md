---
# Test Comparison Report

*Generated on: 2026-04-28*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-04-28/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-04-28/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 493 | 492 | -1 |
| IREE Compilation | 434 | 420 | -14 |
| Gold Inference | 418 | 404 | -14 |
| IREE Inference Invocation | 361 | 399 | +38 |
| Inference Comparison (PASS) | 345 | 397 | +52 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 15 | +1 |
| IREE Compilation | 59 | 72 | +13 |
| Gold Inference | 16 | 16 | 0 |
| IREE Inference Invocation | 57 | 5 | -52 |
| Inference Comparison | 16 | 2 | -14 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-04-25/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-04-28/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 434 | 434 | 0 | ➖ NO CHANGE |
| Gold Inference | 418 | 418 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 400 | 361 | -39 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 398 | 345 | -53 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 59 | 59 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 18 | 57 | +39 | ⚠️ MORE FAILURES |
| Inference Comparison | 2 | 16 | +14 | ⚠️ MORE FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -39 fewer tests passing
- **Inference Comparison (PASS)**: -53 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_51-languages-classifier | PASS | compiled_inference |
| hf_CentralBankRoBERTa-sentiment-classifier | PASS | compiled_inference |
| hf_Gender-Classification | PASS | compiled_inference |
| hf_MeaningBERT | PASS | compiled_inference |
| hf_NSFW_text_classifier | PASS | compiled_inference |
| hf_Sentimental-Analysis | PASS | compiled_inference |
| hf_albert-xlarge-vitaminc-mnli | PASS | compiled_inference |
| hf_autonlp-Gibberish-Detector-492513457 | PASS | compiled_inference |
| hf_bert-base-multilingual-uncased-sentiment | PASS | compiled_inference |
| hf_bert-base-personality | PASS | compiled_inference |
| hf_bert-base-uncased-emotion | PASS | compiled_inference |
| hf_bert-base-uncased-hatexplain | PASS | compiled_inference |
| hf_bert-base-uncased-snli | PASS | compiled_inference |
| hf_bert-japanese-finetuned-sentiment | PASS | compiled_inference |
| hf_bert-tiny-finetuned-sms-spam-detection | PASS | compiled_inference |
| hf_bert-toxic-comment-classification | PASS | compiled_inference |
| hf_bert_turkish_sentiment | PASS | compiled_inference |
| hf_bertweet-base-sentiment-analysis | PASS | compiled_inference |
| hf_beto-sentiment-analysis | PASS | compiled_inference |
| hf_bge-reranker-base | PASS | compiled_inference |
| hf_dehatebert-mono-english | PASS | compiled_inference |
| hf_dehatebert-mono-portugese | PASS | compiled_inference |
| hf_distilbert-base-multilingual-cased-sentiments-student | PASS | compiled_inference |
| hf_distilbert-base-uncased-finetuned-sst-2-english | PASS | compiled_inference |
| hf_distilroberta-finetuned-financial-news-sentiment-analysis | PASS | compiled_inference |
| hf_emotion-english-distilroberta-base | PASS | compiled_inference |
| hf_emotion_text_classifier | PASS | compiled_inference |
| hf_english-abusive-MuRIL | PASS | compiled_inference |
| hf_finbert | PASS | compiled_inference |
| hf_finbert-tone | PASS | compiled_inference |
| hf_german-sentiment-bert | PASS | compiled_inference |
| hf_indonesian-roberta-base-sentiment-classifier | PASS | compiled_inference |
| hf_koelectra-small-v3-nsmc | PASS | compiled_inference |
| hf_ms-marco-MiniLM-L-12-v2 | PASS | compiled_inference |
| hf_ms-marco-MiniLM-L-2-v2 | PASS | compiled_inference |
| hf_ms-marco-MiniLM-L-4-v2 | PASS | compiled_inference |
| hf_ms-marco-MiniLM-L-6-v2 | PASS | compiled_inference |
| hf_ms-marco-TinyBERT-L-2-v2 | PASS | compiled_inference |
| hf_ms-marco-electra-base | PASS | compiled_inference |
| hf_raceBERT-ethnicity | PASS | compiled_inference |
| hf_roberta-base-go_emotions | PASS | compiled_inference |
| hf_roberta-base-suicide-prediction-phr | PASS | compiled_inference |
| hf_roberta-large-mnli | PASS | compiled_inference |
| hf_robertuito-sentiment-analysis | PASS | compiled_inference |
| hf_rubert-base-cased-nli-threeway | PASS | compiled_inference |
| hf_rubert-tiny2-russian-sentiment | PASS | compiled_inference |
| hf_stsb-TinyBERT-L-4 | PASS | compiled_inference |
| hf_suicidality | PASS | compiled_inference |
| hf_tamil-codemixed-abusive-MuRIL | PASS | compiled_inference |
| hf_toxic-bert | PASS | compiled_inference |

*... and 4 more regressed models*

**Total regressed models: 54**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_yolos-tiny | compiled_inference | PASS |

**Total improved models: 1**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-04-25/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-04-28/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 492 | 492 | 0 | ➖ NO CHANGE |
| IREE Compilation | 420 | 420 | 0 | ➖ NO CHANGE |
| Gold Inference | 404 | 404 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 399 | 399 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 397 | 397 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 15 | 0 | ➖ NO CHANGE |
| IREE Compilation | 72 | 72 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 5 | 0 | ➖ NO CHANGE |
| Inference Comparison | 2 | 2 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

