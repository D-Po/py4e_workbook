# 12.02.2021
# PY4E
# Section 14.4 Starting with programs
# A program in its most basic form takes some input, does some
# processing, and produces some output. Our elevator conversion
# program demonstrates a very short but complete program showing
# all three of these steps.

usf = input('Enter the US Floor Number: ')
wf = int(usf) - 1
print('Non-US Floor number is', wf)
