'''Напишите функцию, которая переводит арабские числа в римские.
Например: 2023 ->MMXXIII'''

def arabic_to_roman(num):
    if not isinstance(num, int) or num <= 0:
        return "Invalid input"

    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }

    result = ''
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while num >= value:
            result += numeral
            num -= value

    return result

arabic_number = 2024
roman_number = arabic_to_roman(arabic_number)
print(f"Arabic Number: {arabic_number} -> Roman Number: {roman_number}")


