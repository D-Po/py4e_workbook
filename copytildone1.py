#10.21.2021
#PY4E
#Section 5.3 - Infinite Loops
#copycat loop until done is typed

print('Hello there; program will copy you until you type done\n')

while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')
