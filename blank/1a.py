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
    else:
        result = 'Your blood pressure is normal.'
    return result


def main():
    """
    Prompt user to enter blood pressure numbers until the user press ENTER.\n
    Print the blood pressure category based on the blood pressure numbers.
    """
    reading = input("Enter blood pressure reading (mmHg): ")
    while(reading != ''):
        upperNum = reading.split('/')[0]
        lowerNum = reading.split('/')[1]
        print(getBloodPressureCategory(int(upperNum), int(lowerNum)))
        reading = input("Enter blood pressure reading (mmHg): ")
        
main()
