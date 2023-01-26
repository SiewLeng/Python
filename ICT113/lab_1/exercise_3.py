"""
Write a program that takes in a 3 digit integer and displays the sum and
product of the digits. E.g. if the number is 123, the sum displayed is 6 and the
product is also 6.
"""

num = int(input("Enter 3 digit integer: "))
list = []

for n in range(3):
    r = num % 10
    list.append(r)
    num = num // 10

sum = 0
product = 1

for n in range(len(list)):
    sum = sum + list[n]
    product = product * list[n]

print("sum: ", sum)
print("product: ", product)




