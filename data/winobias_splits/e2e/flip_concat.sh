#!/bin/bash

mkdir data/wino_test/$1
mkdir data/wino_test/$1/test_type1/
mkdir data/wino_test/$1/test_type2/
python flip_concat_multithread.py data/wino_output_conll/$1/test_type1/stereotype/ data/wino_output_conll/$1/test_type1/not_stereotype/ ../data/winobias_splits/wino_uw/test_type1/stereotype/ ../data/winobias_splits/wino_uw/test_type1/not_stereotype/ data/wino_test/$1/test_type1/
python flip_concat_multithread.py data/wino_output_conll/$1/test_type2/stereotype/ data/wino_output_conll/$1/test_type2/not_stereotype/ ../data/winobias_splits/wino_uw/test_type2/stereotype/ ../data/winobias_splits/wino_uw/test_type2/not_stereotype/ data/wino_test/$1/test_type2/
