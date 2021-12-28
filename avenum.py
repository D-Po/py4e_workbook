#11.02.2021
#PY4E
#Section 8.8
#We could rewrite an earlier program that computed the average of a list of numbers
#entered by the user using a list.
#First, the program to compute an average without a list:

#In this program, we have count and total variables to keep the number and
#running total of the user’s numbers as we repeatedly prompt the user for a number.

total = 0
count = 0
while (True):
    inp = input('Enter a number and then type done to compute average: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1

average = total/count
print('Average:', average)
