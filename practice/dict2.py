# Tuples in Python
# A tuple is an immutable sequence type in Python, meaning its elements cannot be changed after creation.

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

# Accessing elements in a tuple
print("First element:", my_tuple[0])  # Accessing by index
print("Last element:", my_tuple[-1])  # Negative indexing

# Slicing a tuple
print("Sliced Tuple (2nd to 4th):", my_tuple[1:4])

# Tuple methods
# 1. count() - Returns the number of occurrences of a value in the tuple
print("Count of 3 in tuple:", my_tuple.count(3))

# 2. index() - Returns the index of the first occurrence of a value
print("Index of 4 in tuple:", my_tuple.index(4))

# Tuples are immutable, so you cannot add, remove, or modify elements.
# However, you can concatenate tuples or create new ones.

# Concatenating tuples
new_tuple = my_tuple + (6, 7)
print("Concatenated Tuple:", new_tuple)

# Repeating tuples
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)

# Nested tuples
nested_tuple = (1, (2, 3), (4, 5))
print("Nested Tuple:", nested_tuple)
print("Accessing nested element:", nested_tuple[1][1])  # Accessing element in nested tuple

# Checking membership
print("Is 3 in tuple?", 3 in my_tuple)
print("Is 10 not in tuple?", 10 not in my_tuple)

# Iterating through a tuple
for item in my_tuple:
    print("Tuple item:", item)

# Tuples are often used for fixed collections of items, such as coordinates or function returns.
coordinates = (10.5, 20.3)
print("Coordinates:", coordinates)

# Returning multiple values from a function using a tuple
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 2, 3, 4, 5])
print("Min value:", min_val, "Max value:", max_val)