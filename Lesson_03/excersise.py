'''Bài 1: Viết chương trình tạo một chuỗi mới gồm ký tự đầu tiên, giữa và cuối cùng của chuỗi đầu vào.
Ví du: "James" --> "Jms"
'''
str1 = 'James'
print("Original String is", str1)

# Get first character
res = str1[0]

# Get string size
l = len(str1)
# Get middle index number
mi = int(l / 2)
# Get middle character and add it to result
res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String:", res)

'''Bài 2: Cho hai chuỗi s1 và s2. Viết chương trình tạo một chuỗi mới s3 bằng cách thêm s2 vào giữa s1.
Ví du: 
s1 = "Ault"
s2 = "Kelly"
--> AuKellylt
'''
s1 = "Ault"
s2 = "Kelly"
print("Original Strings are", s1, s2)

# middle index number of s1
mi = int(len(s1) / 2)

# get character from 0 to the middle index number from s1
x = s1[:mi:]
# concatenate s2 to it
x = x + s2
# append remaining character from s1
x = x + s1[mi:]
print("After appending new string in middle:", x)


'''Bài 3: Chuỗi đã cho chứa tổ hợp chữ thường và chữ hoa. Viết chương trình sắp xếp các ký tự của một chuỗi sao cho tất cả các chữ cái viết thường sẽ xuất hiện trước.
Ví du: 'PyNaTive' --> 'yaivePNT'
'''
str1 = "PYnAtivE"
print('Original String:', str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase characters to lower list
        lower.append(char)
    else:
        # add uppercase characters to lower list
        upper.append(char)

# Join both list
sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)

'''Bài 4: Đếm tất cả các chữ cái, chữ số và ký hiệu đặc biệt từ một chuỗi đã cho.
Ví dụ: 
"P@#yn26at^&i5ve" -->

Total counts of chars, digits, and symbols 
Chars = 8 
Digits = 3 
Symbol = 4
'''
sample_str = "P@yn2at&#i5ve"
char_count = 0
digit_count = 0
symbol_count = 0
for char in sample_str:
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit_count += 1
    # if it is not letter or digit then it is special symbol
    else:
        symbol_count += 1
print("total counts of chars, Digits, and symbols \n")
print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)


'''Bài 5: Viết chương trình tìm tất cả các lần xuất hiện của “USA” trong một chuỗi đã cho, bỏ qua trường hợp này.
Ví duj: 
"Welcome to USA. usa awesome, isn't it?" --> The USA count is: 2
'''
str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

# convert string to lowercase
temp_str = str1.lower()

# use count function
count = temp_str.count(sub_string.lower())
print("The USA count is:", count)

'''Bài 6: Cho một chuỗi s1, hãy viết chương trình trả về tổng và trung bình cộng của các chữ số xuất hiện trong chuỗi, bỏ qua tất cả các ký tự khác.
Ví dụ: 
str1 = "PYnative29@#8496" --> Sum is: 38 Average is  6.333333333333333
'''
input_str = "PYnative29@#8496"
total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)

'''Bài 7: Viết chương trình đếm số lần xuất hiện của tất cả các ký tự trong một chuỗi
Ví duj: 
str1 = "Apple" --> {'A': 1, 'p': 2, 'l': 1, 'e': 1}
'''
str1 = "Apple"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)

'''Bài 8: Viết chương trình tìm vị trí cuối cùng của chuỗi con “Emma” trong một chuỗi đã cho.
"Emma is a data scientist who knows Python. Emma works at google."
'''
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Original String is:", str1)

index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", index)

'''Bài 9: Viết chương trình tách một chuỗi đã cho trên dấu gạch nối và hiển thị từng chuỗi con.
Ví dụ: 
str1 = Emma-is-a-data-scientist --> 

Emma
is
a
data
scientist
'''
str1 = "Emma-is-a-data-scientist"
print("Original String is:", str1)

# split string
sub_strings = str1.split("-")

print("Displaying each substring")
for sub in sub_strings:
    print(sub)

'''Bài 10: Xóa tất cả các ký tự khỏi một chuỗi ngoại trừ số nguyên
Ví dụ: 
str1 = 'I am 25 years and 10 months old' --> 2510
'''
str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)

# Retain Numbers in String
# Using list comprehension + join() + isdigit()
res = "".join([item for item in str1 if item.isdigit()])

print(res)