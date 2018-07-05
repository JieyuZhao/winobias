'''
change the properties and run the run.sh
change_exp.py uw_jsonlines_path model_output_path model
'''
import re
import sys
import os
import fileinput
from tqdm import tqdm
import subprocess


for f in tqdm([2,5]):
    name = str(f)
    count = 0
    for line in fileinput.input("src/edu/stanford/nlp/coref/properties/deterministic-english-conll.properties", inplace=True):
        if count == 28:
            print('dcoref.logFile = out/deterministic/test_type1/stereotype/' + name + '_s.txt')
            count += 1
            continue
        if count == 32:
            print('dcoref.conll2011 = /zf2/jz4fu/Github/CoreNLP/'+ sys.argv[1]+name + '_s.v4_auto_conll')
            count += 1
            continue
        print(line.strip('\n'))
        count += 1
    t = subprocess.check_output(['sh','run.sh'])
