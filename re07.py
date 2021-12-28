#11.16.2021
#PY4E
#Section 11.2 Extracting data using regular Expressions
#[a-zA-Z0-9]\S*@\S*[a-zA-Z]
#This is getting a little complicated and you can begin to see why regular expressions
#are their own little language unto themselves. Translating this regular expression,
#we are looking for substrings that start with a single lowercase letter, uppercase
#letter, or number “[a-zA-Z0-9]”, followed by zero or more non-blank characters
#(\S*), followed by an at-sign, followed by zero or more non-blank characters (\S*),
#followed by an uppercase or lowercase letter. Note that we switched from + to *
#to indicate zero or more non-blank characters since [a-zA-Z0-9] is already one
#non-blank character. Remember that the * or + applies to the single character
#immediately to the left of the plus or asterisk.

#Search for lines that have an at sign between characters
#The characters must be a letter or number

import re

fname = input('Enter your .txt file: ')

try:
    fhand = open(fname)
except:
    if fname == 'u suck':
        print('No u suck')
        quit()
    else:
        print('Error. Cannot open file.')
        quit()
for line in fhand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
