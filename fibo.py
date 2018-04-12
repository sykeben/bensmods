# Ben's Modules Fibonacci Module
# (C)2018 - Ben Sykes

# This is a more useful version of the "fibo" module
# from the "Modules" portion of the Python docs.

def genfib(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result