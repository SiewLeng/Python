"""
Modify the program to display the sum of the consecutive numbers after the
consecutive numbers.
"""

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer (larger than first integer): "))

sum = 0

for i in range (num1, num2 + 1, 1):
    print(i)
    sum += i

print("Total sum of all the above number: {0}".format(sum))
