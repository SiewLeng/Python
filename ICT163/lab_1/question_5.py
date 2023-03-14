"""
Write a ToDo class that allows a user to record things to do for an event, e.g.
travelling trip. The class diagram is as follows:

The class has 2 instance parameters. They are:
 the event (string)
 a list collection to store the to-do actions

The constructor that has an event as parameter. The constructor initializes an
empty collection.

It has the following methods:
 A getter property for the event name.
 A addToDo( toDo) method that adds the toDo (string) action to the
collection.
 A removeToDoItem(index) method that removes a to-do item using the
index position of the todo item. Return True if successful and False
otherwise.
 __str__() method that returns a string of all the toDo action items in the
following format:
Event: travelling
1. Bring passport
2. Change money
3. Bring medicine

Test the ToDo class, with the following:
i. Create a ToDo object for an “Orientation camp” event.
ii. Add a few to do actions to the object.
iii. Display the to do list.
iv. Remove a to do action and display the outcome of the removal.
"""

class ToDo:
    def __init__(self, event: str, actions: list = None):
        self.__event = event 
        self.__actions = [] if actions is None else actions
    
    def getEvent(self) -> str:
        return self.__event
    
    def addToDo(self, toDo: str) -> bool:
        for action in self.__actions:
            if (toDo == action):
                return False
        self.__actions.append(toDo)
        return True
    
    def removeToDoItem(self, index: int) -> bool:
        if (len(self.__actions) > 0 and 
            index >= 1 and 
            index <= len(self.__actions)):
            del self.__actions[index - 1]
            return True
        return False

    def __str__(self):
        string = 'Event: {0}\n'.format(self.getEvent())
        for i in range (0, len(self.__actions) , 1):
            string = string + '{0}. {1}\n'.format(i + 1, self.__actions[i])
        return string
    
def main():
    toDo_1 = ToDo(event = 'Orientation camp')
    toDo_1.addToDo('Bring passport')
    toDo_1.addToDo('Change money')
    toDo_1.addToDo('Bring medicine')
    print(toDo_1)
    toDo_1.removeToDoItem(2)
    print(toDo_1)
    toDo_1.removeToDoItem(2)
    print(toDo_1)
    toDo_1.removeToDoItem(2)
    print(toDo_1)

main()

