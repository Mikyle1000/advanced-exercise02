# Question 3: Grading with Adjustments

# TODO: Input score from user
base_score = int(input("Enter your base score: "))

# TODO: Apply adjustments
new_score = base_score + 5 - 10

# TODO: Clamp score between 0 and 100
# max(0, ...) ensures it doesn't drop below 0
# min(100, ...) ensures it doesn't exceed 100
final_score = max(0, min(100, new_score))

# TODO: Use if-elif-else to determine grade and print it
if final_score >= 90:
    grade = "A"
elif final_score >= 80:
    grade = "B"
elif final_score >= 70:
    grade = "C"
elif final_score >= 60:
    grade = "D"
else:
    grade = "F"

# TODO: Use if-elif-else to determine grade and print it
print(f"Final Adjusted Score: {final_score}")
print(f"Assigned Grade: {grade}")