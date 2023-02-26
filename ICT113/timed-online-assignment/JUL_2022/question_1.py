"""
Question 1a
Write Python statements for each of the following tasks. Do not use collection
structures (str, list, dict, etc) and loop structures.
(i) A coin is fair if the probability of getting head is between 0.45 and 0.55,
inclusive of both numbers at both ends. A coin is tossed multiple times, resulting
in n1 heads and n2 tails. Write one or more statements to evaluate whether the
coin is fair based on n1 heads and n2 tails, and set the result of the evaluation
to a bool variable, fair.
(ii) Given a sting s, print SAME if the letter a appears the same number of times in
the both halves of s, print MORE if it appears more times in the first half of s,
print FEWER if it appears fewer times in the first half of s. If the length of s is
odd, do not include the middle letter in the two halves, so that the lengths of
both halves are exactly the same.
For example, the string s is bananas, and its length is odd. So, the middle
character a in bananas is not included. SAME is printed as the letter a appears
the same number of times in the first half ban and the second half nas.
(10 marks)

Question 1b
Write Python statements for the following tasks. You may use collection structures
restricted to str, list and dict. You may also use loop structures.
Question 1b(i)
Write a code segment to process a string s1 to produce another string s2 without
repeating immediate neighbouring characters. If s1 is empty, s2 is set to empty also.
For example, when processing a string mississippi, the code segment produces the
string is misisipi.
(5 marks)

Question 1b(ii)
Write a code segment to determine whether a word w2, e.g., love can be made from
another word w1, e.g., solve. Print Possible if it is possible and Impossible if it is not
possible. For example, it is not possible to make the word live from solve but it is
possible to make the word love from solve.
(6 marks)

Question 1c
Use an appropriate segment of code written in Q1(a) and Q1(b) to explain why an
expression is a type of building block in program.
(4 marks)
"""

def Qn1_ai():
    n1 = 20
    n2 = 22
    probablityOfHeads = n1 / (n1 + n2)
    fair = False
    if (probablityOfHeads >= 0.45 and probablityOfHeads <= 0.55):
        fair = True
    print('fair >>> ', fair)



def Qn1_aii(string: str):
    index_1 = 0
    index_2 = 0
    if (len(string) % 2 == 1):
        index_1 = len(string) // 2 - 1
        index_2 = index_1 + 2
    else:
        index_2 = len(string) // 2
        index_1 = index_2 - 1
    noOfAInFirstHalf = string[0: index_1 + 1].count('a')
    noOfAInSecondHalf = string[index_2:].count('a')
    if (noOfAInFirstHalf == noOfAInSecondHalf):
        print('SAME')
    elif(noOfAInFirstHalf > noOfAInSecondHalf):
        print('MORE')
    else:
        print('FEWER')

def Qn_1bi(s1: str):
    s2 = ''
    if (s1 != ''):
        for i in range (0, len(s1), 1):
            if (s2 == ''):
                s2 = s2 + s1[i]
            elif (s2[-1] != s1[i]):
                s2 = s2 + s1[i]
    return s2

def Qn1_bii(w1: str, w2: str):
    for i in range (0, len(w1), 1):
        index = w2.find(w1[i])
        if (index == -1):
            return 'Impossible'
        else:
            w2.replace(w1[i], '')
    return 'Possible'


Qn1_aii('bananas')
Qn1_aii('cars')
print(Qn_1bi('mississippi'))
print(Qn1_bii('love', 'solve'))
print(Qn1_bii('live', 'solve'))


