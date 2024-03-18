'''Реализуйте функцию is_palindrome() с использованием рекурсии,
которая принимает один аргумент string — произвольная строка.
Функция должна возвращать значение True, если переданная
строка является палиндромом, или False в противном случае.
Примечание 1. Палиндром — текст, одинаково читающийся в
обоих направлениях.
Примечание 2. Пустая строка является палиндромом, как и строка,
состоящая из одного символа.'''


def is_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])

    return False


print(is_palindrome(""))  # True (empty string)
print(is_palindrome("a"))  # True (one character)
print(is_palindrome("lol"))  # True
print(is_palindrome("tenet"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("level"))  # True
