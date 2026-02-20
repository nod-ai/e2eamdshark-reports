#!/bin/bash
# Copyright 2025 Advanced Micro Devices
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
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



if [ "$BAD_COMMIT_HASH" = "$NEXT_COMMIT_AFTER_BAD" ]; then
    echo "[INFO] First bad commit is immediately after baseline bad commit ($BAD_COMMIT). Skipping CSV update."
else
    echo "$DATE,$MODEL_WITH_DEVICE,$BAD_COMMIT_HASH" >> "$CSV_FILE"
    echo "[INFO] Appended bisect result to CSV -> $DATE -> $MODEL_WITH_DEVICE -> $BAD_COMMIT_HASH"
fi

cat "$CSV_FILE"

git bisect visualize --oneline || true
