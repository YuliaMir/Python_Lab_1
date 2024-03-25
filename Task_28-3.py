'''Напишите функцию, которая рассчитывает наименьшее число перестановок при перемещении
Ханойской башни (n дисков насаженных на одном стержне). Требуется переместить эти диски на
соседний стержень. Разрешается использовать третий стержень. Диски можно класть только на диски
большего диаметра.
Для n = 1, число перестановок равно 1.
Для n = 2, число перестановок равно 3.'''

def tower_of_hanoi_moves(n):
    if n == 1:
        return 1
    return 2 * tower_of_hanoi_moves(n-1) + 1

print(tower_of_hanoi_moves(1))
print(tower_of_hanoi_moves(3))
