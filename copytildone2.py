#10.21.2021
#PY4E
#Section 5.4 example
#loop copies its input until the user types "done"
#but treats lines that start with hash character (#)
#as lines not to be printed(kind of like Python comments)

#10.27.2021 line 12 " if line[0] == '#' : " was fixed to be safe if empty line is input

while True:
    line = input('> ')
    if len(line) > 0 and line[0] == '#' : #could also use if line.startswith('#')
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
