'''Определите класс Person. При создании объекта p = Person(‘Иванов’,
‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
При печати объекта должно выводиться следующее:
print(p) # чивородеФлиахиМвонавИ'''

class Person:
    def __init__(self, *names):
        self.full_name = ''.join(names)

    def __str__(self):
        return self.full_name[::-1]

p = Person('Иванов', 'Петр', 'Сергеевич')
print(p)
