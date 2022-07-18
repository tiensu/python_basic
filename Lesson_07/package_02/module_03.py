# 3. Define a function that accepts 3 arguments, then check whether exist a triangle which is created by them. Return the result.
def is_valid_triangle(a, b, c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False