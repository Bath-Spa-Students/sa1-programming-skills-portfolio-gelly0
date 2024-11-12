'''
Exercise 6: Brute Force Attack - 30 Marks
Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the
password until they provide the correct one.

Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered.
'''

# Define the correct password
correct_password = "12345"

# Use a while loop to repeatedly ask the user for the password
while True:
    # Ask the user to input a password
    password = input("Please enter the password: ")
    
    # Check if the entered password matches the correct one
    if password == correct_password:
        print ("Password correct! Access granted.")
        break  # Exit the loop when the correct password is entered
    else:
        print ("Incorrect password. Please try again.")