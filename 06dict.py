my_dict = {"a": 1, "b": 2} # dict is collection of unordered, changeable and indexed elemnents enclosed in curly brackets
my_dict.clear()
print(my_dict)  # Output: {}

my_dict = {"a": 1, "b": 2}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'a': 1, 'b': 2}

keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

my_dict = {"a": 1, "b": 2}
print(my_dict.get("a"))  # Output: 1 main difference btw get and [] is that if we try to acces the key which is not presenting the dictionary then get will return none but [] will give an error
print(my_dict.get("c"))  # Output: None

my_dict = {"a": 1, "b": 2}
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2)])

my_dict = {"a": 1, "b": 2}
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])

my_dict = {"a": 1, "b": 2}
print(my_dict.pop("a"))  # Output: 1
print(my_dict)  # Output: {'b': 2}

my_dict = {"a": 1, "b": 2}
print(my_dict.popitem())  # Output: ('b', 2) main differnece btw pop and popitem is that pop will remove the element from the dictionary by entering the key but popitem will remove the last element from dict 
print(my_dict)  # Output: {'a': 1}

my_dict = {"a": 1}
print(my_dict.setdefault("b", 3))  # Output: 3
print(my_dict)  # Output: {'a': 1, 'b': 3}
print(my_dict)

my_dict = {"a": 1}
my_dict.update({"b": 2, "c": 3})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

my_dict = {"a": 1, "b": 2}
print(my_dict.values())  # Output: dict_values([1, 2])
