def getReading():
    reading = input("Enter blood pressure reading (mmHg): ")
    splitedReading = reading.split('/')
    if (splitedReading[0].find('-') != -1 or splitedReading[1].find('-') != -1):
        return -1
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
    elif(upperNum < 90 or lowerNum < 60):
        result = 'Your blood pressure is low.'
    else:
        result = 'Your blood is normal.'
    return result

reading = getReading()
if (reading == -1):
    print('You have entered invalid BP numbers')
else:
    (upperNum, lowerNum) = reading
    print(getBloodPressureCategory(upperNum, lowerNum))
    
