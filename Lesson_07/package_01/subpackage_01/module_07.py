import sys
import os

# Case 6. Import module from grandparrent folder/directory/package
current = os.path.dirname(os.path.realpath(__file__))
parrent = os.path.dirname(current)
grand_parrent = os.path.dirname(parrent)
sys.path.append(grand_parrent)
# print(f'grand_parrent: {grand_parrent}')

# absolute_path
# from module_05 import *
# Fibonacci(10)
# import module_05 as md5
# md5.Fibonacci(5)

# relative path
# from ...module_05 import Fibonacci
# Fibonacci(6)


# Define a function that accepts 2 arguments: first argument is a list of integers, second argument is a number with default value is 3.
# Repeat the list by the number, then calculate average of all items in the list.
def list_operations(list, n=2):
    list = list * n
    aveg = sum(list) / len(list)
    return aveg

# print(list_operations([1,2,3], 2))