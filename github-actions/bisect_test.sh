#!/usr/bin/env bash
set -euo pipefail

MODEL="$1"

BASELINE_JSON="model_old_new_status.json"
CURRENT_JSON="X2_regression_bisect.json"

echo "Bisect testing model: $MODEL"

# Clean venv per commit
rm -rf .venv
python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r alt_e2eamdshark/base_requirements.txt
pip install -r alt_e2eamdshark/iree_requirements.txt
pip install --no-deps -r alt_e2eamdshark/torch_mlir_requirements.txt

# Install THIS commit's IREE
# ### TODO:Need To Replace this as we do iree build in amd-shark-ai
pip install -e compiler
pip install -e runtime

cd alt_e2eamdshark

# Run model (always exits 0)
python run.py \
  -r ./test-onnx \
  --tests "$MODEL" \
  -b migraphx \
  -d rocm \
  --mode=cl-onnx-iree \
  --cleanup=3 \
  -v

# Validate result via JSON
python ../github-actions/check_model_status.py \
  "$MODEL" \
  "$BASELINE_JSON" \
  "$CURRENT_JSON"

