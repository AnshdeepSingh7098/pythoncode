"""Recursion is a method of solving problems where a function calls itself as a subroutine. 
This allows the function to be repeated several times as it breaks down the problem into 
smaller, more manageable pieces."""
def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
    n (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the number n.
    """
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Test
print(factorial(5))  # Output: 120

# F(n) = F(n-1) + F(n-2)
def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Parameters:
    n (int): The position in the Fibonacci sequence.

    Returns:
    int: The nth Fibonacci number.
    """
    if n == 0:  # Base case 1
        return 0
    elif n == 1:  # Base case 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Test
print([fibonacci(i) for i in range(10)])  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def sum_list(lst):
    """
    Calculate the sum of all elements in a list.

    Parameters:
    lst (list): The list of numbers to sum.

    Returns:
    int: The sum of all elements in the list.
    """
    if not lst:  # Base case: empty list
        return 0
    else:
        return lst[0] + sum_list(lst[1:])  # Recursive case

# Test
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
