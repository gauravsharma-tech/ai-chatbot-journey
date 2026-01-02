#Dictionaries in Python
"""
Dictionaries are versatile data structures in Python that allow you to store multiple items in a single variable using key-value pairs. They are unordered, changeable, and do not allow duplicate keys. Dictionaries are defined using curly braces
{} and each key is separated from its value by a colon (:). Common operations on dictionaries include adding, removing, and modifying key-value pairs, as well as iterating through the dictionary using loops. Dictionaries also support various built-in methods that facilitate tasks such as retrieving keys, values, and items, as well as checking for the existence of keys.
"""
"""
# Creating a dictionary
student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Science"]
}
print(student)  # Output: {'name': 'John Doe', 'age': 21, 'courses': ['Math', 'Science']}   

# Accessing values
print(student["name"])  # Output: John Doe
print(student.get("age"))  # Output: 21

# Modifying values
student["age"] = 22
print(student["age"])  # Output: 22

# Adding key-value pairs
student["grade"] = "A"
print(student)  # Output: {'name': 'John Doe', 'age': 22, 'courses': ['Math', 'Science'], 'grade': 'A'}

# Removing key-value pairs
del student["courses"]
print(student)  # Output: {'name': 'John Doe', 'age': 22, 'grade': 'A'}

# Using pop() method    
grade = student.pop("grade")
print(grade)  # Output: A   
print(student)  # Output: {'name': 'John Doe', 'age': 22}

# Iterating through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")
# Output:
# name: John Doe    
# age: 22

# Dictionary methods
keys = student.keys()
print(keys)  # Output: dict_keys(['name', 'age'])
values = student.values()
print(values)  # Output: dict_values(['John Doe', 22])
items = student.items()
print(items)  # Output: dict_items([('name', 'John Doe'), ('age', 22)])

# Checking for key existence
print("name" in student)  # Output: True
print("courses" in student)  # Output: False

# Nested dictionaries
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}
print(students["student1"]["name"])  # Output: Alice

# Merging dictionaries
additional_info = {"student3": {"name": "Charlie", "age": 23}}
students.update(additional_info)
print(students)
# Output: {'student1': {'name': 'Alice', 'age': 20}, 'student2': {'name': 'Bob', 'age': 22}, 'student3': {'name': 'Charlie', 'age': 23}}    
# Write a program to count the frequency of each character in a string using a dictionary.
# text = "hello world"
# frequency = {}
# for char in text:
#     if char in frequency:
#         frequency[char] += 1  
#     else:
#         frequency[char] = 1
# print(frequency)
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}  
# Write a program to merge two dictionaries.
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict1.update(dict2)
# print(dict1)
# Output: {'a': 1, 'b': 3, 'c': 4}

phone = input("Enter a phone number: ")
digit_to_word = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
output = ""
for digit in phone:
    output += digit_to_word.get(digit, '!') + " "   
print(output)
# If the user inputs "123", the output will be: "one two three "
"""
message = input(">Enter a message: ")
words = message.split(" ")
emojis = {
    ":)": "😊",
    ":(": "😞",
    ";)": "😉"
}   
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
# If the user inputs "Hello :)", the output will be: "Hello 😊 "

def greet_user():
    print("Hello!")
    print("Welcome to the program.")

print(greet_user())
# Output:
# Hello!
# Welcome to the program.  
# always define the function before calling it

def greet_user(name):
    print(f"Hello, {name}!")
    print("Welcome to the program.")

greet_user("Gaurav")
# Output:
# Hello, Gaurav!

def square(number):
    return number * number
result = square(5)
print(result)  # Output: 25

#parameter vs argument
# A parameter is a variable in the function definition, while an argument is the actual value passed to the function when it is called.
# Example:
def add(a, b):  # a and b are parameters
    return a + b
sum_result = add(3, 5)  # 3 and 5 are arguments
print(sum_result)  # Output: 8