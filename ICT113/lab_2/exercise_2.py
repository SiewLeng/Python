"""
Enter string: java python
Output: avaj nohtyp
Assume input is valid.
"""

stringEntered = input("Enter string: ")
stringSplit = stringEntered.split(" ")
reverseString = ""

for word in stringSplit:
    length = len(word)
    for i in range(length):
        reverseString += word[-(i+1)]
    reverseString += " "

reverseString = reverseString[:len(reverseString) - 1]

print("Output: {0}".format(reverseString))