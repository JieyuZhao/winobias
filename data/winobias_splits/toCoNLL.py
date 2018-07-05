import nltk
import sys

entityIdx = {'[':'1',']':'1','(':'2',')':'2','{':'3','}':'3'}
lines = open(sys.argv[1]).readlines()
# lines = ["300 [The president] was sued because [he] was embezzling funds."]
sents = []
annotations = []
for line in lines:
    tokens = nltk.word_tokenize(line)
    print(tokens)
    annotation = []
    sent = []
    buffer = []
    flag = 0
    for idx in range(0,len(tokens)):
        word = tokens[idx]
        if word == '.':
            sent.append('.')
            annotation.append('-')
            break
        if word in ['[', '(', '{']:
            buffer.append('('+entityIdx[word])
        elif word in [']', ')', '}']:
            if flag == 1:
                buffer[-1] += ')'
                flag = 0
            else:
                buffer.append(entityIdx[word]+')')
            annotation.append('|'.join(buffer))
            buffer = []
        else:
            sent.append(word)
            if tokens[idx+1] not in [']',')','}']:
                if idx > 0 and (tokens[idx-1] in ['[','(','{']):
                    annotation.append('|'.join(buffer))
                    buffer = []
                else:
                    annotation.append('-')
            else:
                if idx > 0 and (tokens[idx-1] in ['[','(','{']):
                    flag = 1 
                
#    print tokens
#    print line
    print sent
    print annotation
    annotations.append(annotation)
    sents.append(sent)
doc = []
for i in range(len(sents)):
    doc.append("#begin document (bc/cnn/00/cnn_0000_3); part %s\n"%str(i))
    for word_id in range(len(sents[i])):
        tmps = 'bc/cnn/00/cnn_0000_3 ' +str(i)+" " + str(word_id) +" " + sents[i][word_id] + " - - - - - "+"Speaker#1 - - - - - "+annotations[i][word_id] + "\n"
        doc.append(tmps)
    doc.append('\n')
    doc.append("#end document\n")
    
with open(sys.argv[1]+".conll", 'w') as f:
    for x in doc:
        f.write(x)
