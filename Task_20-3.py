'''Создайте класс, экземпляр которого генерирует бесконечную
циклическую последовательность из чисел и больших латинский букв.
1, A, 2, B, 3, C, .., X, 25, Y, 26, Z,1,A,2,B,3,C,..,X,25,Y,26,Z, 1, A…'''


class SequenceGenerator:
    def __init__(self):
        self.num = 1
        self.letter = 'A'
        self.is_number = True

    def generate_next(self):
        if self.is_number:
            result = self.num
            self.num += 1
            if self.num > 26:
                self.num = 1
            self.is_number = False
        else:
            result = self.letter
            self.letter = chr(ord(self.letter) + 1)
            if self.letter > 'Z':
                self.letter = 'A'
            self.is_number = True
        return result


generator = SequenceGenerator()

for _ in range(100):
    print(generator.generate_next(), end=', ')

