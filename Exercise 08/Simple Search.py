'''
Exercise 8: Simple Search - 30 Marks
Write a program that searches for a specific string within a list of strings. The list
is initialized with specific names (“Jake”, “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”.
'''

# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

name_search = "Sam"

# Simple search to check if 'name_search' exists in the list
if name_search in names:
    print (f"{name_search} is found in the list!")
else:
    print (f"{name_search} is not found in the list.")