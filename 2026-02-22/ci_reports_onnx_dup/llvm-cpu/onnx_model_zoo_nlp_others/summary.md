## Passing Summary

**TOTAL TESTS = 49**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 49 | 100.0% | 100.0% |
| IREE Compilation | 48 | 98.0% | 98.0% |
| Gold Inference | 48 | 98.0% | 100.0% |
| IREE Inference Invocation | 48 | 98.0% | 100.0% |
| Inference Comparison (PASS) | 42 | 85.7% | 87.5% |
## Fail Summary

**TOTAL TESTS = 49**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 0 | 0.0% |
| IREE Compilation | 1 | 2.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 6 | 12.2% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/onnx_model_zoo_nlp_others.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/onnx_model_zoo_nlp_others.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| albert_Opset18_transformers | PASS | None | |
| auto_Opset17_transformers | PASS | None | |
| bert_Opset18_transformers | PASS | None | |
| bertlmhead_Opset17_transformers | PASS | None | |
| bigbird_Opset18_transformers | PASS | None | |
| blenderbot_Opset17_transformers | PASS | None | |
| blenderbotsmall_Opset18_transformers | PASS | None | |
| camembert_Opset17_transformers | PASS | None | |
| convbert_Opset18_transformers | PASS | None | |
| deberta_Opset16_transformers | PASS | None | |
| distilbert_Opset17_transformers | PASS | None | |
| electra_Opset18_transformers | PASS | None | |
| encoderdecoder_Opset18_transformers | PASS | None | |
| erniem_Opset17_transformers | PASS | None | |
| esm_Opset18_transformers | PASS | None | |
| flaubert_Opset18_transformers | Numerics | None | |
| funnelbase_Opset17_transformers | compilation | None | |
| ibert_Opset16_transformers | PASS | None | |
| longt5_Opset16_transformers | PASS | None | |
| longt5encoder_Opset17_transformers | PASS | None | |
| luke_Opset17_transformers | PASS | None | |
| marian_Opset17_transformers | PASS | None | |
| markuplm_Opset17_transformers | PASS | None | |
| mobilebert_Opset16_transformers | Numerics | None | |
| mobilebert_Opset17_transformers | Numerics | None | |
| mpnet_Opset17_transformers | PASS | None | |
| mra_Opset17_transformers | PASS | None | |
| mt5_Opset17_transformers | Numerics | None | |
| mt5encoder_Opset16_transformers | PASS | None | |
| nezha_Opset17_transformers | PASS | None | |
| nystromformer_Opset17_transformers | PASS | None | |
| opt_Opset17_transformers | PASS | None | |
| prophetnet_Opset17_transformers | PASS | None | |
| roberta_Opset17_transformers | PASS | None | |
| robertaprelayernorm_Opset17_transformers | PASS | None | |
| rocbert_Opset18_transformers | PASS | None | |
| roformer_Opset18_transformers | PASS | None | |
| splinter_Opset17_transformers | PASS | None | |
| squeezebert_Opset17_transformers | PASS | None | |
| switchtransformersencoder_Opset17_transformers | PASS | None | |
| t5_Opset16_transformers | Numerics | None | |
| t5encoder_Opset17_transformers | PASS | None | |
| umt5_Opset17_transformers | Numerics | None | |
| umt5encoder_Opset17_transformers | PASS | None | |
| xlmroberta_Opset18_transformers | PASS | None | |
| xlnet_Opset17_transformers | PASS | None | |
| xlnetlmhead_Opset17_transformers | PASS | None | |
| xmod_Opset18_transformers | PASS | None | |
| yoso_Opset17_transformers | PASS | None | |
