import pytest
import mock
import builtins
from unit_test_practice import *

# def test_capital_str():
#     assert capital_str('python07') == 'Python07'

# def test_validation_input():
#     with pytest.raises(TypeError):
#         capital_str(8)

def test_operations():
    assert operation(4, 10) == [14, 0.4, -6, 40]

def test_is_square():
    with mock.patch.object(builtins, 'input', lambda _: 7):
        assert is_square() == False

def test_is_valid_triangle():
    assert is_valid_triangle(3, 4, 5) == True

def test_count_characters():
    assert count_characters('hello') == [2, 3]

def test_Fibonacci():
    assert Fibonacci(6) == [0, 1, 1, 2, 3, 5]

def test_calculate_circle():
    assert calculate_circle(4) == [50.24, 25.12]

def test_list_operations():
    assert list_operations([1,2,3], 3) == 2