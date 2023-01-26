"""
Write a program that reads 3 numbers and displays the sum and average of these 
3 numbers.
"""

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

sum = num1 + num2 + num3
average = sum / 3

print("Sum of three numbers: ", sum)
print("Average of three numbers: ", average)
