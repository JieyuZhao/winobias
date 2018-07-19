#!/bin/bash
mkdir data/wino_output_conll/$1
mkdir data/wino_output_conll/$1/test_type1/
mkdir data/wino_output_conll/$1/test_type1/stereotype
mkdir data/wino_output_conll/$1/test_type1/not_stereotype
mkdir data/wino_output_conll/$1/test_type2/
mkdir data/wino_output_conll/$1/test_type2/stereotype
mkdir data/wino_output_conll/$1/test_type2/not_stereotype

python convert_to_conll.py ../data/winobias_splits/wino_uw/test_type1/stereotype/ data/wino_predictions/$1/test_type1/stereotype/ data/wino_output_conll/$1/test_type1/stereotype/
python convert_to_conll.py ../data/winobias_splits/wino_uw/test_type1/not_stereotype/ data/wino_predictions/$1/test_type1/not_stereotype/ data/wino_output_conll/$1/test_type1/not_stereotype/
python convert_to_conll.py ../data/winobias_splits/wino_uw/test_type2/stereotype/ data/wino_predictions/$1/test_type2/stereotype/ data/wino_output_conll/$1/test_type2/stereotype/
python convert_to_conll.py ../data/winobias_splits/wino_uw/test_type2/not_stereotype/ data/wino_predictions/$1/test_type2/not_stereotype/ data/wino_output_conll/$1/test_type2/not_stereotype/
