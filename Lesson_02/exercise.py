'''Bài 1: 
Viết chương nhập 2 số từ bàn phím. Tính và in ra giá trị tổng, tích, hiệu, thương của chúng (có kiểm tra điều kiện)
'''

num1 = int(input('Num1: '))
num2 = int(input('Num2: '))

print(f'Tong: {num1 + num2}')
print(f'Tich: {num1 * num2}')
print(f'Hieu: {num1 - num2}')

if num2 == 0:
    print('Không thể thực hiện phép chia cho số 0')
else:
    print(f'Thương: {num1/num2}')




'''Bài 2:
Viết chương trình lặp lại 10 số đầu tiên và trong mỗi lần lặp, in ra tổng của số hiện tại và số trước đó.
'''

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i


'''Bài 3: Viết chương trình nhận một chuỗi từ người dùng và hiển thị các ký tự có ở số chỉ mục chẵn.
Ví dụ: str = "pynative" thì bạn nên hiển thị ‘p’, ‘n’, ‘t’, ‘v’.'''

# accept input string from a user
word = input('Enter word: ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])


'''Bài 4:
Viết chương trình in dãy số sau bằng vòng lặp.
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")

'''Bài 5: 
Viết chương trình nhận một số từ người dùng và tính tổng tất cả các số từ 1 đến một số đã cho.
Ví dụ: nếu người dùng nhập 10 thì đầu ra phải là 55 (1+2+3+4+5+6+7+8+9+10)
'''
# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)


'''Bài 6: Viết chương trình in bảng nhân của một số cho trước
Ví dụ: num = 2 nên đầu ra phải là:
2
4
6
8
10
12
14
16
18
20
'''
n = 2
# stop: 11 (because range never include stop number in result)
# run loop 10 times
for i in range(1, 11, 1):
    # 2 *i (current number)
    product = n * i
    print(product)


'''Bài 7:
Viết chương trình đếm tổng các chữ số của một số bằng vòng lặp while.
Ví dụ: số là 75869, vì vậy đầu ra phải là 5.
'''
num = 75869
count = 0
while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10

    # increment counter by 1
    count = count + 1
print("Total digits are:", count)

'''Bài 8: Viết chương trình sử dụng vòng lặp for để in dãy số đảo ngược sau:
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()


'''Baif 8: Viết chương trình Hiển thị các số từ -10 đến -1 bằng vòng lặp for.
'''
for num in range(-10, 0, 1):
    print(num)

'''Bài 9: Viết chương trình hiển thị tất cả các số nguyên tố trong một phạm vi (tự định nghĩa)
'''
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)

'''Bài 10: Viết chương trình Hiển thị dãy Fibonacci lên đến 10 số hạng
'''
# first two numbers
num1, num2 = 0, 1

print("Fibonacci sequence:")
# run loop 10 times
for i in range(10):
    # print next number of a series
    print(num1, end="  ")
    # add last two numbers to get next number
    res = num1 + num2

    # update values
    num1 = num2
    num2 = res

'''Bài 11: Viết chương trình Đảo ngược 1 số nguyên
Given: 76542
Expected output: 24567
'''
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)

'''Bài 12: Viết chương trình in mẫu bắt đầu sau bằng vòng lặp for:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


str_test = "This is a \" in a string"
if str_test == 'This is a " in a string':
    abcc