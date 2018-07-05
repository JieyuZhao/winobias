'''
get the prediction for each file
python get_individual_prediction.py input_path output_path  model
'''

import os
import sys
import tqdm
import multiprocessing
from multiprocessing import Process, Value, Lock, Manager, Pool
manager = Manager()
index = Value('i', 0, lock=True) #index

def cmd_operation(xt):
    print('sh scripts/predict.sh  ' + sys.argv[3] + ' '  + sys.argv[1] + str(xt) + '/ ' + sys.argv[2]+str(xt) + '_pred.txt')
    os.system('sh scripts/predict.sh  ' + sys.argv[3] + ' '  + sys.argv[1] + str(xt) + '/ ' + sys.argv[2]+str(xt) + '_pred.txt')

pool = Pool(processes=10)
for i in range(0, 395, 10):
    xt = range(i, i+10)
    pool.map(cmd_operation, xt)

