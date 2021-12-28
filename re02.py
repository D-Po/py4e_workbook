#11.15.2021
#PY4E
#Section 11.0 Regular Expressions
#The power of the regular expressions comes when we add special characters to
#the search string that allow us to more precisely control which lines match the
#string. Adding these special characters to our regular expression allow us to do
#sophisticated matching and extraction while writing very little code.
#For example, the caret character is used in regular expressions to match “the
#beginning” of a line. We could change our program to only match lines where
#“From:” was at the beginning of the line as follows:

#Search for lines that start with 'From'

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
    if re.search('^From:', line):       #caret character used to match beginning of line
        print(line)
