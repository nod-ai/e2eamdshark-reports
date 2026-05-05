---
# Test Comparison Report

*Generated on: 2026-05-05*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-05/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-05/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 493 | 492 | -1 |
| IREE Compilation | 434 | 436 | +2 |
| Gold Inference | 418 | 420 | +2 |
| IREE Inference Invocation | 394 | 414 | +20 |
| Inference Comparison (PASS) | 380 | 396 | +16 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 15 | +1 |
| IREE Compilation | 59 | 56 | -3 |
| Gold Inference | 16 | 16 | 0 |
| IREE Inference Invocation | 24 | 6 | -18 |
| Inference Comparison | 14 | 18 | +4 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-04/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-05/hf-model-top1k/rocm/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 286 | 394 | +108 | ✅ IMPROVED |
| Inference Comparison (PASS) | 272 | 380 | +108 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 59 | 59 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 132 | 24 | -108 | ✅ FEWER FAILURES |
| Inference Comparison | 14 | 14 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Inference Invocation**: +108 more tests passing
- **Inference Comparison (PASS)**: +108 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_51-languages-classifier | compiled_inference | PASS |
| hf_CentralBankRoBERTa-sentiment-classifier | compiled_inference | PASS |
| hf_Gender-Classification | compiled_inference | PASS |
| hf_MeaningBERT | compiled_inference | PASS |
| hf_NSFW_text_classifier | compiled_inference | PASS |
| hf_Sentimental-Analysis | compiled_inference | PASS |
| hf_albert-xlarge-vitaminc-mnli | compiled_inference | PASS |
| hf_autonlp-Gibberish-Detector-492513457 | compiled_inference | PASS |
| hf_bert-base-multilingual-uncased-sentiment | compiled_inference | PASS |
| hf_bert-base-personality | compiled_inference | PASS |
| hf_bert-base-uncased-emotion | compiled_inference | PASS |
| hf_bert-base-uncased-hatexplain | compiled_inference | PASS |
| hf_bert-base-uncased-snli | compiled_inference | PASS |
| hf_bert-japanese-finetuned-sentiment | compiled_inference | PASS |
| hf_bert-tiny-finetuned-sms-spam-detection | compiled_inference | PASS |
| hf_bert-toxic-comment-classification | compiled_inference | PASS |
| hf_bert_turkish_sentiment | compiled_inference | PASS |
| hf_bertweet-base-sentiment-analysis | compiled_inference | PASS |
| hf_beto-sentiment-analysis | compiled_inference | PASS |
| hf_bge-reranker-base | compiled_inference | PASS |
| hf_dehatebert-mono-english | compiled_inference | PASS |
| hf_dehatebert-mono-portugese | compiled_inference | PASS |
| hf_distilbert-base-multilingual-cased-sentiments-student | compiled_inference | PASS |
| hf_distilbert-base-uncased-finetuned-sst-2-english | compiled_inference | PASS |
| hf_distilroberta-finetuned-financial-news-sentiment-analysis | compiled_inference | PASS |
| hf_emotion-english-distilroberta-base | compiled_inference | PASS |
| hf_emotion_text_classifier | compiled_inference | PASS |
| hf_english-abusive-MuRIL | compiled_inference | PASS |
| hf_finbert | compiled_inference | PASS |
| hf_finbert-tone | compiled_inference | PASS |
| hf_german-sentiment-bert | compiled_inference | PASS |
| hf_indonesian-roberta-base-sentiment-classifier | compiled_inference | PASS |
| hf_koelectra-small-v3-nsmc | compiled_inference | PASS |
| hf_ms-marco-MiniLM-L-12-v2 | compiled_inference | PASS |
| hf_ms-marco-MiniLM-L-2-v2 | compiled_inference | PASS |
| hf_ms-marco-MiniLM-L-4-v2 | compiled_inference | PASS |
| hf_ms-marco-MiniLM-L-6-v2 | compiled_inference | PASS |
| hf_ms-marco-TinyBERT-L-2-v2 | compiled_inference | PASS |
| hf_ms-marco-electra-base | compiled_inference | PASS |
| hf_raceBERT-ethnicity | compiled_inference | PASS |
| hf_roberta-base-go_emotions | compiled_inference | PASS |
| hf_roberta-base-suicide-prediction-phr | compiled_inference | PASS |
| hf_roberta-large-mnli | compiled_inference | PASS |
| hf_robertuito-sentiment-analysis | compiled_inference | PASS |
| hf_rubert-base-cased-nli-threeway | compiled_inference | PASS |
| hf_rubert-tiny2-russian-sentiment | compiled_inference | PASS |
| hf_stsb-TinyBERT-L-4 | compiled_inference | PASS |
| hf_suicidality | compiled_inference | PASS |
| hf_tamil-codemixed-abusive-MuRIL | compiled_inference | PASS |
| hf_toxic-bert | compiled_inference | PASS |

*... and 58 more improved models*

**Total improved models: 108**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-04/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-05/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 492 | 492 | 0 | ➖ NO CHANGE |
| IREE Compilation | 436 | 436 | 0 | ➖ NO CHANGE |
| Gold Inference | 420 | 420 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 415 | 414 | -1 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 397 | 396 | -1 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 15 | 0 | ➖ NO CHANGE |
| IREE Compilation | 56 | 56 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 6 | +1 | ⚠️ MORE FAILURES |
| Inference Comparison | 18 | 18 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -1 fewer tests passing
- **Inference Comparison (PASS)**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_dragon-multiturn-context-encoder | PASS | compiled_inference |

**Total regressed models: 1**


---

