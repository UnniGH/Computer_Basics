# Integer (int)
my_integer = 10
print(f"Integer: {my_integer}, Type: {type(my_integer)}")

# Floating-point number (float)
my_float = 3.14
print(f"Float: {my_float}, Type: {type(my_float)}")

# String (str) - Text
my_string = "Hello, Python!"
print(f"String: {my_string}, Type: {type(my_string)}")

# Boolean (bool)
my_boolean_true = True
my_boolean_false = False
print(f"Boolean True: {my_boolean_true}, Type: {type(my_boolean_true)}")
print(f"Boolean False: {my_boolean_false}, Type: {type(my_boolean_false)}")

# List (list) - An ordered, mutable collection of items
my_list = [1, "apple", 3.5, True]
print(f"List: {my_list}, Type: {type(my_list)}")
print(f"First element of list: {my_list[0]}")

# Tuple (tuple) - An ordered, immutable collection of items
my_tuple = (10, "banana", False)
print(f"Tuple: {my_tuple}, Type: {type(my_tuple)}")
print(f"Second element of tuple: {my_tuple[1]}")

# Dictionary (dict) - An unordered collection of key-value pairs
my_dictionary = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Dictionary: {my_dictionary}, Type: {type(my_dictionary)}")
print(f"Name from dictionary: {my_dictionary['name']}")

# Set (set) - An unordered collection of unique items
my_set = {1, 2, 3, 2, 1} # Duplicate values are automatically removed
print(f"Set: {my_set}, Type: {type(my_set)}")