# simple sample

def capital_str(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string input')
    return x.capitalize()

# practice
# 1. Define a function that accepts 2 values and returns its sum, division, subtraction and multiplication (use exceptions for division).
# from __future__ import division
from re import A, sub

def operation(value_1, value_2):
    sum = value_1 + value_2
    try:
        division = value_1 / value_2
    except ValueError:
        print("Value 2 is zero, divisision is not possible")
    subt = value_1 - value_2
    mult = value_1 * value_2

    return [sum, division, subt, mult]

# 2. Define a function to check whether a number from keyboard is a square number.
import math

def is_square():
    number = int(input("Enter the Number"))

    sq_root = int(math.sqrt(number))
    return (sq_root*sq_root) == number

# 3. Define a function that accepts 3 arguments, then check whether exist a triangle which is created by them. Return the result.
def is_valid_triangle(a, b, c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

# 4. Define a function that accepts one string argument and returns number of vowels and consonants.
def count_characters(word):
    vowels=0
    consonants=0
    for i in word:
        if i in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    print("The number of vowels:", vowels)
    print("\nThe number of consonant:", consonants)
    return [vowels, consonants]

# 5. Define a function that accepts a number (n) and return n first number of Fibonacci sequences.
def Fibonacci(n):
    # first two terms
    n1, n2 = 0, 1
    count = 0
    list_fibo = []

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
            list_fibo.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
        return list_fibo


# 6. Define a function that accepts a radius argument and returns area and perimeter.
def calculate_circle(radius):
    area = radius * radius * 3.14
    peri = 2 * radius * 3.14
    return [area, peri]

# 7. Define a function that accepts 2 arguments: first argument is a list of integers, second argument is a number with default value is 3.
# Repeat the list by the number, then calculate average of all items in the list.
def list_operations(list, n=2):
    list = list * n
    aveg = sum(list) / len(list)
    return aveg

# print(list_operations([1,2,3], 2))