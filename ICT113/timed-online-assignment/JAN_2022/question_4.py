"""
Solve computational problems using structured programming, apply data structures and
file handling.
A media screening room has rows of seats. The rows are labelled A, B, C, etc and seat
numbers 1, 2, 3 etc. A seating plan for 3 rows, 4 seats per row is as follows:

A O X O X
B O O O X
C O X O O
1 2 3 4

Empty seats are marked with O, while those occupied marked with X.
(a) A seating plan with some seats occupied is stored in a file, seating.txt as
follows:
A,O,X,O,X
B,O,O,O,X
C,O,X,O,O
Write a code segment to read the file and store the seating plan in a dictionary.
The dictionary structure after reading the file should be as follows:
seatingPlan = {'A':['O','X','O','X'], 'B':['O','O','O','X'],
'C':['O','X','O','O'] }
(8 marks)

(b) Write a code segment to display the seating plan based on the dictionary structure
in Q4(a):
A O X O X
B O O O X
C O X O O
1 2 3 4
(8 marks)

(c) Write a code segment to allow for booking of seats. To book seats, the user inputs
a seat by row and seat number, followed by number of seats to book. Assume all
input to be valid. If the seats are available, update the dictionary and display a
message. The following sample shows the scenarios to consider:
Sample 1
Enter seat no: B1
Enter number of seats to book: 2
Seats successfully allocated
Sample 2
Enter seat no: C1
Enter number of seats to book: 2
Not available
Sample 3
Enter seat no: C3
Enter number of seats to book: 5
Not available

Assume seat no is valid. No
validation required.
Update the dictionary with X
for seats allocated.

Not available because C2 is
occupied.

Not available because of
insufficient seats.
(9 marks)
"""

def getSeatingPlan():
    seatingPlan = {}
    infile = open("seating.txt", "r")
    oneLine = infile.readline()
    while oneLine != '':
        key = oneLine[0]
        value = oneLine[2:].replace('\n', '')
        seatingPlan[key] = value.split(',')
        oneLine = infile.readline()
    infile.close()
    return seatingPlan

  
def displaySeatingPlan(seatingPlan: dict):
    keys = []
    for key in seatingPlan:
        keys.append(key)
        string_1 = '{0} '.format(key)
        string_2 = ' '.join(seatingPlan[key])
        string = string_1 + string_2
        print(string)
    stringList = [' ']
    for i in range (1, len(seatingPlan[keys[0]]) + 1, 1):
        stringList.append('{0}'.format(i))
    endString = ' '.join(stringList)
    print(endString)

def bookingSeat(seatNo: str, noOfSeat: int, seatingPlan: dict):
    # seatNo = input('Enter seat no: ')
    # noOfSeat = int(input('Enter number of seats to book: '))
    key = seatNo[0]
    valueArrayStartIndex = int(seatNo[1]) - 1
    isSeatOccupied = False
    seatOccupied = ''
    if (valueArrayStartIndex + noOfSeat > len(seatingPlan[key])):
        print('Not available because of insufficient seats.')
    else:
        for i in range (valueArrayStartIndex, valueArrayStartIndex + noOfSeat, 1):
            if (seatingPlan[key][i]) == 'X':
                isSeatOccupied = True
                seatOccupied = '{0}{1}'.format(key, i + 1)
                break
        if (isSeatOccupied):
            print('Not available because {0} is occupied.'.format(seatOccupied))
        else:
            for i in range (valueArrayStartIndex, valueArrayStartIndex + noOfSeat, 1):
                seatingPlan[key][i] = 'X'
            print('Seats successfully allocated')

def main():
    seatingPlan = getSeatingPlan()
    displaySeatingPlan(seatingPlan)
    seatNo = input('Enter seat no: ')
    while (seatNo != ''):
        noOfSeat = int(input('Enter number of seats to book: '))
        bookingSeat(seatNo, noOfSeat, seatingPlan)
        displaySeatingPlan(seatingPlan)
        seatNo = input('Enter seat no: ')
        
main()