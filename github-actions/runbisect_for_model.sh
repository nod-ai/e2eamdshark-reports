MODEL="$1"
GOOD_COMMIT="$2"
BAD_COMMIT="$3"
DEVICE="$4"

git bisect reset || true
git bisect start
git bisect bad "$BAD_COMMIT"
git bisect good "$GOOD_COMMIT"

git bisect run $PWD/../github-actions/bisect_test.sh "$MODEL" $DEVICE

echo "First bad commit for $MODEL:"
BAD_COMMIT_HASH=$(git bisect log | grep '^# first bad commit' | awk '{print $5}')
DATE=$(date "+%Y-%m-%d")

# Append the information to a CSV file
CSV_FILE="$PWD/../track_test_data/bisect_results.csv"

# Check if the CSV file exists, if not, add headers
if [ ! -f "$CSV_FILE" ]; then
    echo "Date,Model,First Bad Commit" > "$CSV_FILE"
fi

echo "$DATE,$MODEL,$BAD_COMMIT_HASH" >> "$CSV_FILE"

git bisect visualize --oneline || true
