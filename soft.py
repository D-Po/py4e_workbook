#11.11.2021
#PY4E
#section 10.2 
#Sorting a list of words from longest to shortest

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()

for word in words:
    t.append((len(word), word))

t.sort(reverse = True)

res = list()
for (length, word) in t :               #I added parentheses to tuplet
    res.append(word)

print(res)

#The first loop builds a list of tuples, where each tuple is a word preceded by its
#length.
#sort compares the first element, length, first, and only considers the second element to break ties.
#The keyword argument reverse=True tells sort to go in decreasing order.
#The second loop traverses the list of tuples and builds a list of words in descending
#order of length. The four-character words are sorted in reverse alphabetical order,
#so “what” appears before “soft” in the following list.
