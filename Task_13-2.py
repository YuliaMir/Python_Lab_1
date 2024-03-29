'''Создайте функцию-генератор, которая создает последовательность
числовых палиндромов:
1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151
161 171 181 191 202 212…'''

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def palindrome_sequence():
    n = 1
    while True:
        if is_palindrome(n):
            yield n
        n += 1

gen = palindrome_sequence()
for _ in range(30):
    print(next(gen))




