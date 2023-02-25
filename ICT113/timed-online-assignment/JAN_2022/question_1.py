"""
(a) Given a string, display valid if the length of the string is 8 letters, of which the
first 3 must be uppercase letters, followed by 4 digits and the last letter ends with
one of the letters ‘S’, ‘X’, or ‘Z’. Otherwise, display invalid.
(10 marks)

(b) Given a positive integer n less than 10, display a n by n multiplication table. For
example, if n is 5, display the following:
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
(15 marks)
"""

def isValidString(string: str):
    if (len(string) != 8):
        return False
    if (not string[0:3].isupper()):
        return False
    if(not string[3:7].isdigit()):
        return False
    if(string[7] != 'S' and string != 'X' and string != 'Z'):
        return False
    return True

def displayMutiplicationTable(number: int):
    for i in range(1, number + 1, 1):
        string = ''
        for n in range (1, number + 1, 1):
            string = string + '{0:>4}'.format(n * i)
        print(string)

print(isValidString('TFR1234S'))
print(isValidString('TFR12345S'))
print(isValidString('TRf12345S'))
print(isValidString('TRf1234xS'))
print(isValidString('TRf1234xW'))

displayMutiplicationTable(5)
displayMutiplicationTable(8)
