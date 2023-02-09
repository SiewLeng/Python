def getReading():
    reading = input("Enter blood pressure reading (mmHg): ")
    splitedReading = reading.split('/')
    upperNum = int(splitedReading[0])
    lowerNum = int(splitedReading[1])
    return (upperNum, lowerNum)

def getBloodPressureCategory(upperNum, lowerNum):
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

upperNum, lowerNum = getReading()
print(getBloodPressureCategory(upperNum, lowerNum))

