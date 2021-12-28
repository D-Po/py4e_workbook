#11.01.2021
#PY4E
#Section 7.11 Exercise 1
#Write a program to read through a file and print the contents
#of the file (line by line) all in upper case. Executing the program will
#look as follows:

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    new_line = line.upper()
    print(new_line)
