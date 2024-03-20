'''Создайте класс Pet, используя функцию type и с методом dis, определенную
заранее и печатающую все атрибуты класса Pet (например, name, age).
Функцию dis для метода Pet.dis определите заранее.
Подсказка:
def dis(self): # метод определяется заранее
# в цикле печатать атрибуты и их значения из словаря self.__dict__
Pet = type(‘Pet’, (), {‘dis’: dis}) # Определяется класс
my_pet = Pet()
my_pet.name = 'Tom'
'''

def dis(self):
    for attr, value in self.__dict__.items():
        print(f"{attr}: {value}")

Pet = type('Pet', (), {'dis': dis})

my_pet = Pet()
my_pet.name = 'Tom'
my_pet.age = 5

my_pet.dis()
