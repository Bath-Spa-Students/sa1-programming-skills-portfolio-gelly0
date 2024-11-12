'''
Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the
user enters the wrong password, inform them of the remaining attempts. If the
maximum number of attempts is reached, inform the user that the authorities
have been alerted.
'''

# Define the correct password
correct_password = "12345"

# Set the maximum number of attempts
max_attempts = 5
attempts_left = max_attempts

# Use a while loop to repeatedly ask for the password until the correct one is entered
while attempts_left > 0:
    # Ask the user to enter the password
    user_input = input(f"Enter the password (Attempts left: {attempts_left}): ")

    # Check if the entered password is correct
    if user_input == correct_password:
        print ("Password correct!")
        break  # Exit the loop if the password is correct
    else:
        attempts_left -= 1  # Decrease the remaining attempts
        if attempts_left > 0:
            print (f"Incorrect password. You have {attempts_left} attempts left.")
        else:
            print ("Incorrect password. You have no attempts left.")
            break  # Exit the loop after 5 failed attempts