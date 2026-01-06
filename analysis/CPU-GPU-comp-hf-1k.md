# CPU vs ROCm — Status Mismatches Only

| Test | CPU Exit Status | GPU Exit Status |
|------|-----------------|-----------------|
| hf_legal-bert-base-uncased | setup | PASS |
| hf_convnext_base.fb_in22k_ft_in1k | PASS | compilation |
| hf_convnext_large_mlp.clip_laion2b_soup_ft_in12k_in1k_320 | PASS | compilation |
| hf_convnextv2_base.fcmae_ft_in22k_in1k | PASS | compilation |
| hf_efficientnet_b0.ra_in1k | PASS | Numerics |
| hf_efficientnet_b3.ra2_in1k | PASS | Numerics |
| hf_efficientnet_b4.ra2_in1k | PASS | Numerics |
| hf_resnet50.a1_in1k | PASS | Numerics |
| hf_tf_efficientnet_b0.ns_jft_in1k | PASS | Numerics |
| hf_detr-layout-detection | Numerics | compilation |
| hf_detr-resnet-50-panoptic | Numerics | compilation |
| hf_kda-albert-xxlarge-v2-race | compiled_inference | PASS |
| hf_mobilebert-uncased-squad-v2 | compiled_inference | compilation |
