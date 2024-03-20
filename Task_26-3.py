'''Создайте метод Person, определите в нем атрибут self._age
Используйте декоратор @property для определения методов getter,
setter, deleter.
В методе setter определите проверку, что возраст не может быть
меньше 1 и больше 100, при попытке установить этот возраст
программа должна печатать «Недопустимый возраст».'''

class Person:
    def __init__(self):
        self._age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 1 <= value <= 100:
            self._age = value
        else:
            print("Недопустимый возраст")

    @age.deleter
    def age(self):
        del self._age

person = Person()

person.age = 25
print(person.age)

person.age = 120
print(person.age)

del person.age

