import question_1
import question_2

person_1 = question_1.Person('m', 'ah seng', 'ong')
print(person_1)
person_1.name('ah cheng')
print(person_1)
print(person_1.gender())
print(person_1.getName())
print(person_1.lastName())
print(person_1.getFullName())
print(person_1.getInitials())

rect_1 = question_2.Rectangle(10, 5)
rect_2 = question_2.Rectangle(15, 10)
print(rect_2.isBigger(rect_1))
print(rect_1.isBigger(rect_2))
print(rect_2)