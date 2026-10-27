# Question 1: Multi-Step Arithmetic Operations
import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
a += 3

# TODO: Multiply b by 2 using *=
b *= 2 

# TODO: Modulo c by 4 using %=
c %= 4

# TODO: Calculate the square root of (a^2 + b^2 + c^2)
square_root = math.sqrt(a**2 + b**2 + c**2)

# TODO: Print the final result rounded to 2 decimal places
rounding = round(square_root, 2)
print(rounding)
