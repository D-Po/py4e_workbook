# 11.29.2021
# PY4E
# Section 13.5 Parsing JSON JavaScript Object Notation

# In the following program, we use the built-in json library to
# parse the JSON and read through the data. Compare this closely to
# the equivalent XML data and code above. The JSON has less detail,
# so we must know in advance that we are getting a list and that the
# list is of users and each user is a set of key-value pairs.
# The JSON is more succinct (an advantage) but also is less
# self-describing (a disadvantage)

import json

data = '''
[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
      } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Brent"
      }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
