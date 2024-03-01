'''Реализуйте класс Fibonacci, который реализует итератор, генерирующий
бесконечную последовательность чисел Фибоначчи.
Например:
fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
Должен печатать следующие числа:
1
1
2
3'''

class Fibonacci:
    def __init__(self):
        self.a, self.b = 1, 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

