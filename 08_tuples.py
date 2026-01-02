"""
#tuples
# creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')
print("Original tuple:", my_tuple)  
# Output: Original tuple: (1, 2, 3, 'a', 'b', 'c')

# accessing elements in a tuple
print("First element:", my_tuple[0])
# Output: First element: 1
print("Last element:", my_tuple[-1])
# Output: Last element: c

# slicing a tuple
print("Sliced tuple (1 to 4):", my_tuple[1:4])
# Output: Sliced tuple (1 to 4): (2, 3, 'a')

# unpacking a tuple
a, b, c, d, e, f = my_tuple
print("Unpacked values:", a, b, c, d, e, f)
# Output: Unpacked values: 1 2 3 a b c
# tuples are immutable
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)
# Output: Error: 'tuple' object does not support item assignment

# tuple methods
sample_tuple = (1, 2, 2, 3, 4, 4, 4)
print("Count of 2 in tuple:", sample_tuple.count(2))
# Output: Count of 2 in tuple: 2
print("Index of 3 in tuple:", sample_tuple.index(3))
# Output: Index of 3 in tuple: 3
# nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)
# Output: Nested tuple: ((1, 2), (3, 4), (5, 6))
print("Element from nested tuple:", nested_tuple[1][0]) 
# Output: Element from nested tuple: 3
# tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated = tuple1 + tuple2
print("Concatenated tuple:", concatenated)
# Output: Concatenated tuple: (1, 2, 3, 'a', 'b', 'c')
# tuple repetition  
repeated = tuple1 * 3
print("Repeated tuple:", repeated)
# Output: Repeated tuple: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# converting list to tuple
my_list = [1, 2, 3, 4]
converted_tuple = tuple(my_list)
print("Converted tuple from list:", converted_tuple)
# Output: Converted tuple from list: (1, 2, 3, 4)

# converting tuple to list
converted_list = list(my_tuple)
print("Converted list from tuple:", converted_list)
# Output: Converted list from tuple: [1, 2, 3, 'a', 'b', 'c']   

# iterating through a tuple
for item in my_tuple:
    print("Tuple item:", item)
# Output:
# Tuple item: 1
# Tuple item: 2
# Tuple item: 3
# Tuple item: a
# Tuple item: b
# Tuple item: c
# Docstring for 08_tuples
# Tuples are immutable sequences in Python that can store a collection of items. They are similar
# to lists but cannot be modified after creation. Tuples are defined using parentheses () and can
# contain elements of different data types. They support indexing, slicing, and various methods like
# count() and index(). Tuples are often used for fixed collections of items, such as coordinates or
# RGB values, where immutability is desired. They also provide a way to group related
# data together in a single variable.
"""

