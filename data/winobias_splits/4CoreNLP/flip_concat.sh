#!/bin/bash

mkdir data/wino_test
mkdir data/wino_test/$1
mkdir data/wino_test/$1/test_type1/
mkdir data/wino_test/$1/test_type2/
python flip_concat_multithread.py data/wino_predictions/$1/test_type1/stereotype/ data/wino_predictions/$1/test_type1/not_stereotype/ ../data/winobias_splits/wino_berkeley/test_type1/stereotype/all/ ../data/winobias_splits/wino_berkeley/test_type1/not_stereotype/all/ data/wino_test/$1/test_type1/
python flip_concat_multithread.py data/wino_predictions/$1/test_type2/stereotype/ data/wino_predictions/$1/test_type2/not_stereotype/ ../data/winobias_splits/wino_berkeley/test_type2/stereotype/all/ ../data/winobias_splits/wino_berkeley/test_type2/not_stereotype/all/ data/wino_test/$1/test_type2/
