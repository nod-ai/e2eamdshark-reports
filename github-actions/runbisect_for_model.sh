#!/usr/bin/env bash
set -euo pipefail

MODEL="$1"
GOOD_COMMIT="$2"
BAD_COMMIT="$3"

git bisect reset || true
git bisect start
git bisect bad "$BAD_COMMIT"
git bisect good "$GOOD_COMMIT"

git bisect run ./github-actions/bisect_test.sh "$MODEL"

echo "First bad commit for $MODEL:"
git bisect log
git bisect visualize --oneline || true
