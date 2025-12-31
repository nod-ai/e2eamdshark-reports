## Passing Summary

**TOTAL TESTS = 32**
|Stage|# Passing|% of Total|% of Attempted|
|--|--|--|--|
| Setup | 0 | 0.0% | 0.0% |
| IREE Compilation | 0 | 0.0% | 0.0% |
| Gold Inference | 0 | 0.0% | 0.0% |
| IREE Inference Invocation | 0 | 0.0% | 0.0% |
| Inference Comparison (PASS) | 0 | 0.0% | 0.0% |
## Fail Summary

**TOTAL TESTS = 32**
|Stage|# Failed at Stage|% of Total|
|--|--|--|
| Setup | 32 | 100.0% |
| IREE Compilation | 0 | 0.0% |
| Gold Inference | 0 | 0.0% |
| IREE Inference Invocation | 0 | 0.0% |
| Inference Comparison | 0 | 0.0% |
## Test Run Detail
Test was run with the following arguments:
Namespace(device='local-task', backend='llvm-cpu', target_chip='x86_64-linux-gnu', iree_compile_args=None, mode='cl-onnx-iree', torchtolinalg=False, stages=None, skip_stages=None, benchmark=False, load_inputs=False, groups='all', test_filter=None, testsfile='onnx_tests/models/external_lists/hf-model-shards/hf-text-generation-shard.txt', tolerance=None, verbose=True, rundirectory='./test-onnx', no_artifacts=False, cleanup='3', report=True, report_file='reports/hf-text-generation-shard.md', get_metadata=True, dump_data_as_npy=False)

| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|--|--|--|--|
| hf_distilgpt2 | setup | None | |
| hf_gpt2 | setup | None | |
| hf_gpt2-small-spanish | setup | None | |
| hf_llama-68m | setup | None | |
| hf_llama-7b | setup | None | |
| hf_Llama3-8B-1.58-100B-tokens-GGUF | setup | None | |
| hf_Meta-Llama-3.1-8B-Instruct-AWQ-INT4 | setup | None | |
| hf_Meta-Llama-3.1-8B-Instruct-bnb-4bit | setup | None | |
| hf_Midnight-Miqu-70B-v1.5-4bit | setup | None | |
| hf_Mistral-7B-Instruct-v0.2-GPTQ | setup | None | |
| hf_oasst-sft-4-pythia-12b-epoch-3.5 | setup | None | |
| hf_opt-125m | setup | None | |
| hf_Phi-3-mini-128k-instruct | setup | None | |
| hf_Phi-3-mini-4k-instruct | setup | None | |
| hf_Phi-3.5-mini-instruct | setup | None | |
| hf_Qwen1.5-0.5B-Chat | setup | None | |
| hf_Qwen2-0.5B | setup | None | |
| hf_Qwen2-7B-Instruct | setup | None | |
| hf_Qwen2.5-0.5B-Instruct | setup | None | |
| hf_Qwen2.5-1.5B-Instruct | setup | None | |
| hf_Qwen2.5-7B-Instruct | setup | None | |
| hf_really-tiny-falcon-testing | setup | None | |
| hf_StableBeluga2 | setup | None | |
| hf_tiny-dummy-qwen2 | setup | None | |
| hf_tiny-Qwen2ForCausalLM-2.5 | setup | None | |
| hf_tiny-random-GemmaForCausalLM | setup | None | |
| hf_tiny-random-LlamaForCausalLM | setup | None | |
| hf_tiny-random-mistral | setup | None | |
| hf_tiny-random-Phi3ForCausalLM | setup | None | |
| hf_TinyLlama-1.1B-Chat-v1.0 | setup | None | |
| hf_vicuna-7b-v1.5 | setup | None | |
| hf_zephyr-7b-beta | setup | None | |
