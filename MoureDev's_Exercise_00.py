# Exercise 00

# https://www.python.org/

#Syntax for comments in Python, Variables, Constants, Data type and Hello World.

# This is a comment in a single line

"""
This is 
a comment 
in several lines
"""

'''
This is
a comment too
in several lines
'''

#These are variables in Python: 

my_variable = "To name a variable in Python, You must use an underscore '_' instead of spaces"
my_variable = "this is the new value of my variable"

'''
In Python, there is no built-in way to create true constants (unchangeable variables).
However, by convention, programmers use UPPERCASE text to show that a variable should not be changed.
This is just a convention — Python will not stop you from changing it
'''
#Example:

MY_CONSTANT = "My constant" # If the line of code has UPPERCASE it means that it is a constant (an unchangeable variable)

# Python Primitive Data Types (there are only 4 in Python):

'''
interger (int) It is used to represent whole numbers
floating-point numbers (float) It is used to represent numbers with decimal points
booleans (bool) It is used to represent a True or False value
string (str) It is used to store a piece of text.
'''
#Examples:

# Whole Numbers (int):
my_int = 1  
my_int = 2

# Numbers with decimal points(float):

my_float = 1.5
my_float = 2.5

# Boolean logic (bool):

my_bool = True
my_bool = False

# Strings (String):

my_string = "Hello Word!"
my_other_string = "I am learning Python"

# the print() funtion:

'''
The print() function in Python displays text or values on the screen.
It sends output to the console so you can see what your program is doing.
'''
print("!Hello, Python!")

# The type() function + print():

"""
The type() function checks the data type of a value or variable.
The print() function displays that information on the screen.
Together, you use print(type(...)) to see the type in the console.

To check data types means to find out what kind of value you have in a variable or expression.
For example: is it an integer, a string, a float, a list, etc.?
"""

#Examples:

print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))
