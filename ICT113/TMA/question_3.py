#a(i)
def readPricing(filename: str, pricing: dict):
    """
    Read the data from file with filename and update to the pricing dictionary.\n
    The first column of file with filename will be the key of pricing dictionary.\n
    The second column of file with filename will be the value of pricing dictionary.\n
    """
    infile = open(filename, 'r')
    line = infile.readline()
    while (line != ''):
        splitLine = line.split(' ')
        key = splitLine[0]
        value = float(splitLine[1])
        pricing[key] = value
        line = infile.readline()
    infile.close()

#a(ii)
def printHeading(heading):
    underline = ''
    for i in range(0, len(heading), 1):
        underline += '='
    print('\n')
    print(heading)
    print(underline)

def showPricing(charPricing, fontPricing, fontSize):
    overallPricing = {}
    noOfChars = 0
    for key in charPricing:
        value = round(charPricing[key] * fontPricing[str(fontSize)])
        overallPricing[key] = value
        noOfChars += 1
    heading = "Pricing for font size {0}pts".format(fontSize)
    printHeading(heading)
    numOfColumns = 7
    numOfRows = noOfChars // numOfColumns
    arrayToPrint = []
    keys = list(overallPricing.keys())
    for i in range(0, numOfRows, 1):
        string = ''
        for n in range(i * numOfColumns, (i + 1) * numOfColumns, 1):
            key = keys[n]
            string += "{0:<3}{1:<6}".format(key, overallPricing[key])
        print(string)
    for i in range(numOfRows * numOfColumns, noOfChars, 1):
        key = keys[i]
        string += "{0:<3}{1:<6}".format(key, overallPricing[key])
    print(string)
   
#b
def displayPricingTable():
    fontPricing = {}
    readPricing('fonts.txt', fontPricing)
    keyString = ''
    keys = list(fontPricing.keys())
    for i in range (0, len(keys) - 1, 1):
        keyString += keys[i] + ', '
    keyString += keys[len(keys) - 1]
    fontSize = input('Enter fontsize ({0}): '.format(keyString))
    if (fontSize in fontPricing):
        charPricing = {}
        readPricing('characters.txt', charPricing)
        showPricing(charPricing, fontPricing, fontSize)
    else:
        print("Invalid font size")

def requestForQuote():
    chars = input('Enter characters: ')
    chars = chars.replace(' ', '')

    fontPricing = {}
    readPricing('fonts.txt', fontPricing)
    keyString = ''
    keys = list(fontPricing.keys())
    for i in range (0, len(keys) - 1, 1):
        keyString += keys[i] + ', '
    keyString += keys[len(keys) - 1]
    fontSize = input('Enter fontsize ({0}): '.format(keyString))

    if (fontSize in fontPricing):
        charPricing = {}
        readPricing('characters.txt', charPricing)
        price = 0
        cheapestCharPrice = float(charPricing[chars[0]]) * float(fontPricing[fontSize]) / 100
        for i in range(0, len(chars), 1):
            priceOfOneChar = float(charPricing[chars[i]]) * float(fontPricing[fontSize]) / 100
            if (priceOfOneChar < cheapestCharPrice):
                cheapestCharPrice = priceOfOneChar
            price += priceOfOneChar
        print('Pricing: ${0:0.2f}'.format(price))
        if (price > 8):
            discount = 5 / 100 * price
            isFivePercentDiscount = True
            if (cheapestCharPrice > discount):
                discount = cheapestCharPrice
                isFivePercentDiscount = False
            price = price - discount
            if (isFivePercentDiscount):
                print("After 5% discount: ${0:0.2f}".format(price))
            else:
                print("After 1 free character: ${0:0.2f}".format(price))
    else:
        print("Invalid font size")

def addOrUpdateCharacterPricing():
    char = input('Enter a character to update its pricing: ')
    charPricing = {}
    readPricing('characters.txt', charPricing)
    if (char in charPricing):
        print('Current price for character {0} is {1} cents'.format(char, charPricing[char]))
    price = input('Enter the new price for character {0} in cent: '.format(char))
    charPricing[char] = price
    outfile = open('characters.txt', 'w')
    nextLine = False
    for key in charPricing:
        if (nextLine):
            outfile.write('\n{0} {1}'.format(key, charPricing[key]))
        else:
            outfile.write('{0} {1}'.format(key, charPricing[key]))
            nextLine = True
    outfile.close()

def addOrUpdateFontPricing():
    fontSize = input('Enter a font size to update its pricing ratio: ')
    fontPricing = {}
    readPricing('fonts.txt', fontPricing)
    if (fontSize in fontPricing):
        print('Current price ratio for font size {0} is {1}'.format(fontSize, fontPricing[fontSize]))
    price = input('Enter the new price ratio for font size {0}: '.format(fontSize))
    fontPricing[fontSize] = price
    outfile = open('fonts.txt', 'w')
    nextLine = False
    for key in fontPricing:
        if (nextLine):
            outfile.write('\n{0} {1}'.format(key, fontPricing[key]))
        else:
            outfile.write('{0} {1}'.format(key, fontPricing[key]))
            nextLine = True
    outfile.close()

def app():
    isExit = False
    while(not isExit):
        instructions = [
            'MonkeyPrint Embroidery Services',
            '1. Display Pricing Table',
            '2. Request for Quote',
            '3. Add/Update Characters’ Pricings',
            '4. Add/Update Font Sizes’ Pricings',
            '0. Exit',
        ]
        heading = instructions[0]
        printHeading(heading)
        for i in range(1, len(instructions), 1):
            print(instructions[i])
        option = input('Enter select: ')
        if (option == '1'):
            heading = instructions[int(option)].split('1. ')[1]
            printHeading(heading)
            displayPricingTable()
        elif(option == '2'):
            heading = instructions[int(option)].split('2. ')[1]
            printHeading(heading)
            requestForQuote()
        elif(option == '3'):
            heading = instructions[int(option)].split('3. ')[1]
            printHeading(heading)
            addOrUpdateCharacterPricing()
        elif(option == '4'):
            heading = instructions[int(option)].split('4. ')[1]
            printHeading(heading)
            addOrUpdateFontPricing()
        elif(option == '0'):
            print('Exit')
            isExit = True
        else:
            print('Invalid selection!')

app()