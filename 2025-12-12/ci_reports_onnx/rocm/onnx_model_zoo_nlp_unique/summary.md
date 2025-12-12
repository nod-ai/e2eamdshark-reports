## Passing Summary

**TOTAL TESTS = 90**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 0 | 0.0% | 0.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 90**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 90 | 100.0% |
| IREE Compilation | 0 | 0.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/onnx_model_zoo_nlp_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/onnx_model_zoo_nlp_unique.md', get_metadata=True)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| albert_Opset16_transformers | setup | None | |
| albert_Opset17_transformers | setup | None | |
| auto_Opset16_transformers | setup | None | |
| auto_Opset18_transformers | setup | None | |
| bert_Opset16_transformers | setup | None | |
| bert_Opset17_transformers | setup | None | |
| bertlmhead_Opset16_transformers | setup | None | |
| bertlmhead_Opset18_transformers | setup | None | |
| bigbird_Opset16_transformers | setup | None | |
| bigbird_Opset17_transformers | setup | None | |
| blenderbot_Opset16_transformers | setup | None | |
| blenderbot_Opset18_transformers | setup | None | |
| blenderbotsmall_Opset16_transformers | setup | None | |
| blenderbotsmall_Opset17_transformers | setup | None | |
| camembert_Opset16_transformers | setup | None | |
| camembert_Opset18_transformers | setup | None | |
| convbert_Opset16_transformers | setup | None | |
| convbert_Opset17_transformers | setup | None | |
| deberta_Opset17_transformers | setup | None | |
| distilbert_Opset16_transformers | setup | None | |
| distilbert_Opset18_transformers | setup | None | |
| electra_Opset16_transformers | setup | None | |
| electra_Opset17_transformers | setup | None | |
| encoderdecoder_Opset17_transformers | setup | None | |
| ernie_Opset16_transformers | setup | None | |
| ernie_Opset17_transformers | setup | None | |
| ernie_Opset18_transformers | setup | None | |
| erniem_Opset16_transformers | setup | None | |
| erniem_Opset18_transformers | setup | None | |
| esm_Opset16_transformers | setup | None | |
| esm_Opset17_transformers | setup | None | |
| flaubert_Opset16_transformers | setup | None | |
| flaubert_Opset17_transformers | setup | None | |
| flaubertwithlmhead_Opset16_transformers | setup | None | |
| flaubertwithlmhead_Opset17_transformers | setup | None | |
| flaubertwithlmhead_Opset18_transformers | setup | None | |
| ibert_Opset17_transformers | setup | None | |
| longt5_Opset17_transformers | setup | None | |
| longt5encoder_Opset16_transformers | setup | None | |
| luke_Opset16_transformers | setup | None | |
| luke_Opset18_transformers | setup | None | |
| m2m100_Opset16_transformers | setup | None | |
| m2m100_Opset17_transformers | setup | None | |
| m2m100_Opset18_transformers | setup | None | |
| marian_Opset16_transformers | setup | None | |
| marian_Opset18_transformers | setup | None | |
| markuplm_Opset16_transformers | setup | None | |
| markuplm_Opset18_transformers | setup | None | |
| mobilebert_Opset18_transformers | setup | None | |
| mpnet_Opset16_transformers | setup | None | |
| mpnet_Opset18_transformers | setup | None | |
| mra_Opset16_transformers | setup | None | |
| mra_Opset18_transformers | setup | None | |
| mt5_Opset16_transformers | setup | None | |
| mt5encoder_Opset17_transformers | setup | None | |
| nezha_Opset16_transformers | setup | None | |
| nezha_Opset18_transformers | setup | None | |
| nystromformer_Opset16_transformers | setup | None | |
| nystromformer_Opset18_transformers | setup | None | |
| opt_Opset16_transformers | setup | None | |
| opt_Opset18_transformers | setup | None | |
| prophetnet_Opset16_transformers | setup | None | |
| prophetnet_Opset18_transformers | setup | None | |
| roberta_Opset16_transformers | setup | None | |
| roberta_Opset18_transformers | setup | None | |
| robertaprelayernorm_Opset16_transformers | setup | None | |
| robertaprelayernorm_Opset18_transformers | setup | None | |
| rocbert_Opset16_transformers | setup | None | |
| rocbert_Opset17_transformers | setup | None | |
| roformer_Opset16_transformers | setup | None | |
| roformer_Opset17_transformers | setup | None | |
| splinter_Opset16_transformers | setup | None | |
| splinter_Opset18_transformers | setup | None | |
| squeezebert_Opset16_transformers | setup | None | |
| squeezebert_Opset18_transformers | setup | None | |
| switchtransformersencoder_Opset16_transformers | setup | None | |
| t5_Opset17_transformers | setup | None | |
| t5encoder_Opset16_transformers | setup | None | |
| umt5_Opset16_transformers | setup | None | |
| umt5encoder_Opset16_transformers | setup | None | |
| xlmroberta_Opset16_transformers | setup | None | |
| xlmroberta_Opset17_transformers | setup | None | |
| xlnet_Opset16_transformers | setup | None | |
| xlnet_Opset18_transformers | setup | None | |
| xlnetlmhead_Opset16_transformers | setup | None | |
| xlnetlmhead_Opset18_transformers | setup | None | |
| xmod_Opset16_transformers | setup | None | |
| xmod_Opset17_transformers | setup | None | |
| yoso_Opset16_transformers | setup | None | |
| yoso_Opset18_transformers | setup | None | |
