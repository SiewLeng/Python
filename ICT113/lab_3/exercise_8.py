"""
Write a function sumSquares(num) that has 1 integer parameter. The function returns
the sum of the squares from 1 up to num. E.g. sumSquares(4) returns the sum of
1^2 + 2^2 + 3^2 + 4^2. Test the function.
"""

def sumSquares(num):
    sum = 0
    for i in range(1, num + 1, 1):
        sum += i ** 2
    return sum

num = int(input("Enter an integer: "))
sum = sumSquares(num)
print("Sum of squares from 1 up to {0}: {1}".format(num, sum))