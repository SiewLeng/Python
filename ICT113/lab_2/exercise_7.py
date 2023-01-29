"""
(String, if...elif...else) Singapore NRIC numbers have the following format
#0000000@, where
- length of the NRIC is 9
- # is a letter that can be "S", "T", "F" or "G"
- followed by 7 digits
- @ is any reference letter A to Z or a to z
Write a program that inputs a NRIC number and displays whether a NRIC is
valid. Display “Valid NRIC” or, if it is invalid, one of the following error
messages:
- Length must be exactly 9
- The first letter must be S, T, F or G
- Must consist of 7 digits
- Reference letter must be A to Z or a to z
"""

NRIC = input("Enter a NRIC number: ")
output = ""
isSevenDigit = True
for i in range(1, 8):
    if (ord(NRIC[i]) < 48 or ord(NRIC[i]) > 57):
        isSevenDigit = False
        break


if (len(NRIC) != 9):
    output += "Length must be exactly 9"
elif(NRIC[0] != 'S' and NRIC[0] != 'T' and NRIC[0] != 'F' and NRIC[0] != 'G'):
    output  += "The first letter must be S, T, F or G"
elif(isSevenDigit == False):
    output += "Must consist of 7 digits"
elif(ord(NRIC[8]) < 65 or (ord(NRIC[8]) > 90 and ord(NRIC[8]) < 97) or ord(NRIC[8]) > 122):
    output += "Reference letter must be A to Z or a to z"
else:
    output += "Valid NRIC"

print(output)