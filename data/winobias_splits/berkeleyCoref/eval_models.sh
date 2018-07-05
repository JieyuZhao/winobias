if [ -n "$1" ]; then
  NAME="$1"
else
  NAME=""
fi

sh scripts/evaluate.sh avg.gender_final ../data/winobias_splits/wino_berkeley/test_type1/stereotype/ test_type1_stereotype$NAME &
sh scripts/evaluate.sh avg.gender_final ../data/winobias_splits/wino_berkeley/test_type1/not_stereotype/ test_type1_not_stereotype$NAME &
sh scripts/evaluate.sh avg.gender_final ../data/winobias_splits/wino_berkeley/test_type2/stereotype/ test_type2_stereotype$NAME &
sh scripts/evaluate.sh avg.gender_final ../data/winobias_splits/wino_berkeley/test_type2/not_stereotype/ test_type2_not_stereotype$NAME &

wait

sh scripts/evaluate.sh anon.union_avg.gender_final ../data/winobias_splits/wino_berkeley/test_type1/stereotype/ test_type1_stereotype$NAME &
sh scripts/evaluate.sh anon.union_avg.gender_final ../data/winobias_splits/wino_berkeley/test_type1/not_stereotype/ test_type1_not_stereotype$NAME &
sh scripts/evaluate.sh anon.union_avg.gender_final ../data/winobias_splits/wino_berkeley/test_type2/stereotype/ test_type2_stereotype$NAME &
sh scripts/evaluate.sh anon.union_avg.gender_final ../data/winobias_splits/wino_berkeley/test_type2/not_stereotype/ test_type2_not_stereotype$NAME &

wait

sh scripts/evaluate.sh anonymize_avg.gender_final ../data/winobias_splits/wino_berkeley/test_type1/stereotype/ test_type1_stereotype$NAME &
sh scripts/evaluate.sh anonymize_avg.gender_final ../data/winobias_splits/wino_berkeley/test_type1/not_stereotype/ test_type1_not_stereotype$NAME &
sh scripts/evaluate.sh anonymize_avg.gender_final ../data/winobias_splits/wino_berkeley/test_type2/stereotype/ test_type2_stereotype$NAME &
sh scripts/evaluate.sh anonymize_avg.gender_final ../data/winobias_splits/wino_berkeley/test_type2/not_stereotype/ test_type2_not_stereotype$NAME &

wait
