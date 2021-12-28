# 11.29.2021
# PY4E
# Section 13.3 Looping through nodes

# Often the XML has multiple nodes and we need to write a loop
# to process all of the nodes. In the following program, we loop
# through all of the user nodes:

import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)

user_lst = stuff.findall('users/user')
print('User count:', len(user_lst))

user_lst2 = stuff.findall('user')

# print('User count:', len(user_lst2))


for item in user_lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
