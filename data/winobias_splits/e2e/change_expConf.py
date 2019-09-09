'''
change the experiment.conf and run the decoder.py
change_exp.py uw_jsonlines_path model_output_path model
'''
import sys
import os
import fileinput
from tqdm import tqdm


for f in tqdm(range(3)):
    name = str(f)
    count = 0
    inpu = sys.argv[1] + name + '.jsonlines'
    output = sys.argv[2] + name + '.jsonlines'
    # for line in fileinput.input("experiments.conf", inplace=True):
    #     if count == 681:
    #         print('  eval_path = ' + sys.argv[1] + name + '.jsonlines')
    #         count += 1
    #         continue
    #     print(line.strip('\n'))
    #     count += 1
    os.system('python predict.py ' +sys.argv[3] + ' '+ inpu + ' ' + output)
