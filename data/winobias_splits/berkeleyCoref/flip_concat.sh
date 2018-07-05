#!/bin/bash

mkdir res/wino_test/$1
mkdir res/wino_test/$1/test_type1/
mkdir res/wino_test/$1/test_type2/
python flip_concat_multithread.py res/wino_predictions/$1/test_type1/stereotype/ res/wino_predictions/$1/test_type1/not_stereotype/ ../data/winobias_splits/wino_berkeley/test_type1/stereotype/all/ ../data/winobias_splits/wino_berkeley/test_type1/not_stereotype/all/ res/wino_test/$1/test_type1/
python flip_concat_multithread.py res/wino_predictions/$1/test_type2/stereotype/ res/wino_predictions/$1/test_type2/not_stereotype/ ../data/winobias_splits/wino_berkeley/test_type2/stereotype/all/ ../data/winobias_splits/wino_berkeley/test_type2/not_stereotype/all/ res/wino_test/$1/test_type2/
