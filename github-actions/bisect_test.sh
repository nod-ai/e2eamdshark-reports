#!/bin/bash
# Copyright 2025 Advanced Micro Devices
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

# Main Logic for Verifying Regression Commit

set -euo pipefail
echo "********** main logic **********"

MODEL="$1"
DEVICE="$2"

rm -rf iree-build/ || true
rm -f "$PWD/../test-suite/alt_e2eamdshark/X_regression_bisect.json" || true
BASELINE_JSON="$PWD/../github-actions/model_old_new_status.json"
CURRENT_JSON="$PWD/../test-suite/alt_e2eamdshark/X_regression_bisect.json"

echo "Bisect testing model: $MODEL on $DEVICE"

source ${ALT_E2E_VENV_DIR}/bin/activate
which python

pip install -f https://iree.dev/pip-release-links.html --upgrade --pre iree-base-compiler iree-base-runtime iree-turbine
pip install -f https://iree.dev/pip-release-links.html --upgrade --pre \
       iree-base-compiler iree-base-runtime --src deps \
       -e "git+https://github.com/iree-org/iree-turbine.git#egg=iree-turbine"
pip uninstall -y iree-base-compiler iree-base-runtime

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
       -DPython3_EXECUTABLE=$(which python3) ; cmake --build iree-build/

export PATH=$PWD/iree-build/tools/:$PATH
export PYTHONPATH=$PWD/iree-build/compiler/bindings/python:$PWD/iree-build/runtime/bindings/python
source iree-build/.env && export PYTHONPATH

cd $PWD/../test-suite/alt_e2eamdshark
pip install -r ./base_requirements.txt
pip install -r ./alt_e2eamdshark/hf_requirements.txt

# run run.py
if [[ "$DEVICE" == "GPU" ]]; then
  python3 run.py \
    -r ./test-onnx \
    -t "$MODEL" \
    -b rocm \
    -d hip \
    --mode=cl-onnx-iree \
    --report-file "X_regression_bisect.md" \
    --cleanup=3 \
    -v \
    --report
else
  python3 run.py \
    -r ./test-onnx \
    --report \
    -t "$MODEL" \
    -b llvm-cpu \
    -d local-task \
    -c x86_64-linux-gnu \
    --report-file "X_regression_bisect.md" \
    --mode=cl-onnx-iree \
    --cleanup=3 \
    --get-metadata \
    -v
fi

cd $PWD/../../iree
rm -rf iree-build

echo "********** Completed running run.py, now checking the current status with the old status **********"

# Validate result via JSON
python3 $PWD/../github-actions/check_model_status.py \
  "$MODEL" \
  "$BASELINE_JSON" \
  "$CURRENT_JSON"
