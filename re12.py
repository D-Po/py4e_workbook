#11.16.2021
#PY4E
#Section 11.3 Combining searching and extracting
#As another example of this technique, if you look at the file there are a number of
#lines of the form:

#Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772

#If we wanted to extract all of the revision numbers (the integer number at the end
#of these lines) using the same technique as above, we could write the following
#program:

#Search for lines that start with 'Details: rev='
#followed by numbers
#Then print the number if one is found

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
    x = re.findall('^Details:.*rev=([0-9]+)', line)
    if len(x) > 0:
        print(x)

        
