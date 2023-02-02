"""
Write a triangle checker program that reads in the 3 sides of a triangle. The
program checks whether the 3 values can form a triangle. A triangle will not
be possible if the sum of any two is less than or equal to the third. If the
values can form a triangle, print the type of triangle according to the table
below.
All 3 sides are equal:     equilateral
Any two sides are equal:   isosceles
All 3 are unequal:         scalene
"""

a = float(input("Enter side a of triangle: "))
b = float(input("Enter side b of triangle: "))
c = float(input("Enter side c of triangle: "))
output = ""

isValidTriangle = True
if (a + b < c):
    isValidTriangle = False
elif(a + c < b):
    isValidTriangle = False
elif(b + c < a):
    isValidTriangle = False

if (isValidTriangle):
    if (a == b and b == c and a == c):
        output += "Equilateral triangle"
    elif(a == b or b == c or a == c):
        output += "Isosceles triangle"
    else:
        output += "Scalene triangle"
else:
    output += "Invalid triangle!"

print(output)