my_list = [1, 2, 3, 4]
for item in my_list: #iterating through list
    print(item)

# Loop through numbers 0 to 4
for i in range(5):
    print(i)

# Loop through numbers 1 to 4
for i in range(1,5):
    print(i)

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Loop through each character in a string
for char in "hello":
    print(char)

# Loop through keys and values in a dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in person.items():
    print(f"{key}: {value}")

for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

for i in range(5):
    if i == 3:
        continue  # Skip the current iteration when i is 3
    print(i)

#nested loop
# Loop through a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix: 
    for element in row: 
        print(element, end=" ")
    print()


fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits): # enumerate function return the index and value of the list
    print(f"{index}: {fruit}")

names = ['Alice', 'Bob', 'Charlie'] 
ages = [25, 30, 35]
for name, age in zip(names, ages): #zip function return the value of the list in the form of tuple 
    print(f"{name} is {age} years old")

# Create a new list with squared values
squared = [x**2 for x in range(5)]
print(squared)

# pyramid
n=int(input('enter the no.:'))
for i in range(1,n+1):
    print(" "*(n-i),end = '')
    print("*"*(2*i-1),end="")
    print("")
  
# half pyramid
n=int(input('enter the no.:'))
for i in range(1,n+1):
    print("*"*i,end="")
    print("")

n=int(input('enter the no.:'))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print('*'*i,end="")
    print("")

n=int(input('enter the no.:'))
for i in range(1,n+1):
    if (i==1 or i==n):
        print("* "*n,end=" ")
    else:
        print("*",end="")
        print(" "*(n+2),end="")    
        print("*",end="")
    print("")

n=int(input('enter the no.:'))
for i in range(11,0,-1):
    print(f"{n}*{i}={n*i}")