# 11.26.2021
# py4e
# Section 12.9

# The command curl is short for “copy URL” and so the two examples
# listed earlier to retrieve binary files with urllib are cleverly
# named curl1.py and curl2.py on www.py4e.com/code3 as they implement
# similar functionality to the curl command. There is also a curl3.py
# sample program that does this task a little more effectively, in
# case you actually want to use this pattern in a program you are
# writing.

#TEST THIS AGAIN TOMORROW MULTIPLE Py4e jpegs

import os
import urllib.request, urllib.parse, urllib.error

print('Please enter a URL like http://data.pr4e.org/cover3.jpg')
urlstr = input().strip()
img = urllib.request.urlopen(urlstr)

# Get the last "word"
words = urlstr.split('/')
fname = words[-1]

# Don't overwrite the file
if os.path.exists(fname):
    if input('Replace ' + fname + ' (Y/n)?') != 'Y':
        print('Data not copied')
        exit()
    print('Replacing', fname)

fhand = open(fname, 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied to', fname)
fhand.close()
