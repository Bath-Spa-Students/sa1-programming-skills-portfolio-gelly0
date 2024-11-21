# Void function 
def print_message():
    print ("Welcome to Bathspa University")
# Calling function 
print_message()

# Local variable 
def print_message():
    message = "Welcome to Bathspa University"  # Local variable 
    print(message)
# Calling function 
print_message()
# If i call this message it shows an error 

def print_message():
    message = "Welcome to Bathspa University"  # Local variable 
    print(message)     # message is not defined bcz local varaible life is inside of program 
print_message()


# Diffenrent functions have same local variables name - No syntax error 

def print_message():
  message = "hi"
  print(message)
  
def print_message_2():
  message = "hello"
  print(message)
print_message()
print_message_2()

# Pasing argument to variable   

def print_message_2(message):  # parameter 
  print(message)

msg = "Good Morning"
print_message_2(msg)  # Argument 

# Example  parameter x store value and get double 
def main():
    value =5
    show_double(value)
    
def show_double(x):
      print(x*2)

main()
