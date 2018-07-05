import os
import sys

for i in range(395):
    new_p = sys.argv[1] + str(i)
    os.mkdir(new_p)
    os.system('cp '+ sys.argv[1] + 'all/' + str(i) + '.v4_auto_conll ' + sys.argv[1] + str(i) + '/' )
