'''
В кошельке лежат бумажные купюры 10, 50, 100, 200, 500, 1000,
2000, 5000 рублей, каждой купюры по одной штуке.
Какие суммы можно составить, если использовать этот набор
купюр?
Подсказка. Используйте одну из наиболее подходящих функций
модуля itertools.'''


import itertools

bills = [10, 50, 100, 200, 500, 1000, 2000, 5000]

sums = set()
for r in range(1, len(bills) + 1):
    for combination in itertools.combinations(bills, r):
        sums.add(sum(combination))

print(sorted(sums))
