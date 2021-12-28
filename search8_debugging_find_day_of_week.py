#11.05.2021
#PY4E
#Section 8.14 Debugging
#When we read and parse files, there are many opportunities to encounter
#input that can crash our program so it is a good idea to revisit the guardian
#pattern when it comes writing programs that read through a file and look
#for a “needle in the haystack”.
#Let’s revisit our program that is looking for the day of the week on the from
#lines of our file:
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

#This program went through a series of debugging tests shown in 8.14

fhand = open('mbox-short_TEST_FILE_EX2.txt')
count = 0                       #unsure why count is included here
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words) == 0 or len(words) < 3 or words[0] != 'From': continue
    #if words[0] != 'From' : continue
    print(words[2])
