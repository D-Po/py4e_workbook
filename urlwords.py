#11.23.2021
#PY4E
#Section 12.4 Retrieving web pages with urllib
#As an example, we can write a program to retrieve the data
#for romeo.txt and compute the frequency of each word
#in the file as follows:

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()               #intialize count dictionary
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
