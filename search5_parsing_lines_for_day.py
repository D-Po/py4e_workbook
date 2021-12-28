#11.03.2021
#PY4E
#Section 8.10 Parsing lines

#Usually when we are reading a file we want to do something to the lines other than
#just printing the whole line. Often we want to find the “interesting lines” and then
#parse the line to find some interesting part of the line. What if we wanted to print
#out the day of the week from those lines that start with “From”?

#The split method is very effective when faced with this kind of problem. We can
#write a small program that looks for lines where the line starts with “From”, split
#those lines, and then print out the third word in the line:

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
