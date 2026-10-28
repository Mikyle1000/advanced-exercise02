# Question 4: Advanced Calculator

# TODO: Input num1, num2
num1 = int(input("Enter a value (num1): "))
num2 = int(input("Enter a value (num2): "))

# TODO: Input operation
operation = input("Enter an operation (+, -, *, /, %): ")

# TODO: Match operation using if-elif
if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == "%":
    try:
        modulus = num1%num2
        print(f"{num1} % {num2} = {modulus}")
    except ZeroDivisionError:
        print("Invalid value")
elif operation == "/":
    try:
        result = num1/num2
        print(f"{num1} / {num2} = {result}")
    except ZeroDivisionError:
        print("You cannot divide by zero")
else:
    print(num1/num2)

    