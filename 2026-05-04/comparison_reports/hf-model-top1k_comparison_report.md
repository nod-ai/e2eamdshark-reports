---
# Test Comparison Report

*Generated on: 2026-05-04*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-04/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-04/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 286 | 415 | +129 |
| Inference Comparison (PASS) | 272 | 397 | +125 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 15 | +1 |
| IREE Compilation | 59 | 56 | -3 |
| Gold Inference | 16 | 16 | 0 |
| IREE Inference Invocation | 132 | 5 | -127 |
| Inference Comparison | 14 | 18 | +4 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-02/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-04/hf-model-top1k/rocm/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 352 | 286 | -66 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 336 | 272 | -64 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 59 | 59 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 66 | 132 | +66 | ⚠️ MORE FAILURES |
| Inference Comparison | 16 | 14 | -2 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -66 fewer tests passing
- **Inference Comparison (PASS)**: -64 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_face-parsing | PASS | compiled_inference |
| hf_segformer-b0-finetuned-ade-512-512 | PASS | compiled_inference |
| hf_segformer-b0-finetuned-cityscapes-1024-1024 | PASS | compiled_inference |
| hf_segformer-b0-finetuned-cityscapes-512-1024 | PASS | compiled_inference |
| hf_segformer-b1-finetuned-ade-512-512 | PASS | compiled_inference |
| hf_segformer-b1-finetuned-cityscapes-1024-1024 | PASS | compiled_inference |
| hf_segformer-b2-fashion | PASS | compiled_inference |
| hf_segformer-b2-finetuned-ade-512-512 | PASS | compiled_inference |
| hf_segformer-b2-finetuned-cityscapes-1024-1024 | PASS | compiled_inference |
| hf_segformer-b3-fashion | PASS | compiled_inference |
| hf_segformer-b3-finetuned-ade-512-512 | PASS | compiled_inference |
| hf_segformer-b3-finetuned-cityscapes-1024-1024 | PASS | compiled_inference |
| hf_segformer-b4-finetuned-ade-512-512 | PASS | compiled_inference |
| hf_segformer-b4-finetuned-cityscapes-1024-1024 | PASS | compiled_inference |
| hf_segformer-b5-finetuned-ade-640-640 | PASS | compiled_inference |
| hf_segformer-b5-finetuned-cityscapes-1024-1024 | PASS | compiled_inference |
| hf_segformer_b2_clothes | PASS | compiled_inference |
| hf_segformer_b3_clothes | PASS | compiled_inference |
| hf_segformer_for_optic_disc_cup_segmentation | PASS | compiled_inference |
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

*... and 77 more regressed models*

**Total regressed models: 127**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_UL_base_classification | compiled_inference | PASS |
| hf_beit-base-patch16-224-pt22k | compiled_inference | PASS |
| hf_beit-base-patch16-224-pt22k-ft22k | compiled_inference | PASS |
| hf_beit_base_patch16_224.in22k_ft_in22k_in1k | compiled_inference | PASS |
| hf_beitv2_base_patch16_224.in1k_ft_in22k | compiled_inference | PASS |
| hf_convnext_base.fb_in22k_ft_in1k | compiled_inference | PASS |
| hf_convnext_large_mlp.clip_laion2b_soup_ft_in12k_in1k_320 | compiled_inference | PASS |
| hf_convnextv2_base.fcmae_ft_in22k_in1k | compiled_inference | PASS |
| hf_cspdarknet53.ra_in1k | compiled_inference | PASS |
| hf_deit-base-patch16-224 | compiled_inference | PASS |
| hf_deit-tiny-patch16-224 | compiled_inference | PASS |
| hf_deit_base_distilled_patch16_224.fb_in1k | compiled_inference | PASS |
| hf_densenet121.ra_in1k | compiled_inference | PASS |
| hf_efficientnet_b0.ra_in1k | compiled_inference | PASS |
| hf_efficientnet_b3.ra2_in1k | compiled_inference | PASS |
| hf_efficientnet_b4.ra2_in1k | compiled_inference | PASS |
| hf_ese_vovnet19b_dw.ra_in1k | compiled_inference | PASS |
| hf_gender-classification | compiled_inference | PASS |
| hf_hrnet_w18.ms_aug_in1k | compiled_inference | PASS |
| hf_inception_resnet_v2.tf_in1k | compiled_inference | PASS |
| hf_inception_v3.tf_adv_in1k | compiled_inference | PASS |
| hf_inception_v3.tv_in1k | compiled_inference | PASS |
| hf_lcnet_050.ra2_in1k | compiled_inference | PASS |
| hf_mit-b0 | compiled_inference | PASS |
| hf_mit-b5 | compiled_inference | PASS |
| hf_mobilenet_v2_1.0_224 | compiled_inference | PASS |
| hf_mobilenetv2_100.ra_in1k | compiled_inference | PASS |
| hf_mobilenetv3_large_100.miil_in21k_ft_in1k | compiled_inference | PASS |
| hf_mobilenetv3_large_100.ra_in1k | compiled_inference | PASS |
| hf_nfnet_l0.ra2_in1k | compiled_inference | PASS |
| hf_nsfw-classifier | compiled_inference | PASS |
| hf_nsfw_image_detection | compiled_inference | PASS |
| hf_pedestrian_gender_recognition | compiled_inference | PASS |
| hf_regnety_002.pycls_in1k | compiled_inference | PASS |
| hf_resnet-18 | compiled_inference | PASS |
| hf_resnet-50 | compiled_inference | PASS |
| hf_resnet101.a1h_in1k | compiled_inference | PASS |
| hf_resnet18.a1_in1k | compiled_inference | PASS |
| hf_resnet34.a1_in1k | compiled_inference | PASS |
| hf_resnet50.a1_in1k | compiled_inference | PASS |
| hf_resnext50_32x4d.fb_swsl_ig1b_ft_in1k | compiled_inference | PASS |
| hf_tf_efficientnet_b0.ns_jft_in1k | compiled_inference | PASS |
| hf_tf_efficientnetv2_s.in21k | compiled_inference | PASS |
| hf_tf_mobilenetv3_large_minimal_100.in1k | compiled_inference | PASS |
| hf_tf_mobilenetv3_small_minimal_100.in1k | compiled_inference | PASS |
| hf_vgg16.tv_in1k | compiled_inference | PASS |
| hf_vgg19.tv_in1k | compiled_inference | PASS |
| hf_vit-age-classifier | compiled_inference | PASS |
| hf_vit-base-patch16-224 | compiled_inference | PASS |
| hf_vit-base-uppercase-english-characters | compiled_inference | PASS |

*... and 13 more improved models*

**Total improved models: 63**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-02/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-04/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 492 | 492 | 0 | ➖ NO CHANGE |
| IREE Compilation | 420 | 436 | +16 | ✅ IMPROVED |
| Gold Inference | 404 | 420 | +16 | ✅ IMPROVED |
| IREE Inference Invocation | 399 | 415 | +16 | ✅ IMPROVED |
| Inference Comparison (PASS) | 397 | 397 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 15 | 0 | ➖ NO CHANGE |
| IREE Compilation | 72 | 56 | -16 | ✅ FEWER FAILURES |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 5 | 0 | ➖ NO CHANGE |
| Inference Comparison | 2 | 18 | +16 | ⚠️ MORE FAILURES |

## Summary

### ✅ Improvements

- **IREE Compilation**: +16 more tests passing
- **Gold Inference**: +16 more tests passing
- **IREE Inference Invocation**: +16 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_kda-albert-xxlarge-v2-race | PASS | compiled_inference |

**Total regressed models: 1**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_bert-base-cased | compiled_inference | PASS |

**Total improved models: 1**


---

