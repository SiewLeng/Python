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

def main():
    charPricing = {}
    fontPricing = {}
    readPricing('characters.txt', charPricing)
    readPricing('fonts.txt', fontPricing)
    for key in fontPricing:
        showPricing(charPricing, fontPricing, key)

main()