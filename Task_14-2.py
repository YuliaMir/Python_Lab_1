'''Напишите рекурсивную функцию, которая вычисляет сумму цифр
натурального числа'''

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


n = int(input())
if n < 0:
    print("Укажите положительное число")
else:
    digit_sum = sum_of_digits(n)
    print(f"Сумма цифр для  {n} : {digit_sum}")
