my_list = [1, 2, 3, 4]
for item in my_list:  # Iterate through each item in the list
    print(item)

# Loop through numbers 0 to 4
for i in range(5):
    print(i)

# Loop through numbers 1 to 4
for i in range(1, 5):
    print(i)

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:  # Iterate through each fruit in the list
    print(fruit)

# Loop through each character in a string
for char in "hello":
    print(char)

# Loop through keys and values in a dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in person.items():  # Iterate through dictionary items
    print(f"{key}: {value}")

for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

for i in range(5):
    if i == 3:
        continue  # Skip the current iteration when i is 3
    print(i)

# Nested loop
# Loop through a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:  # Iterate through each row in the matrix
    for element in row:  # Iterate through each element in the row
        print(element, end=" ")
    print()

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):  # Use enumerate to get index and value of the list
    print(f"{index}: {fruit}")

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):  # Use zip to iterate through lists in tuples
    print(f"{name} is {age} years old")

# Create a new list with squared values using list comprehension
squared = [x**2 for x in range(5)]
print(squared)

# Pyramid pattern
n = int(input('Enter the number of rows: '))
for i in range(1, n + 1):
    print(" " * (n - i), end='')
    print("*" * (2 * i - 1), end="")
    print()

# Half pyramid pattern
n = int(input('Enter the number of rows: '))
for i in range(1, n + 1):
    print("*" * i, end="")
    print()

# Inverted half pyramid pattern
n = int(input('Enter the number of rows: '))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print('*' * i, end="")
    print()

# Hollow square pattern
n = int(input('Enter the size of the square: '))
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * n, end=" ")
    else:
        print("*", end="")
        print(" " * (n + 2), end="")
        print("*", end="")
    print()

# Multiplication table
n = int(input('Enter a number for the multiplication table: '))
for i in range(11, 0, -1):
    print(f"{n} * {i} = {n * i}")
