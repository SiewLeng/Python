"""
(String, tuple, list) A check digit is usually appended to a number in order to detect
errors arising when the number is transcribed manually.
The check digit for the NRIC No. is the official reference which is determined as
follows:
For example : NRIC No.(with official reference) = S7928964G

Step 1:
Multiply each digit by the following weights.
NRIC No. : 7 9 2 8 9 6 4
Weights : 2 7 6 5 4 3 2
Products: 14 63 12 40 36 18 8
Make use of a tuple for the weights:
weight = (2, 7, 6, 5, 4, 3, 2)

Step 2:
Sum the products of each digit x weight.
Sum : 14 + 63 + 12 + 40 + 36 + 18 + 8 = 191

Step 3:
Find the remainder when the sum is divided by 11.
Sum/11: 17 remainder 4

Step 4:
Take 11 – remainder to get the check digit.
Check digit : 11 – 4 = 7

Step 5:
Look up the following table to get the official reference.
Official Reference : G
Conversion: A B C D E F G H I Z J
Table 1 2 3 4 5 6 7 8 9 10 11
"""

weights = (2, 7, 6, 5, 4, 3, 2)
tableConversion = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Z', 'J')

NRIC = input('Enter NRIC: ')
sum = 0
for i in range(1, 8, 1):
    sum += int(NRIC[i]) * weights[i - 1]
remainder = sum % 11
checkDigit = 11 - remainder
referenceLetter = tableConversion[checkDigit - 1]

if (referenceLetter == NRIC[8]):
    print('Correct reference letter')
else:
    print('Incorrect reference letter')
