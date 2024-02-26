'''Создайте класс Shape, объекты которого имеют атрибуты Colour –
строка, например, «Красный», «Синий»; Square – площадь
объекта
• Создайте несколько методов:
1. Установить цвет объекта
2. Запросить цвет объекта и напечатать его
3. Задать площадь объекта
4. Запросить площадь объекта'''

class Shape:
    def __init__(self):
        self.color = None
        self.area = None

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

class Square(Shape):
    def set_area(self, area):
        self.area = area

    def get_area(self):
        return self.area


square = Square()
square.set_color("Red")
square.set_area(25)
print("Color of the square:", square.get_color())
print("Area of the square:", square.get_area())
