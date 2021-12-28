#11.02.2021
#PY4E
#Section 8.8
#We could rewrite an earlier program that computed the average of a list of numbers
#entered by the user using a list.
#We could simply remember each number as the user entered it and use built-in
#functions to compute the sum and count at the end.

numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done' or inp == 'Done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print(numlist)
print('Average:', average)

#We make an empty list before the loop starts, and then each time we have a number,
#we append it to the list. At the end of the program, we simply compute the sum
#of the numbers in the list and divide it by the count of the numbers in the list to
#come up with the average
