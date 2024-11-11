'''
Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the
values. Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python? Test the
program by entering a string value for age (e.g., “twenty”). What happens?
How can you prevent this issue?
'''

# Storing the given question
# First Name
first_name =  (input("Enter your first name: "))
# Second Name
second_name =  (input("Enter your second name: "))
names= first_name + second_name
# Hometown
hometown= (input("Enter your hometown: "))
#Age
age= (input("Enter your age: "))

# Printing the users input
print (f"{names}\n{hometown}\n{age}")