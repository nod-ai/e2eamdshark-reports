from pathlib import Path
import re
import sys
import json

out_path = Path("model_old_new_status.json")
md_path = Path(sys.argv[1])
text = md_path.read_text()

match = re.search(
    r"##\s+\d+\s+Regressions Found:\n"
    r"\|model name\|old_status\|new_status\|\n"
    r"\|---\|---\|---\|\n"
    r"((?:\|.*\|\n)+)",
    text,
)

if not match:
    print("No regressions found section")
    sys.exit(0)

rows = match.group(1).strip().splitlines()

# Dictionary: model -> {old_status, new_status}
regressions = {}

for row in rows:
    cols = [c.strip() for c in row.strip("|").split("|")]
    if len(cols) != 3:
        continue

    model, old_status, new_status = cols
    regressions[model] = {
        "old_status": old_status,
        "new_status": new_status,
    }
with out_path.open("w") as f:
    json.dump(regressions, f, indent=2)

print(f"Wrote {len(regressions)} regressions to {out_path}")

for model, statuses in regressions.items():
    print(f"{model}: {statuses}")

