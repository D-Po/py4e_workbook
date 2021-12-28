# 12.02.2021
# PY4E
# Section 14.3 Using Objects
# As it turns out, we have been using objects all along in this book.
# Python provides us with many built-in objects. Here is some simple
# code where the first few lines should feel very simple and
# natural to you.

stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()
print(stuff[0])
print(stuff.__getitem__(0))
print(list.__getitem__(stuff,0))
