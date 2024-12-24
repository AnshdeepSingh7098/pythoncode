
#A function is a block of reusable code designed to perform a 
# specific task. Functions are fundamental building blocks in 
# programming and allow for code modularity and reusability.
# structure of function
# def function_name(parameters):
#     """
#     Optional docstring: This describes what the function does.
#     """
#     # Body of the function
#     # Code to execute
#     return value  # Optional: Returns a result

def say_hello():
    """
    Prints a greeting message.
    """
    print("Hello, World!")

# Call the function
say_hello()
def greet(name): #function with parameters
    """
    Greets a person with their name.
    """
    print(f"Hello, {name}!")

greet("Alice")

def add(a, b): #functon with parameters and return statement 
    """
    Returns the sum of two numbers.
    """
    return a + b

result = add(5, 3)
print(result)  # Output: 8

def greet(name="Guest"): #function with default parameters
    """
    Greets a person with a default name if none is provided.
    """
    print(f"Hello, {name}!")

greet()        # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!


"""*args is used to pass a variable number of positional arguments to a function.
 It collects all the extra positional arguments passed to the function and stores
   them as a tuple."""
def sum_all(*args):
    """
    Returns the sum of all arguments.
    """
    return sum(args)

# Calling the function
print(sum_all(1, 2, 3, 4))  # Output: 10
print(sum_all(10, 20))      # Output: 30

"""**kwargs is used to pass a variable number of keyword arguments (arguments with names) to a function. 
It collects all the extra keyword arguments and stores them as a dictionary."""
def print_details(**kwargs):
    """
    Prints key-value pairs of details.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function
print_details(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York

def display_info(*args, **kwargs):
    """
    Displays positional and keyword arguments.
    """
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

# Calling the function
display_info(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments (args): (1, 2, 3)
# Keyword arguments (kwargs): {'name': 'Alice', 'age': 25}


def greet(name, age, city):
    print(f"Hello, {name}! You are {age} years old and live in {city}.")

# Using unpacking
person_info = ("Alice", 25, "New York")
greet(*person_info)#unpacking tuple

details = {"name": "Bob", "age": 30, "city": "Los Angeles"}
greet(**details)#upacking dictionary

def process_data(required, *args, **kwargs):
    """
    Processes required, positional, and keyword arguments.
    """
    print("Required argument:", required)
    print("Additional positional arguments (args):", args)
    print("Additional keyword arguments (kwargs):", kwargs)

# Calling the function
process_data(
    "Mandatory",
    1, 2, 3,
    name="Charlie", age=35, city="Chicago"
)
# Output:
# Required argument: Mandatory
# Additional positional arguments (args): (1, 2, 3)
# Additional keyword arguments (kwargs): {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}

# funtion with multiple 
def multiply(a, b):
    return a * b

print(multiply(2, 3))  # Output: 6
print(multiply(4, 5))  # Output: 20

# function to get input from user
def get_input():
    return int(input("Enter a number: "))

def calculate_square(num):
    return num ** 2

def display_result(result):
    print(f"The square is {result}")

# Main program
number = get_input()
square = calculate_square(number)
display_result(square)


import math

def calculate_circle_area(radius):
    """
    Calculates and returns the area of a circle given its radius.
    """
    if radius < 0:
        return "Invalid radius"
    return math.pi * radius ** 2

# Example usage
r = 5
area = calculate_circle_area(r)
print(f"The area of a circle with radius {r} is {area:.2f}")

# Lambda Functions (Anonymous Functions)
# A single-line function defined with the lambda keyword.

square = lambda x: x ** 2
print(square(4))  # Output: 16


def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x ** 2, 5)
print(result)  # Output: 25






# c/5=(f-32)/9  celsius to farhenheit
def celsius_to_farhenheit(celsius):
    return (celsius * 9/5) +32

celsius=float(input("enter the celsius value:"))
farhenheit=celsius_to_farhenheit(celsius)
print(f"{celsius} degree celsius is equal to {farhenheit} degree farhenheit")

# f to celsius
def farhenheit_to_celsius(farhenheit):
    return (farhenheit - 32) * 5/9

farhenheit = float(input("Enter the farhenheit value:"))
celsius = farhenheit_to_celsius(farhenheit)
print(f"{farhenheit} degree farhenheit is equal to {celsius:.2f} degree celsius")
