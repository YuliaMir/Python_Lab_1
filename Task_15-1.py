'''Создайте рекурсивную функцию, которая получает как аргумент dct словарь,
который может содержать словари, которые могут содержать словари и т.д. и
как аргумент x значение ключа.
Например:
dct = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11,}, 6:22}
Функция должна составить список, состоящий только из значений словаря с
ключем x.
Например, для x = 1
[1, 111, 2222, 11]'''

def get_values_by_key(dct, x):
    result = []
    for key, value in dct.items():
        if key == x:
            result.append(value)
        elif isinstance(value, dict):
            result.extend(get_values_by_key(value, x))
    return result

dct = {1: 1, 2: 2, 3: {2: 22, 3: {1: 111, 2: 222, 3: {0: 1111, 1: 2222, 2: 3333}}, 1: 11}, 6: 22}

x = 3

result = get_values_by_key(dct, x)
print(result)
