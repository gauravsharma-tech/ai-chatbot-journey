"""Math functions in Python
Python provides built-in functions to perform various mathematical operations. Here are some commonly used math functions:

# Absolute Value
abs(x)
Returns the absolute value of a number.

Example:-
num = -10
print(abs(num))  # Output: 10

# Power
pow(x, y)
Returns x raised to the power of y.
Example:-
base = 2
exponent = 3
print(pow(base, exponent))  # Output: 8

# Rounding
round(x, n)
Rounds a number to n decimal places (default is 0).
Example:-
num = 5.6789
print(round(num, 2))  # Output: 5.68

# Maximum and Minimum
max(a, b, c, ...)
Returns the largest of the given arguments.
min(a, b, c, ...)
Returns the smallest of the given arguments.
Example:-
a = 5
b = 10
c = 3
print(max(a, b, c))  # Output: 10
print(min(a, b, c))  # Output: 3

# Summation
sum(iterable)
Returns the sum of all elements in an iterable (like a list or tuple).
Example:-
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Output: 15

# Length
len(s)  
Returns the number of items in an object.
Example:-"""
s = "Hello"
print(len(s))  # Output: 5
# Example usage of math functions
t = -7.56
print(abs(t))          # Output: 7.56
print(pow(3, 4))      # Output: 81
print(round(3.14159, 3))  # Output: 3.142
print(max(1, 5, 3))   # Output: 5
print(min(1, 5, 3))   # Output: 1
print(sum([10, 20, 30]))  # Output: 60
print(len([1, 2, 3, 4, 5]))  # Output: 5
# Note: For more advanced mathematical functions, you can use the 'math' module in Python.
import math
print(math.sqrt(16))  # Output: 4.0
print(math.factorial(5))  # Output: 120

# Trigonometric functions
print(math.sin(math.pi / 2))  # Output: 1.0
print(math.cos(0))            # Output: 1.0
print(math.tan(math.pi / 4))  # Output: 1.0

# Logarithmic functions
print(math.log(100, 10))  # Output: 2.0
print(math.log(math.e))   # Output: 1.0

# Exponential function
print(math.exp(2))  # Output: 7.3890560989306495

# Hyperbolic functions
print(math.sinh(0))  # Output: 0.0
print(math.cosh(0))  # Output: 1.0
# Remember to import the math module to access these advanced functions.
# Note: For more advanced mathematical functions, you can use the 'math' module in Python.
import math
print(math.sqrt(16))  # Output: 4.0
print(math.factorial(5))  # Output: 120

# Trigonometric functions
print(math.sin(math.pi / 2))  # Output: 1.0
print(math.cos(0))            # Output: 1.0
print(math.tan(math.pi / 4))  # Output: 1.0

# Logarithmic functions
print(math.log(100, 10))  # Output: 2.0
print(math.log(math.e))   # Output: 1.0

# Exponential function
print(math.exp(2))  # Output: 7.3890560989306495

# Hyperbolic functions
print(math.sinh(0))  # Output: 0.0
print(math.cosh(0))  # Output: 1.0
# Remember to import the math module to access these advanced functions.
