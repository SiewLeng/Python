"""
Employ structured programming principles to develop a program.
A car park has a grace period of 10 minutes, after which the charge is $1.50 for the first
hour or part thereof of parking and 2 cents per minute after the first hour. The maximum
charge however, is $5.00.
Some examples of the parking charges are:
• 9 minutes, no charge.
• 35 minutes, charge is $1.50.
• 1 hour 10 minutes, charge is $1.70.
• 6 hours, charge is $5.00.
A program continually reads in a float value representing a duration and displays the car
park charge. Input is a value in the format h:mm, where h is the hour and mm the minutes.
Assume input will be in the correct format. The program ends when user presses just the
<Enter> key at the prompt.


A program execution sample is as follows:
Enter duration: 0:15
15 mins parking. Charge is $1.50
Enter duration: 0:07
7 mins parking. No charge
Enter duration: 1:12
1 hr 12 mins parking. Please pay $1.74
Enter duration: 5:00
5 hr 0 mins parking. Please pay $5.00
Enter duration: <Enter>

(a) Write a function getDurationInMinutes(duration) where the parameter
duration is a string in the format h:mm. The function computes and returns the
duration in minutes.
(5 marks)

(b) Write a function computeCharge(minutes) where the parameter is an integer
representing the total minutes parked. The functions calculates and returns the
parking charge.
(10 marks)

(c) Write the program. Make use of the functions in Q2(a) and (b).
(10 marks)
"""

def getDurationInMinutes(duration: str):
    hours = int(duration.split(':')[0])
    mins = int(duration.split(':')[1])
    totalMins = hours * 60 + mins
    return totalMins

def computeCharge(minutes: int):
    charge = 0
    if (minutes <= 10):
        charge += 0
    elif(minutes <= 60):
        charge += 1.5
    else:
        charge += 1.5
        charge += (minutes - 60) * 0.02
        if (charge > 5):
            charge = 5
    return charge

def printCharges(duration: str):
    string = ''
    durationInMinutes = getDurationInMinutes(duration)
    hours = durationInMinutes // 60
    mins = durationInMinutes % 60
    charges = computeCharge(durationInMinutes)
    if (hours > 0):
        string = string + '{0} hr '.format(hours)
    string = string + '{0} mins parking. '.format(mins)
    if (charges == 0):
        string = string + 'No charge'
    else:
        string = string + 'Please pay ${0:.2f}'.format(charges)
    print(string)

duration = input('Enter h:mm: ')
printCharges(duration)