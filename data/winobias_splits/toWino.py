import sys
import os
berkeley_file = sys.argv[1]
uw_file = sys.argv[2]
"""based on the berekeley conll file, translate into uw-conll format"""
b_files = os.listdir(berkeley_file)

for f in b_files:
    if os.path.isdir(berkeley_file + f):
        continue
    lines = open(berkeley_file + f).readlines()
    doc = []
    for line_id in range(len(lines)) :
        lines[line_id] = lines[line_id].replace('../data/winobias_splits/wino_sentences', 'nw')
        if line_id ==0 or line_id == len(lines) - 1:
            doc.append(lines[line_id])
            continue
        words = lines[line_id].strip().split()
        if len(words) == 0:
            doc.append('\n')
            continue
        words[4] = '-'
        words[5] = '-'
        doc.append('\t'.join(words) + '\n')
    with open(uw_file+f, 'w') as tf:
        for sen in doc:
            tf.write(sen)

