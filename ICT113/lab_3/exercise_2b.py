"""
Modify the program to read only a string and displays the output in the following format
in the example:
Input string: hello
h
he
hel
hell
hello
The first line displays the first letter of the string, the second line displays the first two
letters and so on. Use only ONE for range loop. Do not use nested loops.
"""

string = input("Enter a string: ")
length = len(string)

for i in range(0, length, 1):
    print(string[0:i + 1])