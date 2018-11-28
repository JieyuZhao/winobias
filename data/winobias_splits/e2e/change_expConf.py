'''
change the experiment.conf and run the decoder.py
change_exp.py uw_jsonlines_path model_output_path model
'''
import sys
import os
import fileinput
from tqdm import tqdm


for f in tqdm(range(395)):
    name = str(f)
    count = 0
    for line in fileinput.input("experiments.conf", inplace=True):
        if count == 145:
            print('  eval_path = ' + sys.argv[1] + name + '.jsonlines')
            count += 1
            continue
        print(line.strip('\n'))
        count += 1
    os.system('python2 decoder.py ' +sys.argv[3] + ' '+ sys.argv[2] + name + '.jsonlines')
