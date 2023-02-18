def getBloodPressureCategory(upperNum: int, lowerNum: int):
    """
    Return the blood pressure category based on the upperNum and lowerNum
    of blood pressure reading.
    """
    result = ''
    if (upperNum > 180 or lowerNum > 120):
        result = 'Hypertensive crsis!!. Please consult your doctor.'
    elif(upperNum >= 140 or lowerNum >= 90):
        result = 'You have Stage 2 Hypertension.'
    elif(upperNum >= 130 or lowerNum >= 80):
        result = 'You have Stage 1 Hypertension.'
    elif(upperNum >= 120):
        result = 'Your blood pressure is elevated.'
    elif(upperNum < 90 or lowerNum < 60):
        result = 'Your blood pressure is low.'
    else:
        result = 'Your blood is normal.'
    return result

def main():
    """
    Prompt user to enter blood pressure reading.\n
    If both blood pressure numbers are positive, print the blood pressure category.\n
    Otherwise, print error message.
    """
    reading = input("Enter blood pressure reading (mmHg): ")
    while(reading != ''):
        upperNum = reading.split('/')[0]
        lowerNum = reading.split('/')[1]
        if (upperNum.find('-') != -1 or lowerNum.find('-') != -1):
            print('Blood pressure number must be positive')
        else:
            print(getBloodPressureCategory(int(upperNum), int(lowerNum)))
        reading = input("Enter blood pressure reading (mmHg): ")
    print('Thank you and monitoring your blood pressure')

main()
