#11.16.2021
#PY4E
#Section 11.3 Combining searching and extracting
#Now we can use regular expressions to redo an exercise from earlier in the book
#where we were interested in the time of day of each mail message. We looked for
#lines of the form:

#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

#and wanted to extract the hour of the day for each line.

#We can do this in a far simpler way with the following regular expression:
#^From .* [0-9][0-9]:

#Search for lines that start with From and a character
#followed by a two digit number between 00 and 99 followed by ':'
#Then print the number if it is greater than zero

#This is updated code from Sec10.11-Ex2 time of day email

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
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0 : print(x)
