'''Введите список lst, состоящий из чисел. Найдите и напечатайте наименьшее число из списка.'''

lst = [6, 1, 9, 2, 8, 4]
min_number = lst[0]
for i in lst:
    if i < min_number:
        min_number = i
print(min_number)
