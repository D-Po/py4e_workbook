#11.09.2021
#PY4E
#Section 9.4
#We will write a Python program to read through the lines of the file, break each
#line into a list of words, and then loop through each of the words in the line and
#count each word using a dictionary.
# Use string translate method to remove punctuation, capitalization, etc.
#romeo-full.txt
#line.translate(str.maketrans(fromstr, tostr, deletestr))
#Replace the characters in fromstr with the character in the same position in tostr
#and delete all characters that are in deletestr. The fromstr and tostr can be
#empty strings and the deletestr parameter can be omitted.
#We will not specify the tostr but we will use the deletestr parameter to delete
#all of the punctuation.

import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
