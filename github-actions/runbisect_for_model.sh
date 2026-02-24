# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

'''
Bisecting Starts Here.
'''

MODEL="$1"
GOOD_COMMIT="$2"
BAD_COMMIT="$3"
DEVICE="$4"
MODE="${5:-}"
NEXT_COMMIT_AFTER_BAD=$(git rev-list --reverse "${GOOD_COMMIT}..HEAD" | head -n 1)
MODEL_WITH_DEVICE="${MODEL}(${DEVICE})"

if [[ "$DEVICE" == "GPU" ]]; then
    export CACHE_DIR="/home/runner/data/e2eamdshark/amdshark-test-suite-models-cache"
else
    export CACHE_DIR="/home/runner/groups/aig_amdsharks/test-suite-ci-cache"
fi

# Append the information to a CSV file
CSV_FILE="$PWD/../track_test_data/bisect_results_${DEVICE}.csv"
if [[ "$MODE" == "HF" ]]; then
  CSV_FILE="$PWD/../track_test_data/bisect_results_${DEVICE}_HF.csv"
fi

if [[ "$MODE" == "DUP" ]]; then
  CSV_FILE="$PWD/../track_test_data/bisect_results_${DEVICE}_DUP.csv"
fi

if [ ! -f "$CSV_FILE" ]; then
    echo "Date,Model,First Bad Commit" > "$CSV_FILE"
fi

git bisect reset || true
git bisect start
git bisect bad "$BAD_COMMIT"
git bisect good "$GOOD_COMMIT"

git bisect run $PWD/../github-actions/bisect_test.sh "$MODEL" "$DEVICE" "$CSV_FILE"

echo "First bad commit for $MODEL:"
BAD_COMMIT_HASH=$(git bisect log | grep '^# first bad commit' | awk '{print $5}')
DATE=$(date "+%Y-%m-%d")

# Recheck if actual regression
python -m venv venv
source venv/bin/activate

pip install -r $PWD/../test-suite/alt_e2eamdshark/base_requirements.txt
pip install -r $PWD/../test-suite/alt_e2eamdshark/hf_requirements.txt
pip install -r $PWD/../test-suite/alt_e2eamdshark/iree_requirements.txt
pip install --no-deps -r $PWD/../test-suite/alt_e2eamdshark/torch_mlir_requirements.txt
pip install --pre --upgrade iree-base-compiler iree-base-runtime -f https://iree.dev/pip-release-links.html

# Build IREE and verify that the bad commit is actually a regression
echo "********** Verifying bisect result by rebuilding IREE and re-running the model **********"

BASELINE_JSON="$PWD/../github-actions/model_old_new_status.json"
CURRENT_JSON="$PWD/../test-suite/alt_e2eamdshark/X_regression_bisect.json"

rm -rf iree-build/ || true
rm -f "$CURRENT_JSON" || true

pip install -f https://iree.dev/pip-release-links.html --upgrade --pre iree-turbine
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
pip install -r ./hf_requirements.txt

# Run the model to verify
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

echo "********** Completed verification, checking current status with old status **********"

# Validate that the bisect result is correct
python3 $PWD/../github-actions/check_model_status.py \
  "$MODEL" \
  "$BASELINE_JSON" \
  "$CURRENT_JSON" \
  "$CSV_FILE"

VERIFICATION_RESULT=$?
if [ $VERIFICATION_RESULT -eq 0 ]; then
    echo "[INFO] Verification PASSED: Current status matches old status (good commit behavior)"
    echo "[INFO] The bisect result is confirmed - commit $BAD_COMMIT_HASH is the first bad commit"
else
    echo "[WARNING] Verification FAILED: Current status does NOT match old status"
    echo "[WARNING] The model may still be broken at HEAD, bisect result may need review"
fi

if [ "$BAD_COMMIT_HASH" = "$NEXT_COMMIT_AFTER_BAD" ]; then
    echo "[INFO] First bad commit is immediately after baseline bad commit ($BAD_COMMIT). Skipping CSV update."
else
    echo "$DATE,$MODEL_WITH_DEVICE,$BAD_COMMIT_HASH" >> "$CSV_FILE"
    echo "[INFO] Appended bisect result to CSV -> $DATE -> $MODEL_WITH_DEVICE -> $BAD_COMMIT_HASH"
fi

cat "$CSV_FILE"

git bisect visualize --oneline || true
