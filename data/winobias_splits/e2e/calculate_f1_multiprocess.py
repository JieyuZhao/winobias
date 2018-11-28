'''used to calculate the f1 for the predictions
python calculate_f1.py file_path stereotype_result_file not_s_result_file
'''
import os
import sys
import subprocess
import re
from tqdm import tqdm
import multiprocessing
from multiprocessing import Process, Value, Lock, Manager, Pool
manager = Manager()
index = Value('i', 0, lock=True) #index

f1_s = manager.list()
f1_not_s = manager.list()

def calc_f1(i):
    key_file_s = sys.argv[1] + str(i) + '_s.v4_auto_conll'
    pred_file_s = sys.argv[1] + str(i) + '_s_output.txt'
    tmp = 0
    t = subprocess.check_output(['perl','conll-2012/scorer/v8.01/scorer.pl', 'muc', key_file_s, pred_file_s]).decode("utf-8")
    s = re.findall(r"Coreference: .*",t)
    f1_score = s[0].strip().split()[-1][:-1]
    tmp += float(f1_score)
    t = subprocess.check_output(['perl','conll-2012/scorer/v8.01/scorer.pl', 'bcub', key_file_s, pred_file_s]).decode("utf-8")
    s = re.findall(r"Coreference: .*",t)
    f1_score = s[0].strip().split()[-1][:-1]
    tmp += float(f1_score)
    t = subprocess.check_output(['perl','conll-2012/scorer/v8.01/scorer.pl', 'ceafe', key_file_s, pred_file_s]).decode("utf-8")
    s = re.findall(r"Coreference: .*",t)
    f1_score = s[0].strip().split()[-1][:-1]
    tmp += float(f1_score)
    f1_s.append(tmp/3)
    key_file_not_s = sys.argv[1] + str(i) + '_nots.v4_auto_conll'
    pred_file_not_s = sys.argv[1] + str(i) + '_nots_output.txt'
    tmp = 0
    t = subprocess.check_output(['perl','conll-2012/scorer/v8.01/scorer.pl', 'muc', key_file_not_s, pred_file_not_s]).decode("utf-8")
    s = re.findall(r"Coreference: .*",t)
    f1_score = s[0].strip().split()[-1][:-1]
    tmp += float(f1_score)
    t = subprocess.check_output(['perl','conll-2012/scorer/v8.01/scorer.pl', 'bcub', key_file_not_s, pred_file_not_s]).decode("utf-8")
    s = re.findall(r"Coreference: .*",t)
    f1_score = s[0].strip().split()[-1][:-1]
    tmp += float(f1_score)
    t = subprocess.check_output(['perl','conll-2012/scorer/v8.01/scorer.pl', 'ceafe',key_file_not_s, pred_file_not_s]).decode("utf-8")
    s = re.findall(r"Coreference: .*",t)
    f1_score = s[0].strip().split()[-1][:-1]
    tmp += float(f1_score)
    f1_not_s.append(tmp/3)

pool = Pool(processes=10)
for index.value in tqdm(range(0, 1000, 100)):
    xt = range(index.value, index.value+100)
    pool.map(calc_f1, xt)
#    print("xt", xt)
#    print("f1_s:", f1_s)


with open(sys.argv[2], 'w') as f:
    for sc in f1_s:
        f.write(str(sc) + '\n')

with open(sys.argv[3], 'w') as s:
    for sc in f1_not_s:
        s.write(str(sc) + '\n')

