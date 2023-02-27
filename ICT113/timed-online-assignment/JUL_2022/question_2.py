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
    print('List of staffs with salary above average: ')
    for i in range (0, len(staffSalaryList), 1):
        if (staffSalaryList[i][1] > averageSalary):
            print(staffSalaryList[i][0])

def Qn2a_iv_1(staffSalaryList: list):
    for i in range (0, len(staffSalaryList) - 1, 1):
        indexWithHighestSalary = i
        for n in range(i + 1, len(staffSalaryList), 1):
            if (staffSalaryList[n][1] > staffSalaryList[indexWithHighestSalary][1]):
                indexWithHighestSalary = n
        if (indexWithHighestSalary != i):
            temp = staffSalaryList[i]
            staffSalaryList[i] = staffSalaryList[indexWithHighestSalary]
            staffSalaryList[indexWithHighestSalary] = temp
            index = i 
            while(index >= 1 and    
                staffSalaryList[index - 1][1] == staffSalaryList[index][1] and
                staffSalaryList[index - 1][0] > staffSalaryList[index][0] 
            ):
                temp = staffSalaryList[index - 1]
                staffSalaryList[index - 1] = staffSalaryList[index]
                staffSalaryList[index] = temp
                index -= 1
    print('Staff number in descending order of salary: ')
    for i in range (0, len(staffSalaryList), 1):
        print(staffSalaryList[i][0])

def Qn2a_iv_2(staffSalaryList: list):
    def sortBySalary(item):
        return item[1]
    def sortByName(item):
        return item[0]
    staffSalaryList.sort(reverse = True, key = sortBySalary)
    index = 0
    listOfSalary = []
    nestedListOfSalary = []
    for i in range (0, len(staffSalaryList), 1):
        if (len(listOfSalary) == 0):
            listOfSalary.append(staffSalaryList[i][1])
        elif (staffSalaryList[i][1] != listOfSalary[-1]):
            listOfSalary.append(staffSalaryList[i][1])
    index = 0
    for i in range (0, len(listOfSalary), 1):
        listOfStaffWithSameSalary = []
        for n in range(index, len(staffSalaryList), 1):
            if (staffSalaryList[n][1] == listOfSalary[i]):
                listOfStaffWithSameSalary.append(staffSalaryList[n])
            else:
                index = n
                break
        nestedListOfSalary.append(listOfStaffWithSameSalary)
    for i in range (0, len(nestedListOfSalary), 1):
        if (len(nestedListOfSalary[i]) > 1):
            nestedListOfSalary[i].sort(key = sortByName)
    for i in range (0, len(nestedListOfSalary), 1):
        for n in range(0, len(nestedListOfSalary[i]), 1):
            print(nestedListOfSalary[i][n])

def Qn2a_iv_3(staffSalaryList: list):
    nestedListOfSalary = []
    index = 0
    count = 0
    # sort by salary
    staffSalaryList.sort(reverse = True, key = lambda item: item[1])
    while(count < len(staffSalaryList)):
        listOfStaffWithSameSalary = []
        for i in range (index, len(staffSalaryList), 1):
            if (len(listOfStaffWithSameSalary) == 0):
                listOfStaffWithSameSalary.append(staffSalaryList[i])
                count +=1
            elif (staffSalaryList[i][1] == listOfStaffWithSameSalary[-1][1]):
                listOfStaffWithSameSalary.append(staffSalaryList[i])
                count += 1
            else:
                index = i
                break
        if (len(listOfStaffWithSameSalary) > 1):
            # sort by name
            listOfStaffWithSameSalary.sort(key = lambda item: item[0])
        nestedListOfSalary.append(listOfStaffWithSameSalary)

    for i in range (0, len(nestedListOfSalary), 1):
        for n in range(0, len(nestedListOfSalary[i]), 1):
            print(nestedListOfSalary[i][n])
    
def Qn2b_i(staffSalaryList: list, staffSalaryDict: dict):
    for i in range(0, len(staffSalaryList), 1):
        key = staffSalaryList[i][0]
        value = staffSalaryList[i][1]
        staffSalaryDict[key] = value

def Qn2b_ii(staffSalaryDict: dict):
    count = 0
    print('\n')
    for key in staffSalaryDict:
        print('{0:<10} {1:<5}'.format(key, staffSalaryDict[key]))
        count += 1
    print('Number of staff: {0}'.format(count))

def Qn2b_iii(staffSalaryDict: dict):
    key = 'p123'
    if (key in staffSalaryDict):
        staffSalaryDict[key] = 3600
        print('\nUpdated!')
    else:
        print('\nUnable to locate')

def Qn2b_iv(staffSalaryDict: dict):
    staffSalaryPairs = list(staffSalaryDict.items())
    # sort by salary
    staffSalaryPairs = sorted(staffSalaryPairs, key = lambda item: item[1])
    nestedStaffSalaryPairs = []
    count = 0
    index = 0
    while (count < len(staffSalaryPairs)):
        staffSalaryPairsWithSameSalary = []
        for i in range (index, len(staffSalaryPairs), 1):
            if (len(staffSalaryPairsWithSameSalary) == 0):
                staffSalaryPairsWithSameSalary.append(staffSalaryPairs[i])
                count += 1
            elif(staffSalaryPairs[i][1] == staffSalaryPairsWithSameSalary[-1][1]):
                staffSalaryPairsWithSameSalary.append(staffSalaryPairs[i])
                count += 1
            else:
                index = i
                break
        # sort by name
        if (len(staffSalaryPairsWithSameSalary) > 0):
            staffSalaryPairsWithSameSalary = sorted(
                staffSalaryPairsWithSameSalary,
                key = lambda item: item[0]
            )
        nestedStaffSalaryPairs.append(staffSalaryPairsWithSameSalary)
    sortedStaffSalaryDict = {}
    for i in range (0, len(nestedStaffSalaryPairs), 1):
        for n in range(0, len(nestedStaffSalaryPairs[i]), 1):
            key = nestedStaffSalaryPairs[i][n][0]
            value = nestedStaffSalaryPairs[i][n][1]
            sortedStaffSalaryDict[key] = value
    Qn2b_ii(sortedStaffSalaryDict)
    
staffSalaryList = [
    ['apple', 1200],
    ['zee', 1800],
    ['aee', 1800],
    ['orange', 600],
    ['mee', 1800],
    ['p123', 0],
    ['cee', 1800],
]
staffSalaryDict = {}

"""
Qn2a_i(staffSalaryList)
print(staffSalaryList)
print('\n')
Qn2a_ii(staffSalaryList)
print(staffSalaryList)
print('\n')
Qn2a_iii(staffSalaryList)
print('\n')
Qn2a_iv_3(staffSalaryList)
print(staffSalaryList)
"""

Qn2b_i(staffSalaryList, staffSalaryDict)
Qn2b_ii(staffSalaryDict)
Qn2b_iii(staffSalaryDict)
Qn2b_iv(staffSalaryDict)


