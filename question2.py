# Question 2: Complex Conditional Evaluation

# TODO: Input x, y, z
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
z = int(input("Enter a value for z: "))

# TODO: Create conditions:
#   is_even = True if x is even
#   is_positive = True if y > 0
#   is_in_range = True if z between 10 and 50
is_even = (x % 2 == 0)
is_positive = (y > 0)
is_in_range = (10 <= z <= 50)
print(is_even)
print(is_positive)
print(is_in_range)

# TODO: Create final_condition = is_even and is_positive and is_in_range
final_condition = is_even and is_positive and is_in_range

# TODO: Print final_condition
print(f"Final condition is {final_condition}")

