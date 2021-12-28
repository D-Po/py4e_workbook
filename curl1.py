#11.23.2021
#PY4E
#Section 12.5 Reading binary files using urllib
#Sometimes you want to retrieve a non-text (or binary) file such as
#an image or video file. The data in these files is generally not
#useful to print out, but you can easily make a copy of a URL
#to a local file on your hard disk using urllib. The pattern is
#to open the URL and use read to download the entire contents of
#the document into a string variable (img) then write
#that information to a local file as follows:

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')  #wb opens a binary file for writing only.
fhand.write(img)
fhand.close()
