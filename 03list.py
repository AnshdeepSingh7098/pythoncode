# Creating a list
my_list = [1, 2, 3]

# Adding elements
print("Original list:", my_list)
my_list.append(4)
print("After append(4):", my_list)
my_list.extend([5, 6,99])
print("After extend([5, 6]):", my_list)
my_list.insert(2, 99)
print("After insert(2, 99):", my_list)

# Removing elements
my_list.remove(99) #remove the firt occurence of the value we enter inside the remove function
print("after remove(99):", my_list)
removed_item = my_list.pop(0) #remove the index we enter inside the pop function
print("after pop(0):", my_list)
my_list.clear()
print(my_list)

# Searching and counting
my_list = [1, 2, 3, 2, 1]
print(my_list.index(2))  # Output: 1 #index function return the first index of the value we enter inside the function
print(my_list.count(2))  # Output: 2 #count function return the number of occurence of the value we enter inside the function

# Sorting and reversing
my_list.sort() #sort the list in ascending order 
print(my_list)
my_list = [1, 2, 3, 1]
my_list.reverse() #reverse the list
print(my_list)
my_list.sort(reverse=True)
print(my_list)
# Copying
new_list = my_list.copy()
print(new_list)