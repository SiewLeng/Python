"""
Question 2a
staffSalaryList is a list of elements where each element is a list of two elements –
staff number and salary for a staff. Staff numbers are unique in staffSalaryList but
salaries are not unique.
(i) Update the salary for the first element in staffSalaryList to 2500.

(ii) Locate the salary of staff with staff number p123. If the staff can be located,
update salary to 3600 and print Updated! If staff cannot be located, print Unable
to locate.

(iii) Compute the average salary of staff. Print the staff number whose salary is
above the average salary.

(iv) Print the staff number in descending order of salary and in ascending order of
staff number, that is, print the staff number of the staff with the highest salary
first, and if the salaries tie, print the smaller staff number first. Do not print the
salary.

Question 2b
Process the same data in staffSalaryList in Q2(a) now recorded in a dictionary
staffSalaryDict with staff number as key and salary as value.
(i) Initialise staffSalaryDict using the data in staffSalaryList.

(ii) Determine and print the number of staff number and salary pairs there are in
staffSalaryDict.

(iii) Locate the salary of staff with staff number p123. If the staff can be located,
update salary to 3600 and print Updated! If staff cannot be located, print Unable
to locate.

(iv) Print the staff number and salary of staff in ascending order of salary and in
ascending order of staff number if the salaries tie.
"""

def Qn2a_i(staffSalaryList: list):
    staffSalaryList[0][1] = 2500

def Qn2a_ii(staffSalaryList: list):
    isLocated = False
    for i in range (0, len(staffSalaryList), 1):
        if (staffSalaryList[i][0] == 'p123'):
            staffSalaryList[i][1] = 3600
            isLocated = True
            print('Updated!')
    if (not isLocated):
        print('Unable to locate')

def Qn2a_iii(staffSalaryList: list):
    totalSalary = 0
    for i in range (0, len(staffSalaryList), 1):
        totalSalary += staffSalaryList[i][1]
    averageSalary = totalSalary / len(staffSalaryList)
    for i in range (0, len(staffSalaryList), 1):
        if (staffSalaryList[i][1] > averageSalary):
            print(staffSalaryList[i][0])

def Qn2a_iv(staffSalaryList: list):
    for i in range (0, len(staffSalaryList) - 1, 1):
        indexWithHighestSalary = i
        for n in range(i + 1, len(staffSalaryList), 1):
            if (staffSalaryList[n][1] > staffSalaryList[indexWithHighestSalary][1]):
                indexWithHighestSalary = n
        if (indexWithHighestSalary != i):
            temp = staffSalaryList[i]
            staffSalaryList[i] = staffSalaryList[indexWithHighestSalary]
            staffSalaryList[indexWithHighestSalary] = temp
            if (i > 0 and staffSalaryList[i][1] == staffSalaryList[i - 1][1]):
                if (staffSalaryList[i][0] < staffSalaryList[i - 1][0]):
                    temp = staffSalaryList[i]
                    staffSalaryList[i] = staffSalaryList[i - 1]
                    staffSalaryList[i - 1] = temp
    for i in range (0, len(staffSalaryList), 1):
        print(staffSalaryList[i][0])

def Qn2b_i(staffSalaryList: list, staffSalaryDict: dict):
    for i in range(0, len(staffSalaryList), 1):
        key = staffSalaryList[i][0]
        value = staffSalaryList[i][1]
        staffSalaryDict[key] = value

def Qn2b_ii(staffSalaryDict: dict):
    count = 0
    for key in staffSalaryDict:
        print('{0:<10} {1:<5}'.format(key, staffSalaryDict[key]))
        count += 1
    print('Number of staff: {0}'.format(count))

def Qn2b_iii(staffSalaryDict: dict):
    key = 'p123'
    if (key in staffSalaryDict):
        staffSalaryDict[key] = 3600
        print('Updated!')
    else:
        print('Unable to locate')

def Qn2b_iv(staffSalaryDict: dict):
    for key in staffSalaryDict:
        indexWithHighestSalary = i
        for n in range(i + 1, len(staffSalaryList), 1):
            if (staffSalaryList[n][1] > staffSalaryList[indexWithHighestSalary][1]):
                indexWithHighestSalary = n
        if (indexWithHighestSalary != i):
            temp = staffSalaryList[i]
            staffSalaryList[i] = staffSalaryList[indexWithHighestSalary]
            staffSalaryList[indexWithHighestSalary] = temp
            if (i > 0 and staffSalaryList[i][1] == staffSalaryList[i - 1][1]):
                if (staffSalaryList[i][0] < staffSalaryList[i - 1][0]):
                    temp = staffSalaryList[i]
                    staffSalaryList[i] = staffSalaryList[i - 1]
                    staffSalaryList[i - 1] = temp
    for i in range (0, len(staffSalaryList), 1):
        print(staffSalaryList[i][0])
            
staffSalaryList = [
    ['apple', 1200],
    ['orange', 600],
    ['zee', 1800],
    ['mee', 1800],
    ['p123', 0]
]
staffSalaryDict = {}
"""
Qn2a_i(staffSalaryList)
print(staffSalaryList)
print('\n')
Qn2a_ii(staffSalaryList)
print('\n')
Qn2a_iii(staffSalaryList)
print('\n')
Qn2a_iv(staffSalaryList)
print(staffSalaryList)
"""
Qn2b_i(staffSalaryList, staffSalaryDict)
Qn2b_iii(staffSalaryDict)
Qn2b_ii(staffSalaryDict)

