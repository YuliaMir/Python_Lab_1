'''Рассчитать наименьшее общее кратное для списка натуральных чисел'''

a = [int(input()) for z in range(int(input()))]

def prep(a):
    x = 1
    for i in a:
        x *= i
    return x


def calc(a):
    for i in range(1, prep(a) + 1):
        x = 0
        for j in a:
            if i % j == 0:
                x += 1
        if x == len(a):
            return i

print(calc(a))