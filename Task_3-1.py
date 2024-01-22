'''Вводить в бесконечном цикле зарплаты сотрудников. Окончание ввода - ввод 0. После чего вывести среднюю зарплату.'''

payments = []
while True:
    payment = int(input())
    if payment == 0:
        break
    payments.append(payment)

if len(payments) > 0:
    avg_payment = sum(payments) / len(payments)
    print(avg_payment)
else:
    print("Not enough data")
