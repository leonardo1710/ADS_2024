"""
Variables

In the context of programming, a variable is a location for storing some value, such as a string or a number.
You can use variables to store any information that will be needed later in the program's execution.
"""

my_name = "Leon"    # storing a string value
my_age = 31         # storing a number value

# The value stored in a variable can also be defined using other variables:
firstname = "Bart"
lastname = "Simpson"

character = firstname + " " + lastname

print(character)

"""
Here the values stored in the three variables are not obtained from user input. 
They remain the same every time the program is executed. 
This is called hard-coding data into the program.
"""

"""
Reassignment of variables

As implied by the name variable, the value stored in a variable can change.
"""

word = input("Type in a word: ")
print(word)

word = input("Another word: ")
print(word)

"""
Integers

Integers are numbers that do not have a decimal or fractional part, such as -15, 0 and 1.
"""
number1 = 100
number2 = "100"

print(number1)
print(number2)

"""
Variable types matter because different operations affect different types of variables in different ways. Let's have a look at an example:
"""
number1 = 100
number2 = "100"

print(number1 + number1)
print(number2 + number2)
