'''Bài 1:
Đảo ngược một list trong Python:
Ví dụ: 
100, 200, 300, 400, 500] --> [500, 400, 300, 200, 100]
'''
# Solution 1: list function reverse()
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

# Solution 2: Using negative slicing
list1 = [100, 200, 300, 400, 500]
list1 = list1[::-1]
print(list1)

'''Bài 2: Viết chương trình cộng hai danh sách (các phần tử kiểu string) theo index. Tạo một danh sách mới bằng cách cộng các phần từ tại vị trí tương ứng của 2 danh sách với nhau.
Ví dụ: 
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
--> ['My', 'name', 'is', 'Kelly']
'''
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

'''Bài 3: Cho một danh sách các số. Tạo danh sách mới bằng cách bình phương mỗi phần tử của danh sách đó.
Ví dụ: 
numbers = [1, 2, 3, 4, 5, 6, 7]
--> [1, 4, 9, 16, 25, 36, 49]
'''
# Solution 1: Using loop and list method
numbers = [1, 2, 3, 4, 5, 6, 7]
# result list
res = []
for i in numbers:
    # calculate square and add to the result list
    res.append(i * i)
print(res)

# Solution 2: Use list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7]
res = [x * x for x in numbers]
print(res)

'''Bài 4: Cho 2 danh sách. Viết chương trình lặp đồng thời cả hai danh sách và hiển thị các phần tử của danh sách 1 theo thứ tự ban đầu và các phần tử của danh sách 2 theo thứ tự ngược lại.
Ví dụ: 
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
--> 
10 400
20 300
30 200
40 100
'''
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2.reverse()):
    print(x, y)

'''Bài 5: Xóa các chuỗi rỗng khỏi danh sách các chuỗi
Ví dụ:
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
--> ["Mike", "Emma", "Kelly", "Brad"]
'''
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)

'''Bài 6: Viết chương trình thêm sô 7000 vào sau số 6000 trong Danh sách sau:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
--> [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
'''
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

'''Bài 7: Cho một danh sách lồng nhau. 
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Viết chương trình mở rộng nó bằng cách thêm danh sách con ["h", "i", "j"] sao cho nó giống như danh sách sau.
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
'''
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)

'''Bài 8: Viết chương trình tìm giá trị 20 trong danh sách, nếu có thì thay bằng 200. Chỉ cập nhật lần xuất hiện đầu tiên của no.
Ví dụ:
list1 = [5, 10, 15, 20, 25, 50, 20]
--> [5, 10, 15, 200, 25, 50, 20]
'''
list1 = [5, 10, 15, 20, 25, 50, 20]

# get the first occurrence index
index = list1.index(20)

# update item present at location
list1[index] = 200
print(list1)

'''Bài 9: Viết chương trình loại bỏ tất cả các lần xuất hiện của số 20 trong list:
Ví dụ:
list1 = [5, 20, 15, 20, 25, 50, 20]
--> [5, 15, 25, 50]
'''
# Solution 1: Use the list comprehension
list1 = [5, 20, 15, 20, 25, 50, 20]

# list comprehension
# remove specific items and return a new list
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

res = remove_value(list1, 20)
print(res)

# Solution 2: while loop (slow solution)
list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)