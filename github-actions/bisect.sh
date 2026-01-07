echo "============================== in bisect.sh ================================="
#GOOD_COMMIT=$(git tag \
#    | grep '^iree-3\.[0-9]\+\.0rc' \
#    | sort -V -r \
#    | sed -n '7p')
GOOD_COMMIT="d6cb40ab4a53612a0e0a720069ddbcc7e56c80a1"
#BAD_COMMIT=$(git rev-parse HEAD)
BAD_COMMIT="2775a61d76f3ee80cd20c4bdadc090baafb9f8e4"
PWD="$(pwd)/../"
while read -r model; do
  echo "==============================="
  echo "Bisecting $model"
  echo "==============================="
  $PWD/github-actions/runbisect_for_model.sh "$model" "$GOOD_COMMIT" "$BAD_COMMIT"  
done < ../regression_models1.txt


echo "============================== exiting bisect.sh ================================="
