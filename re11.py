#11.16.2021
#PY4E
#Section 11.3 Combining searching and extracting
#But now we have to solve the problem of extracting the numbers. While it would
#be simple enough to use split, we can use another feature of regular expressions
#to both search and parse the line at the same time.
#Parentheses are another special character in regular expressions. When you add
#parentheses to a regular expression, they are ignored when matching the string.
#But when you are using findall(), parentheses indicate that while you want the
#whole expression to match, you only are interested in extracting a portion of the
#substring that matches the regular expression.

#Search for lines that start with 'X' followed by any
#non whitespace characters and ':' followed by a
#space and any number. The number can include a decimal.
#Then print the number if it is greater than zero.

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
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
        
