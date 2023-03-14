class Person:
    def __init__(self, gender: str, name: str, lastName: str):
        self.__gender = gender
        self.__name = name
        self.__lastName = lastName
    
    def gender (self) -> str:
        return self.__gender
    
    def getName(self) -> str:
        return self.__name
    
    def name(self, newName: str):
        self.__name = newName
    
    def lastName(self) -> str:
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


    