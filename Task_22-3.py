'''В Python существуют ключевые слова, которые нельзя использовать для названия
переменных, функций и классов. Для получения списка всех ключевых слов можно
воспользоваться атрибутом kwlist из модуля keyword.
Приведенный ниже код:
import keyword
print(keyword.kwlist)
выводит:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
Напишите программу, которая принимает строку текста и заменяет в ней все
ключевые слова на <kw>'''


import keyword

def replace_keywords_with_kw(text):
    keywords = keyword.kwlist
    for kw in keywords:
        text = text.replace(kw, "<kw>")
    return text

text = "try something like if, else, and while."
updated_text = replace_keywords_with_kw(text)
print(updated_text)
