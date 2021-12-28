#11.15.2021
#PY4E
#Section 11.1 Character Matching in Regular Expressions
#There are a number of other special characters that let us build even more powerful
#regular expressions. The most commonly used special character is the period or
#full stop, which matches any character.
#In the following example, the regular expression F..m: would match any of the
#strings “From:”, “Fxxm:”, “F12m:”, or “F!@m:” since the period characters in the
#regular expression match any character.

#search for lines that start with 'F', followed by 2 characters, follow by 'm:'

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
    if re.search('^F..m:', line):       #caret character used to match beginning of line
        print(line)
