import sys
import re

annos = ['[',']', '(', ')']
lines = open(sys.argv[1]).readlines()
# lines = ["300 [The president] was sued because [he] was embezzling funds."]
sents = []
annotations = []
# lines=['881 [The police] saved the girl from the criminals because [he] upholds the peace.']
for line in lines:
    words = re.sub('^\s*[0-9]+\s*', '', line)
    x = re.sub('[\[\]\(\)\{\}]',"", words)
    sents.append(x)

for i in range(len(sents)):
    with open(sys.argv[2]+str(i), 'w') as f:
        f.write(sents[i])
