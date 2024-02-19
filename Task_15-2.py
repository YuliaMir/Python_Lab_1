'''Напишите функцию, которая принимает строку символов, и
печатает все содержащиеся в ней номера автомашин по
следующему правилу:
LDDDLL78 или LDDDLL178,
где L – буквы, совпадающие по начертанию в русском и латинском
алфавите, D – цифры от 0 до 9.
Например, A123BC78 или X666XX178'''

import re

def extract_vehicle_numbers(text):
    pattern = r'\b([A-Za-z]{1}\d{3}[A-Za-z]{2}\d{2}|\b[A-Za-z]{1}\d{3}[A-Za-z]{2}\d{3})\b'
    vehicle_numbers = re.findall(pattern, text)

    for number in vehicle_numbers:
        print(number)



values = "A123BC78, X666XX178, ABC12345, 1234ABCD789, 0"

extract_vehicle_numbers(values)
