"""
(Dictionary, list) Write a program to manage a collection of student names and their
course marks. Course mark consists of 2 components – course work, and exam. Both
are of equal weightage. Implement the program as described:

a. Assume that student names have been read from a file. Use the following initial
dictionary structure:
marks = { 'John':[0,0], 'Jane':[0,0], 'Peter':[0,0], 'Joe':[0,0] }
Note that for each dictionary entry, name is the key and a list representing the
coursework and exam marks is the value.

b. Allow user to repeatedly select an option from this menu:
Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Exit

c. Add marks option.
Prompt user for a name, coursework and exam. If the name already exists, display
a message, otherwise add an entry to the dictionary with the name as key and
coursework and test score as values. An example run of the option is as follows:

Enter name: John
Coursework: 60
Exam: 0
Added!

d. Update marks option
Similar to add, prompt user for a name, coursework and exam. However, the
name must already exist before user is prompted for coursework and exam. An
example run of the option is as follows:
Enter name: John
(John found. Marks displayed)
Coursework: 60
Exam: 70
Update C or E: C
Enter Coursework: 65
Updated!

e. Remove student option
Prompt for a name and remove the entry if the name is in the dictionary.

f. Display mark option
List all the names and scores of students in the following format:
Name Cw Ex Overall Grade
John 60 70 65.0 P
Jane 50 40 45.0 F
"""

def addMarks(marks):
    print('\nAdd Marks')
    name = input('Enter name: ')
    if (not name in marks):
        cw = int(input('Coursework: '))
        ex = int(input('Exam: '))
        marks[name] = [cw, ex]
        print('Added!')
    else:
        print('Name already exists')

def updateMarks(marks):
    print('\nUpdate Marks')
    name = input('Enter name: ')
    if (name in marks):
        print('Coursework: {0}'.format(marks[name][0]))
        print('Exam: {0}'.format(marks[name][1]))
        option = input('Update C or E: ')
        if (option == 'C'):
            cw = int(input('Enter Coursework: '))
            marks[name][0] = cw
            print('Updated!')
        elif(option == 'E'):
            ex = int(input('Enter Exam: '))
            marks[name][1] = ex
            print('Updated!')
        else:
            print('Invalid option')
    else:
        print('Name does not exist')

def removeMarks(marks):
    print('\nRemove Marks')
    name = input('Enter name: ')
    if (name in marks):
        del marks[name]
        print('Removed!')
    else:
        print('Name does not exist')

def displayMarks(marks):
    print('\nDisplay Marks')
    print('{0:<6} {1:<4} {2:<4} {3:<8} {4:<5}'.format('Name', 'Cw', 'Ex', 'Overall', 'Grade'))
    for key in marks:
        name = key
        cw = marks[key][0]
        ex =  marks[key][1]
        overall = cw * 0.5 + ex * 0.5
        grade = 'F'
        if (overall >= 50):
            grade = 'P'
        print('{0:<6} {1:<4} {2:<4} {3:<8} {4:<5}'.format(name, cw, ex, overall, grade))

def menu(marks):
    toExit = False
    while(not toExit):
        instructions = [
            '1. Add marks',
            '2. Update marks',
            '3. Remove student',
            '4. Display marks',
            '0. Exit'
        ]
        print('\nMenu')
        for i in range (0, len(instructions), 1):
            print(instructions[i])
        option = input('Enter selection: ')
        if (option == '1'):
            addMarks(marks)
        elif(option == '2'):
            updateMarks(marks)
        elif(option == '3'):
            removeMarks(marks)
        elif(option == '4'):
            displayMarks(marks)
        elif(option == '0'):
            toExit = True
        else:
            print('Invalid selection')

marks = { 
    'John':[0,0], 
    'Jane':[0,0], 
    'Peter':[0,0], 
    'Joe':[0,0] 
}

menu(marks)
