#11.01.2021
#PY4E
#Section 7.11 Exercise 3
#Sometimes when programmers get bored or want to have a
#bit of fun, they add a harmless Easter Egg to their program. Modify
#the program that prompts the user for the file name so that it prints a
#funny message when the user types in the exact file name “na na boo
#boo”. The program should behave normally for all other files which
#exist and don’t exist.

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd")
        quit()
    else:
        print('File cannot be opened:', fname)
        quit()


count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
