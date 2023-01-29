"""
(if...elif...else) Write a program that determines whether two integers are even
or odd. Display one of the following messages:
- “The 2 numbers are even”
- “The 2 numbers are odd”
- “One number is even and the other is odd”
"""

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
output = ""

if (num1 % 2 == 0 and num2 % 2 == 0):
    output += "The 2 numbers are even"
elif(num1 % 2 == 1 and num2 % 2 == 1):
    output += "The 2 numbers are odd"
else:
    output += "One number is even and the other is odd"

print(output)