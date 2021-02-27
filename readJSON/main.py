import json

users = open('users.json', 'r').read()
jsonString = json.loads(users)
print('Customers whose score is greater than 3000:')
for object in jsonString:
    if object['score'] is not None and object['score'] > 3000:
        id = object['id']
        name = object['name']
        print('ID: ', id)
        print('Name: ', name)
