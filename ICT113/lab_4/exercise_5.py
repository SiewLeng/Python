"""
(tuple, list) A test consists of 10 MCQ questions. Each question has 4 choices: a, b,
c, d. The solution to each question is stored in a tuple as follows:
( 'a', 'b', 'b', 'a', 'd', 'c', 'b', 'a', 'b', 'c' )
to indicate that the answer to question 1 is a, to question 2 is b, etc.
Write a program that allows a user to take the quiz. The user is prompted for his
answers to the 10 MCQ questions. Assume input will be one of the 4 valid choices is
entered: a, b, c, d. Store the answers in another collection.
After all the questions have been answered, the program displays if each of the
questions is answered correctly, and if not, the program displays the correct answer.
A summary of the number of correct answers is also displayed.
An example run is shown here:
Q1: a
Q2: b
Q3: c
Q4: a
Q5: d
Q6: c
Q7: b
Q8: a
Q9: d
Q10: c
Q1: a correct
Q2: b correct
Q3: c incorrect, answer is b
Q4: a correct
Q5: d correct
Q6: c correct
Q7: b correct
Q8: a correct
Q9: b correct
Q10: c correct
Total 9 out of 10 correct
"""

solutions = ( 'a', 'b', 'b', 'a', 'd', 'c', 'b', 'a', 'b', 'c' )
answersEntered = []
numOfCorrectAns = 0

for i in range(1, 11, 1):
    answersEntered.append(input('Q{0}: '.format(i)))

for i in range(0, len(answersEntered), 1):
    output = ''
    if (answersEntered[i] == solutions[i]):
        numOfCorrectAns += 1
        output += 'Q{0}: {1} correct'.format(i + 1, answersEntered[i])
    else:
        output += 'Q{0}: {1} incorrect, answer is {2}'.format(i + 1, answersEntered[i], solutions[i])
    print(output)

print('Total: {0} out of 10 correct'.format(numOfCorrectAns))

