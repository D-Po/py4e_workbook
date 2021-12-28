#11.15.2021
#PY4E
#Section 11.2 Extracting data using regular Expressions

#We can use this regular expression (from re05) in a program to read
#all the lines in a file and print out anything that looks like an email address as
#follows:

#Search for lines that have an at symbol between characters
import re

fname = input('Please enter .txt file: ')

try:
    fhand = open(fname)
except:
    if fname == 'screw u':
        print('screw u too')
    else:
        print('Error. File not found.')

for line in fhand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)
