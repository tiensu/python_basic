# 1. Define a function that accepts 2 values and returns its sum, division, subtraction and multiplication (use exceptions for division).
from __future__ import division
from re import A, sub

def operation(value_1, value_2):
    sum = value_1 + value_2
    try:
        division = value_1 / value_2
    except ValueError:
        print("Value 2 is zero, divisision is not possible")
    subt = value_1 - value_2
    mult = value_1 * value_2

    return sum, division, subt, mult