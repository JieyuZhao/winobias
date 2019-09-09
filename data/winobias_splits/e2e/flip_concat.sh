#!/bin/bash

# mkdir data/sigtest/wino_test/$1
# mkdir data/sigtest/wino_test/$1/test_type1/
# mkdir data/sigtest/wino_test/$1/test_type2/
python ../winobias_split/e2e/flip_concat_multithread.py data/sigtest/split_pred/$1/dev_T1/pro/ data/sigtest/split_pred/$1/dev_T1/anti/ data/sigtest/gold_split/dev_T1/pro/ data/sigtest/gold_split/dev_T1/anti/  data/sigtest/flip_concat/$1/dev_T1/
echo "Finish dev_T1 for model $1"
python ../winobias_split/e2e/flip_concat_multithread.py data/sigtest/split_pred/$1/dev_T2/pro/ data/sigtest/split_pred/$1/dev_T2/anti/ data/sigtest/gold_split/dev_T2/pro/ data/sigtest/gold_split/dev_T2/anti/  data/sigtest/flip_concat/$1/dev_T2/