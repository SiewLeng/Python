
"""
Question 3
Apply data structures to store and process information, and solve computational
problems using structured programming.
The rates (in cents) for sewing alphabets onto clothing are shown in Figure Q3(a). For
example, the cost of sewing an uppercase H is 45 cents and a lowercase a is 63 cents.
A 44 B 79 C 60 D 56 E 46 F 50 G 65 H 45 I 38
J 49 K 51 L 36 M 48 N 55 O 56 P 53 Q 41 R 58
S 65 T 36 U 23 V 49 W 46 X 48 Y 54 Z 52
a 63 b 55 c 37 d 55 e 63 f 58 g 40 h 31 i 35
j 50 k 51 l 36 m 32 n 58 o 50 p 55 q 55 r 53
s 61 t 57 u 37 v 33 w 59 x 53 y 54 z 39

Figure Q3(a)

Question 3a
Describe how you will store the data shown in Figure Q3(a). Explain why you have
chosen to store the data in that way.
(4 marks)

Question 3b
Write a function computeCost that has a string parameter lines and one or more
parameters for the data in Figure Q3(a), depending on your answer to Q3(a). The
function returns the cost (in dollars) of printing only alphabets appearing in lines.
Cents not making up to 5 cents should be removed.
For example, the cost of sewing 'Ha\nHa\nHa' is (45+63)x3 = 324 cents or $3.24. The
function removes 4 cents and returns 3.2. If the cost is 3.27, the function returns 3.25
after removing 2 cents.
(11 marks)

Question 3c
Write a function justifyLines that has one string parameter lines. The function
returns a formatted string with the lines in lines center-justified to the longest line in
lines. If there are uneven numbers of spaces to pad a line, put the extra space in front
of the line. For example, 'Ms\nLovely\Heart' should be aligned as
' Ms \nLovely\n Heart'.
"""

def getCharacterPriceDict():
    infile = open('characterPrice.txt', 'r')
    oneLine = infile.readline()
    characterPriceDict = {}
    while (oneLine != ''):
        words = oneLine.split(' ')
        for i in range (0, len(words), 2):
            key = words[i]
            value = int(words[i + 1])
            characterPriceDict[key] = value
        oneLine = infile.readline()
    infile.close()
    return characterPriceDict

#3b
def computeCost(string: str):
    characterPriceDict = getCharacterPriceDict()
    string = string.replace('\n', '')
    costInCent = 0
    while (string.find(' ') != -1):
        string = string.replace(' ', '')
    for i in range (0, len(string), 1):
        costInCent += characterPriceDict[string[i]]
    costInCent = (costInCent // 5 ) * 5
    costInDollar = costInCent / 100
    return costInDollar

#3c
def justifyLines_1(string: str):
    lines = string.split('\n')
    maxNoOfWords = len(lines[0])
    for i in range (1, len(lines), 1):
        if (len(lines[i]) > maxNoOfWords):
            maxNoOfWords = len(lines[i])
    justifyLines = []
    for i in range (0, len(lines), 1):
        justifyLine = ''
        noOfWords = len(lines[i])
        numOfFrontPadding = (maxNoOfWords - noOfWords) // 2 + (maxNoOfWords - noOfWords) % 2
        numOfBackPadding = (maxNoOfWords - noOfWords) // 2
        for n in range (0, numOfFrontPadding, 1):
            justifyLine = justifyLine + ' '
        for n in range(0, noOfWords, 1):
            justifyLine = justifyLine + (lines[i][n])
        for n in range (0, numOfBackPadding, 1):
            justifyLine = justifyLine + ' '
        justifyLines.append(justifyLine)
    return '\n'.join(justifyLines)

def justifyLines_2(string: str):
    lines = string.split('\n')
    maxNoOfWords = len(lines[0])
    string = ''
    for i in range (1, len(lines), 1):
        if (len(lines[i]) > maxNoOfWords):
            maxNoOfWords = len(lines[i])
    for i in range(0, len(lines) - 1, 1):
        string = string + '{0:^{1}}'.format(lines[i], maxNoOfWords) + '\n'
    string = string + '{0:^{1}}'.format(lines[-1], maxNoOfWords)
    return string

print(computeCost('Ha\nHa\nHa'))
print(justifyLines_1('Ms\nLovely\nHeart'))
print(justifyLines_2('Ms\nLovely\nHeart'))