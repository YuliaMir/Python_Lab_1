'''Создайте функцию, которая принимает на вход список X и
возвращает в качестве результата два списка:
Список индексов элементов равных минимальному значению
списка X
Список индексов элементов равных максимальному значению
списка X
Например:
Ввод: X = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4]
Вывод: [0, 4, 8], [3, 7, 9]'''


def min_max_indices(X):
    min_val = min(X)
    max_val = max(X)

    min_indices = [i for i, val in enumerate(X) if val == min_val]
    max_indices = [i for i, val in enumerate(X) if val == max_val]

    return min_indices, max_indices


X = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4]
min_indices, max_indices = min_max_indices(X)

print(min_indices, max_indices)
