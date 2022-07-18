# 2. Define a function to check whether a number from keyboard is a square number.
import math
import sys
import os

# 1. Import module from parrent folder
current = os.path.dirname(os.path.realpath(__file__))
# print(f'current: {current}')
parrent = os.path.dirname(current)
# print(f'parrent: {parrent}')
sys.path.append(parrent)

# import module_05 as md5
# md5.Fibonacci(4)

# from ..module_05 import Fibonacci
# Fibonacci(9)

# # 2. Import module from current folder
# from module_02 import operation
# print(operation(2,3))

# 3. Import module from other package
from package_02.module_03 import is_valid_triangle
print(is_valid_triangle(2,3,4))


def is_square():
    number = int(input("Enter the Number: "))
    sq_root = int(math.sqrt(number))
    return (sq_root*sq_root) == number