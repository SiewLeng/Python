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
def printHeading(heading: str):
    """
    Print the heading decorated with ============= below it.
    """
    underline = ''
    for i in range(0, len(heading), 1):
        underline += '='
    print('\n')
    print(heading)
    print(underline)

#a(ii)
def showPricing(charPricing: dict, fontPricing: dict, fontSize: int):
    """
    Print the price of printing each character in the charPricing for \n
    the given fontSize, charPricing and fontPricing in a table.
    """
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
def getFontSizes(fontPricing: dict):
    """
    Return a string of font size available in fontPricing with each font size 
    \n separated by ','.
    """
    keyString = ''
    keys = list(fontPricing.keys())
    for i in range (0, len(keys) - 1, 1):
        keyString += keys[i] + ', '
    keyString += keys[len(keys) - 1]
    return keyString

#b
def displayPricingTable():
    """
    Prompt the user to enter font size.\n
    Based on the font size entered, print a table showing the price \n
    of sewing each character in in character.txt file.\n
    The data in character.txt will be updated to charPricing dictionary.\n
    The data in font.txt will be updated to fontPricing dictionary.
    """
    fontPricing = {}
    readPricing('fonts.txt', fontPricing)
    fontSize = input('Enter font size ({0}): '.format(getFontSizes(fontPricing)))
    if (fontSize in fontPricing):
        charPricing = {}
        readPricing('characters.txt', charPricing)
        showPricing(charPricing, fontPricing, fontSize)
    else:
        print("Invalid font size")

#b
def requestForQuote():
    """
    Prompt the user to enter a string and the font size. \n
    Calculate the price of sewing the string based on the font size entered.
    """
    chars = input('Enter characters: ')
    chars = chars.replace(' ', '')
    fontPricing = {}
    readPricing('fonts.txt', fontPricing)
    fontSize = input('Enter fontsize ({0}): '.format(getFontSizes(fontPricing)))

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

#b
def addOrUpdateCharacterPricing():
    """
    Prompt the user to enter a character to update its pricing.\n
    Prompt the user to enter the price of the character.\n
    If the character exists, update the price of character in characters.txt file.\n
    Otherwise, add the new character with its corresponding price in characters.txt file.
    """
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

#b
def addOrUpdateFontPricing():
    """
    Prompt the user to enter a fontSize to update its pricing.\n
    Prompt the user to enter the price ratio of the font size.\n
    If the font size exists, update the price ratio of the font size in characters.txt file.\n
    Otherwise, add the new font size with its corresponding price ratio in fonts.txt file.
    """
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

#b
def app():
    """
    The program will continue until the user enters 0 to exit.\n
    If the option entered is 1, pricing table will be displayed based on font size entered.
    If the option entered is 2, the price of sewing the string will be displayed based on \n
    string and font size entered.\n
    If the option entered is 3, the price of the character will be added or updated in \n
    characters.txt based on the character and price entered.\n
    If the option entered is 4, the price ratio of the font size will be added or updated in \n
    fonts.txt based on the font size and price ratio entered.\n
    """
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