# 1. Import same level directories
# import absolute_path
# import module_06 as md6 
# print(md6.calculate_circle(2))
# print(md6.calculate_square(2))

# from module_06 import calculate_circle
# print(calculate_circle(2))

# import relative_path
# from .module_06 import calculate_circle, calculate_square
# print(calculate_circle(2))
# run: python -m lesson_07.module_05


# 2. Import from child directory
# from package_01.module_01 import is_square
# from package_01 import module_01 as md1
# print(md1.is_square())

# from package_01.subpackage_01.module_07 import list_operations
# from package_01.subpackage_01 import module_07 as md7
# print(md7.list_operations([1,2,3], 2))


# 5. Define a function that accepts a number (n) and return n first number of Fibonacci sequences.
def Fibonacci(n):
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif n == 1:
        print("Fibonacci sequence upto", n,":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1