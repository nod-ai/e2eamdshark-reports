# Copyright 2025 Advanced Micro Devices
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

'''
Checks if the old status of the
model matches with the current status
'''

import json
import sys
from pathlib import Path

MODEL = sys.argv[1]
BASELINE_JSON = Path(sys.argv[2])
CURRENT_JSON = Path(sys.argv[3])

baseline = json.loads(BASELINE_JSON.read_text())
current = json.loads(CURRENT_JSON.read_text())

if MODEL not in baseline:
    print(f"[ERROR] {MODEL} not found in baseline json")
    sys.exit(1)

if MODEL not in current:
    print(f"[ERROR] {MODEL} not found in current run json")
    sys.exit(1)

expected_status = baseline[MODEL]["old_status"]
actual_status = current[MODEL]["exit_status"]

print(f"Model: {MODEL}")
print(f"Expected (old) status: {expected_status}")
print(f"Actual status:         {actual_status}")

if actual_status == expected_status:
    print(f"========= Status Mathces With Old Status for model: {MODEL} =========")
else:
    print(f"========= Status Did Not Match With Old Status for model: {MODEL} =========")
    sys.exit(1)
