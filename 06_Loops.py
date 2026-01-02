# while loops
# while loops are used to execute a block of code repeatedly as long as a specified condition is true. They are useful for tasks that require repetition, such as iterating over a range of numbers, processing items in a list, or performing actions until a certain condition is met.p can be controlled using various statements like break, continue, and else.
# Example 1: Basic while loop
# count = 1
# while count <= 5:
#     print(f"Count is: {count}")
#     count += 1
# print("Finished counting!")

# Example 2: secret number guessing game
# secret_number = 7
# guess = 0
# guess_limit = 3
# while guess < guess_limit:
#     user_input = int(input("Guess the secret number (between 1 and 10): "))
#     guess = guess + 1               
#     if user_input == secret_number:
#         print("Congratulations! You guessed it right.")
#         break
# else:
#     print("Sorry, you've used all your guesses. The secret number was", secret_number)
# ------------------------------------------------------------------------------
# Example 3: car simulation
# command = ""
# started = False
# print("Welcome to the car simulation!")
# print("Available commands: start, stop, quit")
# while command.lower() != "quit":
#     command = input("Enter a command (start, stop, quit): ")
#     if command.lower() == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#         print("car started... Ready to go!")
#     elif command.lower() == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#         print("car stopped.")
#     elif command.lower() == "quit":
#         print("Exiting the simulation.")
#     else:
#         print("I don't understand that command.")

# Example 4: printing even numbers from 1 to 20
# number = 1
# while number <= 20:
#     if number % 2 == 0:
#         print(number)
#     number += 1

# Example 5: calculating the factorial of a number
# num = int(input("Enter a positive integer to calculate its factorial: "))
# factorial = 1
# count = 1
# while count <= num:
#     factorial *= count
#     count += 1
# print(f"The factorial of {num} is {factorial}")
# Example 6: summing numbers until user decides to stop
# total = 0
# while True:
#     number = input("Enter a number to add to the total (or type 'stop
# ' to finish): ")
#     if number.lower() == 'stop':
#         break
#     total += int(number)
# print(f"The total sum is: {total}")

# Docstring for 06_Loops
# for loops
# for loops are used to iterate over a sequence (like a list, tuple, string, or
# range) and execute a block of code for each item in that sequence. They are useful for tasks that require repetition over a collection of items, such as processing elements in a list, generating sequences of numbers, or performing actions on each character in a string.

# Example 1: Basic for loop with a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(f"I like {fruit}")

# Example 2: for loop with range
# for number in range(1, 6):
#     print(f"Number is: {number}")

# Example 3: for loop with string
# word = "hello"
# for letter in word:
#     print(letter)

# Example 4: calculating the sum of numbers in a list
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total += num
# print(f"The total sum is: {total}")

# Example 5: nested for loops to create a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("-----")

# Example 6: iterating over a dictionary
# student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
# for student, score in student_scores.items():
#     print(f"{student} scored {score} points.")

# Example 7: using break and continue in a for loop
# for number in range(1, 11):
#     if number == 5:
#         print("Skipping number 5")
#         continue
#     if number == 8:
#         print("Stopping the loop at number 8")
#         break
#     print(f"Current number: {number}")

