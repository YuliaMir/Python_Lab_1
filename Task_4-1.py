'''Напишите калькулятор'''

s = input()
x = int(s.split()[0])
y = int(s.split()[2])
operand = s.split()[1]

if operand == '+':
    result = x + y
elif operand == '-':
    result = x - y
elif operand == '*':
    result = x * y
elif operand == '/':
    result = x / y
print(result)


