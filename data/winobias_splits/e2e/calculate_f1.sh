#!/bin/bash

python calculate_f1_multiprocess.py data/wino_test/$1/test_type1/ data/wino_scores/$1_test_type1_stereotype data/wino_scores/$1_test_type1_not_stereotype
python calculate_f1_multiprocess.py data/wino_test/$1/test_type2/ data/wino_scores/$1_test_type2_stereotype data/wino_scores/$1_test_type2_not_stereotype
