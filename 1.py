'''Defining and Calling Functions: Write a function called greet_user that
takes in one parameter, a person's name (a string), and prints 
out a greeting message. For example, if the parameter is "Alice", 
the function should print "Hello, Alice!".'''


def greet_user(name):
    print('Hello,', name + '!')

name = input("What's your name? ")
greet_user(name)


# 90%
