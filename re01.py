#11.15.2021
#PY4E
#Section 11.0 Regular Expressions
#The regular expression library re must be imported into your program before you
#can use it. The simplest use of the regular expression library is the search()
#function. The following program demonstrates a trivial use of the search function.

#Search for lines that contain 'From'

import re

fname = input('Please enter text file:')
try:
    fhand = open(fname)
except:
    if fname == 'screw u':
        print('Screw u too')
        quit()
    else:
        print('Error. Enter .txt file.')
        quit()

for line in fhand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
