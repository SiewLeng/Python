"""
(String, if...else) Write a program that reads a string and checks whether it is
a palindrome. It displays either the message palindrome or the message not a
palindrome. A palindrome is a word that spells the same backwards, e.g., the
word solos is a palindrome.
"""

input = input("Enter a string: ")
result = True
output = ""

for i in range(0, len(input)):
    if (input[i] != input[-(i + 1)]):
        result = False
        break

if (result == True):
    output += "The string is palindrome." 
else:
    output += "The string is not palindrome."

print(output)