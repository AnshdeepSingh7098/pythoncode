# Initial sets
a = {1, 2, 3} #set is collection of unordered and unindexed elements enclosed in curly brackets. The are mutable
b = {3, 4, 5}
c = {5, 6, 7}

# 1. Adding and Removing Elements
a.add(6)  # Adds 6 to a
print("After add:", a)  # {1, 2, 3, 6}

a.remove(2)  # Removes 2 from a
print("After remove:", a)  # {1, 3, 6}

a.discard(10)  # main difference btw remove and discard is that if we try to remove the element which is not present in the set then remove will give an error but discard will not give any error 
print("After discard (non-existing):", a)  # {1, 3, 6}

removed = a.pop()  # Removes an arbitrary element
print(f"Popped element: {removed}, After pop:", a)

a.clear()  # Empties a
print("After clear:", a)  # set()

# Reinitialize a for further operations
a = {1, 2, 3}

# 2. Set Operations
u = a.union(b)  # Union of a and b
print("Union:", u)  # {1, 2, 3, 4, 5}

i = a.intersection(b)  # Intersection of a and b
print("Intersection:", i)  # {3}

d = a.difference(b)  # Difference between a and b
print("Difference:", d)  # {1, 2}

sd = a.symmetric_difference(b)  # Symmetric difference
print("Symmetric Difference:", sd)  # {1, 2, 4, 5}

# 3. Updating Sets
a.update(c)  # Add elements from c to a
print("After update:", a)  # {1, 2, 3, 5, 6, 7}

a.intersection_update(b)  # Keep only elements also in b
print("After intersection_update:", a)  # {5}

a = {1, 2, 3}  # Reset a
a.difference_update(b)  # Remove elements found in b
print("After difference_update:", a)  # {1, 2}

a = {1, 2, 3}  # Reset a
a.symmetric_difference_update(b)  # Symmetric difference update
print("After symmetric_difference_update:", a)  # {1, 2, 4, 5}

# 4. Membership and Comparison
print("Is a disjoint with b?", a.isdisjoint(c))  # False
print("Is a a subset of c?", a.issubset(c))  # False
print("Is c a superset of a?", c.issuperset(a))  # False

# 5. Copying
d = c.copy()  # Create a shallow copy of c
print("Copied d from c:", d)  # {5, 6, 7}
