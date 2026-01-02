"""list
A list is a collection which is ordered and changeable. In Python, lists are written with square brackets.
Lists allow duplicate members.

# Example 1: Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Example 2: Accessing list items
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

# Example 3: Modifying list items
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Example 4: Adding items to a list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Example 5: Removing items from a list 
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'orange']

# Example 6: Looping through a list
for fruit in fruits:
    print(fruit)

    # Example 7: List comprehension
squared_numbers = [x**2 for x in range(1, 6)]   
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example 8: List methods
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 9]

# Example 9: Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Output: 6

# Example 10: Checking membership
print("banana" in fruits)  # Output: True

# Docstring for 07_List
Lists are versatile data structures in Python that allow you to store multiple items in a single variable.
They are ordered, changeable, and can contain duplicate values. Lists are defined using square brackets and can hold items of different data types, including other lists. Common operations on lists include adding, removing, and modifying elements, as well as iterating through the list using loops. Lists also support various built-in methods that facilitate tasks such as sorting, reversing, and searching for elements.
"""
#Write a program to find the largest number in a list.
# numbers = [34, 67, 23, 89, 12, 90, 45]
# largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
# print(f"The largest number in the list is: {largest}")

# 2D list
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0][1] = 10
# print(matrix[0][1]) # Output: 10 

# for row in matrix:
#     for item in row:
#         print(item, end=' ')
#     print()

# numbers = [10, 20, 30, 40, 50]
# numbers.append(60)
# print(numbers)  # Output: [10, 20, 30, 40, 50, 60]

# numbers.remove(30)
# print(numbers)  # Output: [10, 20, 40, 50, 60]

# numbers.pop()
# print(numbers)  # Output: [10, 20, 40, 50]

# print(numbers.count(40)) # Output: 1

# numbers.sort()
# print(numbers)  # Output: [10, 20, 40, 50]

# numbers.reverse()
# print(numbers)  # Output: [50, 40, 20, 10]

# numbers2 = numbers.copy()
# print(numbers2)  # Output: [50, 40, 20, 10]

# remove duplicates from list
numbers_with_duplicates = [10, 20, 20, 30, 40, 40, 50]
uniques = []
for num in numbers_with_duplicates:
    if num not in uniques:
        uniques.append(num)
print(uniques)  # Output: [10, 20, 30, 40, 50]

# flatten a nested list
nested_list = [[1, 2], [3, 4], [5]]
flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)
print(flat_list)  # Output: [1, 2, 3, 4, 5]

# list comprehension to create a list of squares
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filtering even numbers using list comprehension
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# merging two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]

# finding the index of an item in a list
fruits = ["apple", "banana", "cherry", "date"]
index_of_cherry = fruits.index("cherry")
print(index_of_cherry)  # Output: 2

# sorting a list of strings
names = ["John", "Alice", "Bob", "Diana"]
names.sort()
print(names)  # Output: ['Alice', 'Bob', 'Diana', 'John']

# reversing a list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]

# using extend to add multiple items to a list
colors = ["red", "green"]   
colors.extend(["blue", "yellow"])
print(colors)  # Output: ['red', 'green', 'blue', 'yellow']

# using slice to get a sublist
animals = ["cat", "dog", "rabbit", "hamster", "parrot"] 
sublist = animals[1:4]
print(sublist)  # Output: ['dog', 'rabbit', 'hamster']  

# using len() to get the length of a list
numbers = [10, 20, 30, 40, 50]
length = len(numbers)
print(length)  # Output: 5

# using min() and max() to find smallest and largest numbers in a list
values = [15, 22, 8, 19, 31]    
smallest = min(values)
largest = max(values)
print(f"Smallest: {smallest}, Largest: {largest}")  # Output: Smallest: 8, Largest: 31  

#  using sum() to calculate the total of numbers in a list
prices = [19.99, 29.99, 4.99, 9.99]
total_price = sum(prices)
print(f"Total Price: ${total_price}")  # Output: Total Price: $64.96    

# using list() to convert a string into a list of characters
word = "hello"
char_list = list(word)
print(char_list)  # Output: ['h', 'e', 'l', 'l', 'o']

# using clear() to remove all items from a list
items = [1, 2, 3, 4, 5]
items.clear()
print(items)  # Output: []

# using copy() to create a shallow copy of a list
original = [1, 2, 3]
copied = original.copy()
print(copied)  # Output: [1, 2, 3]

# modifying the copied list
copied.append(4)
print(original)  # Output: [1, 2, 3]
print(copied)    # Output: [1, 2, 3, 4]

# using count() to count occurrences of an item in a list
letters = ['a', 'b', 'c', 'a', 'b', 'a']
count_a = letters.count('a')
print(count_a)  # Output: 3

# using insert() to add an item at a specific index
colors = ['red', 'green', 'blue']
colors.insert(1, 'yellow')
print(colors)  # Output: ['red', 'yellow', 'green', 'blue'] 

# using pop() to remove and return an item at a specific index
numbers = [10, 20, 30, 40, 50]  
removed_item = numbers.pop(2)
print(removed_item)  # Output: 30
print(numbers)       # Output: [10, 20, 40, 50]

# using remove() to delete the first occurrence of an item
fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry', 'banana']  

# using index() to find the index of an item
vehicles = ['car', 'bike', 'bus', 'bike']
index_bike = vehicles.index('bike')
print(index_bike)  # Output: 1

# using extend() to add elements from another list
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b)
print(list_a)  # Output: [1, 2, 3, 4, 5, 6]

# using sort() with a custom key
words = ['banana', 'apple', 'cherry', 'date']
words.sort(key=len)
print(words)  # Output: ['date', 'apple', 'banana', 'cherry']

# using reverse() to reverse the order of a list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]

# using slicing to create a reversed copy of a list
original = [1, 2, 3, 4, 5]
reversed_copy = original[::-1]
print(reversed_copy)  # Output: [5, 4, 3, 2, 1]

# using list comprehension to filter a list
mixed_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in mixed_numbers if num % 2 == 0]   
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# using nested list comprehension to flatten a nested list
nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [item for sublist in nested for item in sublist]    
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# using enumerate() to get index and value while looping through a list
colors = ['red', 'green', 'blue']   
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")
# Output:
# Index: 0, Color: red
# Index: 1, Color: green
# Index: 2, Color: blue
# using zip() to combine two lists
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zipped = list(zip(list1, list2))
print(zipped)  # Output: [('a', 1), ('b', 2), ('c', 3)]

# using map() to apply a function to all items in a list    
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# using filter() to filter items in a list
numbers = [10, 15, 20, 25, 30]  
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [10, 20, 30] 

# using reduce() to accumulate values in a list
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# using list comprehension to create a list of tuples
pairs = [(x, x**2) for x in range(1, 6)]
print(pairs)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]  

# using list comprehension with conditional expression
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 11)]
print(labels)  # Output: ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']    

# using list comprehension to create a multiplication table
multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(multiplication_table) 
# Output:
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]


