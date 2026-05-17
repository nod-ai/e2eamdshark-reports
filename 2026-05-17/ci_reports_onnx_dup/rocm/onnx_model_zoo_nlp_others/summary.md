## Passing Summary

**TOTAL TESTS = 49**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 49 | 100.0% | 100.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 49**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 49 | 100.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/onnx_model_zoo_nlp_others.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/onnx_model_zoo_nlp_others.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| albert_Opset18_transformers | compilation | None | |
| auto_Opset17_transformers | compilation | None | |
| bert_Opset18_transformers | compilation | None | |
| bertlmhead_Opset17_transformers | compilation | None | |
| bigbird_Opset18_transformers | compilation | None | |
| blenderbot_Opset17_transformers | compilation | None | |
| blenderbotsmall_Opset18_transformers | compilation | None | |
| camembert_Opset17_transformers | compilation | None | |
| convbert_Opset18_transformers | compilation | None | |
| deberta_Opset16_transformers | compilation | None | |
| distilbert_Opset17_transformers | compilation | None | |
| electra_Opset18_transformers | compilation | None | |
| encoderdecoder_Opset18_transformers | compilation | None | |
| erniem_Opset17_transformers | compilation | None | |
| esm_Opset18_transformers | compilation | None | |
| flaubert_Opset18_transformers | compilation | None | |
| funnelbase_Opset17_transformers | compilation | None | |
| ibert_Opset16_transformers | compilation | None | |
| longt5_Opset16_transformers | compilation | None | |
| longt5encoder_Opset17_transformers | compilation | None | |
| luke_Opset17_transformers | compilation | None | |
| marian_Opset17_transformers | compilation | None | |
| markuplm_Opset17_transformers | compilation | None | |
| mobilebert_Opset16_transformers | compilation | None | |
| mobilebert_Opset17_transformers | compilation | None | |
| mpnet_Opset17_transformers | compilation | None | |
| mra_Opset17_transformers | compilation | None | |
| mt5_Opset17_transformers | compilation | None | |
| mt5encoder_Opset16_transformers | compilation | None | |
| nezha_Opset17_transformers | compilation | None | |
| nystromformer_Opset17_transformers | compilation | None | |
| opt_Opset17_transformers | compilation | None | |
| prophetnet_Opset17_transformers | compilation | None | |
| roberta_Opset17_transformers | compilation | None | |
| robertaprelayernorm_Opset17_transformers | compilation | None | |
| rocbert_Opset18_transformers | compilation | None | |
| roformer_Opset18_transformers | compilation | None | |
| splinter_Opset17_transformers | compilation | None | |
| squeezebert_Opset17_transformers | compilation | None | |
| switchtransformersencoder_Opset17_transformers | compilation | None | |
| t5_Opset16_transformers | compilation | None | |
| t5encoder_Opset17_transformers | compilation | None | |
| umt5_Opset17_transformers | compilation | None | |
| umt5encoder_Opset17_transformers | compilation | None | |
| xlmroberta_Opset18_transformers | compilation | None | |
| xlnet_Opset17_transformers | compilation | None | |
| xlnetlmhead_Opset17_transformers | compilation | None | |
| xmod_Opset18_transformers | compilation | None | |
| yoso_Opset17_transformers | compilation | None | |
