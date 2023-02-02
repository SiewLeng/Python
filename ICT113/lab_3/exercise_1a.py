"""
(for loop) Write a program to display the consecutive numbers between 2 numbers.
Assume that the first number will always be less than the second. Display from the
first number up to and including the second number, one number per line. Input
sample is as follows:
Enter first number: 3
Enter second number: 5
Output:
3
4
5
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number (larger than first number)"))

for i in range (num1, num2 + 1, 1):
    print(i)

print("----------------------")

for i in range (num2, num1, -1):
    print(i)

print("----------------------")
for i in range (num1, num2, -1):
    print(i)
