import math
# Bài 1. Định nghĩa hàm nhận vào 2 giá trị và trả về tổng, phép chia, phép trừ và phép nhân 
# (sử dụng ngoại lệ cho phép chia).
def calculate(num_1, num_2):
    sum = num_1 + num_2
    sub = num_1 - num_2
    mul = num_1 * num_2
    
    # Kiểm tra xem có thực hiện được phép chia hay ko?
    # code ở đây
    if num_2 != 0:
        div = num_1 / num_2
        return sum, div, sub, mul
    print(f'Num_2 = 0. Không thể thực hiện phép chia cho số 0')
    div = None
    return sum, div, sub, mul
    # kết thúc code

# Test function
# first_num = 10
# second_num = 20
# sum_, div_, sub_, mul_ = calculate(num_1=first_num, num_2=second_num)
# print(f'Sum_: {sum_}')
# print(f'Div: {div_}')
# print(f'sub_: {sub_}')
# print(f'mul_: {mul_}')

# Bài 2. Định nghĩa hàm kiểm tra xem một số từ bàn phím có phải là số chính phương hay không.
def is_square():
    number = int(input(('Hãy nhập 1 số nguyên dương bất kì: ')))
    sq_root = int(math.sqrt((number)))
    # return (sq_root*sq_root == number)
    if sq_root*sq_root == number:
        print(f'Số vừa nhập là số chính phương')
        return True
    print(f'Số vừa nhập không phải là số chính phương')
    return False

# Test function
# check_square = is_square()


# Bài 3. Xác định hàm nhận vào 3 đối số, sau đó kiểm tra xem có tồn tại tam giác được tạo bởi chúng hay không. 
# Trả lại kết quả.
def is_valid_triangle(a, b, c):
    # if a > 0 and b > 0 and c > 0:
    if a + b > c and b + c > a and c + a > b:
        print(f'Có tam giác được tạo thành')
        return True
    print(f'Không có tam giác được tạo thành')
    return False

# Test function
# a, b, c = 10, 13, 9
# is_valid_triangle(a, b, c)


# Bài 4. Định nghĩa một hàm nhận vào một đối số chuỗi và trả về số lượng nguyên âm và phụ âm.
def count_characters(sequence):
    num_vowels = 0
    num_consonants = 0
    list_vowels = ['a', 'e', 'i', 'o', 'u']
    list_consonants = \
        ['ă', 'â', 'b', 'c', 'd', 'ê', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ô', 'ơ', 'p', 'q', 'r', \
            's', 't', 'x', 'u', 'v', 'y', 'z']
    for c in sequence:
        if c.lower() in list_vowels:
            print(c)
            num_vowels += 1
        elif c.lower() in list_consonants:
            num_consonants += 1
        else:
            continue
    print(f'Number of vowels: {num_vowels}')
    print(f'Number of consonants: {num_consonants}')
    return num_vowels, num_consonants

# Test function
# sequence = 'Bài 4. Định nghĩa một hàm nhận vào một đối số chuỗi và trả về số lượng nguyên âm và phụ âm.'
# count_characters(sequence)

# Bài 5. Định nghĩa một hàm nhận vào một số (n) và trả về n số đầu tiên của dãy Fibonacci.
def cal_fibonaci(n):
    n_1, n_2 = 0, 1 # Khởi tạo 2 giá trị đầu tiên của dãy FB
    count_fb = 2
    list_fb = []
    if n == 1:
        list_fb.append(n_1)
    else:
        list_fb.append(n_1)
        list_fb.append(n_2)
        while count_fb < n:
            n_th = n_1 + n_2 # Kể từ số thứ 3 trở đi, số hiện tại bằng tổng của 2 số liền trước nó
            list_fb.append(n_th)
            n_1 = n_2
            n_2 = n_th
            count_fb += 1
    return list_fb

# Test function
# list_fb = cal_fibonaci(4)
# print(list_fb)


# Bài 6. Định nghĩa một hàm nhận vào đối số bán kính và trả về diện tích và chu vi.

# Bài 7. Định nghĩa một hàm nhận vào 2 đối số: đối số thứ nhất là danh sách các số nguyên, đối số thứ hai 
# là một số có giá trị mặc định là 3.
# Lặp lại danh sách theo giá trị của tham số thứ 2, sau đó tính giá trị trung bình của tất cả các mục trong 
# danh sách.
def list_operations(list_nums, n=3):
    list_nums = list_nums * n
    avg = sum(list_nums) / len(list_nums)

    return avg

# Test function
list_nums = [1, 4, 6, 3]
avg = list_operations(list_nums)
print(f'Avg: {avg}')
