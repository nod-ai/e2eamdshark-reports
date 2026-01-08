#!/usr/bin/env bash
set -euo pipefail

echo "================= in ../github-actions/bisect_test.sh ================================"


MODEL="$1"
DEVICE="$2"

rm -rf iree-build/ || true
rm -f "$PWD/../../test-suite/alt_e2eamdshark/X2_regression_bisect.json" || true
BASELINE_JSON="$PWD/../github-actions/model_old_new_status.json"
CURRENT_JSON="$PWD/../../test-suite/alt_e2eamdshark/X2_regression_bisect.json"

echo "Bisect testing model: $MODEL"

# Clean venv per commit
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install numpy

#pip install --upgrade pip
#pip install -r alt_e2eamdshark/base_requirements.txt
#pip install -r alt_e2eamdshark/iree_requirements.txt
#pip install --no-deps -r alt_e2eamdshark/torch_mlir_requirements.txt
#git branch
# Install THIS commit's IREE
# ### TODO:Need To Replace this as we do iree build in amd-shark-ai
git submodule update --init
cmake -G Ninja -B iree-build/ -S . \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DIREE_ENABLE_ASSERTIONS=ON \
       -DIREE_ENABLE_SPLIT_DWARF=ON \
       -DIREE_ENABLE_THIN_ARCHIVES=ON \
       -DCMAKE_C_COMPILER=clang \
       -DIREE_HIP_TEST_TARGET_CHIP= \
       -DCMAKE_CXX_COMPILER=clang++ \
       -DIREE_BUILD_PYTHON_BINDINGS=ON \
       -DIREE_HAL_DRIVER_HIP=ON -DIREE_TARGET_BACKEND_ROCM=ON \
       -DIREE_ENABLE_LLD=ON \
       -DPYTHON3_EXECUTABLE=$(which python3) ; cmake --build iree-build/

export PATH=$PWD/iree-build/tools/:$PATH
export PYTHONPATH=$PWD/iree-build/compiler/bindings/python:$PWD/iree-build/runtime/bindings/python
source iree-build/.env && export PYTHONPATH

cd $PWD/../../test-suite/alt_e2eamdshark
pip install --upgrade pip
pip install -r ./base_requirements.txt

#export CACHE_DIR=/home/yrathore/yv/cache2

if [[ "$DEVICE" == "GPU" ]]; then
  python run.py \
    -r ./test-onnx \
    -t "$MODEL" \
    -b rocm \
    -d hip \
    --mode=cl-onnx-iree \
    --report-file "X2_regression_bisect.md" \
    --cleanup=3 \
    -v \
    --report
else
  python run.py \
    -r ./test-onnx \
    --report \
    -t "$MODEL" \
    -b llvm-cpu \
    -d local-task \
    -c x86_64-linux-gnu \
    --report-file "X2_regression_bisect.md" \
    --mode=cl-onnx-iree \
    --cleanup=3 \
    --get-metadata \
    -v
fi

# Run model (always exits 0)
# for gpu
#python run.py \
#  -r ./test-onnx \
#  -t "$MODEL" \
#  -b rocm \
#  -d hip \
#  --mode=cl-onnx-iree \
#  --report-file "X2_regression_bisect.md" \
#  --cleanup=3 \
#  -v \
#  --report

# for cpu
#python ./run.py \
#            -r ./test-onnx \
#            --report \
#            -t "$MODEL" \
#            -b " llvm-cpu" \
#            -d "local-task" \
#            -c "x86_64-linux-gnu" \
#            --report-file "X2_regression_bisect.md" \
#            --mode=cl-onnx-iree \
#            --cleanup=3 \
#            --get-metadata \
#            -v
#
cd $PWD/../../e2eamdshark-reports/iree
rm -rf iree-build

echo "===================== out ../github-actions/bisect_test.sh  ---> ran run.py ====================="

# Validate result via JSON
python $PWD/../github-actions/check_model_status.py \
  "$MODEL" \
  "$BASELINE_JSON" \
  "$CURRENT_JSON"

