'''Строка из символов - выделить буквы, цифры и прочее'''

s = input()
letters = ""
numbers = ""
symbols = ""

for char in s:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        numbers += char
    else:
        symbols += char

print("Буквы:", letters)
print("Цифры:", numbers)
print("Символы", symbols)
