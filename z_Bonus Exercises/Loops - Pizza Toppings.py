'''
Loops- Pizza Toppings:
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
As they enter each topping, Print a message saying you’ll add that topping to their pizza.
'''

# Start a loop to get pizza toppings
while True:
    topping = input("Enter a pizza topping (or type 'quit' to stop): ")
    
    if topping.lower() == 'quit':
        break  # Exit the loop if the user types 'quit'
    
    print (f"Adding {topping} to your pizza.")