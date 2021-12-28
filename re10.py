#11.16.2021
#PY4E
#Section 11.3 Combining searching and extracting
#We can construct the following regular expression to select the lines:
#^X-.*: [0-9.]+
#Translating this, we are saying, we want lines that start with X-, followed by zero
#or more characters (.*), followed by a colon (:) and then a space. After the
#space we are looking for one or more characters that are either a digit (0-9) or
#a period [0-9.]+. Note that inside the square brackets, the period matches an
#actual period (i.e., it is not a wildcard between the square brackets).
#This is a very tight expression that will pretty much match only the lines we are
#interested in as follows:

#Search for lines that start with 'X' followed by any
#non whitespace characters and ':'
#followed by a space and any number.
#The number can include a decimal.

import re

fname = input('Enter your .txt file: ')

try:
    fhand = open(fname)
except:
    if fname == 'u smell':
        print('you smell worse.')
        quit()
    else:
        print('Error. Cannot open file.')
        quit()

for line in fhand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)
