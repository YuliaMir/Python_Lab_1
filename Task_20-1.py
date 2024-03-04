'''Человек регулярно приходит в кафе выпить чашку кофе, выбирая
разные варианты кофе, иногда с пирожным, выбирая, что есть в
меню.
Оплачивает иногда наличными деньгами, иногда картой.
Разработайте классы, их атрибуты, свойства и методы.
Может быть какую-то отчетность.'''

class Cafe:
    def __init__(self, name):
        self.name = name
        self.menu = {
            'coffee': 2.50,
            'cake': 3.00
        }
        self.revenue = 0

    def order(self, item, payment_method):
        if item in self.menu:
            if payment_method == 'cash':
                self.revenue += self.menu[item]
                print(f'Заказ {item} оплачен наличными.')
            elif payment_method == 'card':
                self.revenue += self.menu[item]
                print(f'Заказ {item} оплачен наличными.')
            else:
                print('Выберете другой способ оплаты.')
        else:
            print('Данной позиции нет в меню.')

    def generate_report(self):
        print(f'Выручка {self.name}: ${self.revenue}')


class Person:
    def __init__(self, name):
        self.name = name

    def order_and_drink_coffee(self, cafe, payment_method):
        cafe.order('coffee', payment_method)
        print(f'{self.name} заказал(а) и выпил(a) кофе в кафе {cafe.name}')


# Usage example
cafe = Cafe('Буше')
person = Person('Алиса')
person.order_and_drink_coffee(cafe, 'cash')
cafe.generate_report()
