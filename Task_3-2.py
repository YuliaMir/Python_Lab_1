'''Дано целое число. Сосчитать и напечатать, сколько в его записи нулей, единиц, двоек и так далее. Привер ввода: 136777890'''

x = input()
digits_count = [0] * 10

for digit in x:
    digits_count[int(digit)] += 1

for i, count in enumerate(digits_count):
    print(f"{i}: {count}")
