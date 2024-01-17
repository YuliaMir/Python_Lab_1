'''Ввести два числа x и y. Напечатать ВТОРОЕ ПО ВЕЛИЧИНЕ из чисел x+y, x*y, x-y, x/y, x//y'''

x = float(input())
y = float(input())

a = x + y
b = x * y
c = x - y
d = x / y
e = x // y

list_of_values = [a, b, c, d, e]
list_of_values.remove(max(list_of_values))
list_of_values.remove(min(list_of_values))

if list_of_values[0] > list_of_values[1]:
    print(list_of_values[0]) if list_of_values[0] > list_of_values[2] else print(list_of_values[2])
else:
    print(list_of_values[1]) if list_of_values[1] > list_of_values[2] else print(list_of_values[2])