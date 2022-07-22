# 1. Write a program to read file sample.json. Display all distance and name of locations.
import json
from math import dist

def load_json(filename):
    with open(filename, 'r') as f:
        obj = json.load(f)
        for loc in obj['results']:
            distance = loc['distance']
            name = loc['name']
            long = loc['geocodes']['main']['longitude']
            lat = loc['geocodes']['main']['latitude']
            # print(f'Name: {name}')
            print('-------------------')
    # return obj
    

load_json('sample.json')
abc = 10
print(f'{abc} first lines:')

# 2. Write a program to:
# - Define a python object (dictionary) containing fields: date, location, gps (lat, lon), weather, population.
# - Store a python object (dictionary) into a json file name sample_w.json.

# 3. Write a program to to create a new json file from an existing json file (sample_w.json)

# 4. Write a program to add new user into existing json file (users.json). User information will be input from keyboard.
'''
users.json
[
    {
        'name': 'John',
        'email': 'john@example.com',
        'age': 18,
        'address': 'John Street'
    },
    {
        'name': 'Su',
        'email': 'su@example.com',
        'age': 18,
        'address': 'Su Street'
    }
]
'''

# 5. Write a program to delete users which have age is a number entered from keyboard in users.json file.