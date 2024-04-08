"""
Write a program which prints out the following lines exactly as they are written:

Row, row, row your boat,
Gently down the stream.
Merrily, merrily, merrily, merrily,
Life is but a dream.
"""
# Write your solution here

# multiple invocations (calls) of a print function
print("Row, row, row your boat,")
print("Gently down the stream.")
print("Merrily, merrily, merrily, merrily,")
print("Life is but a dream.")

# new line. another option will be adding \n in the previous line
print()

# i am using new line character and using the print function only once
print("Row, row, row your boat,\nGently down the stream.\nMerrily, merrily, merrily, merrily,\nLife is but a dream.")

print()

# i am calling print function only once and i am using a multiline sting as the argument of the print function
print("""Row, row, row your boat,
Gently down the stream.
Merrily, merrily, merrily, merrily,
Life is but a dream.""")

"""
Print the multiplication of 2*2 using a combination of string and operation
The program should print "the result = 4"
"""
# Write your solution here
print()

# "+" is used to fuse the strings. string concatenation
# "str" function takes an integer (number) as an argument and returns the string rep as a value of a number

print("the result = " + str(2*2))

print()
"""
Write a program which prints out: print("Hello there!")
"""
# Write your solution here

print('print("Hello there!")')

print()
"""
Fix this program so that the entire calculation, complete with result, is printed out on a single line. 
Do not change the number of print commands used.
"""
# Fix the code

print(5, end='')
print(" + ", end='')
print(8, end='')
print(" - ", end='')
print(4, end='')
print(" = ", end='')
print(5 + 8 - 4)