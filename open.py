#10.29.2021
#PY4E
#Section 7.4 open file and count lines script
#text file must be saved in py4e
fhand = open(input('Please input your text file located in py4e:'))
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
