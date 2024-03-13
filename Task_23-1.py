'''Найдите длину наибольшей подстроки данной строки, которая
является палиндромом.
Например, дана строка ‘aabbccddcc’ тогда длиной подстроки с
наибольшим палиндромом является 6 (подстрока ‘ccddcc’)'''


def longest_palindrome_substring_length(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    if not s:
        return 0

    max_length = 0
    for i in range(len(s)):
        length1 = expand_around_center(i, i)
        length2 = expand_around_center(i, i + 1)
        max_length = max(max_length, length1, length2)

    return max_length


s = 'aaaa aabbacccdddcc_ca'
print(longest_palindrome_substring_length(s))
