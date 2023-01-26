"""
The formula to convert temperature in fahrenheit to centigrade is as follows:

c = 5 / 9 * (f - 32)

Write a program that reads an input in fahrenheit and displays the temperature 
in centigrade.
"""

f = float(input ("Enter temp in fahrenheit: "))
c = 5 / 9 * (f - 32)
print("Temp in centigrade: ", c)