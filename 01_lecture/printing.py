print("hello world!")

'''
Why syntax matters?
Try to print text without double quotes:
'''
# print(hello world!)

'''
Multiple commands written in succession will be executed in order from first to last. For example this program
'''
print("Welcome to Algorithms and Data Structures!")
print("First we will practice using the print command.")
print("This program prints three lines of text on the screen.")

# TODO
'''
Write a program which prints out the following lines exactly as they are written:

Row, row, row your boat,
Gently down the stream.
Merrily, merrily, merrily, merrily,
Life is but a dream.
'''

"""
You can also put arithmetic operations inside a print command. 
Running it will then print out the result of the operation. 
For example, the following program
"""
print(2 + 5)
print(3 * 3)
print(2 + 2 * 10)

"""
Notice the lack of quotation marks around the arithmetic operations above. 
Quotation marks are used to signify strings. 
In the context of programming, strings are sequences of characters.
Thus, the following two commands produce two quite different results:
"""
print(2 + 2 * 10)
print("2 + 2 * 10")

"""
Thus far, you have probably used double quotation marks " to print out strings. 
In addition to the double quotation marks, Python also accepts single quotation marks '.
This comes in handy if you ever want to print out the actual quotation marks themselves:
"""
print('"Come right back!", shouted the police officer.')

"""
It is also possible to combine strings with calculations:
"""
print("2 + 2 = ", 2 + 2)

# TODO
# print the multiplication of 2*2 using a combination of string and operation
# the program should print "the result = 4"




