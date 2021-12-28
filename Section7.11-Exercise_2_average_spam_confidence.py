#11.01.2021
#PY4E
#Section 7.11 Exercise 2
#Write a program to prompt for a file name, and then read
#through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:”
#pull apart the line to extract the floating-point number on the line.
#Count these lines and then compute the total of the spam confidence
#values from these lines. When you reach the end of the file, print out
#the average spam confidence.


fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
confidence_sum = 0

for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1                              #equivalent to count = count + 1
        confidence = float(line[20:26])
        confidence_sum += confidence            #same as above comment reg count

average_confidence = confidence_sum/count

print('Average spam confidence:', str(average_confidence))
