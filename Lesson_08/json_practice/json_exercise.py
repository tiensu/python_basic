import json

# Exercise 1: Convert a dictionary to json format
def convert_dict_to_json():
    data = {
        'key1': 'value 1', 
        'key2': 'value 2',
        'key3': 'value 3'
        }
    json_data = json.dumps(data)
    print(json_data)
# test function
# convert_dict_to_json()

# Exercise 2: Access to the value of a key from a json object
def access_to_value():
    json_str = """{"key1": "value 1", "key2": "value 2", "key3": "value 3"}"""
    json_data = json.loads(json_str)
    print(f'Value with key key2 is: {json_data["key2"]}')

# test function
# access_to_value()

# Exercise 3: Pretty print json data
def pretty_json_data():
    json_data = {"key1": "value 1", "key2": "value 2", "key3": "value 3"}
    pretty_json = json.dumps(json_data, indent=2, separators=(",", " = "))
    print(pretty_json)

# test function
# pretty_json_data()

# Exercise 4: Write data to json file
def write_json():
    json_data = {"id": 10, "name": "Pham Van Manh", "age": 31, "address": "Ha Noi"}
    # open json file to write
    with open('sample_json.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=2, sort_keys=True)
    
# test function
# write_json()

# Exercise 5: Acess the key "salary" from a nested json
def json_nested_access():
    json_str = """{
        "company": {
            "employee1":{
                "name": "Pham Van Nam",
                "payble": {
                    "salary": "1200$",
                    "bonus": "300$"
                },
                "position": "Leader"
            },
            "employee2":{
                "name": "Pham Van Tan",
                "payble": {
                    "salary": "2200$",
                    "bonus": "600$"
                },
                "position": "Manager"
            }
        }
    }"""
    json_data = json.loads(json_str)
    # print(json_data)
    salary_emp1 = json_data['company']['employee1']['payble']['salary']
    print(f'Salary of employee 1 is: {salary_emp1}')

    # save to json file
    with open('company.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=2, sort_keys=True)

# test function
# json_nested_access()

# Exercise 6: Read company.json file and show bonus values of all employees
def read_json_file():
    # open json file
    with open('company.json', 'r') as json_file:
        json_data = json.load(json_file)

        # show bonus values
