## Passing Summary

**TOTAL TESTS = 32**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 27 | 84.4% | 84.4% |
| IREE Compilation | 14 | 43.8% | 51.9% |
| Gold Inference | 14 | 43.8% | 100.0% |
| IREE Inference Invocation | 13 | 40.6% | 92.9% |
| Inference Comparison (PASS) | 13 | 40.6% | 100.0% |
## Fail Summary

**TOTAL TESTS = 32**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 5 | 15.6% |
| IREE Compilation | 13 | 40.6% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 1 | 3.1% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='hip', backend='rocm', target_chip='gfx942', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-text-generation-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-text-generation-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_distilgpt2 | PASS | None | |
| hf_gpt2 | PASS | None | |
| hf_gpt2-small-spanish | PASS | None | |
| hf_llama-68m | compilation | None | |
| hf_llama-7b | compilation | None | |
| hf_Llama3-8B-1.58-100B-tokens-GGUF | setup | None | |
| hf_Meta-Llama-3.1-8B-Instruct-AWQ-INT4 | setup | None | |
| hf_Meta-Llama-3.1-8B-Instruct-bnb-4bit | setup | None | |
| hf_Midnight-Miqu-70B-v1.5-4bit | setup | None | |
| hf_Mistral-7B-Instruct-v0.2-GPTQ | setup | None | |
| hf_oasst-sft-4-pythia-12b-epoch-3.5 | compilation | None | |
| hf_opt-125m | PASS | None | |
| hf_Phi-3-mini-128k-instruct | PASS | None | |
| hf_Phi-3-mini-4k-instruct | PASS | None | |
| hf_Phi-3.5-mini-instruct | PASS | None | |
| hf_Qwen1.5-0.5B-Chat | compilation | None | |
| hf_Qwen2-0.5B | compilation | None | |
| hf_Qwen2-7B-Instruct | compilation | None | |
| hf_Qwen2.5-0.5B-Instruct | compilation | None | |
| hf_Qwen2.5-1.5B-Instruct | compilation | None | |
| hf_Qwen2.5-7B-Instruct | compilation | None | |
| hf_really-tiny-falcon-testing | PASS | None | |
| hf_StableBeluga2 | import_model | None | |
| hf_tiny-dummy-qwen2 | PASS | None | |
| hf_tiny-Qwen2ForCausalLM-2.5 | PASS | None | |
| hf_tiny-random-GemmaForCausalLM | compiled_inference | None | |
| hf_tiny-random-LlamaForCausalLM | PASS | None | |
| hf_tiny-random-mistral | PASS | None | |
| hf_tiny-random-Phi3ForCausalLM | PASS | None | |
| hf_TinyLlama-1.1B-Chat-v1.0 | compilation | None | |
| hf_vicuna-7b-v1.5 | compilation | None | |
| hf_zephyr-7b-beta | compilation | None | |
