"""
The area of a triangle with sides a, b, c can be determined using Heron’s
formula:
    Area = ((s)(s - a)(s - b)(s - c))^0.5
where s = 1⁄2 (a + b + c) is the semi-perimeter, or half of the triangle's
perimeter.
Write a program that reads the lengths of the sides of a triangle and displays
the area. Assume that input is valid, i.e. the sides are able to form a triangle.
Import the Math library to use the square root function.
"""
from math import pow

a = float(input("Enter side a of triangle: "))
b = float(input("Enter side b of triangle: "))
c = float(input("Enter side c of triangle: "))

s = 1 / 2 * (a + b + c)
area = pow(s * (s - a) * (s - b) * (s - c), 0.5)

print(f"Area of triangle: {area:.2f}")