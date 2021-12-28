#11.15.2021
#PY4E
#Section 11.1 Character Matching in Regular Expressions
#This is particularly powerful when combined with the ability to indicate that a
#character can be repeated any number of times using the * or + characters in your
#regular expression. These special characters mean that instead of matching a single
#character in the search string, they match zero-or-more characters (in the case of
#the asterisk) or one-or-more of the characters (in the case of the plus sign).
#We can further narrow down the lines that we match using a repeated wild card
#character in the following example:

#Search for lines that start with From and have an at symbol
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
    if re.search('^From:.+@', line):       #caret character used to match beginning of line
        print(line)
