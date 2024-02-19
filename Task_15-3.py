'''Напишите функцию, которая находит в строке все телефонные номера,
которые удовлетворяют следующим шаблонам:
+7(812)DDD-DDDD, +7(812)DDD-DD-DD, +7(921)DDD-DDDD, +7(921)DDD-DD-DD
где D любая цифра'''

import re


def extract_phone_numbers(numbers):
    pattern = r'\+7\((812|921)\)(\d{3}-\d{4}|\d{3}-\d{2}-\d{2})'
    phone_numbers = re.findall(pattern, numbers)

    for number in phone_numbers:
        print(f"+7({number[0]}){number[1]}")


numbers = "+7(812)123-4567, +7(921)987-6543, +7(812)111-22-33, +7(921)222-33-44, +7(921)"

extract_phone_numbers(numbers)

