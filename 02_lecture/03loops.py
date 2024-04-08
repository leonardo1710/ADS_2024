"""
WHILE Loop
"""
i = 1
while i <= 5:
    print("Hello World!")
    i = i + 1

j = 1
while j < 10:
    print(j) # print(j, end="") - this is to remove the new line
    j += 1 # this is equivalent to j = j + 1

"""
While True - infinite loops
"""
while True:
    number = int(input("Please type in a number, -1 to quit: "))

    if number == -1:
        break

    print(number ** 2) # возведение в степень to the power of

print("Thanks and bye!")


while True:
    code = input("Please type in your PIN: ")
    if code == "1234":
        break
    print("Incorrect...try again")

print("Correct PIN entered!")


"""
Break vs Condition
"""

# 1st version using the break command
sum = 0

while True:
    number = int(input("Please type in a number, -1 to exit: "))
    if number == -1:
        break
    sum += number

print (f"The sum is {sum}")

# 2nd version without the break command

sum = 0
number = 0

while number != -1: # != means different from, the opposite of equal
    number = int(input("Please type in a number, -1 to exit: "))
    if number != -1:
        sum += number # sum = sum + number

print (f"The sum is {sum}")

"""
Continue vs Break
"""

sum = 0

while True:
    number = int(input("Please type in a number, -1 to exit: "))
    if number == -1:
        break
    if number >= 10:
        continue # ignore everything that matches, go back to excecuting the loop. continue from the beginning of the loop. never use
    sum += number

print (f"The sum is {sum}")

"""
Nested Loops - because there is while inside while
"""

number = int(input("Please type in a number: "))
while number > 0:
    i = 0
    while i < number:
        print(f"{i} ", end="")
        i += 1
    print()
    number -= 1

original_number = int(input("Please type in a number: "))
number = 1
while number <= original_number:
    i = 0
    while i < number:
        print(f"{i} ", end="")
        i += 1
    print()
    number += 1