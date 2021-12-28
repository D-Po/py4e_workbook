#11.24.2021
#PY4E
#Section 12.7 Parsing HTML using regular expressions

#One simple way to parse HTML is to use regular expressions to repeatedly search
#for and extract substrings that match a particular pattern.
#Here is a simple web page:

#<h1>The First Page</h1>
#<p>
#If you like, you can switch to the
#<a href="http://www.dr-chuck.com/page2.htm">
#Second Page</a>.
#</p>

#We can construct a well-formed regular expression to match and extract the link
#values from the above text as follows:

#href="http[s]?://.+?"

#Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())
