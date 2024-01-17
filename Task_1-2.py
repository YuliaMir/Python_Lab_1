'''Ввести два числа x и y. Напечатать наибольшее из чисел x+y, x*y, x-y, x/y, x//y'''

x = float(input())
y = float(input())
if x == 0 or y == 0:
    print(x + y)
if x == 1 or y == 1:
    print(x + y)
else:
    print(x * y)

