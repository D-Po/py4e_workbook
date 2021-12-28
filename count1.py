#11.09.2021
#PY4E
#Section 9.2
#We will write a Python program to read through the lines of the file, break each
#line into a list of words, and then loop through each of the words in the line and
#count each word using a dictionary.


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
