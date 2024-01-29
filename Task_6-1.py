'''Перевод строки римских цифр в десятичное число'''

s = input()
roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XC': 90, 'XL': 40, 'CD': 400, 'CM': 900}
decimal_num = 0
prev_value = 0
for i in range(len(s) - 1, -1, -1):
    curr_value = roman_numbers[s[i]]
    if curr_value < prev_value:
        decimal_num -= curr_value
    else:
        decimal_num += curr_value
    prev_value = curr_value
print(decimal_num)
