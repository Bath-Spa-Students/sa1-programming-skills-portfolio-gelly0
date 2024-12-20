'''
Exercise 10: Is it even? - 35 Marks
Write a program that tests if a value is even or odd. Follow the instructions
outlined below:

Instructions:
• The program should ask the user for a number from within the main
function.
• The entered number should be passed to a function that determines if the
value is even or odd.
• The function should return a message indicating whether the number is
even or odd.
• The message returned by the function should be printed from within the
main function.
'''

# Check if the number is even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    # Ask the user to enter a number
    user_input = int(input("Enter a number: "))
    result = even_or_odd(user_input)

    # Print the result
    print (f"The number is {result}.")

if __name__ == "__main__":
    main()