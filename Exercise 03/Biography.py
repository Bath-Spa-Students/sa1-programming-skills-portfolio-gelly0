'''
Exercise 3: Biography - 25 Marks

In this exercise, you’ll create a program that stores and prints your name, home-
town, and age to the console using a Python dictionary.

Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a
dictionary.
2. Print the values on separate lines using a single print() statement.
3. Use variables with appropriate data types for each piece of information.
'''

# Store the information as key-value pairs
abt_me = {
    "name": "Angel Leonor Gala",
    "hometown": "Sharjah",
    "age": 18
}

# Printing the values on separate lines using a single print() statement.
print (f"{abt_me['name']}\n{abt_me['hometown']}\n{abt_me['age']}")
