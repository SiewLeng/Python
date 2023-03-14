"""
Write a BankAccount class that models a Bank Account. The class diagram is as
follows:

A BankAccount class has 3 instance variables: accountId, pin and balance.
It has a constructor that has 3 parameters to initialize the accountId, pin and
the amount. The default balance is $100. It has getter properties for accountId
pin, and balance. It has setter property for balance.

It has the following methods:
 A changePin method that has old pin and new pin as parameters. The new
pin is updated only if the old pin matches the existing pin. Return true if the
change is successful and false otherwise.
 A deposit method with parameter amount which represents the amount to
deposit. The method adds the amount to the balance.
A withdraw method with parameter amount which represents the withdrawal
amount. This method deducts the amount from the balance and returns True
if there is sufficient balance, and False otherwise.
 A transfer method that has 2 parameters – another bank account to transfer
to and the amount to transfer. The method returns True if the transfer is
successful and False otherwise.
 The __str__() method returns the accountId and balance as a string.

Test out the BankAccount as follows:
i. Declare a BankAccount object b1 for account ’B1’, pin 111, amount 100.
ii. Make a deposit of $100 for b1. Display the details of the account.
iii. Change the pin for b1. Display the outcome of the change.
iv. Declare another BankAccount object b2 for account ’B2’, pin 222, amount
100.
v. Make a withdrawal amount of $200 for b2 and display whether the
withdrawal is successful.
vi. Transfer $100 from bank account b1 to b2. Display whether the transfer is
successful.
vii. Display the bank balances of both accounts.
"""

class BankAccount:
    def __init__(self, accountId: str, pin: int, balance: float = None):
        self.__accountId = accountId
        self.__pin = pin
        self.__balance = 100 if balance is None else balance

    def getAccountId(self) -> str:
        return self.__accountId

    def getPin(self) -> int:
        return self.__pin
    
    def getBalance(self) -> str:
        return self.__balance
    
    def setBalance(self, amount: float):
        self.__balance = amount

    def changePin(self, oldPin: int, newPin: int) -> bool:
        if (self.getPin() == oldPin):
            self.__pin = newPin
            return True
        return False
    
    def deposit(self, amount: float):
        self.__balance += amount
    
    def withdraw(self, amount: float) -> bool:
        if (self.getBalance() >= amount):
            self.__balance -= amount
            return True
        return False
    
    def transfer(self, account: object, amount: float) -> bool:
        if (type(account) is BankAccount):
            if (self.withdraw(amount)):
                account.deposit(amount)
                return True
        return False

    def __str__(self):
        accountId = 'Account id: {0:<15}'.format(self.getAccountId())
        balance = 'Balance: {0:<10.2f}'.format(self.getBalance())
        return '{0} {1}'.format(accountId, balance)
    
def main():
    b1 = BankAccount(pin = 111, accountId = 'account_B1', balance = None)
    b1.deposit(100)
    print(b1)

    changePinResult = b1.changePin(111, 123)
    result = 'Successful' if changePinResult == True else 'Unsuccessful'
    print('Change pin for accountId: {0} is {1}'.format(b1.getAccountId(), result))

    b2 = BankAccount(accountId = 'account_B2', pin = 222)

    amountWithDrawn = 200
    withdrawResult = b2.withdraw(amountWithDrawn)
    result = 'Successful' if withdrawResult == True else 'Unsuccessful'
    print('Withdrawal of ${0} for accountId: {1} is {2}'.format(amountWithDrawn, b2.getAccountId(), result))

    amountTransferred = 100
    transferMoneyResult = b1.transfer(b2, amountTransferred)
    result = 'Successful' if transferMoneyResult == True else 'Unsuccessful'
    print('Transfer ${0} from accountId: {1} is {2}'.format(amountTransferred, b1.getAccountId(), result))
    print(b1)
    print(b2)

main()
