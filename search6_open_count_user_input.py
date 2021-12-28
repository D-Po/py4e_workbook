#11.01.2021
#PY4E
#Section 7.6 open user inputed file and count subject lines script
#ask the user to enter the file name string each time the program runs
#so they can use our program on different files without changing the Python code

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
