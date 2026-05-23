## Passing Summary

**TOTAL TESTS = 90**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 90 | 100.0% | 100.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 90**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 90 | 100.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/onnx_model_zoo_nlp_unique.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/onnx_model_zoo_nlp_unique.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| albert_Opset16_transformers | compilation | None | |
| albert_Opset17_transformers | compilation | None | |
| auto_Opset16_transformers | compilation | None | |
| auto_Opset18_transformers | compilation | None | |
| bert_Opset16_transformers | compilation | None | |
| bert_Opset17_transformers | compilation | None | |
| bertlmhead_Opset16_transformers | compilation | None | |
| bertlmhead_Opset18_transformers | compilation | None | |
| bigbird_Opset16_transformers | compilation | None | |
| bigbird_Opset17_transformers | compilation | None | |
| blenderbot_Opset16_transformers | compilation | None | |
| blenderbot_Opset18_transformers | compilation | None | |
| blenderbotsmall_Opset16_transformers | compilation | None | |
| blenderbotsmall_Opset17_transformers | compilation | None | |
| camembert_Opset16_transformers | compilation | None | |
| camembert_Opset18_transformers | compilation | None | |
| convbert_Opset16_transformers | compilation | None | |
| convbert_Opset17_transformers | compilation | None | |
| deberta_Opset17_transformers | compilation | None | |
| distilbert_Opset16_transformers | compilation | None | |
| distilbert_Opset18_transformers | compilation | None | |
| electra_Opset16_transformers | compilation | None | |
| electra_Opset17_transformers | compilation | None | |
| encoderdecoder_Opset17_transformers | compilation | None | |
| ernie_Opset16_transformers | compilation | None | |
| ernie_Opset17_transformers | compilation | None | |
| ernie_Opset18_transformers | compilation | None | |
| erniem_Opset16_transformers | compilation | None | |
| erniem_Opset18_transformers | compilation | None | |
| esm_Opset16_transformers | compilation | None | |
| esm_Opset17_transformers | compilation | None | |
| flaubert_Opset16_transformers | compilation | None | |
| flaubert_Opset17_transformers | compilation | None | |
| flaubertwithlmhead_Opset16_transformers | compilation | None | |
| flaubertwithlmhead_Opset17_transformers | compilation | None | |
| flaubertwithlmhead_Opset18_transformers | compilation | None | |
| ibert_Opset17_transformers | compilation | None | |
| longt5_Opset17_transformers | compilation | None | |
| longt5encoder_Opset16_transformers | compilation | None | |
| luke_Opset16_transformers | compilation | None | |
| luke_Opset18_transformers | compilation | None | |
| m2m100_Opset16_transformers | compilation | None | |
| m2m100_Opset17_transformers | compilation | None | |
| m2m100_Opset18_transformers | compilation | None | |
| marian_Opset16_transformers | compilation | None | |
| marian_Opset18_transformers | compilation | None | |
| markuplm_Opset16_transformers | compilation | None | |
| markuplm_Opset18_transformers | compilation | None | |
| mobilebert_Opset18_transformers | compilation | None | |
| mpnet_Opset16_transformers | compilation | None | |
| mpnet_Opset18_transformers | compilation | None | |
| mra_Opset16_transformers | compilation | None | |
| mra_Opset18_transformers | compilation | None | |
| mt5_Opset16_transformers | compilation | None | |
| mt5encoder_Opset17_transformers | compilation | None | |
| nezha_Opset16_transformers | compilation | None | |
| nezha_Opset18_transformers | compilation | None | |
| nystromformer_Opset16_transformers | compilation | None | |
| nystromformer_Opset18_transformers | compilation | None | |
| opt_Opset16_transformers | compilation | None | |
| opt_Opset18_transformers | compilation | None | |
| prophetnet_Opset16_transformers | compilation | None | |
| prophetnet_Opset18_transformers | compilation | None | |
| roberta_Opset16_transformers | compilation | None | |
| roberta_Opset18_transformers | compilation | None | |
| robertaprelayernorm_Opset16_transformers | compilation | None | |
| robertaprelayernorm_Opset18_transformers | compilation | None | |
| rocbert_Opset16_transformers | compilation | None | |
| rocbert_Opset17_transformers | compilation | None | |
| roformer_Opset16_transformers | compilation | None | |
| roformer_Opset17_transformers | compilation | None | |
| splinter_Opset16_transformers | compilation | None | |
| splinter_Opset18_transformers | compilation | None | |
| squeezebert_Opset16_transformers | compilation | None | |
| squeezebert_Opset18_transformers | compilation | None | |
| switchtransformersencoder_Opset16_transformers | compilation | None | |
| t5_Opset17_transformers | compilation | None | |
| t5encoder_Opset16_transformers | compilation | None | |
| umt5_Opset16_transformers | compilation | None | |
| umt5encoder_Opset16_transformers | compilation | None | |
| xlmroberta_Opset16_transformers | compilation | None | |
| xlmroberta_Opset17_transformers | compilation | None | |
| xlnet_Opset16_transformers | compilation | None | |
| xlnet_Opset18_transformers | compilation | None | |
| xlnetlmhead_Opset16_transformers | compilation | None | |
| xlnetlmhead_Opset18_transformers | compilation | None | |
| xmod_Opset16_transformers | compilation | None | |
| xmod_Opset17_transformers | compilation | None | |
| yoso_Opset16_transformers | compilation | None | |
| yoso_Opset18_transformers | compilation | None | |
