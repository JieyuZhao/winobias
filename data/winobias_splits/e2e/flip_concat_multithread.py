"""
randomly (p=0.5) flip each between stereotype and non_stereotype. Calculate |f1_s - f1_n|
sys.argv[1]: pred_stereotype_path  #conll_format
sys.argv[2]: pred_not_stereotype_path
sys.argv[3]: gold_stereotype_path
sys.argv[4]: gold_not_stereotype_path
sys.argv[5]: path_after_concat_all_files
"""
import random
import sys
import os
from tqdm import tqdm
import multiprocessing
from multiprocessing import Process, Value, Lock, Manager, Pool
manager = Manager()
index = Value('i', 0, lock=True) #index

def cmd_operation(i):
        stereotype_pred = []
        not_stereotype_pred = []
        stereotype_gold = []
        not_stereotype_gold = []
        for j in range(1, 397):
            ra = random.random()
            if ra > 0.5 : # flip sterotype and not_stereotype file
                stereotype_pred.append(sys.argv[2] + 'F' + str(j) )
                not_stereotype_pred.append(sys.argv[1] + 'F' + str(j) )
                stereotype_gold.append(sys.argv[4] + 'F' + str(j) + '.v4_auto_conll')
                not_stereotype_gold.append(sys.argv[3] + 'F' + str(j) + '.v4_auto_conll')

            else:
                stereotype_pred.append(sys.argv[1] + 'F' + str(j))
                not_stereotype_pred.append(sys.argv[2] +'F' + str(j))
                stereotype_gold.append(sys.argv[3] + 'F' + str(j) + '.v4_auto_conll')
                not_stereotype_gold.append(sys.argv[4] + 'F' + str(j) + '.v4_auto_conll')



        assert len(stereotype_gold) == 396
        assert len(stereotype_pred) == 396
        assert len(not_stereotype_gold) == 396
        assert len(not_stereotype_pred) == 396

        pred_s_cmd = ' '.join(stereotype_pred)
        pred_nots_cmd = ' '.join(not_stereotype_pred)

        gold_s_cmd = ' '.join(stereotype_gold)
        gold_nots_cmd = ' '.join(not_stereotype_gold)

        os.system("cat " + pred_s_cmd + " > " + sys.argv[5] + str(i) + '_s_output.txt')
        os.system("cat " + pred_nots_cmd + " > " + sys.argv[5] + str(i) + '_nots_output.txt')
        os.system("cat " + gold_s_cmd + " > " + sys.argv[5] + str(i) + '_s.v4_auto_conll')
        os.system("cat " + gold_nots_cmd + " > " + sys.argv[5] + str(i) + '_nots.v4_auto_conll')


pool = Pool(processes=10)
for index.value in tqdm(range(0, 1000, 100)):
    xt = range(index.value, index.value+100)
    pool.map(cmd_operation, xt)
