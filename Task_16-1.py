'''Напишите функцию, которая использует RE.
На вход подается строка, например, Институт точной механики оптики
Функция создает сокращение ИТМО (из первых букв слов, которые
переведены в заглавные).
Есть много разных способов это сделать, например использовать re.sub, а
потом re.split.'''

import re

def create_abbreviation(input_str):
    words = re.findall(r'\b\w', input_str)
    abbreviation = ''.join(word.upper() for word in words)
    return abbreviation

input_str = "Научно-исследовательский институт"
abbreviation = create_abbreviation(input_str)
print(abbreviation)
