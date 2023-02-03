'''
1. Open file
2. Read file
3. Close
'''

# Method 1
# # 1. Open file to read content
# file_o = open('test_rw.txt', 'r', encoding='utf-8')
# # Read content
# content = file_o.read()
# print(content)
# # Close file
# file_o.close()

# Method 2
# with open('test_rw.txt', 'r', encoding='utf-8') as file_o:
#     content = file_o.read()
#     print(content)

# Handle exception
value_config = []
try:
    with open('test_rw.txt', 'r', encoding='utf-8') as file_o:
        content = file_o.read()
        print(content)
except FileNotFoundError:
    print('File not found')
    file_o.close()

# Read file line by line and process
value_config = []
try:
    with open('test_rw.txt', 'r', encoding='utf-8') as file_o:
        # content = file_o.read()
        content = file_o.readlines()
        for line in content:
            value = line.split(':')[1].strip()
            value_config.append(value)
            print(value)
        # print(content)
except FileNotFoundError:
    print('File not found')
    file_o.close()
# return value_config
