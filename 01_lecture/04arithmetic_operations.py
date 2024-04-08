"""
Basic arithmetic operations in Python
"""
rectangle_width = 20
rectangle_length = 5

# Calculate perimeter of the rectangle
perimeter = rectangle_length*2 + rectangle_width*2
print(f"Perimeter of the rectangle: {perimeter}")

# Calculate area of the rectangle
area = rectangle_length * rectangle_width
print(f"Area of the rectangle: {area}")

# Increase the length by 2 units
rectangle_length = rectangle_length + 2
print(f"New length after increasing by 2 units: {rectangle_length}")

# Decrease the width by 1 unit
rectangle_width = rectangle_width - 1
print(f"New width after decreasing by 1 unit: {rectangle_width}")

# Calculate the diagonal of the rectangle using Pythagorean theorem
rectangle_diagonal = (rectangle_length**2 + rectangle_width**2)**0.5 # ** is exponentiation operator -> raised to the power of возвести в степень
print(f"Diagonal of the rectangle: {rectangle_diagonal}")

"""
Modulo operator
"""
# Calculate the remainder when dividing 15 by 4
remainder = 15 % 4
print(f"The remainder when dividing 15 by 4 is: {remainder}")

# Using modulo to check if a number is even or odd
number = 7

# Check if the number is even. == Equality
is_even = number % 2 == 0
print(f"Is the number {number} even? {is_even}")

# Check if the number is odd. != Disequality
is_odd = number % 2 != 0
print(f"Is the number {number} odd? {is_odd}")

"""
Division with corresponding results
"""
# Division with floating-point result. floating point -- a number with a decimal part (float)
result_float = 15 / 4
print(f"Result of 15 / 4 (floating-point): {result_float}")

# Division with integer result using floor division. // is whole division. between whole numbers
result_integer = 15 // 4
print(f"Result of 15 // 4 (integer): {result_integer}")

"""
Numbers as input
"""
input_str = input("Which year were you born? ")
year = int(input_str)
print(f"Your age at the end of the year 2024: {2024 - year}")

# You can even cast without using a second variable
year = int(input("Which year were you born? "))
print(f"Your age at the end of the year 2021: {2024 - year}")


"""
(Re) using variables
"""
number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

sum = number1 + number2 + number3
print(f"The sum of the numbers: {sum}")

# print the sum of 3 numbers using two variables
number1 = int(input("First number: "))
number2 = int(input("Second number: "))
sum = number1 + number2 + int(input("Third number: "))
print(f"The sum of the numbers: {sum}")

# print the sum of 3 numbers using 1 variable
number1 = int(input("First number: "))
sum = number1 + int(input("Second number: ")) + int(input("Third number: "))
print(f"The sum of the numbers: {sum}")

# only sum, no other variables. 3 options
sum = int(input("First number: ")) + int(input("Second number: ")) + int(input("Third number: "))
print(f"The sum of the numbers: {sum}")

sum = int(input("First number: "))
sum = sum + int(input("Second number: "))
sum = sum + int(input("Third number: "))
print(f"The sum of the numbers: {sum}")

sum = int(input("First number: "))
sum += int(input("Second number: "))
sum += int(input("Third number: "))
print(f"The sum of the numbers: {sum}")

# f"..." is needed if i have {variable} inside a string