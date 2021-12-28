#10.29.2021
#PY4E
#Section 7.5 Searching through a file
#script searches a file and finds lines that begin with 'From:'
#rstrip strips white space from the right side of the line

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
