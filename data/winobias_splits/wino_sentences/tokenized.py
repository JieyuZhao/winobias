import os 
import sys
from nltk.tokenize import word_tokenize
'''to tokenize all the sentences.
usage: python tokenzied.py'''
datapath = '/zf2/jz4fu/Github/data/winobias_splits/wino_sentences/all_sentences/'
for file in os.listdir(datapath):
    if not file.startswith('.'):
        print(file)
        with open(datapath+ file, 'r') as f:
            sents = []
            for line in f.readlines():
                tokens = word_tokenize(line)
                sents.append(tokens)
        with open('/zf2/jz4fu/Github/data/winobias_splits/wino_sentences/tokenized/'+file, 'w') as t:
            for line in sents:
                t.write(' '.join(line) + '\n')
