'''
1. Open file
2. Write file
3. Close
'''

# Method 1
# file_w = open('test_rw.txt', 'w', encoding='utf-8')
# file_w.write('2. Write file')
# file_w.close()

# Method 2
# with open('test_rw.txt', 'w', encoding='utf-8') as file_w:
#     file_w.write("file_w = open('test_rw.txt', 'w', encoding='utf-8')")

# Handline exception
# try:
#     with open('test_rw.txt', 'w', encoding='utf-8') as file_w:
#         file_w.write("file_w = open('test_rw.txt', 'w', encoding='utf-8')")
# except:
#     print('Error writing file')

# Write file line by line
# lines = ["print('Error writing file')\n", "# Handline exception\n", "# Method 1\n"]
# try:
#     with open('test_rw.txt', 'w', encoding='utf-8') as file_w:
#         file_w.writelines(lines)
# except:
#     print('Error writing file')

# Append mode
# lines = ["print('Error writing file')\n", "# Handline exception\n", "# Method 1\n"]
# try:
#     with open('test_rw.txt', 'a', encoding='utf-8') as file_w:
#         file_w.writelines(lines)
# except:
#     print('Error writing file')

# Mode for simultaneous read/write: w+/r+
lines = ["print('Error writing file')\n", "# Handline exception\n", "# Method 1\n"]
try:
    with open('test_rw.txt', 'r+', encoding='utf-8') as file_rw:
        # read content
        current_content = file_rw.readlines()
        print(current_content)
        # write content
        file_rw.writelines(lines)
except:
    print('Error writing file')