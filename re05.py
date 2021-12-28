#11.15.2021
#PY4E
#Section 11.2 Extracting data using regular Expressions

#We don’t want to write code for each of the types of lines, splitting and slicing
#differently for each line. This following program uses findall() to find the lines
#with email addresses in them and extract one or more addresses from each of those
#lines.

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)  #We are using a two-character sequence that matches a non-whitespace character (\S).
print(lst)
