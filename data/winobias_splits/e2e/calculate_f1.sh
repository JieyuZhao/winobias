#!/bin/bash

python ../winobias_split/e2e/calculate_f1_multiprocess.py data/sigtest/flip_concat/$1/dev_T1/ data/sigtest/wino_scores/$1_dev_T1_pro data/sigtest/wino_scores/$1_dev_T1_anti
python ../winobias_split/e2e/calculate_f1_multiprocess.py data/sigtest/flip_concat/$1/dev_T2/ data/sigtest/wino_scores/$1_dev_T2_pro data/sigtest/wino_scores/$1_dev_T2_anti
