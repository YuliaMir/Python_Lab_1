'''Напечатайте ряд чисел Фибоначчи до введенного номера n.'''

n = int(input())

x = 1
y = 1

while x <= n:
    print(x, end=" ")
    c = x + y
    x = y
    y = c
