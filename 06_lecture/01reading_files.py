"""
A simple way to include files in a Python program is to use the with statement.
The header line opens the file, and the block where the file can be accessed follows.
After the block the file is automatically closed, and can no longer be accessed.

So, the following code opens the file, reads the contents, prints them out, and then closes the file:
"""
with open("example.txt") as new_file:
    contents = new_file.read()
    print(contents)

"""
Going through the contents of a file

The read method is useful for printing out the contents of the entire file, but more often we will want to go through the file line by line.

Text files can be thought of as lists of strings, each string representing a single line in the file. We can go through the list with a for loop.

The following example reads our example file using a for loop, removes line breaks from the end of each line, counts the number of lines, and prints each line with its line number. 
It also keeps track of the length of the lines:
"""
with open("example.txt") as new_file:
    count = 0
    total_length = 0

    for line in new_file:
        line = line.replace("\n", "")
        count += 1
        print("Line", count, line)
        length = len(line)
        total_length += length

print("Total length of lines:", total_length)

"""
Split method
"""
text = "monkey,banana,harpsichord"
words = text.split(",")
for word in words:
    print(word)


"""
Reading CSV files
"""
with open("grades.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        name = parts[0]
        grades = parts[1:]
        print("Name:", name)
        print("Grades:", grades)

