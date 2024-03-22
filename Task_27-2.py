'''Необходимо реализовать класс Item, описывающий предмет, конструктор
которого принимает три аргумента:
name — название предмета
price — цена предмета в рублях
quantity — количество предметов
При обращении к атрибуту name экземпляра класса Item будет возвращаться
его название с заглавной буквы, а при обращении к атрибуту total —
произведение цены предмета на его количество.'''

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self._name.capitalize()

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def total(self):
        return self.price * self.quantity

# Example Usage
item1 = Item("apple", 2.5, 3)
print(f"Item: {item1.name}")
print(f"Total Price: {item1.total} rubles")
