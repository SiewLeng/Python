"""
(if...else) Write a program that reads in 2 integer values. Display one of the
following messages:

- “The 2 numbers are the same”
- “The 2 numbers are not the same”
"""

num1 = int(input("Enter first interger value: "))
num2 = int(input("Enter second interger value: "))

output = ""
if (num1 == num2):
    output += "The 2 numbers are the same"
else:
    output += "The 2 numbers are not the same"

print(output)