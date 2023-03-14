"""
Write a class Person that models a person’s particulars as shown in the UML
diagram:

The class has 3 instance variables – gender (str), name (str), last name(str).
It has a constructor that initializes the gender, name and last name. It has getter
methods for all instance variables and setter method only for name.

It has the following methods:
- getFullName() returns the full name with a salutation “Mr.“ or “Ms.”,
depending on the person’s gender (m or f). The name is given in this order:
the last name, followed by the name, e.g., “Mr. Ong Ah Seng”
- getInitials() returns the first letter of the name separated by blanks, followed
by the lastname. E.g. it may return “A. Ong”.
- __str__() method that returns a string representation of a Person object as in:
Name: Ong Ah Seng Gender : Male

Test out the class, by creating a Person object and calling the methods in the
class.
"""

class Person:
    def __init__(self, gender: str, name: str, lastName: str):
        """
        gender, name and lastName are private attriutes.
        gender cannot be accessed using person.__gender
        """
        self.__gender = gender
        self.__name = name
        self.__lastName = lastName
    
    def getGender (self) -> str:
        return self.__gender
    
    def getName(self) -> str:
        return self.__name
    
    def name(self, newName: str):
        self.__name = newName
    
    def getLastName(self) -> str:
        return self.__lastName
    
    def getFullName(self) -> str:
        salution = 'Ms' if self.__gender == 'f' else 'Mr' if self.__gender == 'm' else ''
        return '{0}. {1} {2}'.format(salution, self.__lastName.title(), self.__name.title())
     
    def getInitials(self) -> str:
        return '{0}. {1}'.format(self.__name[0].upper(), self.__lastName.title())
    
    def __str__(self) -> str:
        name = '{0} {1}'.format(self.__lastName.title(), self.__name.title())
        gender = 'Male' if self.__gender == 'm' else 'Female' if self.__gender == 'f' else ''
        return 'Name: {0:<15} Gender: {1}'.format(name, gender)


def main():
    person_1 = Person('m', 'ah seng', 'ong')
    person_1.name('ah cheng')
    print('Gender: ', person_1.getGender())
    print('Name: ', person_1.getName())
    print('Last Name: ', person_1.getLastName())
    print('FullName: ', person_1.getFullName())
    print('Initals: ', person_1.getInitials())
    print('Details: ', person_1)

main()