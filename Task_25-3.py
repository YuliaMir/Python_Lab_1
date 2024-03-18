'''Напишите функцию, которой на вход подается строка, содержащая
последовательность слов (которые могут включать буквы верхнего и нижнего
регистра). На выходе должна получиться строка в CamelStyle.
Например, "camel case word" => CamelCaseWord'''

def to_camel_case(input_string):
    words = input_string.split()
    camel_case_words = [word.capitalize() for word in words]
    return "".join(camel_case_words)

print(to_camel_case("camel case word"))
print(to_camel_case("hello world"))
print(to_camel_case("this is a test"))
