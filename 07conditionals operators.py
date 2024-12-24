# value_if_true if condition else value_if_false

x, y = 10, 20
max_value = x if x > y else y
print("Max:", max_value)  # Output: Max: 20

x, y, z = 10, 20, 15
max_value = x if x > y and x > z else (y if y > z else z)
print("Max:", max_value)  # Output: Max: 20

age = 18
eligibility = "Eligible" if age >= 18 else "Not Eligible"
print(eligibility)  # Output: Eligible

numbers = [1, 2, 3, 4]
result = "Even" if sum(numbers) % 2 == 0 else "Odd"
print(result)  # Output: Even

print("Positive" if x > 0 else "Non-Positive")  # Output depends on x

# Incorrect
# result = "Positive" if x > 0  # SyntaxError

# Correct
result = "Positive" if x > 0 else "Non-Positive"

# Incorrect
# result = x > 0 ? "Positive" : "Non-Positive"  # Not Python syntax

# Correct
result = "Positive" if x > 0 else "Non-Positive"

