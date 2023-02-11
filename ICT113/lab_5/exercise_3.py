"""
(Dictionary) This program makes use of a dictionary structure to track currency
rates. The rates are all with respect to 1 SGD. Write the program in parts as follows:

a. Create an initial currency dictionary called currs as follows:
currs = {'USD': 0.73, 'RMB':5.01, 'HKD':5.73 }

b. Create a menu as follows:
Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit
Enter option:
For each option, call one of the functions described below.

c. Function addCurrency(currs). Pass the currs dictionary to the function.
The function should prompt user to input a currency and rate, e.g.

Enter currency: MYR
Enter rate: 2.90

The currency and rate are added to the currs dictionary as a key value pair. If
the currency already exists in the dictionary, print ‘Currency already exists!’,
otherwise, proceed to include the currency in the dictionary.

d. Function adjustCurrency(currs).
The function should prompt user to input a currency, e.g.
Enter currency: HKD
Rate is 5.73
Enter new rate: 5.77
HKD adjusted to 5.77

The program checks that the currency exists before prompting for new rate. A
message ‘Currency not found!’ should be displayed if the currency is not found.

e. Function removeCurrency(currs). The function prompts for currency and if
found, remove the currency from the dictionary.

f. Function displayCurrencyRates(currs). The function displays the currencies in
the following format:
Currency Rate
USD 0.73
RMB 5.01
HKD 5.73
"""

def addCurrency(currs):
    print('\nAdd Currency')
    currency = input('Enter currency: ')
    rate = input('Enter rate: ')
    currs[currency] = rate 

def adjustCurrency(currs):
    print('\nAdjust Currency')
    currency = input('Enter currency: ')
    if (currency in currs):
        print('Rate is {0}'.format(currs[currency]))
        rate = input('Enter new rate: ')
        currs[currency] = rate
        print('{0} is adjusted to {1}'.format(currency, currs[currency]))
    else:
        print('Currency not found')

def removeCurrency(currs):
    print('\nRemove Currency')
    currency = input('Enter currency to be removed: ')
    if (currency in currs):
        del currs[currency]
    else:
        print('Currency not found')

def displayCurrencyRates(currs):
    print('\nDisplay Currency')
    print('{0:<10} {1:<4}'.format('Currency', 'Rate'))
    for key in currs:
        print('{0:<10} {1:<4}'.format(key, currs[key]))

def menu(currs):
    toExit = False
    while (not toExit):
        instructions = [
            'Menu',
            '1. Add Currency',
            '2. Adjust Currency',
            '3. Remove Currency',
            '4. Display Currency rates',
            '0. Quit',
        ]
        print('\n')
        for i in range(0, len(instructions), 1):
            print(instructions[i])
        option = input('Enter option: ')
        if (option == '1'):
            addCurrency(currs)
        elif(option == '2'):
            adjustCurrency(currs)
        elif(option == '3'):
            removeCurrency(currs)
        elif(option == '4'):
            displayCurrencyRates(currs)
        elif(option == '0'):
            toExit = True

currs = {
    'USD': 0.73, 
    'RMB':5.01, 
    'HKD':5.73 
}
menu(currs)