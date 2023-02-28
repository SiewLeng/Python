"""
Question 4a
Implement a function, checkSequence. The function has one string parameter
containing either integers and one or more dashes, separated by commas (,). The string
starts with an integer, not necessarily 1.
The function returns True if a sequence of consecutive integers can be obtained from
the string when the dashes are replaced by integers. The function returns False
otherwise. For example, suppose the string value is:

'2,-,-,5,6,-,-'

The function returns True because when the dashes are replaced by 3, 4, 7 and 8, a
sequence of consecutive integers '2,3,4,5,6,7,8' is formed.

'1,2,-,-,6,-,-,-'

The function returns False because when the first two dashes are replaced by 3 and 4
and the last three dashes are replaced by 7, 8 and 9, the string '1,2,3,4,6,7,8,9'
does not form a sequence of consecutive integers,
(6 marks)

Question 4b
Read a file, data.txt which contains one or more lines, each line containing either
integers and one or more dashes, separated by commas (,). An example content is as
follows:

2,-,-,5,6,-,-
1,2,-,-,6,-,-,-

Process each line in the file by calling the function checkSequence defined in Q4(a),
and appending the result of each call on separate lines in a file, output.txt.
(4 marks)

Question 4c
Implement a function, generateSequence which has an integer parameter length.
The function generates and returns a string consisting of length unique integers and
dashes, separated by commas (,). The string starts with an integer, not necessarily 1. If
length is 0 or negative, the function returns an empty string. If length is 1, the function
returns a string of one integer.
An example string is '2,3,-,-,7,8,9,-,11' when length is 9. Note that the
string also satisfies these conditions:
 Integers are ordered in increasing order and neighbouring numbers are
consecutive, e.g., 2 and 3 are consecutive and 7, 8 and 9 are consecutive.
 Integers immediately after a dash are at least one but not two more than the sum
of the last integer before the dash and the number of dashes, e.g., the number
after the first 2 dashes can be 6 or 7, and 7 is generated and included, instead of
6. Also, the number after the last dash can be 11 or 12, and 11 is generated and
included, instead of 12.

Question 4d
Write a function, main which repeatedly
 prompts for the length of sequence to generate,
 calls the functions generateSequence and checkSequence, and
 prints the output of both function calls
until the user enters 0 when prompted for the length. If the user enters negative numbers,
display an error message and re-prompt the user.
"""

#4a
def checkSequence(string: str):
    string = string.split(',')
    for i in range (1, len(string), 1):
        if (string[i] == '-'):
            string[i] = '{0}'.format(int(string[i - 1]) + 1)
        elif (int(string[i]) != int(string[i - 1]) + 1):
            return False
    return True

#4b
def checkSequenceFromFile():
    infile = open('data.txt', 'r')
    outfile = open('output.txt', 'w')
    line = infile.readline().replace('\n', '')
    while (line != ''):
        print('line: ', line)
        outfile.write('{0}\n'.format(checkSequence(line)))
        line = infile.readline()
    infile.close()
    outfile.close()

print(checkSequence('2,-,-,5,6,-,-'))
print(checkSequence('1,2,-,-,6,-,-,-'))
checkSequenceFromFile()
