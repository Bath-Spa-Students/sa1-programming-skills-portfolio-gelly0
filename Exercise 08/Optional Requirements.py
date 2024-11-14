'''
Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.
'''

# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user to input the name they want to search for
name_search= input("Enter the name you want to search for: ").lower()

# Simple search to check if 'name_search' exists in the list
if name_search in [name.lower() for name in names]:
    print (f"{name_search.capitalize()} is found in the list!")
else:
    print (f"{name_search.capitalize()} is not found in the list.")