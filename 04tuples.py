t = (1, 2, 3, 2, 2) #tuple is a collection of ordered and unchangeable elements enclosed in parentheis  
s=t.count(2) #count function return the number of occurence of the value we enter inside the function
print(s)

t = (1, 2, 3, 2)
s=t.index(2) #index function return the first occurance of the value we enter inside the function
print(s)

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # cocatenation of two tuples

t = (1, 2)
print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)

t = (1, 2, 3)
print(2 in t)  # Output: True
print(4 in t) # output: False
print(4 not in t) # output: True

t = (1, 2, 3)
for item in t:
    print(item)
