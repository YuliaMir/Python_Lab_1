'''Создайте функцию-генератор, которая создает бесконечную
последовательность:
1, -2, 3, -4, 5, -6, …'''

def infinite_subsequence():
    n = 1
    while True:
        if n % 2 == 0:
            yield -n
        else:
            yield n
        n += 1

gen = infinite_subsequence()
for _ in range(10):
    print(next(gen))
