"""
Write a simple calculator program that performs arithmetic operation on 2
numbers. Input consists of 3 values, separated by an arithmetic operator, in
the following format:

float operator float

where float is any decimal number and operator is either +, -, *, /.

Run 1
Enter arithmetic expression: 23.6 + 33.2
Result: 56.8


Run 2
Enter arithmetic expression: 85 % 15
Invalid arithmetic operator
Assume that the numeric values are valid, but the the operator may be
invalid.
"""

input = input("Enter input consists of 3 values, separated by an arithmetic operator: ")
result = 0
output = ""

if (input.find('+') >= 0):
    data = input.split('+')
    result += float(data[0]) + float(data[1])
    output += "Result is: {0:0.3f}".format(result)
elif(input.find('-') >= 0):
    data = input.split('-')
    result += float(data[0]) - float(data[1])
    output += "Result is: {0:0.3f}".format(result)
elif(input.find('*') >= 0):
    data = input.split('*')
    result += float(data[0]) * float(data[1])
    output += "Result is: {0:0.3f}".format(result)
elif(input.find('/') >= 0):
    data = input.split('/')
    result += float(data[0]) / float(data[1])
    output += "Result is: {0:0.3f}".format(result)
else:
    output += "Invalid arithmetic operator"

print(output)