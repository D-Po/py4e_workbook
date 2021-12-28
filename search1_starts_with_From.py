#10.29.2021
#PY4E
#Section 7.5 Searching through a file
#script searches a file and finds lines that begin with 'From:'

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)
