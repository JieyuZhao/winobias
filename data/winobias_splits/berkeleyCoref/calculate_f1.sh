#!/bin/bash

python calculate_f1_multiprocess.py res/wino_test/$1/test_type1/ res/wino_scores/$1_test_type1_stereotype res/wino_scores/$1_test_type1_not_stereotype
python calculate_f1_multiprocess.py res/wino_test/$1/test_type2/ res/wino_scores/$1_test_type2_stereotype res/wino_scores/$1_test_type2_not_stereotype
