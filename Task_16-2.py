'''Вводится двухзначное число, например: 45.
Напишите такой шаблон, чтобы функция re.findall находила только
те положительные целые числа, которые не больше, чем это
введенное число.
Т.е. для 45 она находила бы 0, 1, 12, 45, но не 46, 100, 1000'''


import re

def find_positive_integers_up_to_limit(limit, input_str):
    pattern = r'\b(?:[0-9]|[1-9][0-9]|{})\b'.format(limit)
    positive_integers = [num for num in re.findall(pattern, input_str) if int(num) <= int(limit)]
    return positive_integers

limit = input("Введите двузначное число: ")
input_str = ' '.join(str(num) for num in range(100))
positive_integers = find_positive_integers_up_to_limit(limit, input_str)
print(positive_integers)

