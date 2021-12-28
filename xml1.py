# 11.29.2021
# PY4E
# Section 13.2 Parsing XML

# Here is a simple application that parses some XML and
# extracts some data elements from the XML:

import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
