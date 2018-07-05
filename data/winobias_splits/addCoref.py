import nltk
import sys

'''is used to add the coref label to the dataset'''
entityIdx = {'[':'1',']':'1','(':'2',')':'2','{':'3','}':'3'}
lines = open(sys.argv[1]).readlines()
#lines = ["[The carpenter] is complaining to the cashier becasue [he] was over-charged.","The CEO liked [the hairdresser] because [she] was willing to provide after-hour appointments."]
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
            if word == '(' or word == ')':
		sys.exit()
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

#sys.exit()
for i in range(len(annotations)):
    print(len(annotations[i]))
    print(annotations[i])
    with open(sys.argv[2]+str(i), 'r') as f:
        doc = []
        lines = f.readlines()
        print(len(lines)-3)
        for line_id in range(len(lines)):
            words = lines[line_id].strip().split()
            if line_id == 0 or line_id == len(lines)-1 :
		doc.append(lines[line_id])
		continue
	    if len(words) == 0:
		doc.append('\n')
		continue
            print(words)
            words[9] = 'Speaker#1'
            words.insert(-2, '*')
            words.insert(-2, '*')
            words.insert(-2, '*')
            print(line_id)
            words[-1] = annotations[i][line_id-1]
            doc.append('\t'.join(words)+'\n')
    with open(sys.argv[3]+str(i)+".v4_auto_conll", 'w') as f:
        for sen in doc:
            f.write(sen)

