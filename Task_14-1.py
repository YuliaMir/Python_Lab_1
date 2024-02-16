'''Напишите рекурсивную функцию, которая вычисляет количество
цифр введенного целого числа n (n >= 0).'''

def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

n = int(input())
if n < 0:
    print("Укажите положительное число")
else:
    digit_count = count_digits(n)
    print(f"Количество цифр для {n} : {digit_count}")
