'''Создайте list comprehensions, которое генерирует следующую
последовательность:
1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10'''

result = [num for num in range(1, 11) for _ in range(num)]
print(result)
