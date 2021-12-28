#11.23.2021
#PY4E
#Section 12.4 Retrieving web pages with urllib
#While we can manually send and receive data over HTTP using the
#socket library, there is a much simpler way to perform
#this common task in Python by using the urllib library.
#Using urllib, you can treat a web page much like a file.
#You simply indicate which web page you would like to retrieve
#and urllib handles all of the HTTP protocol and header details.
#The equivalent code to read the romeo.txt file from the web
#using urllib is as follows:

import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
print('')
for line in fhand:
    print(line.decode().strip())
